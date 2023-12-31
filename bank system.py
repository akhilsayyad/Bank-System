import tkinter as tk
from tkinter import *
from tkinter import messagebox
from time import gmtime, strftime


def is_num(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0


def create_new_acc(master,name,oc,pin):
    if ((is_num(name)) or (is_num(oc) == 0) or (is_num(pin) == 0) or name == ""):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    f1=open("account_number.txt", 'r')
    accnt_no=int(f1.readline())
    accnt_no+=1
    f1.close()

    f1=open("account_number.txt", 'w')
    f1.write(str(accnt_no))
    f1.close()

    fdet=open(str(accnt_no) + ".txt", "w")
    fdet.write(pin + "\n")
    fdet.write(oc + "\n")
    fdet.write(str(accnt_no) + "\n")
    fdet.write(name + "\n")
    fdet.close()

    frec=open(str(accnt_no) + "-rec.txt", 'w')
    frec.write("Date                                Credit           Debit          Balance\n")
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + oc + "              " + oc + "\n")
    frec.close()

    messagebox.showinfo("Details", "Your Account Number is:" + str(accnt_no))
    master.destroy()
    return

def cr_amount(master,amount,acc_num,name):
    if (is_num(amount)==0):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    f1=open(acc_num+".txt","r")
    pin=f1.readline()
    camt=int(f1.readline())
    f1.close()
    amti=int(amount)
    cb=amti+camt
    fdet=open(acc_num + ".txt", 'w')
    fdet.write(pin)
    fdet.write(str(cb) + "\n")
    fdet.write(acc_num + "\n")
    fdet.write(name + "\n")
    fdet.close()
    frec = open(str(acc_num) + "-rec.txt", 'a+')
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + str(amti) + "              " + str(cb) + "\n")
    frec.close()
    messagebox.showinfo("Operation Successfull!!", "You have applied for Loan...")
    master.destroy()
    return


def crdtwn(accnum,name):
    crwn = tk.Tk()
    crwn.geometry("800x500")
    crwn.configure(bg="orange")
    m1 = tk.Message(crwn, text="LOAN TYPE", justify="center", padx=175, pady=0, width=1500,font=("Bell MT", 30, "bold"), bg="black", fg="white")
    m1.place(x=0, y=0)
    b1 = tk.Button(crwn, text="Personal Loan", font=("Bell MT", 20),command=lambda:loandt())
    b2 = tk.Button(crwn, text="Vehicle Loan", font=("Bell MT", 20),command=lambda:loandt())
    b3 = tk.Button(crwn, text="Education Loan", font=("Bell MT", 20),command=lambda:loandt())
    b4 = tk.Button(crwn, text="Home Loan", font=("Bell MT", 20),command=lambda:loandt())
    b1.place(x=50, y=150)
    b2.place(x=500, y=150)
    b3.place(x=50, y=250)
    b4.place(x=500, y=250)



def loandt():
    loandtwn = tk.Tk()
    loandtwn.geometry("1000x500")
    loandtwn.configure(bg="orange")
    m1 = tk.Message(loandtwn, text="ENTER YOUR DETAILS", justify="center", padx=175, pady=0, width=1500,font=("Bell MT", 30, "bold"), bg="black", fg="white")
    m1.place(x=0, y=0)
    l1 = tk.Label(loandtwn, text="CBIL Score", font=("Bell MT", 20))
    e1 = tk.Entry(loandtwn, font=("Bell MT", 20))
    l2 = tk.Label(loandtwn, text="Annual Income", font=("Bell MT", 20))
    e2 = tk.Entry(loandtwn, font=("Bell MT", 20))
    l3 = tk.Label(loandtwn, text="No of Family Members", font=("Bell MT", 20))
    e3 = tk.Entry(loandtwn, font=("Bell MT", 20))
    l4 = tk.Label(loandtwn, text="Is paying another EMI or Not", font=("Bell MT", 20))
    e4 = tk.Entry(loandtwn, font=("Bell MT", 20))
    l1.place(x=50, y=150)
    l2.place(x=50, y=200)
    l3.place(x=50, y=250 )
    l4.place(x=50, y=300)
    e1.place(x=500, y=150)
    e2.place(x=500, y=200)
    e3.place(x=500, y=250)
    e4.place(x=500, y=300)
    
    b1 = tk.Button(loandtwn, text="Submit", font=("Bell MT", 20) ,command=lambda:checkel(e1.get(),e2.get(),e3.get(),e4.get()))
    b1.place(x=350, y=400)




