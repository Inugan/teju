import requests
import datetime
import time
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []

api_address = 'https://api.openweathermap.org/data/2.5/'
api_key = '?&appid=a55bdbc3cd30afb5f0db4d557c32bd7c&units=metric&q='
climate_type = 'weather'
city = input("Enter City Name : ")

url = api_address + climate_type + api_key + city
json_data = requests.get(url).json()
return_code = json_data['cod']



if return_code == 200:
    
   type_of_data = input ("Enter the type of data you want >>Forecast(F) or Current(C)<< ---(F/C): ")

   if type_of_data == 'C' or type_of_data == 'c':
       climate_type = 'weather'
       url = api_address + climate_type + api_key + city
       json_data = requests.get(url).json()
                   
       clim_city = json_data['name']
       print("City :",clim_city)
       print("Current Date& Time: ", datetime.datetime.now())
       Climate = json_data['weather'][0]['description']
       print("Climate :", Climate)
       Latitude = json_data['coord']['lat']
       print("Latitude :", Latitude, "°")
       Longitude = json_data['coord']['lon']
       print("Longitude :", Longitude, "°")
       Temperature = json_data['main']['temp']
       print("Temperature :", Temperature, "°C")
       Pressure = json_data['main']['pressure']
       print("Pressure :", Pressure, "hPa")
       Humidity = json_data['main']['humidity']
       print("Humidity :", Humidity, "%")
       Minimum_Temperature = json_data['main']['temp_min']
       print("Minimum_Temperature :", Minimum_Temperature, "°C")
       Maximum_Temperature = json_data['main']['temp_max']
       print("Maximum_Temperature :", Maximum_Temperature, "°C")
       Wind_Speed = json_data['wind']['speed']
       print("Wind_Speed :", Wind_Speed, "m/s")
       Cloudy = json_data['clouds']['all']
       print("Cloudy :", Cloudy, "%")
       Sun_Rise = json_data['sys']['sunrise']
       rise_time = time.ctime(Sun_Rise)
       print("Sun_Rise :", rise_time)
       Sun_Set = json_data['sys']['sunset']
       set_time = time.ctime(Sun_Set)
       print("Sun_Set :", set_time)
       
       f = open("Climfin.txt", "w")
       f.write("CURRENT CLIMATIC CONDITIONS IN {}".format(str(clim_city)) + "\n")
       f.write("Climate:\t{0}".format(str(Climate)) + "\n")
       f.write("Latitude:\t{0}".format(Latitude) + "°\n")
       f.write("Longitude:\t{0}".format(Longitude) + "°\n")
       f.write("Temperature:\t{0}".format(Temperature) + "°C\n")
       f.write("Pressure:\t{0}".format(Pressure) + "°C\n")
       f.write("Humidity:\t{0}".format(Humidity) + "%\n")
       f.write("Minimum_Temperature:\t{0}".format(Minimum_Temperature) + "°C\n")
       f.write("Maximum_Temperature:\t{0}".format(Maximum_Temperature) + "°C\n")
       f.write("Wind_Speed:\t{0}".format(Wind_Speed) + "m/s\n")
       f.write("Cloudy: \t{0}".format(Cloudy) + "%\n")
       f.write("Sun_Rise:\t{0}".format(rise_time) + "\n")
       f.write("Sun_Set:\t{0}".format(set_time) + "\n")
       f.write("****End of the Report****\n\n")
       f.close()

       pdf_name = 'Climate.pdf'
       doc = SimpleDocTemplate(
                pdf_name,
                pagesize=letter,
                bottomMargin=.4 * inch,
                topMargin=.6 * inch,
                rightMargin=.8 * inch,
                leftMargin=.8 * inch)

   with open("climfin.txt", "r") as txt_file:
             text_content = txt_file.read()
             P = Paragraph(text_content, styleN)
             story.append(P)                    
   if type_of_data == 'F' or type_of_data == 'f':
       climate_type = 'forecast'
       url = api_address + climate_type + api_key + city
       json_data = requests.get(url).json()    
       
       print("Current Date& Time: ", datetime.datetime.now())

       clim_city = json_data['city']['name']
       print("City :",clim_city)

       Latitude = json_data['city']['coord']['lat']
       print("Latitude :", Latitude, "°")
       Longitude = json_data['city']['coord']['lon']
       print("Longitude :", Longitude, "°")
       
       day1 = json_data['list'][0]['dt']
       DAY_1 = time.ctime(day1)       
       print("################DAY_1 (Today)################\n", DAY_1)
       Climate = json_data['list'][1]['weather'][0]['description']
       print("Climate :", Climate)
       Temperature = json_data['list'][0]['main']['temp']
       print("Temperature", Temperature)
       Minimum_Temperature = json_data['list'][0]['main']['temp_min']
       print("Minimum_Temperature :", Minimum_Temperature, "°C")
       Maximum_Temperature = json_data['list'][0]['main']['temp_max']
       print("Maximum_Temperature :", Maximum_Temperature, "°C")
       Pressure = json_data['list'][0]['main']['pressure']
       print("Pressure :", Pressure, "hPa")
       Humidity = json_data['list'][0]['main']['humidity']
       print("Humidity :", Humidity, "%")
       Ground_level = json_data['list'][0]['main']['grnd_level']
       print("Ground_Level :", Ground_level, "m")
       sea_level = json_data['list'][0]['main']['sea_level']
       print("Sea_Level :", sea_level, "m")
       Cloudy = json_data['list'][0]['clouds']['all']
       print("Cloudy :", Cloudy, "%")
       Wind_speed = json_data['list'][3]['wind']['speed']
       print("Wind_speed :", Wind_speed, "m/s")

       f = open("ClimFor.txt", "w")
       f.write("CURRENT CLIMATIC CONDITIONS IN {}".format(str(clim_city)) + "\n")
       f.write(">>>>DAY_1 (Today)<<<< :\t{0}".format(DAY_1) + "\n")
       f.write("Climate:\t{0}".format(str(Climate)) + "\n")
       f.write("Temperature:\t{0}".format(Temperature) + "°C\n")
       f.write("Pressure:\t{0}".format(Pressure) + "°C\n")
       f.write("Humidity:\t{0}".format(Humidity) + "%\n")
       f.write("Minimum_Temperature:\t{0}".format(Minimum_Temperature) + "°C\n")
       f.write("Maximum_Temperature:\t{0}".format(Maximum_Temperature) + "°C\n")
       f.write("Wind_Speed:\t{0}".format(Wind_speed) + "m/s\n")
       f.write("Cloudy: \t{0}".format(Cloudy) + "%\n")
       f.write("Sea_level:\t{0}".format(sea_level) + "\n")
       f.write("Ground_level:\t{0}".format(Ground_level) + "\n")
       f.write("****End of the DAY_1 Report****\n\n")
       f.close()

       
       day2 = json_data['list'][11]['dt']
       DAY_2 = time.ctime(day2)
       print("################DAY_2################\n", DAY_2)
       Climate = json_data['list'][11]['weather'][0]['description']
       print("Climate :", Climate)
       Temperature = json_data['list'][11]['main']['temp']
       print("Temperature", Temperature)
       Minimum_Temperature = json_data['list'][11]['main']['temp_min']
       print("Minimum_Temperature :", Minimum_Temperature, "°C")
       Maximum_Temperature = json_data['list'][11]['main']['temp_max']
       print("Maximum_Temperature :", Maximum_Temperature, "°C")
       Pressure = json_data['list'][11]['main']['pressure']
       print("Pressure :", Pressure, "hPa")
       Humidity = json_data['list'][11]['main']['humidity']
       print("Humidity :", Humidity, "%")
       Ground_level = json_data['list'][11]['main']['grnd_level']
       print("Ground_Level :", Ground_level, "m")
       sea_level = json_data['list'][11]['main']['sea_level']
       print("Sea_Level :", sea_level, "m")
       Cloudy = json_data['list'][11]['clouds']['all']
       print("Cloudy :", Cloudy, "%")
       Wind_speed = json_data['list'][11]['wind']['speed']
       print("Wind_speed :", Wind_speed, "m/s")

       
       f = open("ClimFor.txt", "a")
       f.write(">>>>DAY_2<<<< :\t{0}".format(DAY_2) + "\n")
       f.write("\nClimate:\t{0}".format(str(Climate)) + "\n")
       f.write("Temperature:\t{0}".format(Temperature) + "°C\n")
       f.write("Pressure:\t{0}".format(Pressure) + "°C\n")
       f.write("Humidity:\t{0}".format(Humidity) + "%\n")
       f.write("Minimum_Temperature:\t{0}".format(Minimum_Temperature) + "°C\n")
       f.write("Maximum_Temperature:\t{0}".format(Maximum_Temperature) + "°C\n")
       f.write("Wind_Speed:\t{0}".format(Wind_speed) + "m/s\n")
       f.write("Cloudy: \t{0}".format(Cloudy) + "%\n")
       f.write("Sea_level:\t{0}".format(sea_level) + "\n")
       f.write("Ground_level:\t{0}".format(Ground_level) + "\n")
       f.write("****End of the DAY_2 Report****\n\n")
       f.close()


       day3 = json_data['list'][15]['dt']
       DAY_3 = time.ctime(day3)
       print("################DAY_3################\n", DAY_3)
       Climate = json_data['list'][15]['weather'][0]['description']
       print("Climate :", Climate)
       Temperature = json_data['list'][15]['main']['temp']
       print("Temperature", Temperature)
       Minimum_Temperature = json_data['list'][15]['main']['temp_min']
       print("Minimum_Temperature :", Minimum_Temperature, "°C")
       Maximum_Temperature = json_data['list'][15]['main']['temp_max']
       print("Maximum_Temperature :", Maximum_Temperature, "°C")
       Pressure = json_data['list'][15]['main']['pressure']
       print("Pressure :", Pressure, "hPa")
       Humidity = json_data['list'][15]['main']['humidity']
       print("Humidity :", Humidity, "%")
       Ground_level = json_data['list'][15]['main']['grnd_level']
       print("Ground_Level :", Ground_level, "m")
       sea_level = json_data['list'][15]['main']['sea_level']
       print("Sea_Level :", sea_level, "m")
       Cloudy = json_data['list'][15]['clouds']['all']
       print("Cloudy :", Cloudy, "%")
       Wind_speed = json_data['list'][15]['wind']['speed']
       print("Wind_speed :", Wind_speed, "m/s")
       
       f = open("ClimFor.txt", "a")
       f.write(">>>>DAY_3<<<< :\t{0}".format(DAY_3) + "\n")
       f.write("Climate:\t{0}".format(str(Climate)) + "\n")
       f.write("Temperature:\t{0}".format(Temperature) + "°C\n")
       f.write("Pressure:\t{0}".format(Pressure) + "°C\n")
       f.write("Humidity:\t{0}".format(Humidity) + "%\n")
       f.write("Minimum_Temperature:\t{0}".format(Minimum_Temperature) + "°C\n")
       f.write("Maximum_Temperature:\t{0}".format(Maximum_Temperature) + "°C\n")
       f.write("Wind_Speed:\t{0}".format(Wind_speed) + "m/s\n")
       f.write("Cloudy: \t{0}".format(Cloudy) + "%\n")
       f.write("Sea_level:\t{0}".format(sea_level) + "\n")
       f.write("Ground_level:\t{0}".format(Ground_level) + "\n")
       f.write("****End of the DAY_3 Report****\n\n")
       f.close()
       
       day4 = json_data['list'][23]['dt']
       DAY_4 = time.ctime(day4)
       print("################DAY_4################\n", DAY_4)
       Climate = json_data['list'][23]['weather'][0]['description']
       print("Climate :", Climate)
       Temperature = json_data['list'][23]['main']['temp']
       print("Temperature", Temperature)
       Minimum_Temperature = json_data['list'][23]['main']['temp_min']
       print("Minimum_Temperature :", Minimum_Temperature, "°C")
       Maximum_Temperature = json_data['list'][23]['main']['temp_max']
       print("Maximum_Temperature :", Maximum_Temperature, "°C")
       Pressure = json_data['list'][23]['main']['pressure']
       print("Pressure :", Pressure, "hPa")
       Humidity = json_data['list'][23]['main']['humidity']
       print("Humidity :", Humidity, "%")
       Ground_level = json_data['list'][23]['main']['grnd_level']
       print("Ground_Level :", Ground_level, "m")
       sea_level = json_data['list'][23]['main']['sea_level']
       print("Sea_Level :", sea_level, "m")
       Cloudy = json_data['list'][23]['clouds']['all']
       print("Cloudy :", Cloudy, "%")
       Wind_speed = json_data['list'][23]['wind']['speed']
       print("Wind_speed :", Wind_speed, "m")

       f = open("ClimFor.txt", "a")
       f.write(">>>>DAY_4<<<< :\t{0}".format(DAY_4) + "\n")
       f.write("Climate:\t{0}".format(str(Climate)) + "\n")
       f.write("Temperature:\t{0}".format(Temperature) + "°C\n")
       f.write("Pressure:\t{0}".format(Pressure) + "°C\n")
       f.write("Humidity:\t{0}".format(Humidity) + "%\n")
       f.write("Minimum_Temperature:\t{0}".format(Minimum_Temperature) + "°C\n")
       f.write("Maximum_Temperature:\t{0}".format(Maximum_Temperature) + "°C\n")
       f.write("Wind_Speed:\t{0}".format(Wind_speed) + "m/s\n")
       f.write("Cloudy: \t{0}".format(Cloudy) + "%\n")
       f.write("Sea_level:\t{0}".format(sea_level) + "\n")
       f.write("Ground_level:\t{0}".format(Ground_level) + "\n")
       f.write("****End of the DAY_4 Report****\n\n")
       f.close()
              
       day5 = json_data['list'][35]['dt']
       DAY_5 = time.ctime(day5)
       print("################DAY_5################\n", DAY_5)
       Climate = json_data['list'][35]['weather'][0]['description']
       print("Climate :", Climate)
       Temperature = json_data['list'][35]['main']['temp']
       print("Temperature", Temperature)
       Minimum_Temperature = json_data['list'][35]['main']['temp_min']
       print("Minimum_Temperature :", Minimum_Temperature, "°C")
       Maximum_Temperature = json_data['list'][35]['main']['temp_max']
       print("Maximum_Temperature :", Maximum_Temperature, "°C")
       Pressure = json_data['list'][35]['main']['pressure']
       print("Pressure :", Pressure, "hPa")
       Humidity = json_data['list'][35]['main']['humidity']
       print("Humidity :", Humidity, "%")
       Ground_level = json_data['list'][35]['main']['grnd_level']
       print("Ground_Level :", Ground_level, "m")
       sea_level = json_data['list'][35]['main']['sea_level']
       print("Sea_Level :", sea_level, "m")
       Cloudy = json_data['list'][35]['clouds']['all']
       print("Cloudy :", Cloudy, "%")
       Wind_speed = json_data['list'][35]['wind']['speed']
       print("Wind_speed :", Wind_speed, "m")


       f = open("ClimFor.txt", "a")
       f.write(">>>>DAY_5<<<< :\t{0}".format(DAY_5) + "\n")
       f.write("Climate:\t{0}".format(str(Climate)) + "\n")
       f.write("Temperature:\t{0}".format(Temperature) + "°C\n")
       f.write("Pressure:\t{0}".format(Pressure) + "°C\n")
       f.write("Humidity:\t{0}".format(Humidity) + "%\n")
       f.write("Minimum_Temperature:\t{0}".format(Minimum_Temperature) + "°C\n")
       f.write("Maximum_Temperature:\t{0}".format(Maximum_Temperature) + "°C\n")
       f.write("Wind_Speed:\t{0}".format(Wind_speed) + "m/s\n")
       f.write("Cloudy: \t{0}".format(Cloudy) + "%\n")
       f.write("Sea_level:\t{0}".format(sea_level) + "\n")
       f.write("Ground_level:\t{0}".format(Ground_level) + "\n")
       f.write("****End of the DAY_5 Report****\n")
       f.write("\n\n")
       f.write("****End of the FORECAST Report****")
       f.close()

else:
    print("City not found!! Please enter the correct city name")
    
