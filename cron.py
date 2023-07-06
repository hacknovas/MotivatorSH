from apscheduler.schedulers.background import BackgroundScheduler
from pyMotivator import send_whatsapp_text,client,quote
import time

scheduler=BackgroundScheduler(timezone="Asia/KolKata")
scheduler.start()

job=scheduler.add_job(send_whatsapp_text,'cron',[client,quote[0]["quote"]],hour="17",minute="50")

print(job)

while(True):
    time.sleep(1)
