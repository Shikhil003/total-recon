import requests
from ast import If
from ctypes import sizeof
from logging import exception
from tkinter.tix import InputOnly

import pyfiglet
figlet = pyfiglet.figlet_format("Total Recon", font = "slant"  )
#figlet2 = pyfiglet.figlet_format("@VIEH GROUP",=100 )
#print(figlet)
print("Twitter - @shikhilpau                                                                   @VIEH GROUP \n ",end='\n')
print(" WELCOME TO TOTAL RECON ENTER THE OPTION YOU WANT TO USE ")
print(" 1. CHECK HTTP STATUS CODE ")
print(" 2. BRUTEFORCE SUBDOMAINS ")
print(" 3. BRUTEFORCE HIDDEN DIRECTORIES ")
print(" 4. PERFORM AUTOMATED GOOGLE DORKING ")
print(" 5. BRUTEFORCE JWT SIGNATURE ")
choice=int(input("ENTER WHAT IS YOUR CHOICE "))
if (choice==1):
    url=input("Enter the URL: ")
    try:
        response=requests.get("http://"+url)
        print("URL: ", url)
        print("HTTP Status Code: ", response.status_code)
        print("HERE ARE YOUR RESULTS THANKS FOR USING TOTAL RECON")
    except requests.exceptions.RequestException as e:
        print("An error occurred: ", e)
#SUBDOMAIN BRTUEFORCER
#SUBDOMAIN BRUTEFORCER
if (choice==2):
    import requests
    path2=input("Enter your domain ")
    open2=open("Total_recon\secret.txt").read().splitlines()
    for line1 in open2:
        newurl=(line1+"."+path2)
        try:gndec.ac.in
            response1=requests.get("http://"+newurl, timeout=5)
            result=response1.status_code
            print(result, newurl)
        except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
            continue
    print("HERE ARE YOUR RESULTS THANKS FOR USING TOTAL RECON")
if (choice==3):
    import requests
    path3=input("Enter Your Domain ")
    open3=open(r"C:\Users\Dell\Desktop\project\TOTAL RECON\dirbig.txt").read().splitlines()
    for line2 in open3:
        newurl1=("http://"+path3+"/"+line2)
        try:
            response2=requests.get(newurl1, timeout=5)
        except requests.exceptions.ConnectionError or requests.exceptions.ReadTimeout:
            continue
        result1=response2.status_code
        if (result1==200 or result1==403 or result1==302):
            print(result1,newurl1)
    print("HERE ARE YOUR RESULTS THANKS FOR USING TOTAL RECON")
#AUTOMATED GOOGLE DORKER
if(choice==4):
    import webbrowser
    from googlesearch import search
    path4=input("Enter the Target Domain ")
    open4=open("gdorks.txt").read().splitlines()
    for line3 in open4:
        newurl2=("site:"+path4+" "+line3)
        webbrowser.open("https://google.com/search?q="+newurl2)
    print("HERE ARE YOUR RESULTS THANKS FOR USING TOTAL RECON")
#AUTOMATED JWT BRUTEFORCER
if(choice==5):
    import sys
    import jwt
    import argparse
    from termcolor import colored
    file2=input("Enter File Path ")
    token1=input("Enter Your Token ")
    algo=input("Enter Algorithm ")

    with open(file2) as secrets:
       for secret in secrets:
            try:
                payload = jwt.decode(token1, secret.rstrip(), algorithms=[algo])
                print (colored('Success! Token decoded with ....[' + secret.rstrip() + ']','green'))
                break
            except jwt.InvalidTokenError:
                print (colored('Invalid Token .... [' + secret.rstrip() + ']','red'))
            except jwt.ExpiredSignatureError:
                print (colored('Token Expired ....[' + secret.rstrip() + ']','red'))
