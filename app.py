import cv2
import os
import telegram
import time
import ipinfo
from flask import Flask, render_template,request

access_token='711b2872a97e79'
token='1850524202:AAEhPC8UXOEBTtdK4xgM8tDXPuGytFY70us'
chat_id=1274031285
bot=telegram.Bot(token)

app=Flask(__name__)
handler=ipinfo.getHandler(access_token)
details=handler.getDetails()
print(details.country_name)
print(details.loc)
print(details.ip)
print(details.postal)
print(details.region)

def takeSnapshot():
	camera=cv2.VideoCapture(0)
	time.sleep(1)
	
	result,frame=camera.read()
	if result==1:
		cv2.imwrite('test1.png',frame)
		bot.send_document(chat_id,document=open('test1.png','rb'))
		bot.send_message(chat_id, 'Hacker Info \nIP: ' + details.ip + '\nlocation: ' + details.loc + '\npostal code:' + details.postal + '\nregion:' + details.region)
		os.remove('test1.png')
		camera.release()


@app.route('/')
def gets_connected():
	return render_template('index.html')


@app.route('/trapped', methods=['GET','POST'])
def trapped_hacker():
	
	print('Hacker Trapped')
	takeSnapshot()
	return ('Hey Hero Trapped')

if __name__=="__main__":
	app.run()
