from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/sanity')
def sanity():
    return "Server is running"

TOKEN = '7467453386:AAEPsIImeqVnwNfeARnSU_WGeqMVtbTqRXM'
WEBHOOK_URL = 'https://67f4-147-235-214-197.ngrok-free.app/message'
TELEGRAM_INIT_WEBHOOK_URL = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}'

# Initialize webhook
response = requests.get(TELEGRAM_INIT_WEBHOOK_URL)
if response.status_code == 200:
    print("Webhook set successfully!")
else:
    print(f"Failed to set webhook: {response.status_code}, {response.text}")

@app.route('/message', methods=["POST"])
def handle_message():
    try:
        print("Received a message")
        message = request.get_json()
        print(f"Message JSON: {message}")

        # Extract chat_id
        chat_id = message['message']['chat']['id']
        # Send response back to the user
        reply_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": chat_id, "text": "Got it"}
        res = requests.post(reply_url, json=payload)

        if res.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message: {res.status_code}, {res.text}")

        return Response("success")
    except Exception as e:
        print(f"Error handling message: {e}")
        return Response("failure", status=500)

if __name__ == '__main__':
    app.run(port=5002)
