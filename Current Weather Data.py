"""
Current weather data
from API https://openweathermap.org/current
Hossein JALILI
mehr 1400
ver 1.0
"""
import requests

api_key="83eb69e2285d0e061a4f9a52f0221e8c"
base_url="http://api.openweathermap.org/data/2.5/weather?q="

cityName=input("Enter city name:")
#cityName="tehran"
url=base_url + cityName + "&appid=" + api_key
print("\nyour city API is :\t",url,"\n")

result = requests.get(url)
data = result.json()
#print(data)

if data["cod"] == "404":
    print("city not found")
else:
    ###############coord##################
    _coord=data["coord"]
    lon=_coord["lon"]
    lat=_coord["lat"]
    print("***City geo location***\nlongitude:\t",lon)
    print("latitude:\t",lat,"\n")
    #################weather##############
    _weather = data["weather"]
    idd=_weather[0]["id"]
    print("***More info Weather condition codes***\nWeather condition id:\t\t\t",idd)
    mainn=_weather[0]["main"]
    print("Group of weather parameters:\t\t",mainn)
    descriptionn=_weather[0]["description"]
    print("Weather condition within the group:\t",descriptionn)
    iconn=_weather[0]["icon"]
    print("Weather icon id:\t\t\t",iconn,"\n")
    #################base##############
    _base = data["base"]
    print("***Internal parameter***\nbase:\t",_base,"\n")
    #################main##############
    _main=data["main"]
    print("***Main parameter***")
    tempp = _main["temp"]
    print("Temperature:\t",tempp , "\tFahrenheit")
    tc = tempp - 273.15
    print("Temperature:\t",str(round(tc,2)) + "\t\tCelsius")
    feels_like=_main["feels_like"]
    print("Feels_like:\t",feels_like , "\tFahrenheit")
    temp_min=_main["temp_min"]
    print("temp_min:\t",temp_min , "\tFahrenheit")
    temp_max=_main["temp_max"]
    print("temp_max:\t",temp_max , "\tFahrenheit")
    pressure = _main["pressure"]
    print("Pressure:\t",pressure, "\t\thPa")
    humidity = _main["humidity"]
    print("Humidity:\t",humidity, "\t\t%","\n")
    #################visibility##############
    _visibility=data["visibility"]
    print("***visibility***")
    print("visibility:\t",_visibility , "\t\tFahrenheit","\n")
    #################wind##############
    _wind=data["wind"]
    print("***Wind parameter***")
    speed = _wind["speed"]
    print("Wind speed:\t",speed , "\t\tmeter/sec")
    deg = _wind["deg"]
    print("Wind direction:\t",deg , "\t\tdegrees","\n")
    #################clouds##############
    _clouds=data["clouds"]
    print("***clouds parameter***")
    alll = _clouds["all"]
    print("Cloudiness:\t",alll , "\t\t%","\n")
    #################dt##############
    _dt=data["dt"]
    print("***dt parameter***")
    print("Time of data calculation:\t",_dt , "\tUTC","\n")
    #################sys##############
    _sys=data["sys"]
    _type=_sys["type"]
    print("***sys parameter***")
    print("type,Internal parameter:\t",_type )
    _id=_sys["id"]
    print("id,Internal parameter:\t\t",_id )
    _country=_sys["country"]
    print("Country code:\t\t\t",_country )
    _sunrise=_sys["sunrise"]
    print("Sunrise time:\t\t\t",_sunrise, "\tUTC" )
    _sunset=_sys["sunset"]
    print("Sunset time:\t\t\t",_sunset , "\tUTC","\n")
    #################more inf##############
    _timezone=data["timezone"]
    _id=data["id"]
    _name=data["name"]
    _cod=data["cod"]
    print("***More Inf***")
    print("Shift in seconds from UTC:\t",_timezone )
    print("City ID:\t\t\t",_id )
    print("City name:\t\t\t",_name )
    print("req,Internal parameter:\t\t",_cod )
