#!/usr/bin/python3

"Import Module"
import os,sys,time,getpass
from platform import system

"Warna"
Hijau='\033[32m'
Biru='\033[34m'
Merah='\033[31m'
Putih='\033[37m'
Hitam='\033[30m'
Pink='\033[95m'
end="\033[0m"

"resize"
os.system("resize -s 25 95 > /dev/null")

"Functions Untuk Bantuan Nanti"

#Menghapus Directori Lock
def remv():
	os.system("rm -r /var/lib/dpkg/lock")
	os.system("rm -r /var/cache/apt/archives/lock")

#Perintah Output untuk Keluar
def tekan():
	input("Tekan Enter Untuk Melanjutkan atau Ctrl + C Untuk Keluar : ")

#Perintah Membersihkan Terminal
def clear():
	os.system("clear && clear")

#Ping Ke google Untuk Cek Koneksi
def Koneksi():
	cmd_koneksi = cdm_koneksi = os.system('ping -c 1 google.com')
	clear()
	if cdm_koneksi == 512 :
		clear()
		print("\n")
		print(Merah+'[!] Tools Ini Membutuhkan Koneksi Internet ')
		print("\n")
		sys.exit(1)
	else :
		time.sleep(1)
		print("[+] Koneksi Internet"+Hijau+"		[AMAN]"+end)
		time.sleep(1)

#perintah untuk Menjalankan Program dengan Akses ROOT
def root():

	Root = os.getuid()
	if Root != 0:
		clear()
		print(Merah+"[!] Jalankan Program Ini Dengan ROOT"+end)
		exit(1)
	else :
		print("Menjalankan Sebagai ROOT"+Hijau+"	   [OK]")
		time.sleep(1)
		print("")

# OS Diharuskan Menggunakan LINUX
linux = system()
if linux != "Linux":
	print(Merah+"[!] OS = {}".format(linux()))
	print("[!] OS Linux / Unix Dibutuhkan ")
	sys.exit(1)
else:
	pass
#else adalah Perintah Pilihan terakhir jika tidak ada parameter yang bernilai True
#Jadi Jika kalau semua-nya salah mau tidak mau Perintah else ini harus dijalankan....

"banner"
def banner_Lab():

		clear()
		time.sleep(1)
		print(Hijau+"""


        ██           ██     ████████ ██    ██   ██           ██     ██████
       ░██          ████   ░░░░░░██ ░░██  ██   ░██          ████   ░█░░░░██
       ░██         ██░░██       ██   ░░████    ░██         ██░░██  ░█   ░██
       ░██        ██  ░░██     ██     ░░██     ░██        ██  ░░██ ░██████
       ░██       ██████████   ██       ░██     ░██       ██████████░█░░░░ ██
       ░██      ░██░░░░░░██  ██        ░██     ░██      ░██░░░░░░██░█    ░██
       ░████████░██     ░██ ████████   ░██     ░████████░██     ░██░███████
       ░░░░░░░░ ░░      ░░ ░░░░░░░░    ░░      ░░░░░░░░ ░░      ░░ ░░░░░░░

""")

"Waktunya Untuk ngoding :) "

#Def Adalah Perintah Program Untuk Mengembalikan Suatu Nilai Parameter,
#Jadi Perintah Ini dapat Digunakan Berkali kali tanpa Harus Memulai Ulang kembali....

def Utama():

#perintah untuk input data front end
	try:
		banner_Lab()
		print("")
		print(Putih+"""
			    Dibuat Oleh :> {0}
			    Tanggal  	:> {1}

				[1]>	Update & Upgrade Linux
				[2]>	Install PIP
				[3]> 	Install Module Python
				[4]> 	Install Program github
				[5]> 	Tentang Kami  (Kelompok 4)

				[0]> 	[ Keluar ]
	""".format(Biru+"Kelompok 4"+end+Putih,Biru+"22/05/2022"+end+Putih)+end)
		skrip_males = str(input("	[?]#> "))

