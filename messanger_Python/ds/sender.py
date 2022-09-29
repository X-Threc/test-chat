import requests


name = input('имя: ')
password=input('пароль: ')

while True:
    text = input()
    message = {'name': name,
               'password':password,
               'text': text}
    responce = requests.post('http://127.0.0.1:5000/send', json=message)

