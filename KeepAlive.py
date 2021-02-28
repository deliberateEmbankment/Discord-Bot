#This allows the bot to run even if the repl is closed. It will enter a sleep state if it did not receive a request for an hour. It will wake up once it gets another requests

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()