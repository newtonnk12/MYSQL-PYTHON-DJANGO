from django.shortcuts import render
import mysql.connector as sql
e=' '
p=' '
def signin (request):
    global e,p
    if request.method=='POST':
        mycon=sql.connect(host='localhost',user='root',passwoed='12345678',database='website')
        mycur=mycon.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='email':
                e='value'
            if key=='password':
                p='value'
        q="select * from user where email ='{}' and password = ' {}' ".format(e,p)
        mycur.execute(q)
        rec=tuple(mycur.fetchall())
        if rec==():
            return render (request,'error.html')
        else:
            return render (request,'welcome.html')
    return render (request,'signin.html')
