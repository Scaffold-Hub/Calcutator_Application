import  math
import time
import pyqt5_tools


def collection(a,b):
    return a+b
def extraction(a,b):
    return a-b
def impact(a,b):
    return a*b
def chamber(a,b):
    return a/b
def square_root(a,b):
    square = float(input("Enter the number to be squared:"))
    root = square ** 2
    print(root)
def sin(a,b):
    return math.sin(a,b)
def cos(a,b):
    return math.cos(a,b)
def tan(a,b):
    return math.tan(a,b)
def cot(a,b):
    return math.tanh(a,b)
def  cotanjat(a,b):
    return math.acosh(a,b)

print("******************************************* ***\n"
"GELİŞMİŞ HESAP MAKİNESİ PROGRAMI \n"
"LÜTFEN İŞLEM SEÇİN\n"
"Çıkma için = q"
"1. İşlem = Toplama \n"
"2. İşlem = Çıkarma \n"
"3. İşlem = Çarpma \n"
"4. İşlem = Bölme \n"
"5. İşlem = Kare Alma \n"
"6. İşlem = Sin \n"
"7. İşlem = Cos \n"
"8. İşlem = tan\n"
"9. İşlem = Cot \n"
"10. İşlem = Cotanjant \n"
"**********************************************\n" )
gender = input("Are u Madam ;  \n Yes \n No \n Please choose one :")
if gender == "Yes":
    gender = ("Madam")
else:
    gender = ("Gentleman")
process=input("Choose process :")

while True:
    if (process == "q"):
        print("Exit the program , please wait!!!")
        time.sleep(2)
        print(f" See u later {gender}. ")
        break
    elif (process == "1"):
        a = int(input("Pls enter to first number :"))
        b = int(input("Pls enter to second number :"))
        print(collection(a, b))
    elif (process == "2"):
        a = int(input("Pls enter to first number :"))
        b = int(input("Pls enter to second number :"))
        print(extraction(a, b))
    elif (process == "3"):
        a = int(input("Pls enter to first number :"))
        b = int(input("Pls enter to second number :"))
        print(impact(a, b))
    elif (process == "4"):
        a = int(input("Pls enter to first number :"))
        b = int(input("Pls enter to second number :"))
        print(chamber(a, b))
    elif (process == "5"):
        square_root()
    elif(process =="6"):
        sin()
    elif(process == "7"):
        cos()
    elif (process == "8"):
        tan()
    elif(process == "9"):
        cot()
    elif(process == 10):
        cotanjat()
        print(f"Geçersiz İşlem Yaptınız!! Lüfen Tekrar Deneyin !! {gender}")