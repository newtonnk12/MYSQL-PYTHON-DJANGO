from django.shortcuts import render

import mysql.connector as sql
e=' '
p=' '
def signup(request):
    global e,p
    if  request.method=='POST' :
        mycon=sql.connect(host='localhost',user='root',password='12345678',database="db5")
        mycur=mycon.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='email':
                e=value
            if key=='password':
                p=value
        q="insert into user values ( '{}' , '{}')".format(e.p)
        mycur.execute(q)
        mycon.commit()
    return render (request,'signup.html')
        
        
    
