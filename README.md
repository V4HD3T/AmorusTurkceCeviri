Amorous Türkçe Dil Yaması

Bu projede, Amorous oyununu Türkçe oynamak isteyen kullanıcılar için bir çeviri çözümü sunuyorum. Aşağıda hem doğrudan kuruluma yönelik yöntem hem de çeviriyi manuel yapmak isteyenler için detaylı bir rehber yer almaktadır.
🔁 Hızlı Kurulum (Tavsiye Edilen Yöntem)

Eğer dosyalarla manuel uğraşmak istemiyorsanız ve oyunu Steam üzerinden varsayılan kurulum konumuna yüklediyseniz, aşağıdaki adımları izleyerek oyunu Türkçeleştirebilirsiniz:

    Aşağıda verdiğim Quests klasörünü indirin ve çıkartın.

    Dosya yöneticinize aşağıdaki yolu yapıştırarak oyunun dil dosyalarının olduğu konuma gidin:

    C:\Program Files (x86)\Steam\steamapps\common\Amorous\Content-Release\Data

    Buradaki mevcut Quests klasörünü yedekleyin (isteğe bağlı ama önerilir).

    Ardından indirdiğiniz Quests klasörünü bu konuma yapıştırın ve var olan dosyaların üzerine yazılmasına izin verin.

Bu işlemlerden sonra oyun Türkçe olarak çalışacaktır.
🛠️ Manuel Çeviri Süreci

Kendi çevirinizi yapmak isterseniz aşağıdaki adımları takip edebilirsiniz:
1. Dosya Konumuna Erişim

Steam'den indirilen oyunun çeviri dosyaları şurada yer alır:

C:\Program Files (x86)\Steam\steamapps\common\Amorous\Content-Release\Data\Quests

2. Dosyaları Açma

Bu klasörde .json uzantılı ancak sıkıştırılmış ve şifrelenmiş yapıda dosyalar göreceksiniz. Bu dosyaları doğrudan bir kod editörü ile açarsanız içeriği anlamlı olmayacaktır.

Çözüm:
7-Zip yazılımını kullanın. İndirme bağlantısı: https://www.7-zip.org

Adımlar:

    İlgili .json dosyasına sağ tıklayın → 7-Zip → Open Archive seçeneğini tıklayın.

    Açılan pencerede içeriği görebileceksiniz.

    File > Edit (veya F4 tuşu) ile dosyanın içeriğini düzenleyebilirsiniz. Kaydettikten sonra 7-Zip size güncellemek isteyip istemediğinizi soracaktır. Evet diyerek değişiklikleri onaylayabilirsiniz.

🧩 Çeviri Araçları

Çeviri sürecini kolaylaştırmak amacıyla birkaç Python aracı geliştirdim:
1. A_Txt.py – JSON'dan Metin Çıkarımı

Bu script, .json dosyasındaki "Text" anahtarına karşılık gelen metinleri çıkararak aynı isimde bir .txt dosyasına aktarır. ░ gibi özel karakterleri de otomatik olarak temizler. Kodun içinde tüm adımlar ayrıntılı olarak açıklanmıştır.
2. A_Part.py – Metni Parçalara Bölme

Çıkarılan .txt dosyasını çeviri motorlarına (örneğin GPT, DeepL vb.) daha kolay aktarabilmek için bu script, metni 200 blokluk parçalara ayırır. Bu sayede hem kontrol edilebilir hem de sistemli çeviri sağlanır.
📌 Notlar

    Kodları çalıştırmadan önce açıklamaları dikkatlice okuyun.

    Geliştirilen kodlar Python ile yazılmıştır ve çalıştırılmadan önce gerekli dosya yollarının kişisel sisteminize göre düzenlenmesi gerekir.

    Herhangi bir sorunuz olursa bana e-posta ile ulaşabilirsiniz.

🚧 Geliştirme Notları

Bu döküman şu an için v1.1 sürümünü kapsamaktadır. v1.2 ile birlikte çevirilen .txt dosyasının tekrar .json yapısına otomatik olarak aktarılmasını sağlayacak yeni bir script planlanmaktadır.
🎮 Son Adım – Türkçeleştirilmiş JSON'u Oyuna Aktarma

    Elde edilen çevirili .json dosyasını tekrar 7-Zip ile açın.

    Edit (F4) seçeneği ile orijinal dosya içeriğini yeni çeviriyle değiştirin.

    Kaydedip arşiv güncellemeyi onaylayın.

    Oyunu başlattığınızda artık Türkçe içerikle çalışıyor olacaktır.