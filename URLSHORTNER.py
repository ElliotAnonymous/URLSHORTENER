#python3 
#hello guys this is a urlshortener
#Hello My real name is prem and I made this tool in my Android phone because i have no pc , laptop but i have my android And I do coding and practice in my Android phone.
import pyshorteners
import colorama 
from colorama import (Fore, Back, Style)
print()
print(Fore.RED+"""
┏┳┳━┳┓┏━━┳┓┏┳━┳━┳━━┳━┳━┳┳━┳━┓
┃┃┃╋┃┃┃━━┫┗┛┃┃┃╋┣┓┏┫┳┫┃┃┃┳┫╋┃
┃┃┃┓┫┗╋━━┃┏┓┃┃┃┓┫┃┃┃┻┫┃┃┃┻┫┓┫
┗━┻┻┻━┻━━┻┛┗┻━┻┻┛┗┛┗━┻┻━┻━┻┻┛ """)
print(Fore.YELLOW+"ᴄʀᴇᴀᴛᴇᴅ ʙʏ 👑 мя.αиοиγмουѕ 👑")
print("                      v.1.0 ")
print(Style.RESET_ALL)
while(True):
  link = input(Fore.BLUE+"Enter Your Link : ")
  print(Style.RESET_ALL)
  print()
  shortener=pyshorteners.Shortener()
  print(Fore.YELLOW + "Your link is ready ↓")
  s = shortener.tinyurl.short(link)
  print(s)
  print()
  again = input("ENTER for continue and type Exit for end this program : ")
  print()
  Exit = "Exit","exit"
  if again in Exit :
  	print("Thanks for using")
  	break 
     
  
 
  	
  
  
