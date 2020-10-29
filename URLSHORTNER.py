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
  C1 = int(input('''  
{+} 1.URLshort
{+} 2.EXIT\n>>> '''))
  
  if C1 == 1 :
    
     link = input("\nEnter Your Link : ")
     print()
     shortener=pyshorteners.Shortener()
     print("\nYour link is ready ↓")
     print()
     s = shortener.tinyurl.short(link)
     print(s)
     
  if C1 == 2 :
     print(Fore.YELLOW+"\nHave a good day !! ")
     break
  
     
  
 
  	
  
  
