import sys
import datetime
frag=True
def hesap_makinesi():
    hesap=input("Yapmak istediğiniz Hesaplamayı sayı(işlem)sayı şeklinde giriniz.(örn 4/2 veya 6/3)->")
    if "+" in hesap or "-" in hesap or "*"  in hesap or "/" in hesap:
        sonuc=eval(hesap)
        print("Sonuc= ",sonuc)
    else:
        print("GEÇERSİZ İŞLEM GİRDİNİZ!")
def kitap_kayıt():

    dosya=open("deneme.txt","w",encoding="utf-8")
    for x in range(3):
        kitap=input("kitap giriniz-> ")
        print(kitap,file=dosya)
    dosya.close()
    dosya1=open("deneme.txt","r",encoding="utf-8")
    for satir in dosya1:
        print(satir)
    dosya1.close()
    
def calar_saat():
    x=datetime.datetime.now()
    print("Şuan saat= ",x.strftime("%X"))
    k=int(x.strftime("%H"))
    m=int(x.strftime("%M"))
    kurulan_saat=input("İstenilen saati giriniz->")
    kurulan_dakika=input("istenilen dakikayı giriniz->")
    a=int(kurulan_saat)
    b=int(kurulan_dakika)

    if((a-k)>=0 or a!=0 or k!=0):
        saat=a-k
    elif((a-k)<0):
        saat=(24-k)+a
    else:
        saat=0

    if(b-m>0):
        if(a-k>=0):
            dakika=b-m     
        elif(a-k<0):
            saat=(24-k)+a
            dakika=(b-m)
    elif(b-m<0):
        saat=saat-1
        dakika=(60-m)
    print(" {} saat  {} dakika sonra alarm çalacak" .format(saat,dakika))
def palindrome():
    kelime=input("Kelime giriniz->")
    y=int(len(kelime))
    if(kelime!=" "):
        for i in range(0,int(y/2)):#kelimeyi ikiye bölüyor ve sağ ile solun eşit olup olmadığına bakıyor
            if(str(kelime[i])!=str(kelime[y-i-1])):  #örn: x="aya"=> len(x)/2=1,5 but int(len(x))=1
                durum=False                           # x[1]='y' yi tuttu sağa baktı=a sola baktı=a yani palindrom
            else:
                durum=True
        if(durum==True):
            print("Kelimeniz palindromdur")
        else:
            print("Kelimeniz palindrom değildir")
    else:
        print("Kelime Girilmemiştir")
"""

----İşlemler ve işlem kodları----
İşlem kodu:1->Üç tane favori kitabı txt dosyasına kaydetme ve listeleme
İşlem kodu:2->Hesap Makinesi
İşlem kodu:3->Çalar Saat
İşlem kodu:4->Palindrom kontrolü

"""
def main():
    print("-----İşlemler ve işlem kodları--------\nİşlem kodu:1->Üç tane favori kitabı txt dosyasına kaydetme ve listeleme\nİşlem kodu:2->Hesap Makinesi\nİşlem kodu:3->Çalar Saat\nİşlem kodu:4->Palindrom kontrolü")
    islem_kod=int(input("Yapmak istediğiniz işlemin kodunu giriniz->"))
    while(frag):
   
        if(islem_kod==1):
            kitap_kayıt()
            break
        elif(islem_kod==2):
            hesap_makinesi()
            break
        elif(islem_kod==3):
            calar_saat()
            break
        elif(islem_kod==4):
            palindrome()
            break
        else:
            print("Hatali işlem kodu girdiniz!!")
            break

main()
    
    


    
