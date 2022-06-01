from math import *

def L(n):
    if(n==1000):
        return "one thousand"
    elif(n>99):
        if(n%100==0):
            return ( L(n/100)+" hundred")
        else:
            return (L(n//100) + " hundred and " + L(n%100))
    elif(n>19):
        return(D(n//10) + " " +L(n%10))
    else:
        if(n==19):
            return "nineteen"
        elif(n==18):
            return "eighteen"
        elif(n==17):
            return "seventeen"
        elif(n==16):
            return "sixteen"
        elif(n==15):
            return "fifteen"
        elif(n==14):
            return "fourteen"
        elif(n==13):
            return "thirteen"
        elif(n==12):
            return "twelve"
        elif(n==11):
            return "eleven"
        elif(n==10):
            return "ten"
        elif(n==9):
            return "nine"
        elif(n==8):
            return "eight"
        elif(n==7):
            return "seven"
        elif(n==6):
            return "six"
        elif(n==5):
            return "five"
        elif(n==4):
            return "four"
        elif(n==3):
            return "three"
        elif(n==2):
            return "two"
        elif(n==1):
            return "one"
        else:
            return ""

def D(n):
    if(n==2):
        return "twenty"
    elif(n==3):
        return "thirty"
    elif(n==4):
        return "forty"
    elif(n==5):
        return "fifty"
    elif(n==6):
        return "sixty"
    elif(n==7):
        return "seventy"
    elif(n==8):
        return "eighty"
    elif(n==9):
        return "ninety"
    else:
        return n
def somme(L):
    s=0
    for i in L:
        if(i!=" "):
            s+=1
    return s
def f(n):
    S=""
    for i in range(1,n+1):
        A=L(i)
        S=S+A
        print(str(i)+ ": "+A)
    return (somme(S))
print(f(1000))
