import os
import speech_recognition as sr
import random
import datetime
import pyttsx3
import subprocess
import wikipedia
import webbrowser
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests as rq

totalsource = rq.get('https://www.worldometers.info/coronavirus').text.encode('utf-8')

cnts = []

bs = BeautifulSoup(totalsource, 'lxml')
var = bs.find(attrs={"id":"main_table_countries_today"})
val = var.find_all('tbody')[0].find_all('tr')
for i in val:
	s = i.find_all('td', style="font-weight: bold; font-size:15px; text-align:left;")
	if s:
		for j in s:
			if j.a:
				cnts.append(j.a.text)

global prev
prev = ''

def tell(text):
	global prev
	e = pyttsx3.init()
	e.say(text)
	e.runAndWait()
	print('-' + text )
	prev = text

def get_what_telling():
	sp = sr.Recognizer()
	with sr.Microphone(device_index=1) as src:
		listen = sp.listen(src)
		said = ''
		try:
			# sp.energy_threshold = 4000
			# sp.pause_threshold=1
			sp.adjust_for_ambient_noise(src,3) 
			said = sp.recognize_google(listen)
			print('                -' + said)
		except Exception as e:
			print('Can you repeat again? please pardon me.')
	return said.lower()


# def get_what_telling():
# 	inp = input('User: ')

# 	return inp

def tellStats(inp):
	country = inp

	url = f'https://www.worldometers.info/coronavirus/country/{country}'

	src = rq.get(url).text.encode('utf-8')
	soup = BeautifulSoup(src, 'lxml')

	total = soup.find_all("div",
				 id="maincounter-wrap")
	deaths = ''
	cases = ''
	recovered = ''
	for i in total:
		if i.h1 != None:
			if i.h1.text == 'Deaths:':
				deaths = i.div.span.text
			if i.h1.text == 'Coronavirus Cases:':
				cases = i.div.span.text
			if i.h1.text == 'Recovered:':
				recovered = i.div.span.text
	if cases:
		tell('cases are ' + cases+ ', recoveries are ' + recovered + ', deaths are ' + deaths )
	else:
		if country not in cnts:
			tell(text = 'Incorrect country name entered!')

def noteThings(text):
	date = datetime.datetime.now()
	file = str(date).replace(':', '-') + '-note.txt'
	with open(file, 'w') as f:
		f.write(text)
	sublime = 'E:\\sublime text\\Sublime Text portable\\sublime_text.exe'
	subprocess.Popen([sublime, file])



def wish():
	hour = datetime.datetime.now().hour
	if hour >= 0 and hour < 12:
		tell('Good Morning, How can I be of your assistance')
	elif hour >= 12 and hour < 17:
		tell('Good Afternoon, How can I be of your assistance')
	else:
		tell('Good Evening, Ali, How can I be of your assistance')

wake = 'hey Jarvis'
# if __name__ == '__main__':
wish()
run = True
quitstr = ['quit', 'deactivate', 'end', 'finish']
cmdlist = ['cmd', 'command prompt', 'command shell']
notelist = ['write', 'note']
greetlist = ['hi', 'bye', 'morning','night','evening','afternoon','hello']
thanks = ['thanking','thank','awesome','nice','good','wow']
askcovid = ['coronavirus', 'covid','cases','corona']
repeat = ['repeat', 'again','one more time']

while run:
	print('Listening.....')
	qy = get_what_telling()


	if wake in qy:
		tell("yes, I'm there!")
	elif 'wikipedia' in qy:
		qry = qy.replace('wikipedia', '')
		try:
			result = wikipedia.summary(qry, sentences=2)
			tell('According to wikipedia, I can tell')
			tell(result)
			print(str(result))
		except:
			error = 'page not found or There are many ids, try another id'
			tell(error)
	elif 'open youtube' in qy:
		webbrowser.open('youtube.com')
	elif 'open google' in qy and 'search' not in qy:
		webbrowser.open('google.com')
	elif 'search' in qy:
		tell('what must I search?')
		qy = get_what_telling()
		if qy != 'nothing':
			webbrowser.open('http://google.com/?q=' + qy)
		else:
			tell('ok, then i m doing nothing')
	elif 'open bing' in qy:
		webbrowser.open('bing.com')
	elif 'open gmail' in qy:
		webbrowser.open('gmail.com')
	elif 'open yahoo' in qy:
		webbrowser.open('yahoo.com')
	elif 'play music' in qy:
		msc_dir = 'C:\\Users\\user\\Documents\\Songs'
		music = os.listdir(msc_dir)
		os.startfile(os.path.join(msc_dir, music[0]))
	elif 'open sublime' in qy:
		sublime = 'E:\\sublime text\\Sublime Text portable\\sublime_text.exe'
		os.startfile(sublime)
	elif 'open notepad' in qy:
		notepad = 'C:\\Windows\\system32\\notepad.exe'
		os.startfile(notepad)
	elif 'open whatsapp' in qy:
		wtsapp = 'C:\\Users\\user\\AppData\\Local\\whatsapp.exe'
		os.startfile(wtsapp)
	elif 'how are you' in qy:
		tell('I am fine')
	for x in askcovid:
		if x in qy:
			tell('For which country should I tell?')
			inpt = get_what_telling()
			tellStats(inpt.lower())

	for x in cmdlist:
		if x in qy:
			cmd = 'C:\\Windows\\system32\\cmd.exe'
			os.startfile(cmd)
	for x in greetlist:
		if x in qy:
			tell('Hi there!')
	for x in notelist:
		if x in qy and 'pad' not in qy:
			tell('what must I note ?')
			qy = get_what_telling()
			noteThings(qy)
	for x in repeat:
		if x in qy:
			tell(prev)
	for x in thanks:
		if x in qy:
			tell("Your Welcome, It's my pleasure!")
	for x in quitstr:
		if x in qy:
			run = False