def checkel(cb,ai,fm,oth):
    checkelwn = tk.Tk()
    checkelwn.geometry("500x500")
    if int(cb)>=750 and int(ai)>=800000 and int(fm)<=5 and oth == "No" :
        l1 = tk.Label(checkelwn, text="You can Apply for loan", font=("Bell MT", 20))
        l1.place(x=110,y=100)
        b1 = tk.Button(checkelwn, text="Proceed", font=("Bell MT", 20) ,command=lambda:generate_report())
        b1.place(x=200, y=200)

    else:
        l1 = tk.Label(checkelwn, text="Sorry You can not Apply for loan", font=("Bell MT", 20))
        l1.place(x=50,y=100)
  



def generate_report():
    reportwn = tk.Tk()
    reportwn.geometry("500x500")
    l1 = tk.Label(reportwn, text="Principal Amount:")
    e1 = tk.Entry(reportwn)
    l2 = tk.Label(reportwn, text="Interest Rate (% per annum):")
    e2 = tk.Entry(reportwn)
    l3 = tk.Label(reportwn, text="Loan Tenure (years):")
    e3 = tk.Entry(reportwn)

    b1 = tk.Button(reportwn, text="Generate Report", command=lambda:cal_emi(e1.get(),e2.get(),e3.get()))
    l1.place(x=50, y=150)
    l2.place(x=50, y=200)
    l3.place(x=50, y=250)
    e1.place(x=250, y=150)
    e2.place(x=250, y=200)
    e3.place(x=250, y=250)
    b1.place(x=250, y=300)
    output_label = tk.Label(reportwn, text="")
    output_label.pack()
    

def cal_emi(pa,roi,lt):
    calcwn = tk.Tk()
    calcwn.geometry("600x500")
    m1 = tk.Message(calcwn, text="REPORT", justify="center", padx=175, pady=0, width=1500,font=("Bell MT", 30, "bold"), bg="black", fg="white")
    m1.place(x=0, y=0)
    # principal = float(entry_principal.get())
    # rate = float(entry_rate.get())
    # time = float(entry_time.get())
    pa = int(pa)
    lt = int(lt)
    roi = int(roi)
    rate = roi / 12 / 100  # converting annual rate to monthly and to decimal
    time = lt * 12  # converting years to months
    
    emi = pa * rate * (1 + rate) ** time / ((1 + rate) ** time - 1)
    total_payable = emi * time
    total_interest = total_payable - pa
    
    report = (
        f"Principal Amount: {pa}\n"
        f"Interest Rate: {rate * 12 * 100}%\n"
        f"Loan Tenure (years): {time / 12}\n"
        f"Your EMI per month will be: {emi:.2f}\n"
        f"Total Payable Amount: {total_payable:.2f}\n"
        f"Total Interest Paid: {total_interest:.2f}"
    )
    output_label = tk.Label(calcwn, text="",font=("Bell MT", 20),justify="center")
    #output_label.pack()
    output_label.place(x=100, y=100)
    output_label.config(text=report)
    bg_image = tk.PhotoImage(file="background.gif")
    x = tk.Label(image=bg_image)
    x.place(x=0, y=0)
    
def prs():
    prswn = tk.Tk()
    prswn.geometry("1000x500")
    prswn.configure(bg="orange")
    l1 = tk.Label(prswn, text="You Have Applied for Loan successfully!!!", font=("Bell MT", 20))
    l2 =tk.Label(prswn, text="Our team is working on it.Please wait.We will connect with you Soon!!!", font=("Bell MT", 20))
    l1.place(x=250,y=100)
    l2.place(x=150,y=200)

def debit_amount(master,amt,accnt,name):
    if (is_num(amt)==0):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    f1= open(accnt + ".txt", 'r')
    pin=f1.readline()
    camt=int(f1.readline())
    f1.close()
    if (int(amt)>camt):
        messagebox.showinfo("Error!!", "You dont have that amount left in your account\nPlease try again.")
    else:
        amti=int(amt)
        cb=camt-amti
        f1=open(accnt + ".txt", 'w')
        f1.write(pin)
        f1.write(str(cb) + "\n")
        f1.write(accnt + "\n")
        f1.write(name + "\n")
        f1.close()
        frec = open(str(accnt) + "-rec.txt", 'a+')
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + "              " + str(amti) + "              " + str(cb) + "\n")
        frec.close()
        messagebox.showinfo("Operation Successfull!!", "Amount Debited Successfully!!")
        master.destroy()
        return



