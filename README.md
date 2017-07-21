# smser
A python script that gets the weather forecast from [OpenWeatherMap](https://openweathermap.org) API translates it into Latvian with Google translator and then sends it to the specified phones using [Twilio API](https://www.twilio.com/). 

# To Run
Rename shared(template).py to shared.py and add your API keys, if you live in Riga, you're done, if not the you probably want to tweak a bit the get_weather.py and translate_to_lv.py

Send 24h weather forecast with SMS:
```sh
$ python send_sms.py
```


