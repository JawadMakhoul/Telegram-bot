from flask import Flask, Response
import requests


app = Flask(__name__)


@app.route('/sanity')
def sanity():return "Server is running"



TOKEN = '7467453386:AAEPsIImeqVnwNfeARnSU_WGeqMVtbTqRXM'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://67f4-147-235-214-197.ngrok-free.app/message'.format(TOKEN)

requests.get(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")
    return Response("success")



if __name__ == '__main__':
    app.run(port=5002)