def debitwn(acc_num,name):
    dbwn = tk.Tk()
    dbwn.title("DEBIT AMOUNT")
    dbwn.geometry("600x300")
    dbwn.configure(bg="orange")
    m1 = tk.Message(dbwn, text="RISKSIFT", justify="center", padx=175, pady=0, width=1500,font=("Bell MT", 30, "bold"), bg="black", fg="white")
    m1.place(x=0, y=0)
    l1 = tk.Label(dbwn, text="Enter Debited Amount:", font=("Bell MT", 20))
    e1 = tk.Entry(dbwn, font=("Bell MT", 20))
    b1 = tk.Button(dbwn, text="Debit", font=("Bell MT", 20),command=lambda :debit_amount(dbwn,e1.get().strip(),acc_num,name))
    l1.place(x=25, y=150)
    e1.place(x=300, y=150)
    b1.place(x=250, y=225)



def check_bal(accnt):
	f1=open(accnt+".txt",'r')
	f1.readline()
	bal=f1.readline()
	f1.close()
	messagebox.showinfo("Balance",bal)


def trhistory_wn(accnt):
    disp_wn = tk.Tk()
    disp_wn.geometry("900x600")
    disp_wn.title("Transaction History")
    disp_wn.configure(bg="orange")
    fr1 = tk.Frame(disp_wn, bg="blue")
    l_title = tk.Message(disp_wn, text="RISKSIFT", relief="raised", width=2000, padx=600, pady=0, fg="white",bg="black", justify="center", anchor="center")
    l_title.config(font=("Bell MT", "50", "bold"))
    l_title.pack(side="top")
    fr1 = tk.Frame(disp_wn)
    fr1.pack(side="top")
    l1 = tk.Message(disp_wn, text="Your Transaction History:", padx=100, pady=20, width=1000, bg="blue", fg="orange",
                    relief="raised")
    l1.pack(side="top")
    fr2 = tk.Frame(disp_wn)
    fr2.pack(side="top")
    frec = open(accnt + "-rec.txt", 'r')
    for line in frec:
        l = tk.Message(disp_wn, anchor="w", text=line, relief="raised", width=2000)
        l.pack(side="top")
    b = tk.Button(disp_wn, text="Quit", relief="raised", command=disp_wn.destroy)
    b.pack(side="top")
    frec.close()


def check_acc_num(num):
    try:
        f1=open(num+".txt","r")
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invalid Credentials!\nTry Again!")
        return 0
    f1.close()
    return




def check_login(master,name,acc_num,pin):
    if (check_acc_num(acc_num)==0):
        master.destroy()
        return

    if ((is_num(name)) or (is_num(pin) == 0)):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
    else:
        master.destroy()
        login_menu_window(acc_num, name)


def logout(master):
    messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!")
    master.destroy()




