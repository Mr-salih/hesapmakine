
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
 
# Toplama Fonksiyonu
def Topla(x, y):
   return x + y
 
# Çıkarma Fonksiyonu
def Cikar(x, y):
   return x - y
 
# Çarpma Fonksiiyonu
def Carp(x, y):
   return x * y
 
# Bölme Fonksiyonu
def Bol(x, y):
   return x / y
 
print("Yapılacak İşlemi Seçin.")
print("=======================")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")
 
# Kullanıcıdan Seçim İsteme
secim = input("Seçiminiz (1/2/3/4):")
 
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
 
if secim == '1':
   print(sayi1,"+",sayi2,"=", Topla(sayi1,sayi2))
 
elif secim == '2':
   print(sayi1,"-",sayi2,"=", Cikar(sayi1,sayi2))
 
elif secim == '3':
   print(sayi1,"*",sayi2,"=", Carp(sayi1,sayi2))
 
elif secim == '4':
   print(sayi1,"/",sayi2,"=", Bol(sayi1,sayi2))
else:
   print("Geçersiz Giriş")
 