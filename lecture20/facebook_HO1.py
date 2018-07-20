import requests
import json

def removeUnicode(text):
        asciiText = ""
        for char in text:
            if (ord(char) < 128):
                asciiText = asciiText + char
                
        return asciiText

ACCESS_TOKEN = 'your_key_here'
fb_url = 'https://graph.facebook.com/me'
fields = 'id,name'
url = '%s?fields=%s&access_token=%s'% (fb_url, fields, ACCESS_TOKEN,)
results = requests.get(url).json()
print json.dumps(results, indent = 1)