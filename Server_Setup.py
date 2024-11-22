from flask import Flask, Response, request
import requests


app = Flask(__name__)


@app.route('/sanity')
def sanity():return "Server is running"



TOKEN = '7467453386:AAEPsIImeqVnwNfeARnSU_WGeqMVtbTqRXM'
TELEGRAM_INIT_WEBHOOK_URL = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://67f4-147-235-214-197.ngrok-free.app/message'


requests.get(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")
    chat_id = request.get_json()['message']['chat']['id']
    res = requests.get("https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={11}&text={got it}'"
                       .format(TOKEN, chat_id, "Got it"))
    return Response("success")


if __name__ == '__main__':
    app.run(port=5002)

