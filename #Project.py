#Project
import Jv6
import pyttsx3
import speech_recognition as sr
import datetime
import pandas as pd
import mysql.connector as sqltor
import maincode as mc1
import random
import os

#PROGRAM STARTS
while(True):

    # STUDENT LOGIN 

    a1 = int(input("1. Enter 1 for Student login:: \n2. Enter 2 for faculty login:: \n3. Enter 3 for admin login::\n4.What is TALK-AURIS\n5.complaint reports\n"))
    if a1 == 1:
        Jv6.clear()
        a2=int(input("1.Register new account\n2. Log in to existing account\n"))
        if a2==1:
            Jv6.clear()
            
            mc1.register()
            continue
        else:
            Jv6.clear()
            mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
            mycur=mycon.cursor(buffered=True)

            k=0
            choice=input("ENTER email_id:   ")
            
            cmd="select * from student"
            mycur.execute(cmd)
            data=mycur.fetchall()

            for i in data:
                    if i[4]==choice:
                            ps=input("enter password:")
                            if i[5]==ps:
                                    print("wlcm")
                                    mc1.voice()
                            
                            else:
                                    print("incorrect password")
                    
                    
                    
                    else:
                        k=0
            
        
       
            if k==0:
                print("RECORD NOT FOUND")
            
    # FACULTY LOGIN
                
    elif a1 == 2:
        Jv6.clear()
        z=int(input("1.Register new account\n2. Log in to existing account\n"))
        if z==1:
            Jv6.clear()
            mc1.facregister()
        else:
            Jv6.clear()
            mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
            mycur=mycon.cursor(buffered=True)

            k=0
            choice=input("ENTER email_id:   ")
            
            cmd="select * from faculty"
            mycur.execute(cmd)
            data=mycur.fetchall()

            for i in data:
                    if i[1]==choice:
                            ps=input("enter password:")
                            if i[2]==ps:
                                    Jv6.clear()
                                    print("wlcm")
                                    mc1.facvoice()
                            
                            else:
                                    print("incorrect password")
                    
                    
                    
                    else:
                        k=0
            
        
       
            if k==0:
                print("RECORD NOT FOUND")
    
    #ADMIN LOGIN
        
    elif a1 == 3:
        Jv6.clear()

        n=input("Enter Password:")
        if n=="iamnottheadmin":
            Jv6.clear()
            mc1.admin()


            
    

    #WHAT IS TALK_AURIS

    elif a1==4:
        mc1.helpvoice()
    
    #COMPLAINT REPORTS
    else:
        mc1.complaints()

