import boto3
from datetime import datetime
from datetime import timedelta
ecs_client = boto3.client('ecs','us-east-1')
cloudwatch_client = boto3.client('cloudwatch','us-east-1')
ecs_clusters = ['cluster-1', 'cluster-2']
def update_ecs_service_desired_count(cluster_name, service_name):
    ecs_client.update_service(cluster=cluster_name, service=service_name, desiredCount=0)

def get_avg_cpu_utilization(cluster_name, service_name):
    response = cloudwatch_client.get_metric_statistics(
        Namespace='AWS/ECS',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'ClusterName', 'Value': cluster_name}, { 'Name': 'ServiceName', 'Value': service_name}],
        StartTime=datetime.utcnow() - timedelta(days=7),
        EndTime=datetime.utcnow(),
        Period=3600 * 24,  
        Statistics=['Average'])
    datapoints = response['Datapoints']
    if datapoints:        
        average = sum(d['Average'] for d in datapoints) / len(datapoints)
        return average
    else:
        return None

for cluster_name in ecs_clusters:
    services = ecs_client.list_services(cluster=cluster_name)['serviceArns']
    for service_arn in services:
        service_name = service_arn.split('/')[-1]
        service_desc = ecs_client.describe_services(cluster=cluster_name, services=[service_name])
        launch_type = service_desc['services'][0].get('launchType', '')
        if launch_type == 'EC2':
            average_cpu_utilization = get_avg_cpu_utilization(cluster_name, service_name)
            if average_cpu_utilization != 0 and average_cpu_utilization < 15:
                #update_ecs_service_desired_count(cluster_name, service_name)
                print(f"Service {service_name} in cluster {cluster_name} is scaled down to 0 tasks due to less CPU utilization.") 
