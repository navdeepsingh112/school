import time
import datetime
import os
import tkinter as tk
import pyautogui
import mysql.connector as my
import sqlsetup
#if ur trying to understand this its better to give up
def win():
    x='title'
    os.system("title This is the title")
    os.system('lol.bat')
    try:
        pyautogui.getWindowsWithTitle("This is the title")[0].maximize()
    except:
        print('you are using shell run the program in terminal thats what it is made for')
        quit()
#try:
#myl=my.connect(host="localhost",user="root",passwd="12345678")
#except:
 #   print()
    
    
def mysql():
    try:
        fi=open('sql.txt','r')
        qil=fi.readlines()
        qil=qil[0]
        qil=qil.split(',')
        myl=my.connect(host="localhost",user=qil[1],passwd=qil[0])
        mc=myl.cursor()
        fi.close()
        mc.execute("show databases;")
        ml=0
        for i in mc:
            for j in i:
               if j=='gotiyaa':
                   ml=ml+1
                   break
        if ml==0:
            #print('new pc recognised')
            mc.execute('create database gotiyaa;')
            ml=ml+1
        if ml==1:
            mc.execute('use gotiyaa;')
        mc.execute('show tables')
        for i in mc:
            for j in i:
                if j=='users':
                    ml=ml+1
                    break
        if ml==1:
            #print('lol')
            mc.execute('create table users(user varchar(20),date date,time varchar(20));')
    except:
        mysql()
    #    variable()
def abe():
    global bc
    global bc2
    l2=['books','calculator','games','python executor']
    time.sleep(5)
    if mc2==2:
        bc=5
    else:
        bc=3
    #use()
    os.system('cls')
    print('\n'*22)
    print('\t'*10,'+','-'*5,'+')
    print('\t'*10,'|',l2[0],'|')
    print('\t'*10,'+','-'*5,'+')
    print('\t'*10,l2[1])
    print('\t'*10,l2[2])
    print('\t'*10,l2[3])      
def insert(li):
    try:
        fi=open('sql.txt','r')
        qil=fi.readlines()
        qil=qil[0]
        qil=qil.split(',')
        fi.close()
        myl=my.connect(host="localhost",user=qil[1],passwd=qil[0])
        lu=datetime.datetime.now()
        x=str(lu.strftime("%Y/%b/%d"))
        y=str(lu.strftime("%H:%M"))
        #myl=my.connect(host="localhost",user="root",passwd="12345678")
        mc=myl.cursor()
        mc.execute("use gotiyaa;")
        mc.execute("insert into user values('%s','%s','%s');"%(li[0],x,y))
        myl.commit()
    except:
        inser(li)
def show():
    try:
        fi=open("sql.txt",'r')
        qil=fi.readlines()
        qil=qil[0]
        qil=qil.split(',')
        fi.close()
        myl=my.connect(host="localhost",user=qil[1],passwd=qil[0])
        os.system('cls')
        #myl=my.connect(host="localhost",user="root",passwd="12345678")'''
        mc=myl.cursor()
        mc.execute("use gotiyaa;")
        mc.execute('select * from user order by date desc;')
        for i in mc:
                print(i)
    except:
        #sqlsetup.setup()
        show()
def start():
    l=['L','O','A','D','I','N','G']
    x='''  ---------- __o  '''
    y=''' --------  _ \<,_'''
    z='''-------    (*)/ (*)  '''
    q=0

    for i in range(1,21):
        #if i<=7:
           # a=i-1
        print('\n'*24)
        if i<=7:
            a=i-1
            print('\t'*10,' '*a,l[a])
        elif i>7 and i%2==0:
              print('\t'*10,'LOADING')
        else :
              print('')
        print('\t'*9,'█'*i,' '*(21-i),5*i,'%')
        print('\t'*6,3*i*' ',x)
        print('\t'*6,3*i*' ',y)
        print('\t'*6,3*i*' ',z)
        time.sleep(0.3)
        os.system('cls')
