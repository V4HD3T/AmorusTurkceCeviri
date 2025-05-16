import os

# Girdi dosyasının yolu
input_txt_path = r"C:\Users\v4hd3\Desktop\Txt\CobyDate.txt"

# Dosya adı ve dizin bilgisi
input_dir = os.path.dirname(input_txt_path)
input_filename = os.path.basename(input_txt_path)
base_name, _ = os.path.splitext(input_filename)

# Dosya içeriğini oku
with open(input_txt_path, 'r', encoding='utf-8') as f:
    full_text = f.read()

# Metin bloklarını boş satırlara göre ayır
blocks = full_text.split('\n\n')

# Toplam blok sayısını yazdır
total_blocks = len(blocks)
print(f"Toplam metin bloğu sayısı: {total_blocks}")

# 200 blokluk parçalar oluştur
chunk_size = 200
chunks = [blocks[i:i + chunk_size] for i in range(0, total_blocks, chunk_size)]

# Her parçayı dosyaya yaz
for idx, chunk in enumerate(chunks, start=1):
    part_text = '\n\n'.join(chunk)  # Boşlukları koru
    part_filename = f"{base_name}_Part{idx}.txt"
    part_path = os.path.join(input_dir, part_filename)
    with open(part_path, 'w', encoding='utf-8') as f:
        f.write(part_text)

print(f"{len(chunks)} adet dosya oluşturuldu: {base_name}_PartX.txt formatında.")
