import json
import os

json_path = r"C:\Users\v4hd3\Desktop\T Quests\CobyDate.json"
txt_path = r"C:\Users\v4hd3\Desktop\T TxT\CobyDate_T.txt"
output_json_path = json_path.replace(".json", "_updated.json")

# TXT dosyasından düzenlenmiş metinleri oku
with open(txt_path, 'r', encoding='utf-8') as f:
    edited_texts = [line.strip() for line in f.read().split('\n\n') if line.strip()]

# JSON'u yükle
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# JSON içinde 'Text' alanlarını sırayla değiştir
def replace_texts(obj, edited_list):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'Text' and isinstance(v, str) and edited_list:
                obj[k] = edited_list.pop(0)
            else:
                replace_texts(v, edited_list)
    elif isinstance(obj, list):
        for item in obj:
            replace_texts(item, edited_list)

texts_copy = edited_texts.copy()
replace_texts(data, texts_copy)

# Güncellenmiş JSON'u yeni dosyaya yaz
with open(output_json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"{len(edited_texts)} adet metin geri yüklendi ve güncellenmiş JSON '{output_json_path}' dosyasına kaydedildi.")
