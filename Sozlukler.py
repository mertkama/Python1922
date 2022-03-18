#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Sözlükler (Dictionaries)

datam = {
    "country": "Turkey",
    "city":"Istanbul",
     3:5,
    True: False
}

datam2 = {}
datam3 = dict()

print(datam)
print(datam["city"])
print(type(datam))
print(datam[3])
print(datam[True])



sozluk = {
    "book": "Kitap",
    "pencil": "Kalem",
    "noteBook": "Defter",
    "eraser": "Silgi"
}

print(sozluk["book"])


#Ögelere erişmek 1. yöntem
print(sozluk["book"])

#Ögelere erişmek 2. yöntem
print(sozluk.get("book"))


# In[12]:


telefon_rehberi =  {
    "mehmet": "532 532 32 32",
    "ahmet": "544 544 44 44",
    "cem": "530 530 30 30"
}

kisi = input("Numarası bulunacak kişinin adını yazınız")
cevap = "{} adlı kişinin telefon numarası: {}"
print(cevap.format(kisi, telefon_rehberi[kisi.lower]))


# In[21]:


telefon_rehberi =  {
    "mehmet": "532 532 32 32",
    "ahmet": "544 544 44 44",
    "cem": "530 530 30 30"
}

kisi = input("Numarası bulunacak kişinin adını yazınız")
kisi = str(kisi).lower()
if kisi in telefon_rehberi:
    cevap =  "{} adlı kişinin telefon numarası:  {}"
    print(cevap.format(kisi, telefon_rehberi[kisi]))
else:
    print("Bu kişi rehberde bulunamadı !!!")


# In[31]:


sozluk = {
    "ad"         : "Mehmet Nuri",
    "soyad"      : "ÖZTÜRK",
    "dogumTarihi": "20.11.1993",
    "unvan"      : "Sn Software Engineer"
}

print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())
print(len(sozluk))
print("asddd" in sozluk )

print("ad" in sozluk )


# In[35]:


#Sözlüğün anahtar ve değerlerine (keys, values) ulaşma
sozluk = {
    "ad"         : "Mehmet Nuri",
    "soyad"      : "ÖZTÜRK",
    "dogumTarihi": "20.11.1993",
    "unvan"      : "Sn Software Engineer"
}

for k,v in sozluk.items():
    print("Key {} value {} " .format(k,v))
    


# In[37]:


#Sözlüğün anahtarlarına(keys) ulaşma
sozluk = {
    "ad"         : "Mehmet Nuri",
    "soyad"      : "ÖZTÜRK",
    "dogumTarihi": "20.11.1993",
    "unvan"      : "Sn Software Engineer"
}

for k in sozluk.keys():
    print(k)
    


# In[38]:


#Sözlüğün değerlerine ulaşma
sozluk = {
    "ad"         : "Mehmet Nuri",
    "soyad"      : "ÖZTÜRK",
    "dogumTarihi": "20.11.1993",
    "unvan"      : "Sn Software Engineer"
}

for k in sozluk.values():
    print(k)
    


# In[43]:



#Sözlük Güncelleme
s1={"ad":"Selim","soyad":"Kaçar"}
s2={"soyad":"Kaçar","ad":"Selim"}
s3={"soyad":"Varan","ad":"Selim"}
s4={"soy":"Kaçar","ad":"Selim","yas":30}
print(s1)
print(s2)
print(s3)
print(s4)
s2.update(s3)
print(s3)
print(s2)


# In[58]:


#Sözlük Silme
s1={"ad":"Selim","soyad":"Kaçar"}
s1["ad"] = "Mehmet"
del s1
print(s1)


# In[67]:


#Sözlük içinde bir anahtarı(key) silme
s1={"ad":"Selim","soyad":"Kaçar"}
# del s1
print(s1)
s1.pop("ad")
print(s1)
s1.popitem()
print(s1)


# In[63]:


#Sözlüklerin kopyalanması
s1={"ad":"Selim","soyad":"Kaçar"}
s2={"soyad":"Kaçar","ad":"Selim"}
s3=s2.copy()
print(s3)


# In[73]:


#Sözlüğü temizleme
s1={"ad":"Selim","soyad":"Kaçar"}