#perintah format() itu berfungsi untuk mengatur String untuk ditampilkan ke monitor

#menjalankan Perintah untuk update & upgrade OS Linux
		def up():
			os.system("apt update")
			remv()
			yesono = str(input(Biru+"\n[?] Apakah Kamu mau melanjutkan? [Y/N] #> "+end))
			if yesono == "Y" or yesono == "y":
				os.system("apt full-upgrade -y")
				print("")
				tekan()
				time.sleep(1)
				remv()
				Utama()
			else :
				print(Merah+"[!] OK "+end)
				tekan()
				Utama()

#perintah input untuk penginstalan versi PIP
		def pip():
			os.system("apt update")
			print("")
			print(Putih+"Pilih Versi PIP Untuk Di install :")
			print("")
			print("""
		1) PIP
		2) PIP3
	""")

#Perintah Input 1 untuk memulai program penginstalan pip versi 2

			ver = str(input("		[?]#> "+end))
			if ver == "1":
				remv()
				os.system("apt install python-pip -y")
				print("")
				print("")
				tekan()
				remv()
				Utama()

#Perintah Input 2 untuk memulai penginstalan pip versi 3
			elif ver == "2":
				os.system("apt install python3-pip -y")
				remv()
				print("")
				print("")
				tekan()
				Utama()

			else:
				print(Merah+"[!] Jawaban Kamu Salah")
				tekan()
				Utama()

#Program untuk menampilkan banner_Lab
		def python_modul():
			logo = Merah+"""








               ████     ████               ██          ██
              ░██░██   ██░██              ░██         ░██
              ░██░░██ ██ ░██  ██████      ░██ ██   ██ ░██  █████
              ░██ ░░███  ░██ ██░░░░██  ██████░██  ░██ ░██ ██░░░██
              ░██  ░░█   ░██░██   ░██ ██░░░██░██  ░██ ░██░███████
              ░██   ░    ░██░██   ░██░██  ░██░██  ░██ ░██░██░░░░
              ░██        ░██░░██████ ░░██████░░██████ ███░░██████
              ░░         ░░  ░░░░░░   ░░░░░░  ░░░░░░ ░░░  ░░░░░░
                          ██           ██     ██████
                         ░██          ████   ░█░░░░██
                         ░██         ██░░██  ░█   ░██
                         ░██        ██  ░░██ ░██████
                         ░██       ██████████░█░░░░ ██
                         ░██      ░██░░░░░░██░█    ░██
                         ░████████░██     ░██░███████
                         ░░░░░░░░ ░░      ░░ ░░░░░░░




"""+end

			print(logo)
			tekan()
			clear()
			time.sleep(1)

#Mengecek Jalur penginstalan Pip apakah sudah Di install atau Belum...

			anon = os.path.exists("/usr/bin/pip")
			if anon == True:
				print ("")
				print ("")
				print (Hijau+"\n	[+] pip 		[DITEMUKAN]")
				print ("")

#jika module pip tidak ditemukan maka perintah else akan di esekusi untuk
#menampilkan output bahwa pip belum terinstalll

			else :
				print (Merah+"\n	[!] pip 		[TIDAK DITEMUKAN]")
				print ("	Apakah Kamu Mau Menginstall PIP?? [Y/N] "+end)
				print ("")
				nigga = str(input("[?]#> "))
				if nigga == "y" or nigga == "Y":
					remv()
					pip()
				else:
					tekan()
					Utama()

#pengecekan module pip versi 3 apakah sudah di install atau belum...

			anon2 = os.path.exists("/usr/bin/pip3")
			if anon2 == True:
				print (Hijau+"	[+] pip3          	[DITEMUKAN]")
				print ("")
			else:
				print (Merah+"	[!] pip3         	[TIDAK DITEMUKAN]")
				print ("	Apakah Kamu Mau Menginstall PIP3 [Y/N] "+end)
				print ("")
				nigga2 = str(input("[?]#> "))
				if nigga2 == "y" or nigga2 == "Y":
					remv()
					pip()
				else:
					tekan()
					Utama()

