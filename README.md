# 🎮 Amorous Türkçe Yama Projesi

Bu repo, Steam üzerinden edinilebilen **Amorous** adlı görsel roman oyununun Türkçeye çevrilmesini amaçlayan bir açık kaynak projedir. Proje kapsamında, hem otomatik hem de manuel olarak metinlerin çevrilmesi ve oyunun dosyalarının güncellenmesi süreçleri belgelenmiştir.

## 📌 Hızlı Kurulum (Dosya ile)

Eğer teknik işlemlerle uğraşmak istemiyor ve Steam’den oyunu **varsayılan klasör**e kurduysanız, aşağıdaki adımları uygulayarak kolayca Türkçe yama uygulayabilirsiniz:

1. Aşağıdaki dizine gidin:

C:\Program Files (x86)\Steam\steamapps\common\Amorous\Content-Release\Data


2. Buradaki **`Quests`** klasörünü bir yedek aldıktan sonra, bu klasörü WinRAR veya 7Zip gibi bir programla açın.
3. Bu repoda sağlanacak Türkçeye çevrilmiş `Quest` dosyalarıyla değiştirin.
4. Oyunu tekrar başlattığınızda arayüz ve diyaloglar Türkçe olacaktır.

---

## 🛠 Manuel Çeviri Süreci

Daha derinlemesine düzenleme veya kendi çevirinizi yapmak isterseniz aşağıdaki adımları takip edebilirsiniz:

### 1. Dil Dosyalarının Konumu

C:\Program Files (x86)\Steam\steamapps\common\Amorous\Content-Release\Data\Quests


Bu klasördeki `.json` dosyalar oyunun senaryosunu içermektedir. Ancak bu dosyalar doğrudan metin düzenleyiciyle açıldığında **şifrelenmiş** karakterler görünecektir.

### 2. 7Zip ile JSON Dosyalarını Açmak

1. [7Zip](https://www.7-zip.org/) programını indirin ve kurun.
2. İlgili `.json` dosyasına sağ tıklayıp:
   - `7Zip` > `Open Archive` seçeneğine tıklayın.
3. Açılan pencerede dosya içeriği düzgün biçimde görüntülenir.
4. **F4 tuşu** veya `File > Edit` seçeneği ile metni düzenleyebilirsiniz.
5. Kaydettikten sonra, 7Zip güncelleme isteyecek, “Evet” diyerek değişiklikleri kaydedin.

### 3. Gelişmiş Çeviri Aracı Kullanımı

Projeye özel aşağıdaki Python scriptleri ile çeviri sürecini otomatikleştirebilirsiniz:

- `A_TxT.py`: JSON içindeki `"Text"` alanlarını `.txt` dosyasına çıkarır.
- `A_Part.py`: Uzun `.txt` dosyalarını 200 kelimelik parçalara ayırır.
- (v1.2) Yeni: Çevrilmiş `.txt` içeriğini yeniden `.json` dosyasına otomatik olarak entegre eden script (yakında paylaşılacak).

### ⚠ Notlar

- JSON dosyalarında sembolik karakterler (`░` gibi) varsa, bu semboller ek boşluk eklemek içindir. Kullanım tercihinize göre kaldırabilirsiniz.
- Script dosyalarını çalıştırmadan önce açıklamaları dikkatlice okuyunuz.

---

## 🤝 Katkıda Bulunun

Kendi çevirilerinizi, düzeltmelerinizi ya da geliştirdiğiniz scriptleri paylaşmak için lütfen bir **Pull Request (PR)** gönderin veya bizimle iletişime geçin.

---

## 📬 Destek

Herhangi bir sorunuz ya da geri bildiriminiz varsa aşağıdaki iletişim kanallarından ulaşabilirsiniz:

- E-posta: `youremail@example.com`
- GitHub Issue sayfası

---

## 📄 Lisans

Bu proje sadece kişisel kullanım ve modlama amaçlıdır. **Amorous** oyununun tüm hakları [Team Amorous](https://www.amorousgame.com/) ekibine aittir.