#My claculator

import math
from os import sep
import time
import datetime
from speakfunc import speak, speak1

# Operations
def sum():
 s=0
 speak1('enter how many number you want to add')
 n = int(input("Enter how many number you want to add: "))
 l=[*range(0,n)]
 for i in range(0,n):
      m=i+1
      y=float(input(f'Enter a number {m}: '))
      l[i]=y
 s=math.fsum(l)
 speak('The sum of given numbers is:')
 speak(s)

def multi():
     s=0
     speak1("Enter how many number you want to multiply")
     n = int(input("Enter how many number you want to multiply: "))
     l=[*range(0,n)]
     for i in range(0,n):
       m=i+1
       y=float(input(f'Enter a number {m}: '))
       l[i]=y
     s=math.prod(l)
     speak('The product of given numbers is:')
     speak(s)

def power():
     speak1('enter the base number')
     n= int(input("Enter the base number: "))
     speak1('enter the power')
     m=int(input("Enter the power: "))
     x=n**m
     speak(f'The result is:\n{x}' )

def sub():
     speak1('enter the first number')
     num1=float(input("Enter 1st number: "))
     speak1('enter the second number')
     num2=float(input("Enter 2nd number: "))
     sut=num1-num2
     speak(f'The result is \n{sut}')

def divide():
     speak1('enter the dividend')
     num1=float(input('Enter the dividend: '))
     speak1('enter the divisor')
     num2=float(input("Enter the divisor: "))
     num=num1/num2
     q=num1//num2
     r=num1%num2
     speak(f'The result is\n{num:.2f}')
     speak('     OR')
     speak(f'{q} is the quotient and {r} is the reminder')

def conv():
     speak1('enter the index in which you want to convert your distance')
     n=int(input("Enter in which you want to convert the distance\n1. m to km \n2. km to m\n>>>"))
     if n==1:
           speak1('enter the distance in meter')
           d=float(input('Enter the distance in m: '))
           km=d//1000
           m=d%1000
           speak1(f'{km} kilometer and {m} meter')
           print(f'{km} km {m} m')
     elif n==2:
          speak1('enter the distance in kilometer')
          d=float(input('Enter the distance in km: '))
          m=d*1000
          speak1(f'{m} meter')
          print(m, 'm')
     else:
          if n!=1&2:
               speak("Wrong input!!!")
               conv()

def sqrt():
     speak1('enter the number')
     num=float(input("Enter the number: "))  
     n=math.sqrt(num)
     speak(f"Square root of given number is:\n{n:.2f}")    

def oe():
     speak1('enter the number')
     num=int(input("Enter the number: "))
     if num%2==0:
          speak(f"{num} is even.")
     else:
          speak(f"{num} is odd.")

def sqr():
     speak1('enter the number')
     num=float(input("Enter the number: "))
     n=num**2
     speak(f"Square of {num} is {n}.")

def table():
     speak1('enter the number of which you want table')
     n=int(input("Enter the number of which you want table: "))
     for i in range(1,11):
          m=n*i
          speak1(f"{n}  {i}jaa  {m}")
          print(f'{n} x {i} = {m}')

def CI():
     speak1("Enter the initial amount")
     a=int(input("Enter the initial amount: "))
     speak1("Enter the interest rate per year")
     it=float(input("Enter the interest rate per year: "))
     speak1("Enter the time period in year")
     p=int(input("Enter the time period(in year): "))
     speak1("Enter how you plan to invest monthly")
     m=float(input("Enter how you plan to invest monthly: "))
     fa=0
     m=m*12
     for i in range(0,p):
          if fa==0:
               fa=a
          fa=(fa+m)*(1+it)
     speak("This is how much you would have in your account after {} years ".format(p)+str('%.2f'%fa))
     

#def alzebra():
     #num=0
     #a=int(input("enter the number which is associate with x^2: "))
     #b=int(input("enter the number which is associate with x: "))
     #c=int(input("enter the constant: "))
     #d=b**2-4*a*c
     #n=math.sqrt(d)
     #x= -b+n
     #num=a*x**2+b*x+c
     #print(x)

def mole():
     speak1("Enter the given mass")
     m=int(input("Enter the given mass: "))
     speak1('Enter the molar mass')
     M=int(input('Enter the molar mass: '))
     x=m/M
     speak("The total number of mole of given molecule is: ")
     speak(x)
#command code
def cmd():
      time.sleep(0.5)
      speak1('what you want to do select from given below')
      print('''
What you want to do select from given below
     1. SUM 
     2. SUBTRACTE
     3. MULTIPLY 
     4. DIVIDE 
     5. SQUARE 
     6. SQUARE ROOT 
     7. FIND POWER 
     8. DISTANCE CONVERTOR 
     9. ODD/EVEN 
     10. MOLE 
     11. TABLE
     12. COMPOUND INTEREST''')
      time.sleep(2)
      cmd2()
def cmd2():
      speak1("Enter the number of which operation you want to do")
      n=int(input("Enter the number of which operation you want to do: "))
#to execute operations
      if n==1:
          sum()
      elif n==2:
          sub()
      if n==3:
          multi()
      elif n==4:
         divide()
      if n==5:
          sqr()
      elif n==6:
          sqrt()
      if n==7:
          power()
      elif n==8:
          conv()
      if n==9:
          oe()
      if n==10:
          mole()
      if n==11:
           table()
      elif n==12:
           CI()
#If conditions not meet      
      elif n>12 :
          speak("Wrong Input!!!")
          time.sleep(0.6) 
          cmd2()
      if n<1:
           speak("Wrong Input!!!") 
           time.sleep(0.6) 
           cmd2()                                                                                        
      time.sleep(2)
      cmp()
#to repeat it(loop)
def cmp():
     speak1("Do you want to continue")
     k=input("Do you want to continue(1.Yes/2.No): ").lower()
     if k in ('1','y','yes'):
          cmd()
     elif k in ('2','n','no'):
          speak("THANK YOU FOR USING ME :)")
          exit()          
     else:
         cmp()
#greeting and intro code
def wish():
    hour = int(datetime.datetime.now().hour)
    t = time.localtime()
    current_time = time.strftime("%I:%M %p", t)
    
    if hour>=0 and hour<12:
        speak(f"Good Morning Sir. It's {current_time}") 
    elif hour>=12 and hour<=18:
        speak(f"Good afternoon Sir. It's {current_time}")
    else:
        speak(f"Good evening Sir. It's {current_time}") 
    time.sleep(1)
#intro line
    speak('''Hello, I'm CALCY. 
I'm programmed to solve your any basic mathametic calculation like + - / * and many more...
 Feel free to ask your any query.
And also share your opinion regarding me and any upgradation.\n                ｡◕ ‿ ‿ ◕ ｡''' )
    #time.sleep(5)
    speak('''        Programmed  by  ASHISH .
''')
    time.sleep(2)

    cmd()
#run
if __name__=='__main__':

 wish()









