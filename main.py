from tkinter import *
import datetime
import csv
from tkinter import messagebox
import mysql.connector
import os

def rs2():
    c = str(es5.get())
    mycursor1.execute('select * from '+c)
    mydata = mycursor1.fetchall()
    frame1 = Frame(root )
    frame1.place(x = 20 ,y  = 270)
    h1 = Scrollbar(frame1 )
    h1.pack(side = RIGHT,fill = Y )
    mylist = Listbox(frame1, yscrollcommand = h1.set , width = 30 , height = 7)
    for i in mydata:
        mylist.insert(END, i )
    mylist.pack(side = LEFT, fill = BOTH)
    h1.config(command = mylist.yview)



def rs1():
    global es5,myconn1,mycursor1
    h = str(es1.get())
    u = str(es2.get())
    p = str(es3.get())
    try:
        myconn1 = mysql.connector.connect(host=h, user=u, password=p)
        if myconn1.is_connected():
            li4 = Label(root, text='MYSQL IS CONNECTED ')
            li4.place(x=20, y=170)
        else:
            li4 = Label(root, text='MYSQL NOT CONNECTED')
            li4.place(x=20, y=170)

    except:
        li4 = Label(root, text='MySQL server is not active/unreachable')
        li4.place(x=20, y=170)

    mycursor1 = myconn1.cursor()
    mycursor1.execute('create database if not exists Attendence')
    mycursor1.execute('use attendence')
    li5 = Label(root, text='enter class ')
    li5.place(x=20, y=190)
    es5 = Entry(root, )
    bi5 = Button(root, text='SUBMIT', command=rs2)
    es5.place(x=20, y=210)
    bi5.place(x=20, y=230)
def rs():
    global es1,es2,es3
    lu8.destroy()
    la1.destroy()
    bu1.destroy()
    hd.destroy()
    vers.destroy()
    bi3.destroy()
    bi4.destroy()
    bi5.destroy()
    li1 = Label(root, text='Enter the Host id of MySql (enter localhost if database present in local)')
    es1 = Entry(root, )
    li2 = Label(root, text='Enter the user name of MySql')
    es2 = Entry(root, )
    li3 = Label(root, text='Enter the password of MySql')
    es3 = Entry(root, )
    li1.place(x=20, y=30)
    es1.place(x=20, y=50)
    li2.place(x=20, y=70)
    es2.place(x=20, y=90)
    li3.place(x=20, y=110)
    es3.place(x=20, y=130)
    bi1 = Button(root, text='SUBMIT', command=rs1)
    bi1.place(x=20, y=150)
    ba2 = Button(root, text="MAIN MENU", command=main)
    ba2.place(x=250, y=350)
def sql2():
    c = str(ei5.get())
    file3 = open(c + '.csv', 'a+')
    reader = csv.reader(file3)
    mycursor.execute('create table if not exists ' + c + '(Date DATE, NAME varchar(30), ATTENDENCE varchar(20), PRIMARY KEY (Date,NAME))')
    messagebox.showinfo('INFO','DATA IS RECORDED IN (CLASS) TABLE')
    file3.seek(0)
    try:
        for i in reader:
              if i!= [] and i[0]!= 'DATE':
                 print('replace into '+ c + ' values(' + "'"+ str(i[0])+"'"+ ',' + "'" + i[1] + "'" + ','+ "'" + str(i[2])  + "'" + ')')
                 mycursor.execute('replace into '+ c + ' values(' + "'"+ str(i[0])+"'"+ ',' + "'" + i[1] + "'" + ','+ "'" + str(i[2])  + "'" + ')')
                 myconn.commit()
        li6 = Label(root , text = 'Successfully recorded')
        li6.place(x = 20 , y = 270)
    except:
        li6 = Label(root, text = 'FAILED please try again')
        li6.place(x = 20 ,y = 270)
    mycursor.close()
    myconn.close()


def sql():
    global ei1,ei2,ei3
    lu8.destroy()
    la1.destroy()
    bu1.destroy()
    hd.destroy()
    vers.destroy()
    bi3.destroy()
    bi4.destroy()
    bi5.destroy()
    li1 = Label(root , text ='Enter the Host id of MySql (enter localhost if database present in local)')
    ei1 = Entry(root,)
    li2 = Label(root ,text = 'Enter the user name of MySql')
    ei2 = Entry(root,)
    li3 = Label(root, text ='Enter the password of MySql')
    ei3 = Entry(root,)
    li1.place(x = 20 , y = 30)
    ei1.place(x = 20 , y = 50)
    li2.place(x = 20 , y = 70)
    ei2.place(x = 20 , y = 90)
    li3.place(x = 20 , y = 110)
    ei3.place(x = 20 , y = 130)
    bi1 = Button(root, text = 'SUBMIT' , command = sql1)
    bi1.place(x = 20 , y = 150)
    ba2 = Button(root, text="MAIN MENU", command=main )
    ba2.place(x=250, y=350)

