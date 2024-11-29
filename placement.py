
#Children,Senior Citizens,Normal Citizen 
'''age = int(input("Enter your age: "))

if age < 10:
     print("Children") 
elif age > 60:
     print("Senior Citizens") 
elif age > 10 and age < 60:
     print("Normal Citizen")'''

#Positive or Not Positive

'''a=int(input("Enter the number:"))
if(a>0):
    if a%5==0:
      print("Positive")
    else:
      print(" Not Positive")'''
#swap number
'''a=30
b=20
a=a+b
b=a-b
a=a-b
print(a,b)'''

#if
'''if 1:
    print("hello")'''
#marks sum
'''mark=int(input("Enter the mark:"))
if mark<25:
    print("f grade")
elif 25<=mark<45:
    print("e grade")
elif 45<=mark<50:
    print("d grade")
elif 50<=mark<60:
    print("c grade")
elif 60<=mark<80:
    print("b grade")
else:
    print("a grade")'''

#salary or loan
'''a=int(input("Enter the age:"))
b=int(input("Enter the salary:"))
if a>=25:
 if b>=25000:
        print("loan eligible")
 else:
    print("age and not salary eligible")
else:
    print("not loan eligible")'''


#super market
''''print("1.sambar power=70")
print("2.rasam power=30")
print("3.appalam=25")
print("4.oil=150")
print("5.rice=2000")
a=70
b=30
c=25
d=150
e=2000
total=0
choice=int(input("enter the choice"))
if  choice==1:
    total=total+sambarpower
elif choice==2:
    total=total+2.rasampower=30
elif choice==3:
    total=total+kiwi
elif choice==4:
    total=total+orange
else:
    print("invalid choice")
print(total)'''


'''print(''''''1.Apple 30
2.banana 40
3.kiwi 50
4.orange 60'''''')
apple=30
banana=40
kiwi=50
orange=60
total=0
choice=int(input("enter the choice"))
if  choice==1:
    total=total+apple
elif choice==2:
    total=total+banana
elif choice==3:
    total=total+kiwi
elif choice==4:
    total=total+orange
else:
    print("invalid choice")
print(total)'''

#21/5/2024
#for loop
'''for i in range(1,5):
    print(i)'''
#while loop
'''i=0
while i<=10:
    print(i)
    i+=1'''
#continue

'''for i in range(10):
    if i ==5:
        continue
    print(i)'''

#break
'''for i in range(10):
    if i==5:
        break
    else:
        print(i)'''

#pass

'''for i in range(10):
    if i==5:
        pass
print(i)


n = int(input("Enter the number:"))
for i in range(1,n+1):
    print(i)'''

#odd and even number
'''n = int(input("Enter the number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i," ","Even")
    else:
        print(i," ","Odd")'''

#sum of digit
'''n = int(input("Enter the number:"))
sum=0
while n!=0:
    r=n%10
    sum+=r
    n=n//10
print(sum)'''

#count of number
'''n = int(input("Enter the number:"))
count=0
while n!=0:
    n=n//10
    count+=1
print(count)'''

'''for i in range(1,10):
    if i==6:
        continue;
    print(i)
else:
    print("end")'''

#multiply of number
'''n = int(input("Enter the number:"))
for i in range(1,11):
    print(n,'*',i,'=',i*n)'''
#sep
#print("suba","vani",sep="_")

#end
'''print("world",end="_")
print("hello")
print(6)'''

#write a program to get numbers till the user want ad count the positive , negative and zeros
'''n = int(input())
while 1:
    choice='yes'or'no'
    if choice==yes:
        if n>0:
            print("Positive")
            if n<0:
                print("Negative")'''
#month
'''while 1:
    m=int(input("Enter the month:"))
    if m==1 or m==3 or m==5 or m==7  or m==8 or m==10 or m==12:
        print("31 days")
    if m==4 or m==6 or m==9 or m==11:
        print("30 days")
    if m==28:
        print("28 days")'''
        



