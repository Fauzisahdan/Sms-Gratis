#!/usr/bin/python2

# Creator :  ./FUKUR0-3XP
# Team : Black Coders Satanic Exploiter Team ( BCA - X666X )
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode :3

from time import sleep
from bs4 import BeautifulSoup as Bs
import mechanize, cookielib, random, urllib2, sys, re, os

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

os.system('clear')

def MesinTik(text):
	for x in text + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(random.random() * 0.02)
                                            
def Banner():
	MesinTik(''+C+'''
  ______                _____               
 |  ____|              / ____|              
 | |__ _ __ ___  ___  | (___  _ __ ___  ___ 
 |  __| '__/ _ \/ _ \  \___ \| '_ ` _ \/ __|
 | |  | | |  __/  __/  ____) | | | | | \__ \\
 |_|  |_|  \___|\___| |_____/|_| |_| |_|___/
                '''+W+'Creator : ./Fukur0\n\t\t   YT : Mr.Ucok')
     
                   
def FreeSms():
	print
	print
	number = raw_input(C+'NOMOR TARGET'+W+' ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
	msg = raw_input(C+'ISI PESAN'+W+' ('+H+' Ex :'+C+' Hai Bro !'+W+' ) : ')
	
	kode = 'AbCdEfGhIjKlMnOpQrStUvWxYz1234567890'
	Random = ''.join([random.choice(kode) for _ in range(5)])
	message = msg +'\n'+(26*'-')+'\nKode : '+str(Random).upper()
	
	print
	MesinTik(''+C+'-------------- '+W+'Starting'+C+' --------------')
	print
	
	try:
		
		bro = mechanize.Browser()
		Cookie = cookielib.LWPCookieJar()
		
		bro.set_handle_robots(False)
		bro.set_cookiejar(Cookie)
		
		bro.addheaders = [
		('User-Agent', 'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36'),
		('Referer', 'http://sms.payuterus.biz/alpha')
		]
		
		url = 'http://sms.payuterus.biz/alpha/'
		
		open_web = bro.open(url).read()
		soup = Bs(open_web, 'html.parser')
		finder =  re.search(r'\<input\ type\=\'hidden\'\ name\=\"key\"\ value\=\"(.*?)\"\>', open_web).group(1)
		find_tag = soup.find('span').text
		
		captcha = find_tag.strip().split('+')[0].replace('=','')
		captcha_2 = find_tag.strip().split('+')[1].replace('=','')
		add = int(captcha) + int(captcha_2)
		
		bro.select_form(nr=0)
		bro.form ['nohp'] = number
		bro.form ['pesan'] = message
		bro.form ['captcha'] = str(add)
		bro.submit()
		
		if bro.geturl() == 'http://sms.payuterus.biz/alpha/send.php':
			print(C+'Pesan'+W+' : '+msg);sleep(1)
			print(C+'Nomor'+W+' : '+number);sleep(1)
			print(H+'Berhasil'+W+' Di Kirimkan :)')
			
		else:
			print(C+'Pesan'+W+' : '+msg);sleep(1)
			print(C+'Nomor'+W+' : '+number);sleep(1)
			print(H+'Gagal'+W+' Di Kirimkan :(')
			
	except urllib2.URLError:
		print(M+'Cek Koneksi Jaringan !')
		
if __name__ == '__main__':
	os.system('clear')
	print(C+'Subscribe YT'+W+' Gua Dlu Su !'+C+' :V')
	sleep(1.5)
	os.system('xdg-open https://www.youtube.com/channel/UCx2f35A_IwvnzteWWWU8tAg ')
	os.system('clear')
	sleep(1.3)
	Banner()
	FreeSms()
