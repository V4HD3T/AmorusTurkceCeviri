# Gerekli modül: Bu modül dosya yolu işlemleri ve karakter kodlaması açısından yardımcı olur.
import os

# İncelenecek dosyanın yolu (kendi bilgisayarınızdaki yol)
dosya_yolu = r"C:\Users\v4hd3\Desktop\T TxT\C.txt"

# Etiketleri saymak için iki sayaç tanımlıyoruz
acilis_etiketi_sayisi = 0  # <i> etiketi
kapanis_etiketi_sayisi = 0  # </i> etiketi

# Dosyanın var olup olmadığını kontrol ediyoruz
if os.path.exists(dosya_yolu):
    # Dosyayı okuma modunda açıyoruz (encoding kısmı Türkçe karakter hataları yaşamamak için eklendi)
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        # Dosyadaki tüm içeriği tek bir metin olarak okuyoruz
        icerik = dosya.read()
        
        # Açılış etiketlerini sayıyoruz
        acilis_etiketi_sayisi = icerik.count("<i>")
        
        # Kapanış etiketlerini sayıyoruz
        kapanis_etiketi_sayisi = icerik.count("</i>")
        
        # Sonuçları ekrana yazdırıyoruz
        print(f"<i> etiketi sayısı: {acilis_etiketi_sayisi}")
        print(f"</i> etiketi sayısı: {kapanis_etiketi_sayisi}")
else:
    # Eğer dosya belirtilen konumda yoksa kullanıcıyı uyarıyoruz
    print("Belirtilen dosya bulunamadı. Lütfen dosya yolunu kontrol edin.")