#without using divisin operation
'''s = int(input("Enter the number:"))
d = int(input("enter the difference:"))
count = 0
while n>0:
    s==d
    count+=1
print("count",count)'''

#amstrong
'''n=int(input())
temp=n
sum=0
a=len(str(n))
for i in range(a):
    rem=n%10
    n//=10
    sum+=pow(rem,a)
if(sum==temp):
    print("Amstrong")
else:
    print("not")'''
 
#trailing no.of zero
'''n=int(input("Enter the number:"))
sum=0
p=5
while(n//p):
    sum+=(n//p)
    p=p*5
print(sum)'''


#write a python code to single line sequence (input6)(output234669) *ass
'''n = int(input())
for i in range(2,n+1):
    if i==5:
        continue
    print(i,end=" ")
    if i==6:
       print(6,9)'''
#sum of digit of given number is odd or even (input123)(True)  *ass
'''n=int(input())
sum=0
while(n):
    rem=n%10
    sum+=rem
    n//=10
if (sum%2==0):
    print("Yes")
else:
    print("False")'''
#last digit of given number is positive and divisible by 3 print yes or no (input 126)(outputyes)  *ass
'''n=int(input())
for i in range(2,n+1):
    if i==5:
        continue
    print(i,end=" ")
    if i==6:
        print(6,9)'''
#magic number
'''def Single_Digit(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return Single_Digit(sum) if sum > 9 else sum
num15 = int(input("Enter the number: "))
sum2 = Single_Digit(num15)
print(num15, "is a magic number.") if sum2 == 1 else print(num15, "is not a magic number.")'''

#22/5/2024

#reverse the number:
'''n=int(input("Enter the number:"))
rev =0
while n!=0:
    rev=(rev*10)+n%10
    n=n//10
print(rev)'''

'''n=int(input("Enter the value:"))
temp=n
rev=0
while n!=0:
    rev=(rev*10)+n%10
    n=n//10
if temp== rev:
    print("this is palindom:")
else:
    print("this is not palindrom:")'''

# check pefect number or not
'''n=int(input("Enter the number:"))
sum = 0
for i in range(1,n):
    if n%i==0:
       sum+=i
if sum==n:
    print("perfect")
else:
    print("not perfect") '''

#pefect number 1 to 100 kulavara number
'''for j in range(1,101):
    n=j
    sum = 0
    for i in range(1,n):
        if n%i==0:
           sum+=i
    if sum==n:
      print("perfect",n)'''
#factorial   
'''n=int(input("Enter the number:"))
ss = 1
for i in range(1,n+1):
       ss*=i
print(ss)'''

#sum
'''n=int(input("enter the number:"))
sum=0
n = 1
for i in range(1,n+1):
    sum+=(n//i)
print(sum)'''
#duck number
'''s=str(input("Enter the number:")) 
f=0
if s[0]=='0':
    f==1
else:
    for i in s:
        if i=='0':
            f=1
            break
if s==0:
    print("not")
else:
     print("duck number")'''
# retanangle pattern
'''rows = int(input("Enter the number:"))
columns = int(input("Enter the number:"))
for i in range(rows):
    for j in range(columns):
        print('*',end="")
    print()'''
#squre pattern
'''rows = int(input("Enter the number:"))
for i in range(rows):
    for j in range(rows):
        print('*',end="")
    print()'''
#right angle pattern 
'''rows= int(input("Enter the number:"))
for i in range(rows):
    for j in range(i+1):
        print('*',end="")
    print()'''
#left angle pattern
'''rows= int(input("Enter the number:"))
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end="")
    for k in range(i+1):
        print('*',end="")
    print()'''
#pyraming pattern
'''rows= int(input("Enter the number:"))
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print('*',end="")
    print()'''
#down pyraming pattern
'''for i in range(rows-1,0,-1):
    for j in range(rows-i-1):
        print(" ",end="")
    for k in range(2*i-1):
        print('*',end="")
    print()'''