def login():
    logwn = tk.Tk()
    logwn.title("LOGIN")
    logwn.geometry("1000x500")
    logwn.configure(background="orange")
    m1 = tk.Message(logwn, text="RISKSIFT", justify="center", padx=400, pady=0, width=1500,font=("Bell MT", 30, "bold"), bg="black", fg="white", anchor="center", relief="raise")
    m1.place(x=0, y=0)
    l1 = tk.Label(logwn, text="Enter Your Name:", font=("Bell MT", 20))
    l2 = tk.Label(logwn, text="Enter Acc Number:", font=("Bell MT", 20))
    l3 = tk.Label(logwn, text="Enter PIN:", font=("Bell MT", 20))
    l1.place(x=280, y=150)
    l2.place(x=270, y=200)
    l3.place(x=365, y=250)
    e1 = tk.Entry(logwn, font=("Bell MT", 20))
    e2 = tk.Entry(logwn, font=("Bell MT", 20))
    e3 = tk.Entry(logwn, show="*", font=("Bell MT", 20))
    e1.place(x=520, y=150)
    e2.place(x=520, y=200)
    e3.place(x=520, y=250)
    b1 = tk.Button(logwn, text="Log In", font=("Bell MT", 20), command=lambda:check_login(logwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b2 = tk.Button(logwn, text="Back", font=("Bell MT", 20), command=logwn.destroy)
    b1.place(x=700, y=350)
    b2.place(x=600, y=350)
    logwn.bind("<Return>", lambda x: check_login(logwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))


def login_menu_window(acnum,name):
    menuwn = tk.Tk()
    menuwn.title("LOGIN MENU")
    menuwn.geometry("1000x500")
    menuwn.configure(bg="orange")
    m1 = tk.Message(menuwn, text="RISKSIFT", justify="center", padx=400, pady=0, width=1500, bg="black",fg="white")
    m1.config(font=("Bell MT", "30", "bold"))
    m1.place(x=0, y=0)
    l1=tk.Label(menuwn,text="Login as " +name,font=("Bell MT",15),anchor="center",justify="center",bg="black",fg="white")
    l1.place(x=450,y=100)
    b1 = tk.Button(menuwn, text="APPLY FOR LOAN", font=("Bell MT", 15), command=lambda:crdtwn(acnum,name))
    b2 = tk.Button(menuwn, text="DEBIT AMOUNT FROM ACCOUNT", font=("Bell MT", 15), command=lambda:debitwn(acnum,name))
    b3 = tk.Button(menuwn, text="CHECK ACCOUNT BALANCE", font=("Bell MT", 15), command=lambda :check_bal(acnum))
    b4 = tk.Button(menuwn, text="CHECK TRANSACTION HISTORY", font=("Bell MT", 15), command=lambda:trhistory_wn(acnum))
    b5 = tk.Button(menuwn, text="LOG OUT", font=("Bell MT", 15),command=lambda: logout(menuwn))
    b1.place(x=100, y=150)
    b2.place(x=100, y=250)
    b3.place(x=550, y=150)
    b4.place(x=550, y=250)
    b5.place(x=450, y=350)


def create_acc():
    crwn = tk.Tk()
    crwn.title("CREATE NEW ACCOUNT")
    crwn.geometry("1000x500")
    crwn.configure(background="orange")
    m1 = tk.Message(crwn, text="RISKSIFT", relief="raise", bg="black", fg="white", width="1500",justify="center", padx=400, pady=0, font=("Bell MT", 30, "bold"), anchor="center")
    m1.place(x=0, y=0)
    l1 = tk.Label(crwn, text="Name :", font=("Bell MT", 20,), relief="raised")
    l2 = tk.Label(crwn, text="Opening Creadit Amount :", font=("Bell MT", 20), relief="raise", )
    l3 = tk.Label(crwn, text="Enter Desired PIN :", font=("Bell MT", 20), relief="raise")
    l1.place(x=415, y=150)
    l2.place(x=197, y=200)
    l3.place(x=266, y=250)
    e1 = tk.Entry(crwn, font=("Bell MT", 20))
    e2 = tk.Entry(crwn, font=("Bell MT", 20))
    e3 = tk.Entry(crwn, font=("Bell MT", 20))
    e1.place(x=525, y=150)
    e2.place(x=525, y=200)
    e3.place(x=525, y=250)
    b1 = tk.Button(crwn, text="Submit", font=("Bell MT", 20),command=lambda:create_new_acc(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b1.place(x=720, y=350)
    b2 = tk.Button(crwn, text="Cancel", font=("Bell MT", 20), command=crwn.destroy)
    b2.place(x=585, y=350)
    crwn.bind("<Return>", lambda x:create_new_acc(crwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))
    return



def Main_Menu():
    mainwn = tk.Tk()
    mainwn.title("RISK SIFT")
    mainwn.geometry("1500x800")
    mainwn.configure(background="orange")
    fr1 = tk.Frame(mainwn)
    fr1.pack(side="top")
    bg_image = tk.PhotoImage(file="background.gif")
    x = tk.Label(image=bg_image)
    x.place(x=0, y=0)
    t1 = tk.Message(text="RISKSIFT", relief="raise", width=1500, bg="black", fg="white", justify="center",anchor="center", padx=600, pady=0)
    t1.config(font=("Bell MT", "50", "bold"))
    t1.pack(side="top")
    t1.place(x=0, y=0)
    login_image = tk.PhotoImage(file="login1.gif")
    newacc_image = tk.PhotoImage(file="createacc.gif")
    quite_image = tk.PhotoImage(file="exit.gif")
    img_login = login_image.subsample(2, 2)
    img_newacc = newacc_image.subsample(1, 1)
    img_exit = quite_image.subsample(10, 10)

    b1 = tk.Button(image=img_login,relief="raise",command=login)
    b2 = tk.Button(image=img_newacc,relief="raise",command=create_acc)
    b3 = tk.Button(image=img_exit,relief="raise",command=mainwn.destroy)
    b1.place(x=900, y=300)
    b2.place(x=825, y=450)
    b3.place(x=975, y=600)

    mainwn.mainloop()


Main_Menu()
