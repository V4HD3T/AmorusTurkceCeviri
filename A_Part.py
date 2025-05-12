import os

# Girdi dosyasının tam yolu – örnek olarak masaüstündeki bir dosya
input_txt_path = r"C:\Users\v4hd3\Desktop\Txt\CobyDate.txt"

# Dosya ve isim bilgileri ayrıştırılır
input_dir = os.path.dirname(input_txt_path)
input_filename = os.path.basename(input_txt_path)
base_name, _ = os.path.splitext(input_filename)

# Girdi dosyası okunur
with open(input_txt_path, 'r', encoding='utf-8') as f:
    full_text = f.read()

# Metin blokları boş satırlara göre ayrılır
blocks = full_text.split('\n\n')
total_blocks = len(blocks)
print(f"Toplam metin bloğu sayısı: {total_blocks}")

# Bloklar 200’lük gruplara ayrılır
chunk_size = 200
chunks = [blocks[i:i + chunk_size] for i in range(0, total_blocks, chunk_size)]

# Her parça ayrı bir .txt dosyasına yazılır
for idx, chunk in enumerate(chunks, start=1):
    part_text = '\n\n'.join(chunk)  # Bloklar arasındaki boşluk korunur
    part_filename = f"{base_name}_Part{idx}.txt"
    part_path = os.path.join(input_dir, part_filename)
    with open(part_path, 'w', encoding='utf-8') as f:
        f.write(part_text)

print(f"{len(chunks)} adet dosya oluşturuldu: {base_name}_PartX.txt formatında.")
