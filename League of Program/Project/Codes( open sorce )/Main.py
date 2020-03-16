from selenium import webdriver
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep    
import os
import socket 

def Matchup_centers(Your_champ , Enemy_champs):#aval -
   yc=Your_champ.replace(" ", "-")
   ec= Enemy_champs.replace(" ", "-")
   driver.get(f"https://www.counterstats.net/league-of-legends/{yc}/vs-{ec}/middle/all")

def Your_Champ_Centers(Your_Champune):#op.gg +
   your_c=Your_Champune.replace(" ", "+")
   driver.execute_script("window.open('');")
   driver.switch_to.window(driver.window_handles[1])
   driver.get(f"https://na.op.gg/champion/{your_c}/statistics/mid")

def userProfile(EnemyName):#op.gg +
   e_champ=EnemyName.replace(" ", "+")
   driver.execute_script("window.open('');")
   driver.switch_to.window(driver.window_handles[2])
   driver.get(f"https://na.op.gg/summoner/userName={e_champ}")

def Mini_game():
   print("\n \n")
   char=input("Your Want Mini_game in Loading game?(y/n)")
   if char=='y':
      n=input("You Want dodge game or skillshot?")
      if n=="dodge":
         driver.execute_script("window.open('');")
         driver.switch_to.window(driver.window_handles[3])
         driver.get("https://loldodgegame.com/play/")
         print("Your first loading is so long but for next game is short! Your dodge Game is redy go and play!")
      elif n=="skillshot":
         driver.execute_script("window.open('');")
         driver.switch_to.window(driver.window_handles[3])
         driver.get("https://loldodgegame.com/skillshot/")
         print("Your first loading is so long but for next game is short! Your skillshot Game is redy go and play!")
   else:
      pass   


def close():
   print("\n \n")
   s=input("You Want Close program?(y/n)")
   if s=='y':
      print("\n")
      print("Have Fun Game !!!")
      print("   Good bye :D   ")
      sleep(5)
      driver.close()
      exit()
   elif s=='n':
      print("Have Fun Game !!!")

def ping():
   print("\n \n")
   n=input("You want Check Your Ping ?(y/n)")
   if n=='y': 
      host_name = socket.gethostname() 
      host_ip = socket.gethostbyname(host_name) 
      print("Hostname :  ",host_name) 
      print("IP : ",host_ip) 
      ping=os.system('ping 8.8.8.8')
      if ping > 300 :
         print("Your ping is not normal for play !")
      else:
         pass   
   else:
      pass   

c1=input("Enter Your Champune :")
c2=input("Enter Enemy Champune :")
print("\n Plase Wait ... \n")
driver=webdriver.Firefox()
Matchup_centers(c1,c2)
Your_Champ_Centers(c1)
e_n=input("Enter Enemy Name :")
userProfile(e_n)
ping()
Mini_game()
close()
