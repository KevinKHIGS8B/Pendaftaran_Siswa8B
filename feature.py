from json import dump, load
from os import system
from time import sleep


fileUser = 'user.json'
fileSiswa = 'item.json'
user = {}
member = {}



def loadData():
	global user, member
	with open(fileUser) as f:
		user = load(f)
	with open(fileSiswa) as f:
		member = load(f)
	return True


def saveData():
	global user, member

	with open(fileUser, 'w') as f:
		dump(user, f)

	with open(fileSiswa, 'w') as f:
		dump(member, f)

	return True


def login():
	counter = 1
	Username = input('Enter Username : ')
	Password = input('Enter Password : ')
	dataCheck = False
	passLogin = False
	if Username in user:
		dataCheck = True
		passLogin = (user[Username] == Password)

	while (not dataCheck) or (not passLogin):
		counter += 1
		if counter > 3:
			return False
		print('Combination Username and Password is Wrong')
		Username = input('Enter Username : ')
		Password = input('Enter Password : ')
		if Username in user:
			dataCheck = True
			passLogin = (user[Username] == Password)
	else:
		print('Login Pass')
		return True


def print_menu():
	print('Pendaftaran Siswa')
	print('[1] Lihat daftar Siswa')
	print('[2] Tambah Siswa')
	print('[3] Hapus Siswa')
	print('[4] Update Siswa')
	print('[5] Print Data Dalam Bentuk Excel')
	print('[q] Keluar Aplikasi')


def print_member():
	if len(member) > 0:
		for info in member:
			print(f'Nama \t: {info}\t Usia \t: {member[info]}')
	else:
		print('Gaada Siswa.')


def tambah_siswa():
	print('Tambah Siswa Baru\n')
	nama = input('Nama \t:')
	jumlah = input('Usia \t:')

	member[nama] = jumlah
	saveData()
	print('proses dulu tunggu yak ...')
	sleep(1)
	print('Udah disimpan.')



def hapus_siswa():
	print('Hapus Siswa\n')

	nama = input('Nama \t:')

	if nama in member:
		del member[nama]
		saveData()
		print('Proses dulu coy ...')
		sleep(1)
		print('Udah di Hapus.')
	else:
		print(f'{nama} Siswa yang ingin dihapus tidak ditemukan')


def update_siswa():
	print('Update Siswa\n')

	nama = input('Nama Siswa \t:')
	Jumlah = input('Usia baru \t:')

	member[nama] = Jumlah
	saveData()
	print('Proses dulu yak ...')
	sleep(1)
	print('Udh selesai nih.')	

