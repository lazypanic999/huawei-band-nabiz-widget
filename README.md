# Huawei Band canlı nabız göstergesi

Huawei Band'in nabzını Windows masaüstünün sol üstünde küçük, diğer pencerelerin üstünde duran bir pencerede gösterir. Gösterge, [Huawei HR Overlay](https://github.com/fishuvn/huawei-hr-overlay) uygulamasının yerel durum adresinden veri okur. İnternet hesabı veya ek Python paketi gerekmez.

## Gerekenler

- Windows 10/11 ve Python 3.10 veya üzeri
- Nabız verisi yayını destekleyen bir Huawei Band/Watch
- Çalışır durumda [Huawei HR Overlay](https://github.com/fishuvn/huawei-hr-overlay/releases)

## Kurulum

1. Bileklikte **Ayarlar → Nabız Verisi Yayını** özelliğini aç.
2. Huawei HR Overlay'i aç; **Scan** ile bilekliği bul, seç ve **Connect** düğmesine bas.
3. `nabiz_gostergesi.pyw` dosyasına çift tıkla.

Gösterge varsayılan olarak ekranın sol üstünde açılır. Sol fare tuşuyla sürükleyebilirsin. Kapatmak için pencerenin **X** düğmesini veya sağ tıkı kullan.

Nabız yerine `--` görünüyorsa Huawei HR Overlay'in açık ve bilekliğin bağlı olduğunu kontrol et. Gösterge her saniye `http://localhost:8764/status` adresini okur. Bağlantı kesilip son değer ekranda kalırsa bilekliği Huawei HR Overlay içinde yeniden bağla.

## Çalışma şekli

Bu proje yalnızca yerel HTTP adresinden nabız değerini alır ve Tkinter penceresinde gösterir. Kodu ve pencereyi değiştirmek için `nabiz_gostergesi.pyw` dosyasını düzenleyebilirsin. Huawei HR Overlay bu depoya dahil değildir; kendi [projesinden](https://github.com/fishuvn/huawei-hr-overlay) edinilir.
