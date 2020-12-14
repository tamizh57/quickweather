# Python program to find   
# weather details of any city 
# using openweathermap api 
  

import requests, json, pprint 


#api key for openweather.org
api_key = "66f4d47306b215cafcfe2300480b2c04"

# base_url
url = "https://api.openweathermap.org/data/2.5/onecall"  



#function to get coordinates
def getcoords(city, apikey):
    r = requests.get(url= "https://api.openweathermap.org/data/2.5/weather", params={'q': city,'appid': apikey})
    coords =  r.json()
    return [coords["coord"]["lat"],coords["coord"]["lon"]]

#function to get weather data
def getweatherdata(url,lat,lon, exclude):
    weather_params = {'apikey':api_key,'lat':lat,'lon':lon,'units':'metric','lang':'en', 'exclude':exclude}
    response = requests.get(url = url, params = weather_params)
    return json.loads(response.text)



#getting options from user to choose type of weather data
print('\n')
print('''Please choose from below options
--------------------------------
1. current report
2. minutely report for next 1 hour
3. hourly report for next 48 hours
4. daiy report for next 7 days\n''')

option = int(input("Option: "))

exlist = ["current","minutely","hourly","daily","alerts"]
exclude = ",".join([x for x in exlist if x != exlist[option - 1] ])

  
# calling getcoords to get latitude and longitude
coords = getcoords(input("Enter city name : "), api_key)
latitude = coords[0]
longitude = coords[1]

#calling getweatherdata
weatherdata = getweatherdata(url,latitude,longitude,exclude)


pprint.pprint(weatherdata)
