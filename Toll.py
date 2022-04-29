from tkinter import *
from datetime import  datetime
import pymongo
from tkinter import StringVar, messagebox
from PIL import ImageTk,Image
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("525x450")
    global username
    global password
    global vehicle
    global menu
    global username_entry
    global password_entry
    global vehicle_entry
    username = StringVar()
    password = StringVar()
    vehicle = StringVar()
    menu = StringVar()
    Label(register_screen, text="User Registration", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    Label(register_screen, text="Please enter your details below", bg="white",width="300", height="2").pack(pady=5)
    username_lable = Label(register_screen,bg="#94DAFF", text="Username")
    username_lable.pack(padx=5,pady=10)
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen,bg="#94DAFF", text="Password")
    password_lable.pack(padx=5,pady=10)
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    menu.set("Select the Vehicle type:")
    drop=OptionMenu(register_screen,menu,"Car","Truck","Bike")
    drop.pack(padx=5,pady=20)
    vehicle_lable = Label(register_screen,bg="#94DAFF", text="Vehicle Number")
    vehicle_lable.pack(padx=5,pady=10)
    vehicle_entry = Entry(register_screen, textvariable=vehicle)
    vehicle_entry.pack(pady=10)
    Button(register_screen, text="Register", width=10, height=1, bg="red", command = register_user).pack()
    register_screen.config(bg="#94DAFF")
 
card_list=[]
def register_user():
    document = dict()
    document['name'] = username_entry.get()
    document['password'] = password_entry.get()
    document['vehicleType'] = menu.get()
    document['vehicleNo']= vehicle_entry.get()
    C=vehicle_entry.get()+username_entry.get()[0:2]
    document['CardId']= C 
    R='User_info'
    collect = database(R)
    collect.insert_one(document)
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    messagebox.showinfo("Card Id ","Your Card ID is:"+C)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    vehicle_entry.delete(0,END)
    register_screen.withdraw()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x400") 
    photo0=ImageTk.PhotoImage(file="C:\\Users\\hp\\OneDrive\\Desktop\\Py_MiniProject\\log3.png")
    Label(login_screen,image=photo0).pack()
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    global cardid_verify
    global password_verify
    cardid_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Card Id * ").pack()
    username_login_entry = Entry(login_screen, textvariable=cardid_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, bg='red', command = login_verify).pack()
    login_screen.mainloop()
 
def login_verify():
    cardid1 = cardid_verify.get()
    password1 = password_verify.get()
    card_list.append(cardid_verify.get())
    R='User_info'
    collect=database(R)
    a=collect.find({"CardId":cardid1})
    if(a!=1):
        for x in a:
            verify=collect.find({"password":password1})
            if x in verify:
               login_sucess()
            else:
                password_not_recognised()
    else:
        user_not_found()  
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
        
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success!!").pack()
    Button(login_success_screen, text="OK",command=profile).pack()   
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
def delete_login_success():
    login_success_screen.destroy()
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
def profile():
    global profile_page
    profile_page = Toplevel(login_success_screen)
    profile_page.title("Profile")
    profile_page.geometry("600x550")
    L1=Label(profile_page,text="Welcome User", bg="red", width="300", height="2", font=("Calibri", 13))
    L1.pack(pady=5)
    b1=Button(profile_page,text="Top Up",height=2,width=12,bg="#5B7DB1",command=topup)
    b1.pack(pady=5)
    b2=Button(profile_page,text="Pay Toll",height=2,width=12,bg="#5B7DB1",command=paytoll)
    b2.pack(pady=5)
    b3=Button(profile_page,text="View Transaction",height=2,width=12,bg="#5B7DB1",command=transaction)
    b3.pack(pady=5)
    photo0=ImageTk.PhotoImage(file="C:\\Users\\hp\\OneDrive\\Desktop\\Py_MiniProject\\perfectpicresized.png")
    Label(profile_page,image=photo0).pack()
    profile_page.mainloop()
 
