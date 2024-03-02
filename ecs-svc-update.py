import boto3 ,pytz, time, logging
from datetime import datetime, timedelta
from botocore.exceptions import ClientError
session = boto3.Session(profile_name='dev')
cloudwatch_client = session.client('cloudwatch','us-east-1')
ecs_client = session.client('ecs','us-east-1')
ec2_client = session.client('ec2','us-east-1')
ecs_clusters = ['cluster-1', 'cluster-2']

def update_ecs_service_desired_count(cluster_name, service_name):
    ecs_client.update_service(cluster=cluster_name, service=service_name, desiredCount=0)

def get_avg_cpu_utilization(cluster_name, service_name):
    response = cloudwatch_client.get_metric_statistics(Namespace='AWS/ECS',
                                                       MetricName='CPUUtilization',
                                                       Dimensions=[{'Name': 'ClusterName', 'Value': cluster_name}, { 'Name': 'ServiceName', 'Value': service_name}],
                                                       StartTime=datetime.now(pytz.utc) - timedelta(days=7),
                                                       EndTime=datetime.now(pytz.utc),
                                                       Period=3600 * 24,
                                                       Statistics=['Average'])
    datapoints = response['Datapoints']
    if datapoints:        
        average = sum(d['Average'] for d in datapoints) / len(datapoints)
        return average
    else:
        return None

def stop_solr (service_name):
    custom_filter1 = [{'Name': 'instance-state-name', 'Values': ['running']},{'Name':'tag:env', 'Values': [service_name]}]
    while True:                
        try:        
            resp1 = ec2_client.describe_instances(Filters=custom_filter1)
            if len(resp1['Reservations']):
                for instance_details in resp1['Reservations']:
                    for each_inst in instance_details['Instances']:
                        ec2_client.stop_instances(each_inst["InstanceId"])
                        print(each_inst["InstanceId"] + " is being stopped")
        except ClientError as e :
                                    print(e.response['Error']['Code'], e.response['Error']['Message'])
                                    if e.response['Error']['Code'] == "Throttling" or e.response['Error']['Code'] == "ThrottlingException" or  e.response['Error']['Code'] == 'ThrottledException':
                                        time.sleep(20)
                                    else:
                                        logging.exception ("Failed to stop the instance "+each_inst["InstanceId"])
                                        break

for cluster_name in ecs_clusters:
    services = ecs_client.list_services(cluster=cluster_name)['serviceArns']
    for service_arn in services:
        service_name = service_arn.split('/')[-1]
        service_desc = ecs_client.describe_services(cluster=cluster_name, services=[service_name])
        launch_type = service_desc['services'][0].get('launchType', '')
        if launch_type == 'EC2':
            average_cpu_utilization = get_avg_cpu_utilization(cluster_name, service_name)
            if average_cpu_utilization != 0 and average_cpu_utilization < 10:
                #update_ecs_service_desired_count(cluster_name, service_name)
                print(f"Service {service_name} in cluster {cluster_name} is scaled down to 0 tasks due to less CPU utilization.")
                print("Now stopping the respective solr engines ...")
                #stop_solr (service_name)
