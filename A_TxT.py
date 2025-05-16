import json
import os

json_path = r"C:\Users\v4hd3\Desktop\JSON Quests\CobyDate.json"

# JSON dosyasının adı ve yeni çıkış yolu
json_filename = os.path.basename(json_path)
txt_filename = os.path.splitext(json_filename)[0] + ".txt"
output_txt_path = os.path.join(r"C:\Users\v4hd3\Desktop\Txt", txt_filename)

def find_all_texts(obj, texts):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'Text' and isinstance(v, str):
                texts.append(v)  # ░ yerine boşluk koymuyoruz
            else:
                find_all_texts(v, texts)
    elif isinstance(obj, list):
        for item in obj:
            find_all_texts(item, texts)

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

texts = []
find_all_texts(data, texts)

# Çıkış dizini yoksa oluştur
os.makedirs(os.path.dirname(output_txt_path), exist_ok=True)

with open(output_txt_path, 'w', encoding='utf-8') as f:
    for text in texts:
        f.write(text + "\n\n")  # Her metinden sonra boş satır bırakıyoruz

print(f"{len(texts)} adet metin başarıyla çıkarıldı ve '{output_txt_path}' dosyasına yazıldı.")
