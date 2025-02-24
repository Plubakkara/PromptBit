from tkinter import*
import random
from operator import index
from tkinter import font
import tkinter.messagebox
import csv

filepath = './UserData.csv'

main=Tk()
main.title('PromptBit')
main.minsize(650,250)

datapassword=[]
first_name=[]
last_name=[]
cvc=[]
id=[]

name_1=StringVar()
surname_1=StringVar()
password=StringVar()
id_card=StringVar()
login_password=StringVar()

round=0

id_label=Label(text='').grid(row=8,column=0)

filepath = './UserData.csv'
...
with open(filepath, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([first_name,last_name,password,id_card])


mainmenu=Label(text='Mainmenu',font=('arial',15,'bold')).grid(row=1,column=3,)
regis=Label(text='Register',font=('arial',13,'bold')).grid(row=3,column=1)
name_re=Label(text='ชื่อ').grid(row=4,column=0)
entername=Entry(main,textvariable=name_1).grid(row=4,column=1)
surname_re=Label(text='นามสกุล').grid(row=5,column=0)
entersurname=Entry(main,textvariable=surname_1).grid(row=5,column=1)
password_re=Label(text='Password').grid(row=6,column=0)
enterpass=Entry(main,textvariable=password).grid(row=6,column=1)
#cf=Button(text='Confirm').grid(row=5,column=1)
id_label=Label(text='ID CARD:').grid(row=9,column=0)

log=Label(text='login',font=('arial',13,'bold')).grid(row=3,column=5,)
id_card_label=Label(text='ใส่:ID (ไม่ต้องเว้น)').grid(row=4,column=4,)
enterid_card=Entry(main,textvariable=id_card).grid(row=4,column=5)
password_label=Label(text='ใส่:Password').grid(row=5,column=4)
enter_password=Entry(main,textvariable=login_password).grid(row=5,column=5)
def card():
    global index1
    window=Toplevel()
    window.title('PromptBit')
    canvas=Canvas(window,width=540,height=960)
    canvas.pack()
    my_image=PhotoImage(file='card.png')
    canvas.create_image(0, 0, anchor=NW,image=my_image)
    id_gui_card=id[index1]
    show_id_gui2=(str(id_gui_card)[0:4]+" "+(str(id_gui_card)[4:8]+" "+str(id_gui_card)[8:12]+" "+str(id_gui_card[12:16])))

    cvc_gui_card=cvc[index1]
    show_user_gui=first_name[index1]+'  '+last_name[index1]
    card_label_1=Label(window,font=('aria',18,'bold'),text=show_id_gui2,bg='black',fg='gold').place(x=120,y=280)
    card_label_1=Label(window,font=('aria',14),text=show_user_gui,bg='black',fg='gold').place(x=120,y=350)
    card_label_1=Label(window,font=('aria',14,'bold'),text=show_id_gui2,bg='black',fg='gold').place(x=120,y=550)
    card_label_1=Label(window,font=('aria',14,'bold'),text=cvc_gui_card,bg='black',fg='gold').place(x=310,y=490)
    window.mainloop()

def register():
    global password,datapassword,enter_password
    print(surname_1.get())
    
    if password.get() == '' or name_1.get() == '' or surname_1 == '':
        register_empty()
    elif password.get() in datapassword:
        pass_sum()
    elif len(password.get()) <4:
        error_len_short()
    elif len(password.get()) >16:
        error_len_long()
    else:
        global round,id,filepath
        random_id="{:016}".format(random.randint(1,9999999999999999))
        id.append(random_id)
    
        random_cvc="{:03}".format(random.randint(1,999))
        cvc.append(random_cvc)
    
        show_id_gui=(str(random_id)[0:4]+" "+(str(random_id)[4:8]+" "+str(random_id)[8:12]+" "+str(random_id[12:16])))
        random_label=Label(main,text=show_id_gui).grid(row=9,column=1)

        first_name.append(name_1.get())
        last_name.append(surname_1.get())
        datapassword.append(password.get())
        print (id)
        with open(filepath, "w", encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(first_name)
            writer.writerow(last_name)
            writer.writerow(datapassword)
            writer.writerow(id)
            writer.writerow(cvc)
        round=round+1

def error_data():
    tkinter.messagebox.showerror("เกิดข้อผิดพลาด","ไม่พบข้อมูลในระบบ")
def error_IDpass():
    tkinter.messagebox.showerror("เกิดข้อผิดพลาด","เลขบัตรหรือรหัสผ่านผิด")
def error_empty():
    tkinter.messagebox.showerror("เกิดข้อผิดพลาด","กรุณาใส่ข้อมูล")
def pass_sum():
    tkinter.messagebox.showerror("เกิดข้อผิดพลาด","กรุณาใช้ Password อื่น")
def error_len_short():
    tkinter.messagebox.showerror("เกิดข้อผิดพลาด","Password สั้นเกินไป")
def error_len_long():
    tkinter.messagebox.showerror("เกิดข้อผิดพลาด","Password ยาวเกินไป")
def register_empty():
    tkinter.messagebox.showerror("เกิดข้อผิดพลาด","กรุณาใส่ข้อมูลให้ครบถ้วน")

def login():
    global datapassword,id,index1
    try:
        print(login_password.get())
        index1=datapassword.index(login_password.get())
        if login_password.get() == '' and id_card.get() == '':
            error_empty()

        elif login_password.get() in datapassword[index1] and id_card.get() in id[index1]:
            card()
        else:
            error_IDpass()
    except:
        error_data()

cf=Button(text='Confirm',command=register).grid(row=7,column=1)
btlogin=Button(text='Login',command=login).grid(row=7,column=5)
main.mainloop()

