n = int(input("Kaç adet sayı girilecek: "))
a = []

for i in range(0,n):
   element=int(input("Sayıyı girin: "))
   a.append(element)

avg=sum(a)/n
print("Ortalama: ", round(avg,2))

