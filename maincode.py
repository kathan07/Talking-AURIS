import pyttsx3
import speech_recognition as sr
import datetime
import pandas as pd
import mysql.connector as sqltor
import os
import random
import Jv6

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#working of code

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query
def takecommand2():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak out the day please...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query2=r.recognize_google(audio, language='en-in')
        print(f"user said: {query2}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query2
def scheduletake():
    
    mycon=sqltor.connect(host="localhost", user="root",passwd="tiger")
    mycur=mycon.cursor(buffered=True)
    cmd="create database if not exists auris"
    mycur.execute(cmd)
    cmd="use auris"
    mycur.execute(cmd)
    try:
        ts=input("enter time slot:")
        mon=input("mon:")
        tue=input("tue:")
        wed=input("wed:")
        thu=input("thu:")
        fri=input("fri:")
        sat=input("sat:")
        cmd= "insert into schedule values ('{}','{}','{}','{}','{}','{}','{}')".format(ts, mon, tue, wed, thu, fri, sat)
        mycur.execute(cmd)
        mycon.commit()
        
    except (NameError,ValueError,IndexError):

        print("YOU ENTERED WRONG VALUE")
def display():
    mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
    mycur=mycon.cursor(buffered=True)
    cmd="select * from schedule"
    mycur.execute(cmd)
    data= mycur.fetchall()
    ts,m,tu,w,th,f,s='Timeslot','Monday','Tuesday','wednesday','Thursday','Friday','Saturday'
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print('|'+str(ts).center(14)+ '|' +m.center(25)+ '|' +tu.center(10)+ '|' +w.center(9)+ '|' +th.center(15)+ '|' +f.center(26)+ '|'  +s.center(20)+ '|')
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in data:        
        print( '|'+str(i[0]).center(14)+ '|' +i[1].center(25)+ '|' +str(i[2]).center(10)+ '|' +i[3].center(9)+ '|' +i[4].center(15)+ '|' +i[5].center(25)+ '|'  +str(i[6]).center(20)+ '|')

        
def register():
    
    mycon=sqltor.connect(host="localhost", user="root",passwd="tiger")
    mycur=mycon.cursor(buffered=True)
    cmd="create database if not exists auris"
    mycur.execute(cmd)
    cmd="use auris"
    mycur.execute(cmd)
   
    try:
        rn=input("enter Roll Number:")
        name=input("Enter Name:")
        pgm=input("Enter Programme:")
        course=input("Enter Course:")
        e_id=input("Enter email id:")
        pswd=input("Set Password:")

        
        cmd= "insert into student values ('{}','{}','{}','{}','{}','{}')".format(rn, name, pgm, course, e_id, pswd)
        mycur.execute(cmd)
        mycon.commit()
                
    except (NameError,ValueError,IndexError):

        print("YOU ENTERED WRONG VALUE")
def facscheduletake():
    
    mycon=sqltor.connect(host="localhost", user="root",passwd="tiger")
    mycur=mycon.cursor(buffered=True)
    cmd="create database if not exists auris"
    mycur.execute(cmd)
    cmd="use auris"
    mycur.execute(cmd)
    try:
        ts=input("enter time slot:")
        mon=input("mon:")
        tue=input("tue:")
        wed=input("wed:")
        thu=input("thu:")
        fri=input("fri:")
        sat=input("sat:")
        cmd= "insert into facschedule values ('{}','{}','{}','{}','{}','{}','{}')".format(ts, mon, tue, wed, thu, fri, sat)
        mycur.execute(cmd)
        mycon.commit()
        
    except (NameError,ValueError,IndexError):

        print("YOU ENTERED WRONG VALUE")
def display():
    mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
    mycur=mycon.cursor(buffered=True)
    cmd="select * from schedule"
    mycur.execute(cmd)
    data= mycur.fetchall()
    ts,m,tu,w,th,f,s='Timeslot','Monday','Tuesday','wednesday','Thursday','Friday','Saturday'
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print('|'+str(ts).center(14)+ '|' +m.center(25)+ '|' +tu.center(10)+ '|' +w.center(9)+ '|' +th.center(15)+ '|' +f.center(26)+ '|'  +s.center(20)+ '|')
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in data:        
        print( '|'+str(i[0]).center(14)+ '|' +i[1].center(25)+ '|' +str(i[2]).center(10)+ '|' +i[3].center(9)+ '|' +i[4].center(15)+ '|' +i[5].center(25)+ '|'  +str(i[6]).center(20)+ '|')

        
def register():
    
    mycon=sqltor.connect(host="localhost", user="root",passwd="tiger")
    mycur=mycon.cursor(buffered=True)
    cmd="create database if not exists auris"
    mycur.execute(cmd)
    cmd="use auris"
    mycur.execute(cmd)
   
    try:
        rn=input("enter Roll Number:")
        name=input("Enter Name:")
        pgm=input("Enter Programme:")
        course=input("Enter Course:")
        e_id=input("Enter email id:")
        pswd=input("Set Password:")

        
        cmd= "insert into student values ('{}','{}','{}','{}','{}','{}')".format(rn, name, pgm, course, e_id, pswd)
        mycur.execute(cmd)
        mycon.commit()
                
    except (NameError,ValueError,IndexError):

        print("YOU ENTERED WRONG VALUE")
def facregister():
    
    mycon=sqltor.connect(host="localhost", user="root",passwd="tiger")
    mycur=mycon.cursor(buffered=True)
    cmd="create database if not exists auris"
    mycur.execute(cmd)
    cmd="use auris"
    mycur.execute(cmd)
    cmd="create table if not exists faculty (Name varchar (30),email_id varchar(30), Password varchar(20))"
    mycur.execute(cmd)
   
    try:
       
        name=input("Enter Name:")
       
        e_id=input("Enter email id:")
        pswd=input("Set Password:")

        
        cmd= "insert into faculty values ('{}','{}','{}')".format( name, e_id, pswd)
        mycur.execute(cmd)
        mycon.commit()
                
    except (NameError,ValueError,IndexError):

        print("YOU ENTERED WRONG VALUE")
def search():
    mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
    mycur=mycon.cursor(buffered=True)

    k=0
    choice=input("ENTER email_id:   ")
        
    cmd="select * from student"
    
    mycur.execute(cmd)
    data=mycur.fetchall()
    print(data)
    for i in data:
            if i[4]==choice:
                    ps=input("enter password:")
                    if i[5]==ps:
                            print("wlcm")
                            k=1
                            return k
                    else:
                            print("inc password")
                
                
                
            else:
                print("RECORD NOT FOUND")
def voice():

    speak("hello student. Welcome to auris. how may i help you? ")
    z=0
    r1=0
    l=["monday","tuesday","wednesday","thursday","friday","saturday"]
                
    while True:
        query=takecommand().lower()
                    
                    
        if 'wake up' in query:
            speak("online and ready.")
                    
        elif 'how are you' in query:
            speak("I am doing good. How may I help you?")
                    
        elif  'music' in query:
            speak("sure")
            music_dir = 'D:\\songs'
            songs=os.listdir(music_dir)
                    
            z=len(songs)
            r1=random.randint(0,z-1)

                        
            os.startfile(os.path.join(music_dir, songs[r1]))
        elif 'stop' in query:
            os.close()
        elif 'the time' in query:
            now_time=datetime.datetime.now().strftime("%H : %M : &S")
            speak(f"It is {now_time}")

        elif 'edit' in query:
            scheduletake()

                    
        elif 'schedule' in query:
                        #os.startfile("C:\\Users\\p_ayu\\Downloads\\Bank Aggregated Details (1).xlsx")
                        
                        #df=pd.read_excel(r"C:\\Users\\p_ayu\\OneDrive\\Desktop\\CSE100\\SCHEDULE (1).xlsx")
            speak("Tell me the day !!")
            query2=takecommand2().lower()
                        
                        #df.set_index("TIMESLOT", inplace=True)
                        
            mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
            mycur=mycon.cursor(buffered=True)
            cmd="select * from schedule"
            mycur.execute(cmd)
            data= mycur.fetchall()
            ts,m,tu,w,th,f,s='Timeslot','Monday','Tuesday','wednesday','Thursday','Friday','Saturday'
            if query2=="monday":
                for i in data:
                    speak(i[0])
                    speak(i[1])
                            
            elif query2=="tuesday":
                for i in data:
                    speak(i[0])
                    speak(i[2])
                            
            elif query2=="wednesday":
                for i in data:
                    speak(i[0])
                    speak(i[3])
            elif query2=="thursday":
                for i in data:
                    speak(i[0])
                    speak(i[4])
            elif query2=="friday":
                for i in data:
                    speak(i[0])
                    speak(i[5])
            elif query2=="saturday":
                for i in data:
                    speak(i[0])
                    speak(i[6])
            elif query2=="sunday":
                speak("there are no classes on sunday.")
                        
            else:
                speak("Can you please say that again?")
                continue
def facvoice():

    speak("Welcome to auris. how may i help you? ")
    z=0
    r1=0
    
                
    while True:
        query=takecommand().lower()
                    
                    
        if 'wake up' in query:
            speak("online and ready.")
                    
        elif 'how are you' in query:
            speak("I am doing good. How may I help you?")
                    
        elif  'music' in query:
            speak("sure")
            music_dir = 'D:\\songs'
            songs=os.listdir(music_dir)
                    
            z=len(songs)
            r1=random.randint(0,z-1)

                        
            os.startfile(os.path.join(music_dir, songs[r1]))
        elif 'stop' in query:
            os.close()
        elif 'the time' in query:
            now_time=datetime.datetime.now().strftime("%H : %M : &S")
            speak(f"It is {now_time}")
        #elif 'attendance' in query:
           # os.startfile("C:\Users\\p_ayu\\Downloads\\Attendance.xlsx")

        elif 'edit' in query:
            facscheduletake()

                    
        elif 'schedule' in query:
                        #os.startfile("C:\\Users\\p_ayu\\Downloads\\Bank Aggregated Details (1).xlsx")
                        
                        #df=pd.read_excel(r"C:\\Users\\p_ayu\\OneDrive\\Desktop\\CSE100\\SCHEDULE (1).xlsx")
            speak("Tell me the day !!")
            query2=takecommand2().lower()
                        
                        #df.set_index("TIMESLOT", inplace=True)
                        
            mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
            mycur=mycon.cursor(buffered=True)
            cmd="select * from facschedule"
            mycur.execute(cmd)
            data= mycur.fetchall()
            ts,m,tu,w,th,f,s='Timeslot','Monday','Tuesday','wednesday','Thursday','Friday','Saturday'
            if query2=="monday":
                for i in data:
                    
                    speak(i[0])
                    speak(i[1])
                    
                            
            elif query2=="tuesday":
                for i in data:
                    speak(i[0])
                    speak(i[2])
                            
            elif query2=="wednesday":
                for i in data:
                    speak(i[0])
                    speak(i[3])
            elif query2=="thursday":
                for i in data:
                    speak(i[0])
                    speak(i[4])
            elif query2=="friday":
                for i in data:
                    speak(i[0])
                    speak(i[5])
            elif query2=="saturday":
                for i in data:
                    speak(i[0])
                    speak(i[6])
            elif query2=="sunday":
                speak("there are no classes on sunday.")
                        
            else:
                speak("Can you please say that again")
                continue


def admin():
    Jv6.clear()
    t=int(input("1.Show Database\n2.Delete Record\n"))
    if t==1:
        Jv6.clear()
        n1=int(input("1.Student Database\n2.Faculty Database\n"))
        if n1==1:
            Jv6.clear()
            mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
            mycur=mycon.cursor(buffered=True)
            cmd="select * from student"
            mycur.execute(cmd)
            data= mycur.fetchall()
            r,n,p,c,e_id='Roll_No','Name','Programme','Course','email_id'
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
            print('|'+str(r).center(10)+ '|' +n.center(25)+ '|' +p.center(10)+ '|' +c.center(9)+ '|' +e_id.center(15)+ '|' )
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
            for i in data:        
                print( '|'+str(i[0]).center(10)+ '|' +i[1].center(25)+ '|' +str(i[2]).center(10)+ '|' +i[3].center(9)+ '|' +i[4].center(15)+ '|')

        else:
            Jv6.clear()
            mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
            mycur=mycon.cursor(buffered=True)
            cmd="select * from faculty"
            mycur.execute(cmd)
            data= mycur.fetchall()
            n,e_id='Name','email_id'
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
            print('|' +n.center(25)+ '|' +e_id.center(15)+ '|' )
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
            for i in data:        
                print( '|' +i[0].center(25)+ '|' +i[1].center(9)+ '|')
            
    elif t==2:
        Jv6.clear()
        n2=int(input("1.Student Record\n2. Faculty Record"))   
        if n2==1:
            Jv6.clear()
            mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
            mycur=mycon.cursor(buffered=True)

            k=0
            choice=input("ENTER Roll No.:   ")
                
            cmd="select * from student"
            mycur.execute(cmd)
            data=mycur.fetchall()


            for i in data:
                    if i[0]==choice:
                            print (i[0])
                            cmd="delete from student where Roll_No='{}'".format(i[0])
                            print("deleted")
                            mycur.execute(cmd)
                            mycon.commit()
                    else:
                            continue
        else:
            mycon=sqltor.connect(host="localhost", user="root",passwd="tiger",database="auris")
            mycur=mycon.cursor(buffered=True)

            k=0
            choice=input("ENTER email id:   ")
                
            cmd="select * from faculty"
            mycur.execute(cmd)
            data=mycur.fetchall()


            for i in data:
                    if i[1]==choice:
                            
                            cmd="delete from faculty where email_id='{}'".format(i[1])
                            print("deleted")
                            mycur.execute(cmd)
                            mycon.commit()
                    else:
                            continue
def helpvoice():
    speak("Welcome to talk-auris. This is partially voice based desktop assistant mainly designed for Ahmedabad University students and faculties. In this program, following functionalities can be executed. For student usage, 1 playing music, 2 edit daily schedule, 3 know daily schedule, 4 know time. For faculty usage, 1 play music, 2 edit daily schedule, 3 know daily schedule, 4 open attendance file. In case you find any difficulty, report to the admin in complaint section. Enjoy your time. thankyou.")

def complaints():
    comp=input("Enter your issue: ")
    
    with open('complaint.txt','w') as f:
        f.write(comp)