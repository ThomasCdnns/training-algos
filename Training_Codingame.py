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