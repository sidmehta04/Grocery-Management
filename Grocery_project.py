import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import Error
import pandas as pd
import sys
import time
import os
from os import system,name
def login(email,passw):
    try:
        print("email: ",email)
        print("passw: ",passw)

        connection=mysql.connector.connect(host="localhost",
                                           database="bigbasket",
                                           user="root",
                                           password="root")
 
        cursor=connection.cursor()
        sql_select=("SELECT * FROM user_details")
        cursor.execute(sql_select)
        record=cursor.fetchall()
        for row in record:
            emailid=row[2]
            password=row[3]
            print(emailid)
            print(password)
            if((emailid==email) and(password==passw)):
                print("returning true")
                return True
            else:
                print("returning false")
                return False
    except Error as e:
        print("error",e)
    finally:
       if(connection.is_connected()):
           connection.close()
           cursor.close()

def signin(name,surname,emailid,password,Address_line1,pincode):
    print("defined successfully")
    try:
        connection=mysql.connector.connect(host="localhost",
                                           database="bigbasket",
                                           user="root",
                                           password="root")
        cursor=connection.cursor()
        query = 'insert into user_details values (%s, %s, %s, %s, %s, %s)'
        record = (name, surname, emailid, password, Address_line1, pincode)
        cursor.execute(query,record)
        connection.commit()
    finally:
       if(connection.is_connected()):
           connection.close()
           cursor.close()
def signup():
    name=input("enter name")
    surname=input("enter surname")
    emailid=input("enter mailid")
    password=input("enter password")
    Address_line1=input("enter address")
    pincode=int(input("enter pincode"))
    
    if (any(x.isupper() for x in password) and any(x.islower() for x in password)
        and any(x.isdigit() for x in password) and len(password)>=7):
        print("Your password is strong")
        signin(name,surname,emailid,password,Address_line1,pincode)
        print("You have signed in")
    else:
        print("Your password is weak")
        print("please change it")
        
        passw1=input("enter new pass")
        
        if (any(x.isupper() for x in passw1) and any(x.islower() for x in passw1)
        and any(x.isdigit() for x in passw1) and len(passw1)>=7):
            print("You have set a strong password now")
            signin(name, surname, emailid, passw1, Address_line1, pincode)
        else:
            
            print("The number of tries to set a strong password have exhausted.Please signin again")
            sys.exit()
    
        print("Your password is strong")
        print("You have signed in")
def change_passw():
    connection=mysql.connector.connect(host="localhost",
                                           database="bigbasket",
                                           user="root",
                                           password="root")
    cursor=connection.cursor()
    query = "insert into user_details values (%s,%s)"
    email=input("enter email")
    password=input("enter pass")
   
    record = (password, email)
    cursor.execute(query,record)
    connection.commit()
    

    
print("welcome to bigbasket") 
print("1:Login")
print("2:Signup")
ch=int(input("enter choice"))
if ch==1:
    email=input("enter email")
    passw=input("enter pass")
    
        
    if(login(email,passw))==True:
        print("logged in")
    else:
        print("logged in details are false, redirecting to sign in")
        name=input("enter name")
        surname=input("enter surname")
        emailid=input("enter mailid")
        password=input("enter password")
        Address_line1=input("enter address")
        pincode=int(input("enter pincode"))
        signin(name,surname,emailid,password,Address_line1,pincode)

        
        

elif ch==2:
   signup()

def Items(itemname,Quantity,amount):
    try:
        connection=mysql.connector.connect(host="localhost",
                                           database="bigbasket",
                                           user="root",
                                           password="root")
        cursor=connection.cursor()
        query = 'insert into add_to_cart values (%s, %s, %s)'
        record =(itemname,Quantity,amount)
        cursor.execute(query,record)
        connection.commit()
    finally:
       if(connection.is_connected()):
           connection.close()
           cursor.close()
           
def Item_price(itemname):
    try:
        connection=mysql.connector.connect(host="localhost",
                                           database="bigbasket",
                                           user="root",
                                           password="root")
        query = "select Price from Item_master where Item_name='"+itemname+"'" 
        cursor=connection.cursor()
        cursor.execute(query)
        record=cursor.fetchone()
        return record[0]
    finally:
       if(connection.is_connected()):
           connection.close()
           cursor.close()
def credit_card_or_cash():
    a=int(input("press 1 to pay using credit card or press 2 to pay using cash"))
    if a==1:
        print("****Enter details in this format-xxxx_xxxx_xxxx_xxxx_****")
        cardnumber=int(input())
        cardnumber=str(cardnumber)
        if (len(cardnumber)==4):
            print(""""The card number is correct
            Your card number is""",cardnumber)
            print("Proceed to enter your expiration date")
            expiry_date=(input("Enter in this format-expiry month / expiry year"))
            print("expiry dates is",expiry_date)
            if (len(expiry_date)==5): 
                print("expiry date is valid proceed to enter your cvv")
                cvv=int(input("enter your cvv-"))
                cvv=str(cvv)
                if  (len(cvv)==3):
                    print("cvv is correct")
                    print("your cvv is",cvv)
                    name=str(input("enter the name on the card"))
                    print("card belongs to",name)
                    db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
                    cursor=db.cursor()
                    cursor.execute("SELECT sum(amount) FROM add_to_cart")
                    record=cursor.fetchall()
                    for i in record:
                        print(i[0],"has been paid you will recieve your order within 2 days")
                    
            
            else:
               print("card number is wrong.Please pay using cash")
        
    if a==2:
        print("**********************************************************************************")
        db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
        cursor=db.cursor()
        cursor.execute("SELECT sum(amount) FROM add_to_cart")
        record=cursor.fetchall()
        for i in record:
            print("Please pay",i[0],"using cash.You will recieve your order within 2 days ")
        print("**********************************************************************************")
        

        
           
           
