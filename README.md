
# 🇹🇷 Amorous Türkçe Dil Yaması

Bu proje, **Amorous** oyununu Türkçe oynamak isteyen kullanıcılar için hazırlanmıştır. Aşağıda hem hızlı kurulum yöntemi hem de manuel çeviri yapmak isteyen kullanıcılar için detaylı bir rehber sunulmaktadır.

---

## 🔁 Hızlı Kurulum

Eğer dosyalarla manuel olarak uğraşmak istemiyorsanız ve oyunu Steam üzerinden **varsayılan kurulum konumuna** yüklediyseniz, aşağıdaki adımları takip ederek oyunu hızlıca Türkçeleştirebilirsiniz:

1. Aşağıda verilen Quests klasörünü indirin ve çıkartın.
2. Dosya yöneticinize aşağıdaki yolu yapıştırarak oyunun dil dosyalarının olduğu konuma gidin:

```
C:\Program Files (x86)\Steam\steamapps\common\Amorous\Content-Release\Data
```

3. Buradaki mevcut `Quests` klasörünü **yedeklemeniz önerilir**.
4. İndirdiğiniz `Quests` klasörünü bu konuma yapıştırın ve dosyaların üzerine yazılmasına **izin verin**.

> ✅ Bu işlemlerden sonra oyunu başlattığınızda artık Türkçe içerik ile çalışıyor olacaktır.

---

## 🛠️ Manuel Çeviri Süreci

Kendi çevirinizi yapmak isterseniz aşağıdaki adımları takip edebilirsiniz:

### 1. Dosya Konumuna Erişim

Oyun Steam üzerinden indirildiyse çeviri dosyaları şu klasördedir:

```
C:\Program Files (x86)\Steam\steamapps\common\Amorous\Content-Release\Data\Quests
```

### 2. Dosyaları Açma

Bu klasörde `.json` uzantılı fakat **sıkıştırılmış ve şifrelenmiş** yapıda dosyalar bulunmaktadır. Bu dosyaları bir kod editörüyle doğrudan açmak sağlıklı sonuç vermez.

#### 🔓 Çözüm:

* **7-Zip** yazılımını kullanın: [https://www.7-zip.org](https://www.7-zip.org)

**Adımlar:**

1. İlgili `.json` dosyasına sağ tıklayın → 7-Zip → "Open Archive" seçeneğini tıklayın.
2. Açılan pencerede içeriği görebileceksiniz.
3. File > Edit (veya `F4` tuşu) ile düzenleyin.
4. Kaydettikten sonra güncellemeyi onaylayın.

---

## ⚠️ Önemli Not – Türkçe Karakter Desteği

Amorous oyunu, bazı Türkçe özel karakterleri (`ç, ğ, ı, ö, ş, ü`) doğrudan desteklememektedir.  
Bu nedenle **manuel çeviri sürecinde** bu karakterlerin kullanımından kaçınılması önerilir.

---

## 🧩 Çeviri Araçları

Aşağıdaki Python scriptleri çeviri sürecini hızlandırmak için geliştirilmiştir:

### 1. `A_Txt.py` – JSON'dan Metin Çıkarımı

- `.json` dosyasındaki `"Text"` alanlarını çıkarır.  
- Aynı isimde bir `.txt` dosyasına aktarır.  
- `░` gibi özel karakterleri temizler.  
- Kod içi açıklamalarla kullanımı kolaydır.

### 2. `A_Part.py` – Metni Parçalara Bölme

- `.txt` dosyasını 200 satırlık parçalara ayırır.  
- GPT, DeepL gibi çeviri motorlarına aktarmayı kolaylaştırır.  
- Parçalı çeviri sürecinde kontrolü artırır.

> ⚠️ Kodları çalıştırmadan önce dosya yollarını kendi sisteminize göre düzenlemeyi unutmayın.

---

## 🎮 Son Adım – Türkçeleştirilmiş JSON'u Oyuna Aktarma

1. Çevirdiğiniz `.txt` içeriğini orijinal `.json` dosyasına aktarın.  
2. 7-Zip ile ilgili `.json` arşivini açın.  
3. Edit (`F4`) ile içeriği düzenleyin ve kaydedin.  
4. Güncelleme onayını verin.  
5. Oyunu başlattığınızda Türkçeleştirme aktif olacaktır.

---

## 📁 Ek Klasörler Hakkında

### 🔓 JSON_Unpacked

Bu klasör, oyunun `.json` formatındaki çeviri dosyalarının **şifrelenmemiş ve sıkıştırılmamış** halini içerir.  
Çeviri sürecine doğrudan başlamak isteyen kullanıcılar bu dosyalar üzerinden çalışabilir.  
Her `.json` dosyası, `"Text"` alanları düzenlenebilir şekilde yapılandırılmıştır. Bu klasör, özellikle manuel çeviri yapmak isteyen kullanıcılar için **zaman kazandırmayı** hedefler.

> ⚠️ Düzenleme sonrası dosyaları tekrar sıkıştırmayı ve orijinal yapıya uygun şekilde oyuna entegre etmeyi unutmayınız.

---

### 🗂️ Quests Backup

Bu klasör, oyunun **orijinal `Quests` klasörünün yedeklenmiş** halini içerir.  
Eğer çeviri işlemleri sırasında `Quests` klasörü bozulur ya da çalışmaz hale gelirse, bu yedek klasör kullanılarak oyun eski haline döndürülebilir.

> ✅ Olası veri kaybını önlemek için kurulumdan önce bu yedeğin alınması şiddetle tavsiye edilir.

---

## 🚧 Geliştirme Notları

* Yakında eklenecek `.py` kodu ile `.txt` çevirisini tekrar `.json` yapısına otomatik aktaran yeni bir script yayınlanacaktır.

---

## 📬 Destek

Herhangi bir sorunuz veya öneriniz olursa benimle e-posta üzerinden iletişime geçebilirsiniz.

---

**Amorous** oyununun Türkçeleştirilmesine katkı sağlamak isterseniz, Pull Request gönderebilir, Issues kısmından bildirimde bulunabilirsiniz veya e-posta üzerinden iletişime geçebilirsiniz.
