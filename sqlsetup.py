import mysql.connector as my
def setup():
    f=open("sql.txt","w")
    p=input('enter pass(sql)')
    pl=input('enter user(sql)')
    p=p+','+pl
    f.write (p)
    f.close()
    ok()

def ok():
    try:
        fi=open("sql.txt",'r')
        q=fi.readlines()
        print(q)
        fi.close()
        pas=q[0]
        pas=pas.split(',')
        print(pas)
        global myl
        myl=my.connect(host="localhost",user=pas[1],passwd=pas[0])
    except:
        setup()