def sql1():
    global ei5,mycursor,myconn
    h = str(ei1.get())
    u = str(ei2.get())
    p = str(ei3.get())
    try:
        myconn = mysql.connector.connect(host = h , user = u , password = p )
        if myconn.is_connected():
            li4 = Label(root , text = 'MYSQL IS CONNECTED (data will be stored in database Attendence) ')
            li4.place(x = 20 , y = 170)
        else:
            li4 = Label(root , text = 'MYSQL NOT CONNECTED')
            li4.place(x = 20 ,y = 170)

    except:
        li4 = Label(root ,text = 'MySQL server is not active/unreachable')
        li4.place(x = 20 ,y = 170)

    mycursor = myconn.cursor()
    mycursor.execute('create database if not exists Attendence')
    mycursor.execute('use attendence')
    li5 = Label(root , text = 'enter class whose data should be copied to database')
    li5.place(x = 20 , y = 190)
    ei5 = Entry(root , )
    bi5 = Button(root , text = 'SUBMIT', command = sql2)
    ei5.place(x = 20 , y = 210)
    bi5.place(x = 20 , y = 230)




def writefile():
    global file1
    L1 = e3.get()
    words = L1.split()
    if os.path.exists(a + '.csv'):
        file1 = open(a + '.csv', 'a+')
        writer = csv.writer(file1)

    else:
        file1 = open(a + '.csv', 'a+')
        writer = csv.writer(file1)
        writer.writerow(['DATE','NAME OF STUDENT','PRESENT/ABSENT'])

    file2.seek(0)
    y3 = file2.read().split()
    for i in y3:
        if i in words:
            writer.writerow([datetime.datetime.now().date(), i, 'present'])
        else:
            writer.writerow([datetime.datetime.now().date(), i, 'absent'])
    lab = Label(root, text='ATTENDENCE SUCCESSFULLY RECORDED')
    lab.place(x=10, y=230)
    ba2 = Button(root, text="MAIN MENU", command=main)
    ba2.place(x=250, y=350)
    try:
        file1.close()
        file2.close()
    except:
        print('')


def click2():
    global L, e3, file2
    lu1.destroy()
    L = e1.get()
    if L is not NONE:
        words = L.split()
        file2.seek(0)
        x = file2.read().split()
        for i in words:
            if i not in x:
                file2.write(i + ' ')
                file2.flush()
    file2.seek(0)
    l2 = Label(root, text='NAMES OF STUDENTS REGISTERED = ' + file2.read(80) + '\n' + file2.read(100))
    l2.place(x=10, y=150)
    l3 = Label(root, text='COPY AND PASTE THE TEXT FROM CHAT BOX')
    l3.place(x=10, y=170)
    e3 = Entry(root, width=50)
    e3.place(x=10, y=190)
    b3 = Button(root, text='ENTER', command=writefile)
    b3.place(x=170, y=210)


def record():
    global classinput, classbutton, classname
    lu8.destroy()
    la1.destroy()
    bu1.destroy()
    hd.destroy()
    vers.destroy()
    bi3.destroy()
    bi4.destroy()
    bi5.destroy()
    classname = Label(root, text='ENTER CLASS (eg : 12b , 1a,)')
    classname.place(x=10, y=10)
    classinput = Entry(root)
    classinput.place(x=10, y=30)
    classbutton = Button(root, text='ENTER', command=click1, activeforeground='blue')
    classbutton.place(x = 140, y=25)
    c3 = Label(root, text='NOTE : \n CLASS NAME ACTS LIKE AN USERNAME, U CAN ENTER ANY WORDS')


