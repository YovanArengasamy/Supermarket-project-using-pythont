import datetime
import re
import store
import random
import smtplib
print(" *** STAR SUPERMARKET ***")
print("Welcome Sir/Madam")
y=datetime.datetime.now()
print(y)
f=open("detail.txt","r")
txt=f.read()
def super_market():
    print("NOTE: Enter the Product name FIRST LETTER should be CAPTIAL" )
    user=input("Enter the product name:")
    x=re.search(user,txt)
    print(x)
    if user == x:
        print("This product is available") 
    try:
        get=int(input("Enter the number:"))
        how_many=int(input("How many:"))
        if get==1:
            x=random.randint(0000,9999)
            print(f" Your OTP number is:{x}")
            z=int(input("Enter your OTP number:"))
            store.Horlicks()
            rate=200
            gst_amount=10
            total=how_many * rate
            print(f"Your total bill is : {total}")
            gst_price=total*(gst_amount)/100
            price=total+gst_price
            print(f"Your Within GST bill is:{price}")  
            var=input("Do you want to continue press yes:")
            if var=="yes":
                super_market()
            else:
                print("Thanks for visiting our Supermarket")
                print("bill generated successfully")


        elif get==2:
            x=random.randint(0000,9999)
            print(f"Your OTP number is:{x}")
            z=int(input("Enter your OTP number:"))
            store.Boost()
            rate=150
            gst_amount=8
            total=how_many * rate
            print(f"Your total bill is : {total}")
            gst_price=total*(gst_amount)/100
            price=total+gst_price
            print(f"Your GST bill is:{price}")
            var=input("Do you want to continue press yes:")
            if var=="yes":
                super_market()
            else:
                print("Thanks for visiting our Supermarket")
                print("bill generated successfully")
        elif get==3:
            x=random.randint(0000,9999)
            print(f"Your OTP number is:{x}")
            z=int(input("Enter your OTP number:"))
            store.Bournvita()
            rate=100
            gst_amount=7
            total=how_many * rate
            print(f"Your total bill is:{total}")
            gst_price=total*(gst_amount)/100
            price=total+gst_price
            print(f"Your GST bill is:{price}")
            var=input("Do you want to continue press yes:")
            if var=="yes":
                super_market()
            else:
                print("Thanks for visiting our Supermarket")
                print("bill generated successfully")
        elif get==4:
            x=random.randint(0000,9999)
            print(f"Your OTP number is:{x}")
            z=int(input("Enter your OTP number:"))
            store.Complan()
            rate=200
            gst_amount=7
            total=how_many * rate
            print(f"Your total bill is:{total}")
            gst_price=total*(gst_amount)/100
            price=total+gst_price
            print(f"Your GST bill is:{price}")
            var=input("Do you want to continue press yes:")
            if var=="yes":
                super_market()
            else:
                print("Thanks for visiting our Supermarket")
                print("bill generated successfully")
        elif get==5:
            x=random.randint(0000,9999)
            print(f"Your OTP number is:{x}")
            z=int(input("Enter your OTP number:"))
            store.Glucon_D()
            rate=100
            gst_amount=8
            total=how_many * rate
            print(f"Your total bill is:{total}")
            gst_price=total*(gst_amount)/100
            price=total+gst_price
            print(f"Your GST bill is:{price}")
            var=input("Do you want to continue press yes:")
            if var=="yes":
                super_market()
            else:
                print("Thanks for visiting our Supermarket")  
                print("bill generated successfully") 
    except:
        print("please...type number only")  
    else:
        print("Sorry...This product are not avaliable")
def email_sending():
    try:
        receiver_mails=int(input("Enter your email id:"))
        for i in receiver_mails:
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login("yo22062002","wrei nfuh zrof uphe")
            message=f("Your GST bill is:{price}")
            print(message)
            s.sentmail("yo22062002",i,message)
            s.quit()  
    except:
        print("Email not sent")
super_market()
email_sending()
