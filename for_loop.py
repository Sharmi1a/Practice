def markscard(a):
    
    if (a>=70):
        print("1st division")
    elif(a<=69 and a>=50 ):
        print("2nd division")
    elif(a<=49 and a>30):
        print("3rd division")
    else:
        print("failed")
        

        
mark = []
for i in range(0,5):
    c= int(input("Enter the marks of subjects: "))
    mark.append(c)
    
#mark = [10,20,30,40,50]

total = 0
full_m = 500

for i in range(0,len(mark)):
    total += mark[i]
    
b = (total/full_m)*100
print(total)
print(b)
    
x = markscard(b)
print(x)


z = markscard(b+30)
print(z)
