#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[ ]:





# In[9]:


# KÜME FARKI

kume={11,22,33,44}
kume2={33,44,55,66,77,88,99}

#1. yöntem
kumeFarki =  kume - kume2
print(kumeFarki)

#2. yöntem
kumeFarki = kume.difference(kume2)
print(kumeFarki)

kumeFarki =  kume2.difference(kume)
print(kumeFarki)


# In[10]:


#Küme kesişim
kume={11,22,33,44}
kume2={33,44,55,66,77,88,99}

#1. yöntem
kumeKesisim = kume & kume2
print(kumeKesisim)

#2. yöntem
kum


# In[11]:


# KÜME BİRLEŞİM

kume={11,22,33,44}
kume2={33,44,55,66,77,88,99}

kumeBirlesim =  kume.union(kume2)
print(kumeBirlesim)


# In[17]:


#1 1-15 arasında 5'er adet sayı üretip 2 farklı kümeye kaydediniz.


# Kebap  kebap-case-yontemi
# Camel Case camelCase
#FullCase FULLCASE
#Pascal Case PascalCase
#Snake Case snake_case

from random import randint as randomGenerator 

kume1 = set()
kume2 = set()

for i in range(5):
    while True:
        sayi = randomGenerator(1,15)
        if(sayi not in kume1):
            kume1.add(sayi)
            break
        else:
            print("Bu sayı 1. kümede var: ", sayi)
    while True:
        sayi =  randomGenerator(1,15)
        if(sayi not in kume2):
            kume2.add(sayi)
            break
        else:
            print("Bu sayı 2. kümede var: ", sayi)
            
print(kume1)
print(kume2)


# In[18]:


# ikinci olusturma yöntemi
from random import randint as randomGenerator 

kume1 = set()
kume2 = set()

while len(kume1) <5:
    kume1.add(randomGenerator(1,15))
    

while len(kume2) <5:
    kume2.add(randomGenerator(1,15))

print(kume1)
print(kume2)



# In[19]:


# SORU: 1-100 arasında rastgele 10 sayı üretip bir listeye atayın


from random import randint as sayici
liste =  list()
for i in range(10):
    liste.append(sayici(1,100))
print(liste)


# In[21]:


#Daha sonra bu listedeki en büyük ve en küçük elemanları hazır fonksiyon kullanmadan bulun. (liste ile çözün-max(),min(),sort(),reverse())
from random import randint as sayici
liste =  list()
for i in range(10):
    liste.append(sayici(1,100))

print(liste)

kucuk = 100
buyuk = 0
for i in liste:
    if(i > buyuk):
        buyuk = i
    
    if (i < kucuk):
        kucuk = i

print(kucuk)
print(buyuk)


# In[ ]:




