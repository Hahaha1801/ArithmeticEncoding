# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


def createRange(p):
    previous_value=0
    treshold=0
    for key , value in p.items():
        lower_p[key]=treshold
        treshold=round(value+previous_value,5)
        upper_p[key]=treshold
        previous_value=treshold
    print("Range : ")
    for key in p.keys():
        print(key , " } ", lower_p[key] , " - " , upper_p[key])
    print(p)
    
def expandNext(encode_letter,mul):
    print("Multiplication value : ",mul)
    print("Expanding : ",encode_letter)
    p1 = {key:round( value * mul,5) for key, value in p.items()}
    return p1
    
    
    
#take user input
p={'start':0}
print("How many letter probability data you want to enter")
n=int(input())
for i in range(n):
    print("Enter ",i+1, " letter : ")
    key=input()
    print("Enter probability of ",key , " : ")
    value=float(input())
    p[key]=value
#p={'start':0,'a':0.4,'g':0.2,'s':0.25,'t':0.1,'e':0.05}

print("---------------------------------")

encode=input("Enter String to be encoded")
print(p)
p1=p.copy()
lower_p={}
upper_p={}
createRange(p)
length=len(encode)
iteration=1
print(length)
for encode_letter in encode:
    print("---------- ",encode_letter ," : ",lower_p[encode_letter], " - ",upper_p[encode_letter])
    if iteration==length:
        break
    if encode_letter in p.keys():
        mul=p1[encode_letter]
        p1=expandNext(encode_letter,mul)
    else:
        print("Encoded letter not found in data")
    
    p1['start']=lower_p[encode_letter]
    print(p1)
    createRange(p1)
    iteration+=1
    

