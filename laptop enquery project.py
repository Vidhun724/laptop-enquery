class laptop:
   
    def hp(self):
        a=int(input("Enter the price:"))
        if(a>=10000 and a<=20000):
            print("HP-->processor:i3")
            print("HP-->RAM=8gb")
            print("laptop is available right now!!")
        elif(a>=20000 and a<=30000):
            print("HP-->processor=i5")
            print("HP-->RAM=8gb")
            print("laptop is available right now!!")
        else:
            print("HP-->Laptop is not available")


    def lenovo(self):
        b=int(input("Enter the price:"))
        if(b>=20000 and b<=30000):
            print("LENOVO-->processor:i3")
            print("LENOVO-->RAM=16gb")
            print("laptop is available right now!!")
        elif(a>=30000 and a<=40000):
            print("LENOVO-->processor=i5")
            print("LENOVO-->RAM=16gb")
            print("laptop is available right now!!")
        else:
            print("LENOVO-->Laptop is not available")
                  
            

HP = laptop()
LENOVO = laptop()

print("AVAILABLE BRANDS IS hp AND lenovo!")
print()
print("Available price of HP laptop is 10000 to 30000!")
print()
print("Available price of lenova laptop is 20000 to 40000!")
print()
print("Choose the available brands!")
print()
user=str(input("Enter the brand name:"))

vidhun="hp"
apoorvan="lenovo"
if(user==vidhun):
    HP.hp()
elif(user==apoorvan):
    LENOVO.lenovo()
else:
    print("SOORY..THE BRAND NOT AVAILABLE RIGHT NOW")





