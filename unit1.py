#avg temp of week
'''a,b,c,d,e,f,g=int(input("day1=")),int(input("day2=")),int(input("day3=")),int(input("day4=")),int(input("day5=")),int(input("day6=")),int(input("day7="))
avg=((a+b+c+d+e+f+g)/7)
print("avg temp of the week:",avg)

#GST
item_name=input("enter name=")
sp=int(input("enter sp="))
cgst_rate=float(input("enter cgst rate="))
sgst_rate=float(input("enter sgst rate="))
cgst=(sp*(cgst_rate)/100)
sgst=(sp*(sgst_rate)/100)
total_amount=sp+cgst+sgst
print(f'total_amount:{total_amount:.2f}')

#details
name='akshitha'
rollno=1234
per=80
exam='intermediate'
print(name,type(name))
print(rollno,type(rollno))
print(per,type(per))
print(exam,type(exam))

#squre
n=int(input("enter numb="))
square=n**2
print("the square of",n,'is',square,sep='')

#area of triangle
b=2
h=6
area=0.5*b*h
print(area)'''

#datatypes
a=10
print(a,type(a))
b=5.5
print(b,type(b))
c='akshitha'
print(c,type(c))
d=True
print(d,type(d))
e=[12,23,34]
print(e,type(e))
f=(12,56)
print(f,type(f))
g={"name":"akshitha","rollno":"1"}
print(g,type(g))
h={1,2,3,4}
print(h,type(h))
i=2+4j
print(i,type(i))

