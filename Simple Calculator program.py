a=int(input('enter first number'))
b=int(input('enter the second number'))

print('select choise:')
print('1.add\n2.sub\n3.mul\ndiv\npower\n')
choise=input('enter the choice:')
if choise=='1':
    print(a,'+',b,'=',a+b)
elif choise=='2':
    print(a,'-',b,'=',a-b)
elif choise=='3':
    print(a,'*',b,'=',a*b)
elif choise=='4':
    print(a,'/',b,'=',a/b)
elif choise=='5':
    print(a,'**',b,'=',a**b)
else:
    print('INVALID')
    
       