# Perintah input untuk memilih penginstalan module python dengan jalur penginstalan pip versi 2 atau 3

			print(Putih+"""

Pilih Module Python :

	1)  urllib 		[pip3,pip]		9)  Random		[pip3,pip]
	2)  Mechanize		[pip3,pip]		10) PyQT		[pip3,pip]
	3)  BeautifulSoup	[pip3,pip]		11) OptParse		[pip3,pip]
	4)  PyAutoGUI		[pip3,pip]		12) SMTPLib		[pip3,pip]
	5)  Selenium		[pip3,pip]		13) FTPLib		[pip3,pip]
	6)  PyGame		[pip3,pip]		14) PxSsh		[pip3,pip]
	7)  Tqdm		[pip3,pip]		15) Xmpppy		[pip3,pip]
	8)  Socket		[pip3,pip]		16) HashLib		[pip3,pip]
							17) Thread		[pip3,pip]

				    	   99) [ Kembali ]
	""")

# Jika Pengguna Memilih 1 maka program yang di jalankan adalah penginstalan module urllib
# Fungsi module urllib yaitu untuk membuka atau membaca URL. module ini berfungsi untuk melakukan
# Request HTTP pada halaman website..

			module_paket = str(input("[?]#> "))
			if module_paket == "1":
				os.system("pip3 install urllib3")
				os.system("pip install urllib")
				tekan()
				Utama()

# Pilihan ke 2 adalah penginstalan module mechanize, Dimana ini bisa berfungsi Untuk
# membuat program login dengan python. ataupun kamu juga bisa melakukan teknik bruceforce untuk login pada
# halaman website

			elif module_paket == "2":
				os.system("pip3 install mechanicalsoup")
				os.system("pip install mechanize")
				tekan()
				Utama()

# bs4 atau module BeautifulSoup, Digunakan untuk mengambil data pada halaman HTMl atau XML.
# BeautifulSoup juga banyak sekali fungsinya untuk pentesting halaman website, module ini bisa
# digunakan juga untuk Melakukan navigasi objek DOM pada HTML.

			elif module_paket == "3":
				os.system("pip3 install bs4")
				os.system("pip install bs4")
				tekan()
				Utama()

# module pyautogui, program ini cukup lumayan canggih dikalangan module python yang lain-banyak
# module ini bisa bekerja dengan otomatis dengan beberapa perintah. fungsinya bisa untuk mengotomatisasi
# interaksi mouse, kata kuci, kotak pesan dan screenshot.

			elif module_paket == "4":
				os.system("pip3 install pyautogui")
				os.system("pip install pyautogui")
				tekan()
				Utama()

# module selenium ini biasanya untuk membuat program test automatis untuk webiste, module ini
# bisa mengotomatiskan pencarian informasi yang dapat membantu programer melakukan pengujian script.
			elif module_paket == "5":
				os.system("pip3 install selenium")
				os.system("pip install selenium")
				tekan()
				Utama()

# module paket pygame, biasanya untuk membuat game yang level-nya tingkat menengah sampai kebawah module Ini
# sering dipakai. module ini memang di rancang untuk membuat game dengan bahasa pemograman python...

			elif module_paket == "6":
				os.system("pip3 install pygame")
				os.system("pip install pygame")
				tekan()
				Utama()

# module ini berfungsi untuk menampilkan progress bar dengan Looping yang cukup sederhana,
# module ini bisa jadi pilihan untuk mempercantik tampilan pada output permograman...

			elif module_paket == "7":
				os.system("pip3 install tqdm")
				os.system("pip install tqdm")
				tekan()
				Utama()

# Module untuk Pemograman Networking python, biasanya digunakan untuk komunikasi dua arah
# seperti membuat server HTTP untuk menampilkan file HTML, CSS atau Javascript pada halaman chrome.

			elif module_paket == "8":
				os.system("pip3 install socket")
				os.system("pip install socket")
				tekan()
				Utama()