#Rastgele eleman çıkarma
s1.popitem()
print(s1)

#2. yöntem
s2={"ad":"Selim","soyad":"Kaçar"}
s2.clear()
print(s2)


#Sözlüğü Tamamen Silme
del s1
del s2


# In[76]:


#İç içe sözlükler
sozluk={
    "sehir1": {
        "sehir": "Ankara",
        "plaka": "06"
    },
    "sehir2":{
        "sehir": "Istanbul",
        "plaka": "34"
    },
    "sehir3": {
        "sehir": "Malatya",
        "plaka": "44"
    }
    
}

sehir1={"sehir": "Ankara", "plaka": "06"}
sehir2={"sehir": "Istanbul","plaka": "34"}
sehir3={"sehir": "Malatya","plaka": "44"}

yenisehirler = {
    "sehir1": sehir1,
    "sehir2": sehir2,
    "sehir3": sehir3
}

print(yenisehirler["sehir1"]["sehir"])
print(sozluk["sehir1"]["sehir"])


# In[77]:


# SORU: Kullanıcıdan alınan ad,soyad,yas,cinsiyet bilgilerini Personel isimli bir sözlükte saklayın ve ad soyad bilgisini sözlükten alarak ekrana yazdırınız.
Person = {}
# person != Person

Person["name"] =  input("Adınız ")
Person["lastName"] = input("Soyadınız ")
Person["age"] = input("Yaşınız ")
Person["gender"] = input("Cinsiyetiniz")

print(Person["name"], Person["lastName"])


# In[79]:


#SORU: Bir firmanın İnsan kaynakları,Bilgi İşlem ve
#Muhasebe departmanlarının çalışan listelerini yöneticiden 
#isteyerek bir dict atınız
# ve ekrana istenilen bölümdeki çalışanları listeyiniz.


IK = list()
IT = list()
FN = list()
company = dict()

for i in range(1):
    IK.append(input("İnsan kaynakları personel ad soyad"))
    IT.append(input("Bilgi işlem personel ad soyad"))
    FN.append(input("Muhasebe personel ad soyad"))
    
company["İnsan Kaynakları"] = IK
company["Bilgi İşlem"] =  IT
company["Muhasebe"] = FN

choise = input("İnsan Kaynakları- Bilgi İşlem-Muhasebe bölüm adı giriniz:")

for i in company[choise]:
    print(i)


# In[82]:


yasakliKarakterler = ['ı', 'ş', 'ç', 'ğ', 'ö', 'ü']
uygunKarakterler = ['i','s','c', 'g', 'o', 'u']

metin = input("Lütfen metninizi giriniz :")

for i in metin:
    if i in yasakliKarakterler:
        indx = yasakliKarakterler.index(i)
        krkter = uygunKarakterler[indx]
        print(krkter)
        metin = metin.replace(i,krkter)

print(metin)


# In[ ]:


import time
sozluk = {"arastirma": "survey", "ummak": "expect", "dikkate almak": "consider"}

while True:
    print("***************************************TR-ENG Sözlük***************************************")
    secenek = input("""
            1- Arama
            2- Çıkarma
            3- Listeleme
            4- Çıkış
            Seçiniz:""")

    if secenek == "1":
        kelime = input("Aramak istediğiniz kelimeyi giriniz: ")
        if kelime in sozluk:
            print(sozluk[kelime])
        else:
            print("Sözlükte bu kelime bulunamadı! Uygulamayı geliştirmek ister misiniz ?")
            cevap = input("E/H").upper()

            if cevap == "E":
                kelimeEng = input(kelime + " kelimesinin İngilizce karşılığını yazınız: ")
                sozluk[kelime] = kelimeEng
            else:
                print("Teşekkürler")
    elif secenek == "2":
        silenecekKelime =  input("Lütfen silinecek kelimeyi yazınız :")
        if silenecekKelime in sozluk:
            del sozluk[silenecekKelime]
        else:
            print("Böyle bir değer sözlükte bulunamadı")
    elif secenek == "3":
        print(sozluk)
    elif secenek == "4":
        print("Çıkılıyor...")
        break
    else:
        print("Hatalı tuşlama")
        time.sleep(3)

