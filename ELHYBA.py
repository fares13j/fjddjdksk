from mody import Mody
import requests
import telebot
import time, Python, marshal, zlib, py_compile
import os , sys
token = Mody.ELHYBA
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def start(message):
 
 bot.send_message(message.chat.id,f"""<strong>❀~ مرحبا انا بوت تشفير الملفات 🧑🏻‍💻 .
♆〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰♆

❀~ نوع تشفير : marshal, Python, zlib 🔒 .
❀~ الفئه : null 🌪️ .
❀~ عدد طبقات : 6 🚸 .

♆〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰♆</strong>""",parse_mode="html")
 @bot.message_handler(content_types=['document'])
 def send(message):
 	 bot.get_file(message.document.file_id)
 	 #bot.download_file(file_info.file_path)
 	# bot.send_photo(message.chat.id,open("file","rb"))
 	 file_info = bot.get_file(message.document.file_id)
 	 use = bot.download_file(file_info.file_path)
 	 bot.send_message(message.chat.id, f"""<strong>انتظر…</strong>""",parse_mode="html")
 	 cv =str("#@J_G_JG")
 	 sa = compile(use, 'dg', 'exec')
 	 sb = marshal.dumps(sa)
 	 sc = zlib.compress(sb)
 	 sd = base64.b85encode(sc)
 	 b = '#https://@J_G_JG\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b85decode(' + repr(sd) + '))))'
 	 d = open('[@J_G_JG].py', 'w')
 	 d.write(b+'\n'+cv)
 	 d.close()
 	 file = {'document':open('[@J_G_JG].py','rb')}
 	 tex = ("❀~ تم التشفير بواسطة : @J_G_JG\n❀~ شكرا لاستخدامك بوت التشفير الخاص بنا 🚸\n❀~ كل ما يهمنا هو سعادتكم و امانكم 🔱\n❀~ للتواصل مع المطور @J_G_JG")
 	 requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={message.chat.id}&caption={tex}', files=file)
 	 bot.send_message(message.chat.id, f"[🔱 @J_G_JG 🔱](t.me/J_G_JG)",parse_mode="markdown",disable_web_page_preview="true")
 	 os.system(f'rm -rf [@J_G_JG].py')

print ("تم التشغيل بنجاح بواسطة @J_G_JG")
  	
bot.polling(True)

#هذه هي المصادر لا تغيرها
#المطور @J_G_JG