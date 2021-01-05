global giris
giris=False

def giris():
    isim=raw_input("isim Girin:")
    dosya=open("admin.txt","r")
    print dosya
    dosya2=dosya.read()
    dosya2=dosya2.split(":")
    for i in range(len(dosya2)):
        if dosya2[i]==isim:
            hak=0
            print "hos geldin",isim
            while hak<3:
                parola=raw_input("Parola Girin:")
                if dosya2[i+1]==parola:
                    print "sisteme hos geldiniz"
                    giris=True
                    break
                else:
                    hak+=1
    dosya.close()

def urunler():
    print "urun gorme:1"
    print "urun ekleme:2"
    print "urun silme:3"
    print "urun guncelleme:4"
    numara=input("numara girin:")
    if numara==1:
        urunselect()
    elif numara==2:
        uruninsert()
    elif numara==3:
        urundelete()
    elif numara==4:
        urunupdate()
    else:
        print "hatali giris"


def uruninsert():
    urunadi=raw_input("urun adi girin:")
    print "plastik=1"
    print "cam=2"
    print "temizlik=3"
    print "oyuncak=4"
    print "bakim ve benzeri=5"
    urunkategori=input("urun kategori girin:")
    print "fiyat yazarken lütfen liradan sonra nokta koyun ve 2 hane girin (örn:2.50)"
    urungelisfiyat=input("urun gelis fiyati girin:")
    urunsatis=input("urun satis fiyati girin:")
    urunfirma=raw_input("urun firma girin(mumkun oldugunca kisa ve oncekilerle ayni girin):")
    urunbarkod=raw_input("urun barkod girin:")



    
def yonlendirme(numara):
    if numara==1:
        urunler()
    elif numara==2:
        yoneticiler()

    elif numara==3:
        musteriler()

    elif numara==4:
        ayarlar()

    elif numara==5:
        firmalar()

    else:
        print "hatali giris"

    
def anayer():
    giris()
    print "urunler:1"
    print "yoneticiler:2"
    print "musteriler:3"
    print "ayarlar:4"
    print "firmalar:5"
    numara=input("numara girin:")
    yonlendirme(numara)
        


anayer()
