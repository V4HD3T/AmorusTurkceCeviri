import json   # JSON dosyalarını işlemek için
import os     # Dosya/dizin işlemleri için

# Kaynak JSON dosyasının yolu – LÜTFEN kullanıcı adınızı güncelleyin
json_path = r"C:\Users\v4hd3\Desktop\JSON Quests\DustinDate.json"

# Çıktı dosya adı: JSON dosyasından alınır, .txt uzantısı eklenir
json_filename = os.path.basename(json_path)
txt_filename = os.path.splitext(json_filename)[0] + ".txt"

# .txt çıktısının yazılacağı dizin – Masaüstünde 'Txt' klasörü
output_txt_path = os.path.join(r"C:\Users\v4hd3\Desktop\Txt", txt_filename)

# JSON'daki tüm "Text" alanlarını rekürsif olarak arayan yardımcı fonksiyon
def find_all_texts(obj, texts):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'Text' and isinstance(v, str):
                texts.append(v.replace('░', ' '))  # Özel karakteri boşlukla değiştir
            else:
                find_all_texts(v, texts)
    elif isinstance(obj, list):
        for item in obj:
            find_all_texts(item, texts)

# JSON dosyasını oku
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Tüm metinler bu listede toplanır
texts = []
find_all_texts(data, texts)

# Çıktı klasörü yoksa oluştur
os.makedirs(os.path.dirname(output_txt_path), exist_ok=True)

# Metinleri .txt dosyasına yaz
with open(output_txt_path, 'w', encoding='utf-8') as f:
    for text in texts:
        f.write(text + "\n\n")  # Her metni boşlukla ayır

# Bilgilendirme
print(f"{len(texts)} adet metin başarıyla çıkarıldı ve '{output_txt_path}' dosyasına yazıldı.")
