import urllib
import requests

def get(text):
  sourceLang = 'auto'
  sourceText = text
  targetLang = 'lv'

  url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl="+\
  	sourceLang+ "&tl=" + targetLang + "&dt=t&q=" + urllib.quote(sourceText)
  
  r = requests.get(url)
  r = r.json()
  return r[0][0][0]