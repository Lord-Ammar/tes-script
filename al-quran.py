#Don't Decode This Script
#Decompile By ©AmmarBN









































































































import requests as r, os,time
from bs4 import BeautifulSoup as par
clear = lambda : os.system('clear')

localtime = time.asctime(time.localtime(time.time()))
def main():
	clear()
	print(''' ▄▀▄ █░░   ▄▀█ █░█ █▀▀▄ ▄▀▄ █▄░█
 █▀█ █░▄   █░█ █░█ █▐█▀ █▀█ █░▀█
 ▀░▀ ▀▀▀   ░▀█ ░▀░ ▀░▀▀ ▀░▀ ▀░░▀
\x1b[1;97m=============================================
\x1b[1;91m   * \x1b[1;97mAuthor : \x1b[1;92mAmmarBN
\x1b[1;91m   * \x1b[1;97mSupport: \x1b[1;92mArifatul Nurul
\x1b[1;91m   * \x1b[1;97mTeam   : \x1b[1;92mPython Cyber Team
\x1b[1;91m   * \x1b[1;97mGithub : \x1b[1;92mhttps://github.com/Lord-Ammar
\x1b[1;91m   * \x1b[1;97mWaktu  : \x1b[1;92m'''+localtime)
	os.system('python ip.py')
	print('''\x1b[1;97m=============================================''')
	try:
		a = r.get('https://litequran.net').text
	except r.exceptions.ConnectionError:
		exit('\x1b[1;91m! \x1b[1;97mTidak Ada Koneksi')
	a = par(a,'html.parser')
	print('\n\x1b[1;92m1\x1b[1;91m. Exit This Program')
	# <!-- Variabel --!>
	no, ayat, bacaan, arti, link = 0, 0, 0, 0, []
	for x in a.find_all('a'):
		no += 1
		titel = x.get('title')
		if titel == None:
			pass
		else:
			print(f'\x1b[1;92m{str(no)}\x1b[1;91m. \x1b[1;97m{titel}')
	for z in a.find_all('a'):
		run = z.get('href')
		link.append(run)
	try:
		pil = input('\033[1;95m[\033[1;90m•\033[1;95m]\033[1;96m Input Menu:\033[1;93m ')
		if pil =='1':
			exit('\x1b[1;91m! \x1b[1;97mEnd Program Page')
		else:
			pil = int(pil) - 1
			lanjut = r.get(str(link[pil])).text
			scrap = par(lanjut,'html.parser')
			find1 = scrap.find('h1', class_="page-title").text
			print("\x1b[1;97m="*45)
			print("\x1b[1;92m            "+find1)
			print("\x1b[1;97m="*45)
			print("\x1b[1;97mTulisan Arab: \n")
			for al in scrap.find_all('span', class_="ayat"):
				ayat += 1
				al = (al.text)
				print(f'\x1b[1;92m{str(ayat)}\x1b[1;91m.\x1b[1;97m {al.strip()}')
			print("\x1b[1;97m="*45)
			print("Cara Bacanya: \n")
			for bc in scrap.find_all('span', class_="bacaan"):
				bacaan += 1
				bc = (bc.text)
				print(f'\x1b[1;92m{str(bacaan)}\x1b[1;91m. \x1b[1;97m{bc.strip()}')
			print("\x1b[1;97m="*45)
			print("Artinya: \n")
			for ar in scrap.find_all('span', class_="arti"):
				arti += 1
				ar = (ar.text)
				print(f'\x1b[1;92m{str(arti)}\x1b[1;91m. \x1b[1;97m{ar.strip()}')
			print("="*45)
	except ValueError:
	        exit('\x1b[1;91m! \x1b[1;97mWrong Input!!')
	except IndexError:
	        exit('\x1b[1;91m! \x1b[1;97mIsi Dengan Benar Gan')

if __name__=='__main__':
	main()

# <!-- Copyright By AmmarBN
# <!-- THANKS TO ALL MEMBER Python Cyber Team
