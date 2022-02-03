#Don't Decode This Script
#Decompile By ©AmmarBN









































































































import requests as r, os,time
from bs4 import BeautifulSoup as par
clear = lambda : os.system('clear')

IP = r.get('https://api.ipify.org').text
localtime = time.asctime(time.localtime(time.time()))
def main():
	clear()
	print('''
				\033[1;95m╔═╗\033[1;97m┬   \033[1;95m╔═╗ \033[1;97m┬ ┬┬─┐┌─┐┌┐┌
				\033[1;95m╠═╣\033[1;97m│───\033[1;95m║═╬╗\033[1;97m│ │├┬┘├─┤│││
				\033[1;95m╩ ╩\033[1;97m┴─┘ \033[1;95m╚═╝╚\033[1;97m└─┘┴└─┴ ┴┘└┘
			         [\033[1;0m\033[1;41mCreated By ©AmmarBN\033[1;0m]
────────────────────────────────────────────────────────────────────────────────────────────────────''')
	print ("")
	print ("     •  Creator\033[1;93m: \033[1;97mAmmarBN")
	print ("\033[1;97m     •  Your IP\033[1;93m: \033[1;92m"+IP)
	print ("\033[1;97m     •  Youtube\033[1;93m: \033[1;97mAmmarBN")
	print ("\033[1;97m     •  Github\033[1;93m: \033[1;92mgithub.com/Lord-Ammar")
	print ("\033[1;97m     •  Waktu\033[1;93m: \033[1;92m"+localtime)
	print ("\033[1;97m")
	print ("────────────────────────────────────────────────────────────────────────────────────────────────────")
	try:
		a = r.get('https://litequran.net').text
	except ModuleNotFoundError:
		print("Module Data Belum Terinstall...")
		time.sleep(2)
		print("Install Module (Install Data Module)")
		os.system("pip install requests && pip2 install requests && pip install bs4 && pip2 install bs4")
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