def sc():
     l=['admin','guest']
     os.system('cls')
     print('\n'*24)
     print('\t'*10,'+','-'*8,'+')
     print('\t'*10,'|',l[0],' '*(7-len(l[0])),'|')
     print('\t'*10,'+','-'*8,'+')
     print('\t'*10,l[1])
def sc2():
    global a
    if a==1:
        os.system('cls')
        print('\n'*24)
        print('\t'*10,'Admin')
        print('\t'*9,'+','-'*20,'+')
        print('\t'*8,'PASSWORD','|',' '*(20),'|')
        print('\t'*9,'+','-'*20,'+')
    elif a==2:
        os.system('cls')
        print('\n'*24)
        print('\t'*10,'GUEST')
        print('\t'*9,'+','-'*20,'+')
        print('\t'*8,' '*4,'NAME','|',' '*(20),'|')
        print('\t'*9,'+','-'*20,'+')
    
def login(event):
 global root
 l=['admin','guest']
 global aa
 global a
 global li
 global bc
 global lun
 global vj
 global bc2
 global mc2
 if bc==1:
    if event.keysym=='Up':
        if a==1:
            pass
        else:
            a=a-1
    elif event.keysym=='Down':
        if a==2:
            pass
        else:
            a=a+1
    elif event.keysym=='Return':
        bc=2
        
        sc2()
        '''qw=1
        r=tk.Tk()
        r.bind_all('<Key>',pas)
        r.withdraw()
        r.mainloop()'''
    elif event.keysym=="Escape":
        quit()
    if bc==1:
      if a==1:
        os.system('cls')
        print('\n'*24)
        print('\t'*10,'+','-'*8,'+')
        print('\t'*10,'|',l[0],'  ','|')
        print('\t'*10,'+','-'*8,'+')
        print('\t'*10,l[1])
      elif a==2:
        os.system('cls')
        print('\n'*24)
        print('\t'*10,l[0])
        print('\t'*10,'+','-'*8,'+')
        print('\t'*10,'|',l[1],'  ','|')
        print('\t'*10,'+','-'*8,'+')
 elif bc==2:
    global ab    
    
    if a==1:    
         if event.char==event.keysym:
             aa=aa+event.keysym
         elif event.keysym=='BackSpace':
             b=''
             for i in range(len(aa)):
                 if i==(len(aa)-1):
                     pass
                 else:
                     b=b+aa[i]
             aa=b
         os.system('cls')
         print('\n'*24)
         print('\t'*10,'Admin')
         print('\t'*9,'+','-'*20,'+')
         print('\t'*8,'PASSWORD','|',aa,' '*(20-len(aa)),'|')
         print('\t'*9,'+','-'*20,'+')
         if event.keysym=='Return':
                aa=''
                bc=5
                os.system('cls')
                print("#careless admn with no password told him not to be careless now look somebody else is usin me")
                print('\n'*22)
                print('\t'*10,'+','-'*5,'+')
                print('\t'*10,'|','books','|')
                print('\t'*10,'+','-'*5,'+')
                print('\t'*10,'caculator')
                print('\t'*10,'games')
                print('\t'*10,'python executor')
                print('\t'*10,'history of guests')


    elif a==2: 
         
         if event.char==event.keysym:
             aa=aa+event.keysym
         elif event.keysym=='BackSpace':
             b=''
             for i in range(len(aa)):
                 if i==(len(aa)-1):
                     pass
                 else:
                     b=b+aa[i]
             aa=b
         if ab==1:
             li=list()
             os.system('cls')
             print('\n'*24)
             print('\t'*10,'Guest')
             print('\t'*9,'+','-'*20,'+')
             print('\t'*8,' '*4,'NAME','|',aa,' '*(20-len(aa)),'|')
             print('\t'*9,'+','-'*20,'+')
         if event.keysym=='Return':
                li=li+[aa,]
                aa=''
                insert(li)
                bc=3
                os.system('cls')
                print('\n'*22)
                print('\t'*10,'+','-'*5,'+')
                print('\t'*10,'|','books','|')
                print('\t'*10,'+','-'*5,'+')
                print('\t'*10,'caculator')
                print('\t'*10,'games')
                print('\t'*10,'python executor')
                #if ab==4:
             #   insert(li)
    if event.keysym=="Escape":
        bc=1
        os.system('cls')
        print('\n'*24)
        print('\t'*10,'+','-'*8,'+')
        print('\t'*10,'|',l[0],'  ','|')
        print('\t'*10,'+','-'*8,'+')
        print('\t'*10,l[1])

         
             
 elif bc==3:
    mc2=1
    l2=['books','calculator','games','python executor']
    if event.keysym=='Up':
        if bc2==1:
            pass
        else:
            bc2=bc2-1
    elif event.keysym=='Down':
        if bc2==4:
            pass
        else:
            bc2=bc2+1
            
    
    
    if bc2==1:
            os.system('cls')
            print('\n'*22)
            print('\t'*10,'+','-'*5,'+')
            print('\t'*10,'|',l2[0],'|')
            print('\t'*10,'+','-'*5,'+')
            print('\t'*10,l2[1])
            print('\t'*10,l2[2])
            print('\t'*10,l2[3])
    elif bc2==2:
            os.system('cls')
            print('\n'*22)
            print('\t'*10,l2[0])
            print('\t'*10,'+','-'*10,'+')
            print('\t'*10,'|',l2[1],'|')
            print('\t'*10,'+','-'*5,'+')
            print('\t'*10,l2[2])
            print('\t'*10,l2[3])
    elif bc2==3:
            os.system('cls')
            print('\n'*22)
            print('\t'*10,l2[0])
            print('\t'*10,l2[1])
            print('\t'*10,'+','-'*5,'+')
            print('\t'*10,'|',l2[2],'|')
            print('\t'*10,'+','-'*5,'+')
            print('\t'*10,l2[3])
    elif bc2==4:
            os.system('cls')
            print('\n'*22)
            print('\t'*10,l2[0])
            print('\t'*10,l2[1])
            print('\t'*10,l2[2])
            print('\t'*10,'+','-'*15,'+')
            print('\t'*10,'|',l2[3],'|')
            print('\t'*10,'+','-'*5,'+')                      
    if event.keysym=="Return":
        bc=4
        if bc2==1:
            print('press one more time')
        elif bc2==2:
            print('write exi to exit')
            print('write statements like (1+2+3) or (1/2+3)')
        elif bc2==3:
            os.system('cls')
            s=' '
            l=[s,s,s,s,s,s,s,s,s]
            print('there is only one game')
            for i in range(1,10):
                if i%3==0:
                    print(l[i-1])
                    print('-+-+-')
                else:
                    print(l[i-1],end='|')
        elif bc2==4:
            os.system('cls')
            print('1.open saved file \n 2.use new one')
            lun=0
    elif event.keysym=="Escape":
        bc=2
        os.system('cls')
        print('\n'*24)
        print('\t'*10,'Guest')
        print('\t'*9,'+','-'*20,'+')
        print('\t'*8,' '*4,'NAME','|',aa,' '*(20-len(aa)),'|')
        print('\t'*9,'+','-'*20,'+')
 elif bc==4:
     l2=['books','calculator','games','python executor']
     if bc2==1:
         print('not completed yet')
         bc=3







         
     elif bc2==2:
         os.system('cls')
         if event.char==event.keysym:
             aa=aa+event.keysym
         elif event.keysym=='BackSpace':
             b=''
             for i in range(len(aa)):
                 if i==(len(aa)-1):
                     pass
                 else:
                     b=b+aa[i]
             aa=b
         elif len(event.char) == 1:
             aa=aa+event.char
         print('write exi to exit')
         if aa!='exi':
             print(aa)
             if event.keysym=='Return':
                    try:
                          exec('print('+aa+')')
                          aa=''
                          abe()
                    except:
                         print(aa)
                         print('here u go')
                         aa=''
                         abe()           
         


         
     elif bc2==3:
        global q
        global l9
        os.system('cls')
        s=' '
        x='X'
        y='O'
        if (l9[0]==x and l9[1]==x and l9[2]==x) or (l9[3]==x and l9[4]==x and l9[5]==x) or (l9[6]==x and l9[7]==x and l9[8]==x) or (l9[0]==x and l9[3]==x and l9[6]==x) or (l9[1]==x and l9[4]==x and l9[7]==x) or (l9[2]==x and l9[5]==x and l9[8]==x) or (l9[0]==x and l9[4]==x and l9[8]==x) or (l9[2]==x and l9[4]==x and l9[6]==x):
                print(x,'won')
                abe()
        elif (l9[0]==y and l9[1]==y and l9[2]==y) or (l9[3]==y and l9[4]==y and l9[5]==y) or (l9[6]==y and l9[7]==y and l9[8]==y) or (l9[0]==y and l9[3]==y and l9[6]==y) or (l9[1]==y and l9[4]==y and l9[7]==y) or (l9[2]==y and l9[5]==y and l9[8]==y) or (l9[0]==y and l9[4]==y and l9[8]==y) or (l9[2]==y and l9[4]==y and l9[6]==y):
                print(y,'won')
                abe()
            
        print('type box number')
        if event.keysym.isnumeric():
            z=int(event.keysym)
        else:
            z=1
        if q%2==0:
                if l9[z-1]!=x or l9[z-1]!=y:
                    l9[z-1]=x
                    q=q+1
        else:
                if l9[z-1]!=x or l9[z-1]!=y:
                    l9[z-1]=y
                    q=q+1
        for i in range(1,10):
                if i%3==0:
                    print(l9[i-1])
                    print('-+-+-')
                else:
                    print(l9[i-1],end='|')
        if event.keysym=="Escape":
            abe()
        
     elif bc2==4: 
         global ch
         if event.keysym=="Escape":
             ch=3
             abe()
         if ch==1:
             os.system('cls')
             fil=open("pyth.txt",'r')
             lin=fil.readlines()
             aw=0
             for i in lin:
                 if i[0]=='#' and i[1]=='$' and i[2]=='^':
                     aw=aw+1
                     print(aw,i)
             print('enter the file no')
             if event.keysym.isnumeric():
                 ch3=int(event.keysym)
             else:
                 ch3=1
             aw=0
             for i in lin:
                 if i[0]=='#' and i[1]=='$' and i[2]=='^':
                     aw=aw+1
                 if aw==ch3:
                     print(i)
                 elif aw==ch3+1:
                     break
             if aw-1==ch3:
                 print('when you read it press escape and wait 5 sec')
             if event.keysym=="Escape":
                 ab()
            
                     
             
             
         elif ch==2:
             os.system('cls')
             if event.char==event.keysym:
                 aa=aa+event.keysym
             elif event.keysym=='BackSpace':
                 b=''
                 for i in range(len(aa)):
                     if i==(len(aa)-1):
                         pass
                     else:
                         b=b+aa[i]
                 aa=b
             elif len(event.char) == 1:
                 aa=aa+event.char
             print(vj)
             print(aa)
             if event.keysym=="Return":
                 vj=vj+'\n'+aa
                 aa=''
             elif event.keysym=='Shift_L':
                     lu=datetime.datetime.now()
                     z=li[0]
                     x=str(lu.strftime("%Y/%b/%d"))
                     y=str(lu.strftime("%H:%M"))
                     fil=open("pyth.txt",'a')
                     xy='#$^'+z+' '+x+' '+y+'\n'
                     fil.write(xy)
                     fil.write(vj)
                     exec(vj)
                     fil.close
                     abe()
         if event.keysym.isnumeric() and lun==0:
             ch=int(event.keysym)
             if ch==1:
                 fil=open("pyth.txt",'r')
                 lin=fil.readlines()
                 aw=0
                 print(lin)
                 for i in lin:
                     if i[0]=='#' and i[1]=='$' and i[2]=='^':
                         aw=aw+1
                         print(aw,i)
                 print('enter the file no')
             elif ch==2:
                 print('this is python executor')
                 print('now type your code and press left shift to run your code')
                 

             lun=lun+1
     elif bc2==5:
         if event.keysym=="Escape":
             abe()
         else:
             show()
 elif bc==5:
    mc2=2
    l2=['books','calculator','games','python executor','history of users']
    if event.keysym=='Up':
        if bc2==1:
            pass
        else:
            bc2=bc2-1
    elif event.keysym=='Down':
        if bc2==5:
            pass
        else:
            bc2=bc2+1
            
    
    
    if bc2==1:
            os.system('cls')
            print('\n'*22)
            print('\t'*10,'+','-'*5,'+')
            print('\t'*10,'|',l2[0],'|')
            print('\t'*10,'+','-'*5,'+')
            print('\t'*10,l2[1])
            print('\t'*10,l2[2])
            print('\t'*10,l2[3])
    elif bc2==2:
            os.system('cls')
            print('\n'*22)
            print('\t'*10,l2[0])
            print('\t'*10,'+','-'*10,'+')
            print('\t'*10,'|',l2[1],'|')
            print('\t'*10,'+','-'*10,'+')
            print('\t'*10,l2[2])
            print('\t'*10,l2[3])
    elif bc2==3:
            os.system('cls')
            print('\n'*22)
            print('\t'*10,l2[0])
            print('\t'*10,l2[1])
            print('\t'*10,'+','-'*5,'+')
            print('\t'*10,'|',l2[2],'|')
            print('\t'*10,'+','-'*5,'+')
            print('\t'*10,l2[3])
    elif bc2==4:
            os.system('cls')
            print('\n'*22)
            print('\t'*10,l2[0])
            print('\t'*10,l2[1])
            print('\t'*10,l2[2])
            print('\t'*10,'+','-'*15,'+')
            print('\t'*10,'|',l2[3],'|')
            print('\t'*10,'+','-'*15,'+')
    elif bc2==5:
            os.system('cls')
            print('\n'*22)
            print('\t'*10,l2[0])
            print('\t'*10,l2[1])
            print('\t'*10,l2[2])
            print('\t'*10,l2[3])
            print('\t'*10,'+','-'*16,'+')
            print('\t'*10,'|',l2[4],'|')
            print('\t'*10,'+','-'*16,'+')
    if event.keysym=="Return":
        bc=4
        if bc2==1:
            print('press one more time')
        elif bc2==2:
            print('write exi to exit')
            print('write statements like (1+2+3) or (1/2+3)')
        elif bc2==3:
            os.system('cls')
            s=' '
            l=[s,s,s,s,s,s,s,s,s]
            print('there is only one game')
            for i in range(1,10):
                if i%3==0:
                    print(l[i-1])
                    print('-+-+-')
                else:
                    print(l[i-1],end='|')
        elif bc2==4:
            os.system('cls')
            print('1.open saved file \n 2.use new one')
            lun=0
        elif bc2==5:
            print('ky bkc h ye')
    elif event.keysym=="Escape":
        bc=2
        os.system('cls')
        print('\n'*24)
        print('\t'*10,'Guest')
        print('\t'*9,'+','-'*20,'+')
        print('\t'*8,' '*4,'NAME','|',aa,' '*(20-len(aa)),'|')
        print('\t'*9,'+','-'*20,'+')
     

def variable():
    mysql()
    global mc2
    mc2=0
    global a
    a=1
    global ch
    ch=0
    global s
    s=' '
    global l9
    l9=[s,s,s,s,s,s,s,s,s]
    global aa
    aa=''
    global bc
    bc=1
    global ab
    ab=1
    global li
    li=list()
    global bc2
    bc2=1
    global vj
    vj=''
    global q
    q=0
    
     
     
def use():
    global root
    root = tk.Tk()
    root.bind_all('<Key>',login)
    root.withdraw()
    root.mainloop()
    
    

