import requests
from twillo_conn import send_whatsapp_text,set_twilio_conn

def get_quote_of_day(category):

    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)

    response = requests.get(api_url, headers={'X-Api-Key': 'WNvlHG7Wbvtnvsf1MHIO0g==plvqrwcTfgHUfhU5'})

    match response.status_code:
        case 200:
            return response.json()
        case _:
            return "Error"

quote=get_quote_of_day("happiness")
client=set_twilio_conn()