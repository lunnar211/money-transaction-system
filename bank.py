import sqlite3
import random as r
class Bank:
    print("WELCOME TO SBI BANK")
    print("-------------------")
    def __init__(self):
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()

    def CreateAccount(self):
        #self.c.execute("drop table Bank")        
        self.c.execute("""create table if not exists Bank
            (
                account_name text,
                acc_no integer,
                balance integer
            )""")
        n1 = input("Enter Your First Name:- ").upper()
        n2 = input("Enter Your Last Name:- ").upper()
        print("---------------------------------------")
        if n1.isalpha() and not n1.isspace() and n2.isalpha() and not n2.isspace() and len(n1)>2 and len(n2)>2:
            name = n1+" "+n2
            num = r.randint(10000000,99999999)
            self.amount = 0
            self.c.execute("insert into Bank values(?,?,?)",(name,num,self.amount))
            print("Hello {} Your Account got Created, Note your Your Account Number.".format(name))
            print("Your Account Number is:- {}".format(num))
            print("---------------------------------------")
            self.con.commit()
            self.con.close()
            #self.c.execute("select * from Bank")
            #print(self.c.fetchall())
            
        else:
            print("Enter Valid Name, Try Again...!")
    def OpenAccount(self):
        print("------------------------------")
        a_num = int(input("Enter the Account Number:- "))
        check = True
        flag = False
        for a,b,c in self.c.execute("select * from Bank"):
            if b == a_num:
                flag = True
                check = False
                val = c
                na = a
                print("(c)-Check Balance")
                print("(d)-Deposit")
                print("(w)-Withdraw")
                ope = input("Enter any of the operation (c)/(d)/(w):- ")
        if flag and (ope=='d' or ope=='D'):
            dep = int(input("Enter the Amount to Deposit:- "))
            deposit = dep + val 
            self.c.execute("update Bank set balance = ? where acc_no = ?",(deposit,a_num))
            self.con.commit()
            print("Amount Deposited {} ₹, Available Balance is {} ₹".format(dep,deposit))
            #self.c.execute("select * from Bank")
            #print(self.c.fetchall())
        if flag and (ope == 'w' or ope == 'W'): 
            wit = int(input("Enter the Amount to Withdraw:- "))
            if val>0 and val >= wit:
                withdraw_bal = val - wit
                self.c.execute("update Bank set balance = ? where acc_no = ?",(withdraw_bal,a_num))
                self.con.commit()
                print("Withdraw {} ₹ done successfully...! Available balance {} ₹".format(wit,withdraw_bal))
                #self.c.execute("select * from Bank")
                #print(self.c.fetchall())
            else:
                print("Low Balance")
        if flag and (ope == 'c' or ope == 'C'):
            print("Hello {}, Your Account Balance is {} ₹".format(na,val))
        print("----------------------------------------------------------")
        if check:
            print("Invalid Account Number.")
bk = Bank()
print("(c)-Create Account")
print("(o)-Open Account")
op = input("Enter your choice (c)/(o):- ")
if op == 'c' or op == 'C':
    bk.CreateAccount()
elif op =='o' or op == 'O':
    bk.OpenAccount()