#diamond pattern
''''rows= int(input("Enter the number:"))
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print('*',end="")
    print()
for i in range(rows-1,0,-1):
    for j in range(rows-i-1):
        print(" ",end="")
    for k in range(2*i-1):
        print('*',end="")
    print()'''

#23/5/2024

'''l=[1,3,5]
for i in l:
    print(i)'''

'''l=[]
n=int(input())
for i in range(0,n):
    element=int(input())
    l.append(element)
print(i)'''
#sim of lise
'''l=[1,2,3]
sum=0
for i in l:
    sum=sum+i
print(sum)'''
#sum of tuple
'''t=(1,2,3)
sum=0
for i in t:
    sum=sum+i
print(sum)'''
#max of list
'''l=[1,2,4,67,89]
max=l[0]
for i in l:
    if max<i:
        max=i
print(max)'''
#min of list
'''l=[1,2,4,67,89]
min=l[0]
for i in l:
    if min>i:
        min=i
print(min)'''
#tuple of max
'''t=(1,2,4,67,89)
max=t[0]
for i in t:
    if max<i:
        max=i
print(max)'''
#list of sort
'''l=[10,34,67]
l.sort()
print(l[-1])'''
#list of duplicate
'''l=[1,2,3,4,1,3]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)'''
#duplicate count
'''l=[1,2,3,4,1,3]
count=0
n=int(input())
for i in l:
    if i==n:
          print(count)'''
#left rotaion
'''def left(a,n):
    temp=a[0]
    for i in range(n-1):
        a[i]=a[i-1]
    a[0]=temp
def rot (a,k,n):
    for i in range(k):
        left(a,n)
a=list(map(int,input().split()))
n=len(a)
k=int(input())
rot=(a,k,n)
print(a)'''
#24/5/2024
#set
'''set={45,67,'d',4,'bcs',7,'r'}
print(set)'''
#len set
'''s={23,45,67,'hju',56,'er'}
print(len(s))'''
#remove duplicate
'''s={12,34,12,45}
print(s)'''
#list of set
'''list1=[1,2,34,4]
set1=set(list1)
print(set1)'''
#string of set
'''string=['h','e','l','l','0']
set1=set(string)
print(set1)'''
#tuple of set
'''tuple=[1,2,4,5]
set1=set(tuple)
print(set1)'''
#true or false
'''s={0,1,'true','false'}
print(s)'''
#duplicate list to set
'''l=[1,2,3,4,55,1,2]
s=set(l)
print(s)'''
#set split
'''a="hello word"
a.split()
set=set(a)
print(set)'''
#set split
'''s="hello word"
print(set(s))'''

#s='hello word'
'''s1=set(s)
print(type(s))
print(type(s1))
print(s1)'''

'''l=[10,20,30]
print(l)
print(*l)'''

'''d={1:'a',2:'c',3:'f'}
print(d)
print(*d)'''

'''d={0:10,1:20}
print(d)
d={2:30}
d.update({2:30})
print(d)'''
#sum of all item
'''my_dict = {'data1': 10, 'data2': -5, 'data3': 27}
result = sum(my_dict.values())
print(result)'''

'''color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))'''

#to get keys in dictionary
'''dict={'a':100,'b':200,'c': 300}
if dict.get('b')==None:
    print("not present")
else:
    print("present")'''

#values check in dict using membership operator
'''dict={'a':100,'b':200,'c': 300}
if 100 not in dict==None:
    print("not present")
else:
    print("present")'''	

#sum of all item
'''my_dict = {'data1': 10, 'data2': -5, 'data3': 27}
result = sum(my_dict.values())
print(result) '''

#remove duplicate elements in dictionary
'''student_data={'Id1':100,'Id2':200,'Id3':100}
result={}
for key,value in student_data.items():
   if value not in result.values():
        result[key]= value
print(result)'''
#28/5/2024
#string multiply comment
#print('''Hi welcome
#Hello world
#placement class''')

#char in sting
'''a='suba'
print(a)
print(a[0])'''
# for in string
'''for i in "suba":
    print(i)'''