db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
cursor=db.cursor()
cursor.execute("Delete FROM add_to_cart")
db.commit()


    

time.sleep(3) 
system("cls")

print("""***********************************************************
      **************************************************************
      **************************************************************
                      Welcome to bigbasket
             We have 6 categories available for you
      **************************************************************
      **************************************************************
      *************************************************************""")
a = 0    
while (a != 99):
    print("These are the categories available")
    db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
    cursor=db.cursor()
    cursor.execute("SELECT * FROM category")
    record=cursor.fetchall()
    for i in record:
        print(i)
    a=int(input("Please enter your category or enter 99 to enter item to the cart"))
    if a==1:
       db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
       cursor=db.cursor()
       cursor.execute("select item_id,item_name,price from item_master where category_id=1  ")
       record=cursor.fetchall()
       for i in record:
           print("item_id:",i[0],"item_name:",i[1],"Price",i[2])
    elif a==2: 
       db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
       cursor=db.cursor()
       cursor.execute("SELECT Item_id,Item_name,Price FROM Item_master where Category_id=2")
       record=cursor.fetchall()
       for i in record:
           print("item_id:",i[0],"item_name:",i[1],"Price",i[2])
    elif a==3:
       db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
       cursor=db.cursor()
       cursor.execute("SELECT Item_id,Item_name,Price FROM Item_master where Category_id=3")
       record=cursor.fetchall()
       for i in record:
           print("item_id:",i[0],"item_name:",i[1],"price",i[2])
    elif a==4:
       db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
       cursor=db.cursor()
       cursor.execute("SELECT Item_id,Item_name,Price FROM Item_master where Category_id=4")
       record=cursor.fetchall()
       for i in record:
           print("item_id:",i[0],"item_name:",i[1],"price",i[2])
    elif a==5: 
       db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
       cursor=db.cursor()
       cursor.execute("SELECT Item_id,Item_name,Price FROM Item_master where Category_id=5")
       record=cursor.fetchall()
       for i in record:
           print("item_id:",i[0],"item_name:",i[1],"price",i[2])
    elif a==6:
       db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
       cursor=db.cursor()
       cursor.execute("SELECT Item_id,Item_name,Price FROM Item_master where Category_id=6")
       record=cursor.fetchall()
       for i in record:
            print("item_id:",i[0],"item_name:",i[1],"price",i[2])

b=0
price=0
amount=0
while b!="20":
    
    itemname=input("Enter Item name : ")
    Quantity=int(input("Enter quantitiy : "))
    print(" Quantity : " , Quantity)
    price=Item_price(itemname)
    print(" Price : " , price)
    amount = price*Quantity
    Items(itemname,Quantity,amount)    
    print("added to cart sucessfully")
    b=input(("Please press enter to add another item or enter 20 to start the billing process:"))


print("These are the items you have selected and their price per kg:")    
db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
cursor=db.cursor()
cursor.execute("SELECT * FROM add_to_cart")
record=cursor.fetchall()
for i in record:
    print(" Item : ",i[0], " Quantity : ", i[1], "Amount : ", i[2])
    
    
print("The sum total of your items is :")
db=mysql.connector.connect(host="localhost",database="bigbasket",user="root",password="root")
cursor=db.cursor()
cursor.execute("SELECT sum(amount) FROM add_to_cart")
record=cursor.fetchall()
for i in record:
    print(i[0])
credit_card_or_cash()






print("We were happy to serve you please do shop with us again")

time.sleep(5)
print("""***********************************************************
      *************************************************************""")
print("Hi customer look at the progress in our sales over the past 2 years.")
print("2016-2017")
Categories=["Fruits","Vegetables","DryFruits","Snacks","DairyProducts","Pulses"]
Sales_in_numbers=["1000kg","5000kg","700kg","8000kg","6100kg","1000kg"]
plt.plot(Categories,Sales_in_numbers)
plt.xlabel(["Categories"])
plt.ylabel(["Number of sales"])
plt.show()


time.sleep(5)
print("2017-2018")
Categories1=["Fruits","Vegetables","DryFruits","Snacks","DairyProducts","Pulses"]
Sales_in_numbers1=["2000kg","6000kg","1900kg","10000kg","6900kg","1900kg"]
plt.bar(Categories1,Sales_in_numbers1)
plt.xlabel(["Categories"])
plt.ylabel(["Number of sales"])
plt.xticks(["Fruits","Vegetables","DryFruits","Snacks","DairyProducts","Pulses"],rotation=30)
plt.show()







 
 
 