# Fungsi Module Random pada python biasanya digunakan untuk menghasilkan parameter angka acak,
# tapi bukan bener bener ngasal yaa.. cara ngacak-nya menggunakan pseudo-acak. Jadi fungsi perintah random()
# untuk menghasilkan angka acak untuk beberapa nilai String
			elif module_paket == "9":
				os.system("pip3 install random")
				os.system("pip install random")
				tekan()
				Utama()

# Module ini cukup lumayan banyak fungsinya, bisa untuk graphic user interface, komunikasi network,
# handle XML dan database SQL juga bisa module handle. Program ini juga cukup berguna pada program python..
			elif module_paket == "10":
				os.system("pip3 install pyqt")
				os.system("pip install pyqt")
				tekan()
				Utama()

# Module ini menjadi pilihan programer python, karena module ini dapat berfungsi untuk membuat Perintah
# Opsi command-line yang dimana banyak digunakan untuk bantuan pengguna program tersebut. Seperti perintah
# Namaprogram.py -h atau Namaprogram.py --help...

			elif module_paket == "11":
				os.system("pip install optparse")
				os.system("pip3 install optparse")
				tekan()
				Utama()

# Module SMTP Server atau SMTPlib ini bisa berfungsi untuk mengirimkan email dari server kita sendiri
# ke email server lain. Entah itu email yang @gmail.com atau @email lain-nya, kita juga bisa mengcostume
# alamat email kita sendiri dengan @domain kita pribadi... biasanya email seperti ini digunakan Untuk
# mengelola bisnis perusahaan yang mempunyai server atau website..

			elif module_paket == "12":
				os.system("pip install smtplib")
				os.system("pip3 install smtplib")
				tekan()
				Utama()

# FTPLib atau File Transfer Protocol ini cukup banyak kita gunakan sehari hari
# khususnya module ini dipakai untuk mendownload suatu file yang tersimpan secara online
# jadi jika kita mendownload file di internet biasanya kita memakai jalur FTP ini..

			elif module_paket == "13":
				os.system("pip install ftplib")
				os.system("pip3 install ftplib")
				tekan()
				Utama()

# module ini dipakai untuk mengatur koneksi SSh pada sebuah server, module ini juga bisa berfungsi
# untuk melakukan sesi login, logout dan command shell via SSh. jadi kita bisa mengatur sebuah Server
# hanya dengan menggunakan terminal command line secara remote.
			elif module_paket == "14":
				os.system("pip install pxssh")
				os.system("pip3 install pxssh")
				tekan()
				Utama()

# Module ini mirip dengan aplikasi yang namanya XAMP, module ini juga bisa dipakai untuk
# membuat jalur koneksi TCP atau Transmission Control Protocol, koneksi internet dari client ke Server
# kita bisa membuat program chattingan dengan module ini dengan bahasa pemograman python...
			elif module_paket == "15":
				os.system("pip install xmppy")
				os.system("pip3 install xmppy")
				tekan()
				Utama()

# Program Algoritma untuk encoding dan Decoding, berfungsi untuk membuat hash suatu password menjadi
# bahasa program. Dengan ada-nya Hash ini manusia jadi tidak bisa membanca password kita secara mentah...
# Contoh-nya :
# Password kamu adalah UBSI KULIAH ONLINE
# maka Jika dihash dengan MD5 adalah ( 04cfdba38a22da3317bc7124e291caec )

			elif module_paket == "16":
				os.system("pip3 install hashlib")
				os.system("pip install hashlib")
				tekan()
				Utama()

# Module thread ini berfungsi untuk memisahkan perintah esekusi pada program python3
# supaya kita tidak harus menunggu python untuk menyelesaikan perintah yang kita jalani
# sebelum-nya. namun menggunakan module ini juga harus dipikirkan resouce-nya jika program
# kita terlalu banyak maka komputer akan meledak hehe...

			elif module_paket == "17":
				os.system("pip install thread")
				os.system("pip3 install thread")
				tekan()
				Utama()

