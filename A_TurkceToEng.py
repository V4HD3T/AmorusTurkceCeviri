# Bu program, bir .txt dosyasındaki Türkçe karakterleri İngilizce Latin harflerine çevirir
# ve sonucu aynı klasörde farklı bir dosyaya kaydeder.

import os  # Dosya yolları ile çalışmak için gerekli modül

def turkce_karakterleri_donustur(metin):
    """
    Bu fonksiyon, verilen metindeki Türkçe karakterleri İngilizce karşılıklarına çevirir.
    """
    turkce_karakterler = "çğıöşüÇĞİÖŞÜ"
    latin_karsiliklari = "cgiosuCGIOSU"
    ceviri_tablosu = str.maketrans(turkce_karakterler, latin_karsiliklari)
    return metin.translate(ceviri_tablosu)

# Giriş dosyasının tam yolu (Windows için iki ters eğik çizgi \\ veya r'' ile raw string kullanılır)
giris_dosyasi = r"C:\Users\v4hd3\Desktop\T TxT\CobyDate_Part1_T.txt"

# Çıkış dosyasının tam yolu
cikis_dosyasi = r"C:\Users\v4hd3\Desktop\T TxT\CobyDate_Part1_T_Temiz.txt"

# Dosya açma işlemi: Giriş dosyasını okuma modunda açarız
with open(giris_dosyasi, "r", encoding="utf-8") as dosya:
    orijinal_metin = dosya.read()  # Dosya içeriğini okur

# Metni dönüştürme fonksiyonuna göndeririz
temiz_metin = turkce_karakterleri_donustur(orijinal_metin)

# Sonucu çıkış dosyasına yazarız (yeni bir dosya oluşur)
with open(cikis_dosyasi, "w", encoding="utf-8") as dosya:
    dosya.write(temiz_metin)

# İşlem tamamlandıktan sonra kullanıcıya bilgi verilir
print("Dönüştürme işlemi tamamlandı. Yeni dosya oluşturuldu:")
print(cikis_dosyasi)
