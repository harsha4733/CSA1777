a=int(input("Enter Jug A Capacity: "))
b=int(input("Enter Jug B Capacity: "))
ai=int(input("Initially Water in Jug A: "))
bi=int(input("Initially Water in Jug B: "))
af=int(input("Final State of Jug A: "))
bf=int(input("Final State of Jug B: "))
print("List Of Operations You can Do:\n")
print("1.Fill Jug A Completely\n")
print("2.Fill Jug B Completely\n")
print("3.Empty Jug A Completely\n")
print("4.Empty Jug B Completely\n")
print("5.Pour From Jug A till Jug B filled Completely or A becomes empty\n")
print("6.Pour From Jug B till Jug A filled Completely or B becomes empty\n")
print("7.Pour all From Jug B to Jug A\n")
print("8.Pour all From Jug A to Jug B\n")
while ((ai!=af or bi!=bf)):
    op=int(input("Enter the Operation: "))
    if(op==1):
        ai=a
    elif(op==2):
        bi=b
    elif(op==3):
        ai=0
    elif(op==4):
        bi=0
    elif(op==5):
        if(b-bi>ai):
            bi=ai+bi
            ai=0
        else:
            ai=ai-(b-bi)
            bi=b
    elif(op==6):
        if(a-ai>bi):
            ai=ai+bi
            bi=0
        else:
            bi=bi-(a-ai)
            ai=a
    elif(op==7):
        ai=ai+bi
        bi=0
    elif(op==8):
        bi=bi+ai
        ai=0
    print(ai,bi);