# Perintah 99 untuk kembali ke halaman awal...
			elif module_paket == "99":
				clear()
				Utama()

			else :
				print(Merah+"[!] Pilihan Kamu Salah"+end)
				tekan()
				clear()
				python_modul()
		def tool_python():
			clear()
			print(Merah+"""




                    ██████████                    ██
                   ░░░░░██░░░                    ░██
                       ░██      ██████   ██████  ░██  ██████
                       ░██     ██░░░░██ ██░░░░██ ░██ ██░░░░
                       ░██    ░██   ░██░██   ░██ ░██░░█████
                       ░██    ░██   ░██░██   ░██ ░██ ░░░░░██
                       ░██    ░░██████ ░░██████  ███ ██████
                       ░░      ░░░░░░   ░░░░░░  ░░░ ░░░░░░



"""+end)

#Perintah untuk ke penginstalan program github
			tekan()
			clear()
			time.sleep(1)
			print(Putih+"""


				   @> Bahasa Pemograman
			Silahkan Dipilih Bosque :
			1) Python3.x
			2) Perl
			3) Ruby
			4) PHP

					@> Software github
			5)  Veil-Evation		12) Cupp
			6)  Empire			13) Fsociety
			7)  Shellphish			14) Backdoor-Apk
			8)  Hitameye			15) Katoolin
			9)  Evil-Droid			16) FaceBash
			10) Netool-SH 			17) InstaShell
			11) Deliver			18) Fluxion

					19)  Kostum Program
					99) [ Kembali ]
""")

			program_git = str(input("	[?]#> "+end))
			if '1' in program_git or '2' in program_git or '3' in program_git or '4' in program_git :remv()

# Perintah untuk penginstalan program Ular python3

			if program_git == "1":
				os.system("apt install python3")
				tekan()
				clear()
				tool_python()

# Perintah Untuk menginstall Package bahasa pemograman perl
			elif program_git == "2":
				os.system("apt install perl")
				tekan()
				clear()
				tool_python()

# Perintah Untuk menginstall Package bahasa pemograman ruby
			elif program_git == "3":
				os.system("apt install ruby")
				tekan()
				clear()
				tool_python()

# Perintah Untuk menginstall Package bahasa pemograman PHP
			elif program_git == "4":
				os.system("apt install php")
				tekan()
				clear()
				tool_python()

# Perintah Untuk menginstall Package veil Evasion dari dir github
			elif program_git == "5":
				os.system("git clone https://github.com/Veil-Framework/Veil-Evasion")
				tekan()
				clear()
				tool_python()

# Perintah Untuk menginstall Package Empire dari dir github
			elif program_git == "6":
				os.system("git clone https://github.com/EmpireProject/Empire")
				tekan()
				clear()
				tool_python()

# Perintah Untuk menginstall Package Shell Phish dari dir github
			elif program_git == "7":
				os.system("git clone https://github.com/thelinuxchoice/shellphish")
				tekan()
				clear()
				tool_python()

# Perintah Untuk menginstall Package Hitam eye dari dir github
			elif program_git == "8":
				os.system("git clone https://github.com/thelinuxchoice/Hitameye")
				tekan()
				clear()
				tool_python()
			elif program_git == "9":

# Perintah Untuk menginstall Package Evil Droid dari dir github
				os.system("git clone https://github.com/M4sc3r4n0/Evil-Droid")
				tekan()
				clear()
				tool_python()

# Perintah Untuk menginstall Package netool dari dir github
			elif program_git == "10":
				os.system("git clone https://github.com/r00t-3xp10it/netool-toolkit")
				tekan()
				clear()
				tool_python()

# Perintah Untuk menginstall Package Deliver dari dir github
			elif program_git == "11":
				os.system("git clone https://github.com/M4sc3r4n0/deliver")
				tekan()
				clear()
				tool_python()