def topup():
    global topup_page
    topup_page= Toplevel(profile_page)
    topup_page.title("TopUp")
    topup_page.geometry("500x500")
    global Card_id
    global password
    global s
    global card_entry
    global password_entry
    Card_id=StringVar
    password=StringVar
    Label(topup_page,text="RECHARGE YOUR CARD", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    #Label(text="").pack()
    Label(topup_page,bg='#F6E7D8', text="Enter your Password ").pack(pady=10)
    password_entry = Entry(topup_page, textvariable=password, show= '*')
    password_entry.pack(pady=10)
    Label(topup_page,bg='#F6E7D8', text="Choose TopUp Amount").pack(pady=10)
    s=Spinbox(topup_page,from_=50,to_=500,increment=50)
    s.pack(pady=10)
    Button(topup_page, text="TOP UP", width=10, height=1,bg="white" ,command =topup_recharge).pack(pady=40)
    Button(topup_page, text="CURRENT BALANCE", width=15, height=1,bg="white" ,command =display).pack(pady=40)
    topup_page.config(bg='#F6E7D8')
    
def topup_recharge():
    document = dict()
    document['card_id'] = card_list[0]
    document['amount'] = int(s.get())
    R='Recharge_Info'
    collect = database(R)
    amt_card = collect.find_one({'card_id':document['card_id']})
    if amt_card is not None:
        a=amt_card['amount']+int(s.get())
        collect.find_one_and_update({'card_id':document['card_id']}, {'$set': {'amount':a}})
    else:
        collect.insert_one(document)
    Label(topup_page, text="Recharge Successfull", fg="green", font=("calibri", 11)).pack()
    password_entry.delete(0, END)

def display():
    document = dict()
    document['card_id'] = card_list[0]
    R='Recharge_Info'
    collect = database(R)
    amt_card = collect.find_one({'card_id':document['card_id']})
    a=amt_card['amount']
    L=Label(topup_page, text="Current Balance is "+str(a), fg="blue", font=("calibri", 11))
    L.pack()
       
def paytoll():
    global pay_page
    pay_page= Toplevel(profile_page)
    pay_page.title("Payment")
    pay_page.geometry("600x600")
    global card_id
    global Tolls_name
    global password
    global password_entry
    global password
    global toll_entry
    global s
    global amount
    Tolls_id=StringVar
    password=StringVar
    card_id=StringVar
    amount=StringVar   
    photo0=ImageTk.PhotoImage(file="C:\\Users\\hp\\OneDrive\\Desktop\\Py_MiniProject\\pay3.png")
    Label(pay_page,image=photo0).pack()
    Label(pay_page,bg='#F6E7D8',text="Enter the Tolls ID ").pack(pady=10)
    toll_entry = Entry(pay_page, textvariable=Tolls_id)
    toll_entry.pack(pady=10)
    Label(pay_page,bg='#F6E7D8', text="Enter your Password ").pack(pady=10)
    password_entry = Entry(pay_page, textvariable=password, show= '*')
    password_entry.pack(pady=10)
    Label(pay_page,bg='#F6E7D8', text="Amount").pack(pady=10)
    s=Spinbox(pay_page,from_=50,to_=500,increment=50)
    s.pack(pady=10)
    Button(pay_page, text="MAKE PAYMENT", width=20, height=1,bg="blue" ,command =Pay_toll).pack(pady=40)
    Button(pay_page, text="BACK", width=10, height=1,bg="grey" ,command =pay_page.destroy).pack()
    pay_page.config(bg='#F6E7D8')
    pay_page.mainloop()
   
def Pay_toll():
    document = dict()
    x=toll_entry.get()
    if x=='DH6':
        document['Tolls_name']='Delhi National Highway'
    elif x=='MU7':
        document['Tolls_name']='Mumbai National Highway'
    elif x=='KE8':
        document['Tolls_name']='Kerala National Highway'
    document['password']=password_entry.get()
    document['card_id'] = card_list[0]
    document['amount'] = int(s.get())
    now=datetime.now()
    format_date=now.strftime('%d-%m-%Y  %H:%M:%S')
    document['date']=format_date
    R='Recharge_Info'
    collect = database(R)
    amt_card = collect.find_one({'card_id':document['card_id']})
    if amt_card is not None and amt_card['amount']>=int(s.get()):
        collect.find_one_and_update({'card_id':document['card_id']}, {'$set': {'amount':amt_card['amount']-int(s.get())}})
        T='Toll_Info'
        collect= database(T)
        collect.insert_one(document)
        Label(pay_page, text="Toll pay Successfull", fg="green", font=("calibri", 11)).pack()
        messagebox.showinfo('Welcome Message',"Welcome! to "+document['Tolls_name']+" Toll",parent=pay_page)
    else:
        Label(pay_page, text="Toll pay not Successfull,Insufficient balance", fg="red", font=("calibri", 11)).pack()
    password_entry.delete(0, END)
        
def transaction():
    global transaction_page
    transaction_page= Toplevel(profile_page)
    transaction_page.title("Transactions")
    transaction_page.geometry("650x400")
    Label(transaction_page, text="Database").pack()   
    Button(transaction_page, text="SHOW DATA", width=20, height=1,bg="blue" ,command =transaction_display).pack()
    Button(transaction_page, text="BACK", width=10, height=1,bg="grey" ,command =transaction_page.destroy).pack()

def transaction_display() :
    R='Toll_Info'
    collect=database(R)
    a=collect.find({"card_id":card_list[0]},{'_id':0,'Tolls_name':1,'amount':1,'date':1}) 
    for doc in a:
        Label(transaction_page,text=doc).pack(pady=10)
 
def database(D):
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['Toll_Boooth'] 
        collection = db[D]  
        return collection  
    except pymongo.errors.ConfigurationError:
        messagebox.showerror("Network Error","No internet connection")
 
def main_account_screen(): 
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Toll Booth Management System", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    card_list.clear()
    main_screen.mainloop()
 
main_account_screen()
 

