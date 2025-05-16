# -*- coding: utf-8 -*-
"""
Bu betik, verilen bir .txt dosyasında kaç adet boş satır (enter boşluğu) olduğunu sayar.
Boş satır, yalnızca '\n' karakterinden oluşan veya tamamen boş olan satırdır.
"""

def count_blank_lines(file_path):
    """
    Verilen dosyada boş satır (yalnızca boşluk veya '\n') sayısını döner.

    Args:
        file_path (str): Dosyanın tam yolu.

    Returns:
        int: Boş satırların toplam sayısı.
    """
    blank_line_count = 0  # Sayacı başlat
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Satır sadece boşluk veya boşsa sayaç artırılır
            if line.strip() == '':
                blank_line_count += 1
    return blank_line_count


if __name__ == "__main__":
    # Hedef dosya yolu
    file_path = r"C:\Users\v4hd3\Desktop\T TxT\CobyDate_T.txt"

    # Fonksiyon çağrılır ve sonuç ekrana yazdırılır
    count = count_blank_lines(file_path)
    print(f"Boş satır sayısı: {count}")