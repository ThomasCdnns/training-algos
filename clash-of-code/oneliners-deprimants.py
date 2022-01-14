#Pyramide Inversée Somme 

n = int(input())
numbers = []
for i in input().split():
    numbers += [int(i)]
somme = numbers
while len(somme) != 1:
    numbers = somme
    somme = []
    for i in range(len(numbers)-1):
        somme += [numbers[i]+numbers[i+1]]
print(somme[0])

#==============================================

# Heure arrivée avion

def to_time(t):
    splits = t.split(":")
    return int(splits[0])*3600+int(splits[1])*60+int(splits[2])
t = to_time(input())
t_2 = to_time(input())
if t == t_2:
    print("ON TIME")
elif t > t_2:
    print("EARLY")
else:
    print("DELAYED")

#==============================================

# Pourcentage Import-Export

I=input
f=lambda :map(int,I().split())
I(f"{sum(f())*100//sum(f())}%")

#==============================================

e,s,l,i=input().split(" "),0,0,input().split(" ")
for k in e:s+=int(k)
for j in i:l+=int(j)
print(str(int(s/l*100))+"%")

#==============================================

c=0
k=input
for i in range(int(k()),int(k())+1):
 if i%100==0 and i%400!=0:i+=1
 if i%4==0:c+=1
k(c)

#==============================================

I=input
I(sum([(0,1)[i%100!=0 and i%4==0 or i%100==0 and i%400==0]for i in range(int(I()),int(I())+1)]))