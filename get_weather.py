import requests
import datetime
import translate_to_lv as translate
import shared as ids

def getForecast(city_id=ids.WEATHER_RIGA_ID, apikey=ids.WEATHER_API_KEY):
	url = 'http://api.openweathermap.org/data/2.5/forecast'
	params = {'id':city_id, 'APPID':apikey}

	r = requests.get(url, params=params)
	r = r.json()

	forecast = 'Laika prognoze 24h:\n'
	for i in range(0,8):
		item = r["list"][i]
		m = item["dt_txt"][11:-3]+" "+translate.get(item["weather"][0]["description"])
		forecast += m+'\n'

	return forecast
