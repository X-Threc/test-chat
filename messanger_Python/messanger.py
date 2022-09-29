from _datetime import datetime
import time
from PyQt5 import QtWidgets, QtCore
from clientui import Ui_MainWindow
import requests


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,url):
        super().__init__()
        self.setupUi(self)
        self.url=url
        self.pushButton.pressed.connect(self.send_message)
        self.after= time.time() - 24 * 60 * 60
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    def add_text(self,text):
        self.textBrowser.append(text)
        self.textBrowser.append('\n')
        self.textBrowser.repaint()

    def format_message(self,message):
        name = message['name']
        text = message['text']
        dt = datetime.fromtimestamp(message['time'])
        dt_beauty = dt.strftime('%Y/%m/%d %H:%M:%S')
        return f'{name} {dt_beauty}\n{text}'

    def update_messages(self):
        try:
            responce = requests.get(f'{self.url}messages', params={'after': self.after})
        except:
            return
        messages = responce.json()['messages']
        for message in messages:
            self.add_text(self.format_message(message))
            self.after = message['time']

    def send_message(self):
        name = self.lineEditName.text()
        password = self.lineEditPass.text()
        text = self.textEdit.toPlainText()
        if not name or not password or not text:
            self.add_text('Введите данные')
            return

        message = {'name': name,
                   'password': password,
                   'text': text}
        try:
            responce = requests.post(f'{self.url}send', json=message)
        except:
            self.add_text('сервер недоступен')
            return

        if responce.status_code==200:
            self.textEdit.setText('')
            self.textEdit.repaint()
        elif responce.status_code==401:
            self.add_text('неправильный логин или пароль')
        else:
            self.add_text('Ошибка')




app = QtWidgets.QApplication([])
window=ExampleApp('http://127.0.0.1:5000/')
window.show()
app.exec_()

