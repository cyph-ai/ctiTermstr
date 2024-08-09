# CTITerms

CTITerms, siber tehdit istihbaratı alanında kullanılmak üzere özel bir domain için fine-tuning yapılmış bir dil modeli (LLM) geliştirmeyi amaçlar. Bu proje, özellikle İngilizce-Türkçe çeviri çiftlerini kullanarak, belirli bir alanda (domain-specific) çeviri yapabilecek bir model oluşturmayı hedeflemektedir.

## Proje Amacı
CTITerms projesinin amacı, siber tehdit istihbaratı (CTI) kapsamında kullanılan terimlerin doğru ve etkili bir şekilde çevrilmesini sağlayacak bir model geliştirmektir. Proje, LoRA optimizasyonu, T5 çeviri modeli ve mBERT gibi çok dilli modeller kullanılarak, bu alana özgü bir çeviri modeli üretmeyi hedeflemektedir.

## Proje Kapsamı
Proje, aşağıdaki veri kaynaklarından elde edilen çeviri çiftleri üzerine odaklanır:
- Endüstri raporları
- Güvenlik raporları
- Olay raporları
- Saldırı raporları
- Hacking forumları
- Dark web
- Haber kaynakları

## Kullanılan Yöntemler ve Teknikler
- **LoRA**: Model optimizasyonu
- **T5**: Çeviri
- **mBERT**: Çok dilli modelleme
- **Tokenization**: Veri parçalama
- **Beam Search**: Arama algoritması
- **Fine-Tuning**: Model ince ayarı

## Veri Seti
- CSV formatında İngilizce-Türkçe çeviri çiftleri
- Veri seti eğitim ve doğrulama olarak ikiye ayrıldı
- Tokenizer ve model yüklendi
- Ön işleme uygulandı
- Model eğitildi ve test edildi

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
3. Veri setini hazırlayın:
    - CSV formatındaki veri setini `data/` klasörüne yükleyin.
4. Modeli eğitin:
    ```bash
    python train.py
    ```

## Lisans
Bu proje, Apache 2.0 lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyebilirsiniz.
