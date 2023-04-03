
moedas = [1,5,8,11]
n = 13
arr = [float('inf')] * (n+1)
arr[0] = 0

moeda_usadas = [0] * (n+1)

for i in range(1, n+1):
   for moeda in moedas:
      if (moeda <= i and 1+arr[i-moeda] < arr[i]):
         arr[i] = 1+arr[i-moeda]
         moeda_usadas[i] = moeda

print(arr)
print(moeda_usadas)

troco = []

while(n>0):
   troco.insert(0, moeda_usadas[n])
   n = n-moeda_usadas[n]

print(troco)
