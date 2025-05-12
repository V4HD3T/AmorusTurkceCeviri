# 🇹🇷 Amorous Türkçe Dil Yaması

Bu proje, **Amorous** oyununu Türkçe oynamak isteyen kullanıcılar için hazırlanmıştır. Aşağıda hem hızlı kurulum yöntemi hem de manuel çeviri yapmak isteyen kullanıcılar için detaylı bir rehber sunulmaktadır.

---

## 🔁 Hızlı Kurulum

Eğer dosyalarla manuel olarak uğraşmak istemiyorsanız ve oyunu Steam üzerinden **varsayılan kurulum konumuna** yüklediyseniz, aşağıdaki adımları takip ederek oyunu hızlıca Türkçeleştirebilirsiniz:

1. Aşağıda verilen `Quests` klasörünü indirin ve çıkartın.
2. Dosya yöneticinize aşağıdaki yolu yapıştırarak oyunun dil dosyalarının olduğu konuma gidin:

C:\Program Files (x86)\Steam\steamapps\common\Amorous\Content-Release\Data

3. Buradaki mevcut `Quests` klasörünü **yedeklemeniz önerilir**.
4. İndirdiğiniz `Quests` klasörünü bu konuma yapıştırın ve dosyaların üzerine yazılmasına **izin verin**.

> ✅ Bu işlemlerden sonra oyunu başlattığınızda artık Türkçe içerik ile çalışıyor olacaktır.

---

## 🛠️ Manuel Çeviri Süreci

Kendi çevirinizi yapmak isterseniz aşağıdaki adımları takip edebilirsiniz:

### 1. Dosya Konumuna Erişim

Oyun Steam üzerinden indirildiyse çeviri dosyaları şu klasördedir:

C:\Program Files (x86)\Steam\steamapps\common\Amorous\Content-Release\Data\Quests

### 2. Dosyaları Açma

Bu klasörde `.json` uzantılı fakat **sıkıştırılmış ve şifrelenmiş** yapıda dosyalar bulunmaktadır. Bu dosyaları bir kod editörüyle doğrudan açmak sağlıklı sonuç vermez.

#### 🔓 Çözüm:
- **7-Zip** yazılımını kullanın: [https://www.7-zip.org](https://www.7-zip.org)

**Adımlar:**
1. İlgili `.json` dosyasına sağ tıklayın → `7-Zip` → `Open Archive` seçeneğini tıklayın.
2. Açılan pencerede içeriği görebileceksiniz.
3. `File > Edit` (veya `F4` tuşu) ile düzenleyin.
4. Kaydettikten sonra güncellemeyi onaylayın.

---

## 🧩 Çeviri Araçları

Aşağıdaki Python scriptleri çeviri sürecini hızlandırmak için geliştirilmiştir:

### 1. `A_Txt.py` – JSON'dan Metin Çıkarımı

- `.json` dosyasındaki `"Text"` alanlarını çıkarır.
- Aynı isimde bir `.txt` dosyasına aktarır.
- `░` gibi özel karakterleri temizler.
- Kod içi açıklamalarla kullanımı kolaydır.

### 2. `A_Part.py` – Metni Parçalara Bölme

- .txt dosyasını 200 satırlık parçalara ayırır.
- GPT, DeepL gibi çeviri motorlarına aktarmayı kolaylaştırır.
- Parçalı çeviri sürecinde kontrolü artırır.

> ⚠️ Kodları çalıştırmadan önce dosya yollarını kendi sisteminize göre düzenlemeyi unutmayın.

---

## 🎮 Son Adım – Türkçeleştirilmiş JSON'u Oyuna Aktarma

1. Çevirdiğiniz `.txt` içeriğini orijinal `.json` dosyasına aktarın.
2. `7-Zip` ile ilgili `.json` arşivini açın.
3. `Edit (F4)` ile içeriği düzenleyin ve kaydedin.
4. Güncelleme onayını verin.
5. Oyunu başlattığınızda Türkçeleştirme aktif olacaktır.

---

## 🚧 Geliştirme Notları

- Bu belge **v1.1** sürümünü kapsamaktadır.
- Yakında çıkacak **v1.2** ile `.txt` çevirisini tekrar `.json` yapısına otomatik aktaran yeni bir script yayınlanacaktır.

---

## 📬 Destek

Herhangi bir sorunuz veya öneriniz olursa benimle e-posta üzerinden iletişime geçebilirsiniz.

---

**Amorous** oyununun Türkçeleştirilmesine katkı sağlamak isterseniz, Pull Request gönderebilir veya Issues kısmından bildirimde bulunabilirsiniz.
