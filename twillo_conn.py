from twilio.rest import Client
from config import auth_token,account_sid,Phone

def set_twilio_conn():
    client = Client(account_sid, auth_token)
    return client

def send_whatsapp_text(client,quote):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=quote,
        to=Phone
    )

    return message.sid