# Dahlah Capekk eyyy

			elif program_git == "12":
				os.system("git clone https://github.com/Mebus/cupp")
				tekan()
				clear()
				tool_python()
			elif program_git == "13":
				os.system("git clone https://github.com/Manisso/fsociety")
				tekan()
				clear()
				tool_python()
			elif program_git == "14":
				os.system("git clone https://github.com/dana-at-cp/backdoor-apk")
				tekan()
				clear()
				tool_python()
			elif program_git == "15":
				os.system("git clone https://github.com/LionSec/katoolin")
				tekan()
				clear()
				tool_python()
			elif program_git == "16":
				os.system("git clone https://github.com/thelinuxchoice/facebash")
				tekan()
				clear()
				tool_python()
			elif program_git == "17":
				os.system("git clone https://github.com/thelinuxchoice/instashell")
				tekan()
				clear()
				tool_python()

# nah penginstalan dari github hanya sampai sini ajaa
			elif program_git == "18":
				os.system("git clone https://github.com/wi-fi-analyzer/fluxion")
				tekan()
				clear()
				tool_python()
			elif program_git == "99":
				clear()
				Utama()
				tool_python()

# Perintah untuk menginput nama Package sendiri
			elif program_git == "19":
				print("Software apa Yang Ingin Kamu Install?")
				kostum_sendiri = str(input("[?]#> "))
				os.system("apt install {}".format(kostum_sendiri))
				tekan()
				clear()
				tool_python()
			else:
				print(Merah+"[!] Pilihan Kamu Salah "+end)
				tekan()
				clear()
				tool_python()

# Perintah Tentang Kelompok 4
		def tentang_kami():

			clear()
			print("\t")
			print("\t")
			print(Merah+"""




          ███████                            ██
         ░██░░░░██                          ░██
         ░██   ░██  ██████    ██████ ██   ██░██  ██  ██████   ███████
         ░███████  ░░░░░░██  ██░░░░ ░██  ░██░██ ██  ░░░░░░██ ░░██░░░██
         ░██░░░░    ███████ ░░█████ ░██  ░██░████    ███████  ░██  ░██
         ░██       ██░░░░██  ░░░░░██░██  ░██░██░██  ██░░░░██  ░██  ░██
         ░██      ░░████████ ██████ ░░██████░██░░██░░████████ ███  ░██
         ░░        ░░░░░░░░ ░░░░░░   ░░░░░░ ░░  ░░  ░░░░░░░░ ░░░   ░░



"""+end)

#nama nama Kelompok 4
			print(Biru+"Nama Pasukan	:->	Rafly Ahzami_19215209")
			print(Hijau+"        	:->	Dedek Syaputra_19215148")
			print(Biru+"		:->	Roebana Aja_19215214")
			print(Hijau+"		:->	Rizky Alfi_19215324"+end)
			print("\t")
			print("\t")
			tekan()
			clear()
			Utama()
			print('\t')

# ini perintah Halaman Utama
		if skrip_males == "1":
			clear()
			up()
		elif skrip_males == "2":
			clear()
			pip()
		elif skrip_males == "3":
			clear()
			python_modul()
		elif skrip_males == "4":
			clear()
			tool_python()
		elif skrip_males == "5":
			tentang_kami()
		elif skrip_males == "0":
			time.sleep(1)
			clear()
			print(Merah+"[!] Sedang Keluar ")
			print("")
			sys.exit(1)
		else:
			print(Merah+"[!] Pilihan Kamu Salah "+end)
			tekan()
			clear()
			Utama()

# Perintah untuk Exit
	except KeyboardInterrupt:
		clear()
		print(Merah+"[!] Ctrl +C Kepencet kaya-nya !")
		print("[!] Membersihkan Terminal ..")
		os.system("apt clean")

if __name__ == "__main__":
	clear()
	root()
	Koneksi()
	banner_Lab()
	Utama()

# All Done MY friendd
