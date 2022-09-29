from datetime import datetime

import requests
import time

def format_message(message):
    name= message['name']
    text= message['text']
    dt=datetime.fromtimestamp(message['time'])
    dt_beauty=dt.strftime('%Y/%m/%d %H:%M:%S')
    return f'{name} {dt_beauty}\n{text}\n'

after = time.time() - 24 * 60 * 60
while True:
    responce = requests.get('http://127.0.0.1:5000/messages', params={'after': after})
    messages = responce.json()['messages']
    for message in messages:
        print(format_message(message))

        after1 = message['time']
        if after1>=after:
            after=after1
    time.sleep(1)