#in
'''a = "Hello word"
print("Hello"in a)'''
#not in
'''a = "Hello word"
print("Hello" not in a)'''
#if in 
'''a = "Hello word"
if "Hello" in a:
    print('true')
else:
    print('false')'''
#if not in
'''a = "Hello word"
if "Hello" not in a:
    print('true')
else:
    print('false')'''
#modify the string
'''a=" hello world "
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.split())
print(a.strip())
print(a.replace('hello','hii'))
print(a.find('h'))
print(a.count('l'))
print(len(a))
print(a[2:5])#slicing
print(a.startswith(''))
print(a.endswith('welcome'))
print('*'.join(a))
t="This is \"placement\" class"
print(t)'''

#find the len of the string without built in function
'''a='hello world'
length=0
for char in a:
    length+=1
print(length)'''

#individual char string in reverse order
'''a = "world"
b=a[::-1]
print(b)
for i in b:
    print(i)'''

#count the no.of words
'''a="hello world"
count=a.split()
print(len(count))'''

#to count number,alphabltes,digits,special char
'''u="my name is suba & my age is 18"
a=0
n=0
s=0
for i in u:
    if ('a'<=i<='z' or 'A'<=i<='Z'):
        a+=1
    elif('0'<=i<='9'):
        n+=1
    else:
        s+=1
print("alphabets:",a)
print('number:',n)
 print("special char",s)'''
#Write a python program to sort a string array in ascending order
'''str = ["a","o","b","g","c"]
print("Original array:")
print(" ".join(str))
sorted = sorted(str)
print("Sorted array in ascending order:")
print(" ".join(sorted))'''
#Write a program in python to extract a substring from a given string.
'''string = input("Enter the string: ")
start_index = int(input("Enter the starting index: "))
substring = int(input("Enter the  substring: "))
substring = string[start_index:start_index + substring]
print("Extracted snibstring:", substring)'''
#Write a python  program to check whether a substring is present in a string.
'''string = input("Enter the string: ")
substring = input("Enter the substring: ")
is_present = substring in string
if is_present:
    print(f"The substring is present.")
else:
    print(f"The substring is not present.")'''

'''string = input("Enter the string: ")
word_to_count = input("Enter the word to count: ")
word_count = string.split().count(word_to_count)
print(f"The word '{word_to_count}' appears {word_count} times in the string.")'''

# user's first and last name and prints them in reverse order with a space between them.
'''a=input("1st name:")
b=input("2nd name:")
print(b,a,end=" ")'''
# the Values of Two Numbers without Using a Temporary Variable
'''a=10
b=5
print(b,a)'''
#Read a Number n and Compute n+nn+nnn
'''n=input("enter num:")
nn=n+n
nnn=n+n+n
result=int(n)+int(nn)+int(nnn)
print('Result:',result)'''

#remove duplicate element in list
'''l=[1,2,3,4,1,3]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)'''
#two type ofp duck number
'''s = input("Enter the number:")
if s.isdigit() and s[0] != '0' and '0' in s:
    print("duck number")
else:
    print("not a duck number")'''
'''s=str(input("Enter the number:")) 
f=0
if s[0]=='0':
    f==1
else:
    for i in s:
        if i=='0':
            f=1
            break
if s==0:
    print("not")
else:
     print("duck number")'''
#bio data
'''name = input("name:")
age = int(input("age:"))
Email= input("Email:")
phone = int(input("phone number:"))

print("Name:",name)
print("Age:",age)
print("mail:",Email)
print("phone:",phone)'''
#find the location of the word in the string
'''s = "this is placement class"
j="class"
l=s.split()
b=l.index(j)
print(b+1)'''
#type two
'''a="taj is taj was taj"
j="taj"
l=a.split()
for i in range(len(l)):
    if l[i]==j:
        loc=i
print(loc+1)'''
#split the string vowles
''''import re
a="placement"
l=re.split('a|e|i|o|u',a)
print(l)'''

