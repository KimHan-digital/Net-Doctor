# 🩺 Net-Doctor - Ağ Sağlığı ve Loglama Aracı

Bu proje, Blue Team (Savunma) odaklı bir başlangıç aracıdır. Bilgisayarınızın temel ağ bilgilerini (IP, Gateway, Subnet) toplar, internet bağlantısını test eder ve tüm sonuçları tarih bazlı log dosyalarına kaydeder.

## 🎯 Projenin Amacı (Blue Team Perspektifi)

Savunma ekiplerinin en önemli kuralı **"Kayıt tutmayan, savunma yapmıyordur"** dur. 
Bu araç, bir ağ sorunu yaşandığında veya bir siber saldırı anında (örn: DNS zehirlenmesi, bağlantı kopmaları) olayın *kanıtını* (log) tutarak analiz yapmanıza olanak tanır.

## ⚙️ Kullanılan Teknolojiler

- **Python 3.x**
- **`netifaces`** : Ağ geçidi (Gateway) ve arayüz bilgilerine erişmek için.
- **`subprocess`** : İşletim sistemi seviyesinde ping komutunu çalıştırmak için.
- **`socket`** : Yerel hostname ve IP bilgisini almak için.
- **`os` / `datetime`** : Klasör oluşturmak ve zaman damgası (timestamp) eklemek için