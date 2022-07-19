
import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '32bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support Tolls Enjoy\033[1;37m")
if __name__ == "__main__":
	try:
		__import__("idz")._login()
	except Exception as e:
		exit(str(e))
elif bit == '64bit':
    os.system('xdg-open https://youtube.com/c/TalhaTechnologychannel')
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
