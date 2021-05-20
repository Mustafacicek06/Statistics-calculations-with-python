# -*- coding: utf-8 -*-

# dizileri fonksiyonda kullanabilmek için 
# numpy arrayine donusturmek icin
import numpy as np 
# boxplot cizimi icin verileri dataFrame'ye dönüşüm için
import pandas as pd 
# array'lere verileri random atamak icin library
import random 
# boxplot cizimi icin library
import matplotlib.pyplot as plt 



# artimetik ortalama bulma fonksiyonu
def  arithmeticMean(array):
    total =0
    size = 0
    # finding array size
    for i in array:
        size = size +1
        
    if size<=1:
        return array
    else:
        for i in array:
            total +=i
        return total / size   
    
# medyan bulma fonksiyonu 
def findingMedian(array):
    # array sorted
    array = sorted(array)
    size = 0
    # finding array size
    for i in array:
        size = size +1
    # array boyutu tek ise ortadaki eleman median     
    if size %2 ==1:
        return array[size // 2]
    # cift ise ortadaki 2 elemanin toplami bölü 2
    else:
        i = size//2
        return (array[i-1]+array[i]) / 2 

# mod bulma fonskiyonu 
def findMode(array):
    mod = 0
    # sıklık degeri 
    frequency= 0
    counter = 0
    size = 0
    # finding array size
    for i in array:
        size = size +1
    mod = array[0]
    
    for i in range(size):
        counter = 0
        for k in range(size):
            if array[k] == array[i]:
                counter = counter +1
        # bulunan modun kac kez tekrar edecegini hesaplama         
        if counter > frequency:
            frequency = counter
            mod = array[i]
    return str(mod) + " Frequency value : " + str(frequency)    

# degisim araligi bulma fonskiyonu
def degisimAraligi(array):
    elementMax = 0
    elementMin = 0
    count =0
    # finding array size
    for i in array:
        count = count +1
           
    # dizinin max ve min elemanını bulma islemi        
    for i in range(count):
        if array[i]> elementMax:
            elementMax = array[i]
        else :
            elementMin = array[i]
            
    # bulduktan sonra dizinin max ve min eleman farki        
    outcome = elementMax - elementMin
    
    return outcome

# mean Absolute Deviation Function
def meanAbsoluteDeviation(array):
    absSum = 0
    count = 0
    # finding array size
    for i in array:
        count = count +1
        
    # abs() fonksiyonu mutlak deger icin kullanıldı    
    for i in range(count):
        absSum = absSum + abs(array[i]-arithmeticMean(array))
    return absSum / count

# Varyans hesaplama       
def variance(array):
    return standardDeviation(array)**2

# standart sapma bulma fonskiyonu 
def standardDeviation(array):
    std =0.0
    # array boyutu hesaplama 
    size = 0
    for i in array:
        size = size +1
    if size <= 1:
        return 0
    else:
        for i in array:
            std += (float(i) - arithmeticMean(array))**2
            std = (std / float(size))** 0.5
            return std
            
def coefficientofVariation(array):
    return (standardDeviation(array)/arithmeticMean(array))*100      
     
                
     
# ceyrek acikligi bulma
def ceyreklerAcikligi(dizi):
    # diziyi siralama
    dizi = sorted(dizi)
    medyan = findingMedian(dizi)
    # dizinin hangi indexinde medyani oldugu
    index = 0
    ceyrek1 = 0 # ilk ceyrek icin
    newArr =[] # diziyi kopyalamak icin baska bir dizi
    # dizi boyutu hesaplama
    count = 0
    for i in dizi:
        count = count +1 
    
    # dizinin medyanini bulma   
    for i in range(count):
        if dizi[i] == medyan:
            print(index)
        else:
            index = index +1
    # dizinin yarisini bulup ceyrek medyan bulma
    if index %2 ==1:
        ceyrek1= dizi[index // 2]
    else:
            i = index//2
            ceyrek1 = (dizi[i-1]+dizi[i]) / 2    
    
    for i in range(60,120):
        newArr= dizi
    # 2. ceyrek medyan bulma
    ceyrek2 = findingMedian(newArr)
    return abs(ceyrek2 - ceyrek1)    
            

        
# istenilen diziye eleman ekleme islemi
def addingElement(array):
    
    # dizi bos ise kontrol 
    if not array:
        return "HATA 404 : Diziye ekleme basarisiz oldu. ! "
    else:
        
        print("Eklemek istediginiz deger : ")
        addValue = int(input())
        array.append(addValue)
        count =0
        # finding array size
        for i in array:
            count = count +1 
        print(array[count-1])
        
        print("\nGirdiginiz veri basarili bir sekilde diziye eklendi.\n\n")
    
# diziden eleman silme icin     
def deleteElement(dizi):
    
    # dizi bos ise kontrol    
    if not dizi:
        print("HATA 404 : Diziye ekleme basarisiz oldu. ! ")
    else:
        print("Silmek istediginiz verinin indexini giriniz : ")
        sayiIndex = int(input())
        
        # diziden eleman cikarmak icin pop() fonksiyonu kullandim.
        dizi.pop(sayiIndex)
        print("\nGirdiginiz indexdeki sayi basarili bir sekilde silindi.\n\n")
        
# verileri yuklemek icin array'ler

bmw = []
tesla = []
mercedes = []
toyota = []

# Dizinin iclerini doldurma islemi
for i in range(120):
    bmw.append(random.randint(2500,5050))
    tesla.append(random.randint(2350,4900))
    mercedes.append(random.randint(2400,5000))
    toyota.append(random.randint(2400,5000))
        
# verileri fonskiyonlarda kullanabilmek icin numpy dizisine cevirdim       
numpybmw = np.array(bmw)
numpytesla = np.array(tesla)
numpymercedes = np.array(mercedes)
numpytoyota = np.array(toyota) 

# boxplot ile verileri cizdirmek icin dataframe kullanarak dizileri birlestiriyorum
bmwpd = pd.DataFrame(data = numpybmw)
teslapd = pd.DataFrame(data= numpytesla)
mercedespd = pd.DataFrame(data = numpymercedes)
toyotapd = pd.DataFrame(data = numpytoyota)
con = pd.concat([bmwpd,teslapd,mercedespd,toyotapd],axis=1)
con.columns = ["BMW","TESLA","MERCEDES","TOYOTA"]     

# Menu kontrol islemi 
def switch(value):
    
    while True:
        if value == 0:
            while(True):
                 print("Eklemek istediginiz dizinin indexini giriniz \nbmw icin 0\ntesla icin 1\nmercedes icin 2\ntoyota icin 3")
                 val = int(input())
                 if val ==0:
                     addingElement(bmw)
                     break
                 elif val == 1:
                     addingElement(tesla)
                     break
                 elif val == 2:
                     addingElement(mercedes)
                     break
                 elif val == 3:
                     addingElement(toyota)
                     break
                 else:
                     print("Lutfen dogru secim yapin.\n")
                     continue
                     
            
        elif value == 1:
            while(True):
                 print("Silmek istediginiz dizinin indexini giriniz \nbmw icin 0\ntesla icin 1\nmercedes icin 2\ntoyota icin 3")
                 val = int(input())
                 if val ==0:
                     deleteElement(bmw)
                     break
                 elif val == 1:
                     deleteElement(tesla)
                     break
                 elif val == 2:
                     deleteElement(mercedes)
                     break
                 elif val == 3:
                     deleteElement(toyota)
                     break
                 else:
                     print("Lutfen dogru secim yapin.\n")
                     continue
        elif value ==2 : 
            
            plt.boxplot(con,0,'gD')
            plt.show()
            break
        
        
        elif value ==3:
            # hesaplanan verileri txt dosyasina yazdirma
            dosya = open("datas.txt","w")
            with open("datas.txt","r+") as dosya:
                veri = dosya.read()
                dosya.write("Bmw Sirketinin Gunluk Satis Ortalmasi : "+ str(arithmeticMean(numpybmw)) +
            
            
                         "\nTesla Sirketinin Gunluk Satis Ortalmasi : " + str(arithmeticMean(numpytesla))+
                         "\nMercedes Sirketinin Gunluk Satis Ortalmasi :" + str(arithmeticMean(numpymercedes))+
                         "\nToyota Sirketinin Gunluk Satis Ortalmasi :" + str(arithmeticMean(numpytoyota))+
                         "\nBmw verilerinin medyani : "+ str(findingMedian(numpybmw))+
                         "\nTesla verilerinin medyani : " + str(findingMedian(numpytesla))+
                         "\nMercedes verilerinin medyani : "+ str(findingMedian(numpymercedes))+
                         "\nToyota verilerinin medyani : "+ str(findingMedian(numpybmw))+
                         "\nBmw verilerinin mod degeri : "+str(findMode(numpybmw))+
                         "\nTesla verilerinin mod degeri : "+ str(findMode(numpytesla))+
                         "\nMercedes verilerinin mod degeri : "+ str(findMode(numpymercedes))+
                         "\nToyota verilerinin mod degeri : "+ str(findMode(numpytoyota))+
                         "\nBmw verilerinin degisim araligi : " + str(degisimAraligi(numpybmw))+
                         "\nTesla verilerinin degisim araligi : " + str(degisimAraligi(numpytesla))+
                         "\nMercedes verilerinin degisim araligi : "+ str(degisimAraligi(numpymercedes))+
                         "\nToyota verilerinin degisim araligi : " + str(degisimAraligi(numpytoyota))+
                         "\nBmw verilerinin ortalama mutlak sapma degeri : " +str(meanAbsoluteDeviation(numpybmw))+
                         "\nTesla verilerinin ortalama mutlak sapma degeri : " +str(meanAbsoluteDeviation(numpytesla))+
                         "\nMercedes verilerinin ortalama mutlak sapma degeri : " +str(meanAbsoluteDeviation(numpymercedes))+
                         "\nToyota verilerinin ortalama mutlak sapma degeri : " +str(meanAbsoluteDeviation(numpytoyota))+
                         "\nBmw verilerinin varyans degeri : "+ str(variance(numpybmw))+
                         "\nTesla verilerinin varyans degeri : "+ str(variance(numpytesla))+
                         "\nMercedes verilerinin varyans degeri : "+ str(variance(numpymercedes))+
                         "\nToyota verilerinin varyans degeri : "+ str(variance(numpytoyota))+
                         "\nBmw verilerinin standart sapma degeri : "+ str(standardDeviation(numpybmw))+
                         "\nTesla verilerinin standart sapma degeri : "+ str(standardDeviation(numpytesla))+
                         "\nMercedes verilerinin standart sapma degeri : "+ str(standardDeviation(numpymercedes))+
                         "\nToyota verilerinin standart sapma degeri : "+ str(standardDeviation(numpytoyota))+
                         "\nBmw verilerinin degisim katsayisi ve ceyrekler acikligi : " + str(coefficientofVariation(numpybmw))+"  "+str(ceyreklerAcikligi(numpybmw))+
                         "\nTesla verilerinin degisim katsayisi ve ceyrekler acikligi : " + str(coefficientofVariation(numpytesla))+"  "+str(ceyreklerAcikligi(numpytesla))+
                         "\nMercedes verilerinin degisim katsayisi ve ceyrekler acikligi : " + str(coefficientofVariation(numpymercedes))+"  "+str(ceyreklerAcikligi(numpymercedes))+
                         "\nToyota verilerinin degisim katsayisi ve ceyrekler acikligi : " + str(coefficientofVariation(numpytoyota))+"  "+str(ceyreklerAcikligi(numpytoyota)))
            break
        else:
            break 
        break

# program calisinca calisacak ilk fonksiyon
def main():
    while True:
        
            print("Veri setine eleman eklemek isterseniz '0' a basiniz : "+
            "\n\nVeri setinden eleman silmek isterseniz '1' e basiniz : " +
            "\n\nVerilerin boxplotunu cizdirmek istiyorsaniz 2 ye basiniz : " +
           "\n\nVeri setinin Ortalama deger,Varyans ve bir cok degerini txt dosyasina yazdirmak icin '3' e basiniz."+
           "\n\nbir islem yapmak istemiyorsaniz 'herhangi bir tusa basabilirsiniz.")
            
            
            secim = int(input())
            switch(secim)
            if not(secim ==0 or secim == 1 or secim==2 or secim == 3 ):
                break
            

# ilk calisacak fonksiyonu cagirma    
main() 








