# ctiTermsTr
CTITerms, siber tehdit istihbaratı alanında kullanılmak üzere özel bir domain için fine-tuning yapılmış bir dil modeli (LLM) geliştirmeyi amaçlar. Bu proje, özellikle İngilizce-Türkçe çeviri çiftlerini kullanarak, belirli bir alanda (domain-specific) çeviri yapabilecek bir model oluşturmayı hedeflemektedir.

## Proje Amacı
CTITerms projesinin amacı, siber tehdit istihbaratı (CTI) kapsamında kullanılan terimlerin doğru ve etkili bir şekilde çevrilmesini sağlayacak bir model geliştirmektir. Proje, LoRA optimizasyonu, mBART gibi çok dilli modeller kullanılarak, bu alana özgü bir çeviri modeli üretmeyi hedeflemektedir.

[cyiTermstr-Amaç](https://drive.google.com/file/d/1KAUrDZxrNcYhY67JRJPZ2E3o10gIzMFd/view?usp=drive_link)

## Proje Kapsamı
Proje, aşağıdaki veri kaynaklarından elde edilen çevirmeyi hedefleyerek, modeli fine tune etmiştir:
- Endüstri raporları
- Güvenlik raporları
- Olay raporları
- Saldırı raporları
- Hacking forumları
- Dark web
- Haber kaynakları

## Kullanılan Yöntemler ve Teknikler
- **LoRA**: Model optimizasyonu
- **mBART**: Çok dilli modelleme
- **Tokenization**: Veri parçalama
- **Fine-Tuning**: Model ince ayarı

## Veri Seti
TMMOB Bilgisayar Mühendsiliği Odasının oluşturmuş olduğu "Siber Güvenlik Terim Karşılıkları" adlı dosya kullanıldı.
Belgeye linkten ulaşabilirsiniz: https://www.bmo.org.tr/wp-content/uploads/2023/12/Siber-Guvenlik-Terim-Karsiliklari.pdf 

## Kurulum Talimatları
1. Projeyi klonlayın:
    ```bash
    git clone https://github.com/cyph-ai/ctiTermstr.git
    cd ctiTermstr
    ```
2. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
[cyiTermstr-Çalışma](https://drive.google.com/file/d/1hxPDh0j2sXGT06sZLXis7-55GpDYD7U3/view?usp=sharing)

## Lisans
Bu proje, Apache 2.0 lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyebilirsiniz.