def click1():
    global l1, a, stu, e1, b1, lu1, file2
    a = classinput.get()
    l1 = Label(root,
               text=a + ' ' + 'CLASS CREATED - LEAVE IT EMPTY IF NO NEW RECORDS ARE TO BE ADDED\n enter the name of the students as per username with one white space').place(
        x=10, y=70)
    e1 = Entry(root, width=50)
    e1.place(x=10, y=110)
    b1 = Button(root, text='ENTER', command=click2)
    b1.place(x=320, y=105)
    file2 = open(a + ' ' + 'student list', 'a+')
    file2.seek(0)
    lu1 = Label(root, text='NAMES OF STUDENTS REGISTERED = ' + file2.read(80) + '\n' + file2.read(100))
    file2.seek(0)
    lu1.place(x=10, y=150)
    messagebox.showinfo('REMEMBER' ,'IF THE STUDENT HAS LASTNAME, REGISTER THE NAME WITHOUT SPACE INBETWEEN  OR WITH UNDERSCORE IN BETWEEN  ALSO THE STUDENTS SHOULD TYPE THE SAME NAME IN THE CHAT BOX')


def eclick1():
    global ev , xc
    xc = ce.get()
    Lv = Label(root, text = 'Enter the date [YYYY-MM-DD] (leave black for total attendence percentage)')
    ev = Entry(root )
    Lv.place(x = 10 , y = 90)
    ev.place(x = 10 , y = 110)
    bv = Button(root , text = 'ENTER' , command = eclick2)
    bv.place(x = 160 , y = 110)

def eclick2():
    L = ev.get()
    pc = 0
    ac = 0
    file1 = open(xc + '.csv', 'a+')
    file1.seek(0)
    reader = csv.reader(file1)
    for row in reader:
        if row != []:
            if L == '':
                if row[2] == 'present' :
                    pc = pc + 1
                elif row[2] == 'absent':
                    ac = ac + 1
            elif L in row:
                if row[2] == 'present' :
                    pc = pc + 1
                elif row[2] == 'absent':
                    ac = ac + 1
    try:
        calu = str(round((pc/(ac+pc))*100,2))
    except:
        calu = 'NO RECORDS FOUND ----- 0'
    La3 = Label(root , text = 'TOTAL ATTENDENCE = ' + calu + '%')
    La3.place(x = 10 , y = 200)
    ba2 = Button(root, text="MAIN MENU", command=main)
    ba2.place(x=250, y=350)

def extra():
    global ce
    la1.destroy()
    bu1.destroy()
    lu8.destroy()
    hd.destroy()
    vers.destroy()
    bi3.destroy()
    bi4.destroy()
    bi5.destroy()
    cc = Label(root, text = 'ENTER CLASS')
    ce = Entry(root)
    cc.place(x = 10 , y = 20)
    ce.place(x = 10, y = 40)
    cb = Button(root, text = 'ENTER' , command = eclick1)
    cb.place(x = 160 , y = 40)





def main():
    global root, la1, bu1, bu2, lu8,vers,hd,bi3,bi4,bi5
    try:
        file1.close()
        file2.close()
    except:
        print('')
    try:
        root.destroy()
    except:
        print('')
    root = Tk(className=' ATTENDENCE RECORDER')
    root.geometry('600x400')
    hd = Label(root, text='ATTENDENCE RECORDER', font = ('Times',32 ,'bold') , bg = 'grey' , fg = 'white')
    hd.place(x=20, y=20)
    vers = Label(root, text = 'Version V1.0.0 beta')
    vers.place(x = 480 , y = 375)
    la1 = Label(root, text='WHAT DO YOU WANT TO DO?', font = ('Times',16 ,'bold'))
    bu1 = Button(root, text='RECORD IN EXCEL\n(FIRST STEP)', command=record, font= ('Times',16 ))
    bi3 = Button(root , text = ' ATTENDENCE \n PERCENTAGE' , command =extra , font = ('Times' , 16))
    bi4 = Button(root, text = 'RECORD TO MYSQL DATABASE\n(AFTER RECORDED IN EXCEL)', command = sql , font = ('Times' , 16))
    bi3.place(x = 30, y = 230)
    la1.place(x=160, y=100)
    bu1.place(x=30, y=150)
    bi4.place(x=250 ,y=150)
    lu8 = Label(root, text='NOTE: \n YOU CAN OPEN THE CSV FILE IN EXCEL TO GET A EXCEL SHEET \n THE CSV FILE WILL BE LOCATED IN THE PROGRAM FOLDER \n DEFAULT CSV FILE IS STORED AS EXCEL SHEET')
    lu8.place(x=130, y=300)
    bi5 = Button(root, text = 'SEE RECORDS FROM DATABASE' , font = ('Times',16),command = rs)
    bi5.place(x = 240 , y = 230)

    root.mainloop()




main()
