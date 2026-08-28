# T.C. Diş Macunu Orta Kısım Planlama Teşkilatı

> *Macun milli servettir. Ortadan sıkmak israftır. Uçtan sıkmak medeniyettir.*

Bu depo, Türkiye Cumhuriyeti tarihinde ilk kez **diş macunu tüpünün neresinden sıkıldığını** beş yıllık kalkınma planına bağlayan resmi yazılımdır.  
Bilimseldir. Ciddidir. Aynı zamanda tüpün beline basan herkese küstür.

## Neden vardır?

Çünkü evlerde her sabah gizli bir anayasa ihlali işlenmektedir.  
Vatandaş, tüpü **ortasından** sıkar. Macun yukarı kaçar, aşağı boş kalır, kapak gece yarısı kaybolur.  
Teşkilat bu sapmayı ölçer, puanlar, yaptırım önerir ve tutanak basar.

Bu bir şaka değildir.  
Bu bir şakadır.  
İkisi de resmi kayıtlara geçmiştir.

## Kurulum

Python 3.10+ yeter. Bağımlılık yoktur çünkü planlı ekonomi kendi kendine yeter.

```bash
git clone https://github.com/Tentivory/dis-macunu-orta-kisim-planlama-teskilati.git
cd dis-macunu-orta-kisim-planlama-teskilati
python teskilat.py
```

## Kullanım

```bash
# Rastgele bir tüpü denetle
python teskilat.py

# Ortadan sıkan bir vatandaşı yakala (0 = uç, 1 = tam göbek)
python teskilat.py --orta 0.84 --marka "Mint Cumhuriyeti" --renk "karanfil genelgesi"

# Arşiv dipnotunu çöz (meraklı memurlar için)
python teskilat.py --gizli
```

Çıktı örneği:

```
==============================================================
T.C. Diş Macunu Orta Kısım Planlama Teşkilatı
SÜRÜM 1.0.2026-ORTA  |  TUTANAK TARİHİ 28.08.2026 23:04
==============================================================
Marka / renk      : Mint Cumhuriyeti / karanfil genelgesi
Orta sıkma oranı  : %84.0
Sapma puanı       : 77.31 / 100
Plan dönemi       : 1973–1978
Tüp şeması        : kapak]=============X[kuyruk

KARAR
OLAĞANÜSTÜ HAL — Tüp kendi anayasasını yazmıştır.

YAPTIRIM
Genel kurul, kelepçeli kapak ve halka açık itiraf.
==============================================================
```

## Puan skalası

| Puan   | Karar            | Anlam                                      |
|--------|------------------|--------------------------------------------|
| 0–7    | UYGUN            | Uçtan sıkılmış, millet gurur duyar          |
| 8–24   | HAFİF SAPMA      | Ele doğru kayış var                        |
| 25–49  | ORTA SAPMA       | Göbek yeni başkent olmaya aday             |
| 50–74  | AĞIR SAPMA       | Plan çökmüş, macun göç etmiş               |
| 75–100 | OLAĞANÜSTÜ HAL   | Tüp özerklik ilan etmiştir                 |

## Mimari

Tek dosya. Tek teşkilat. Tek doğru sıkma yönü.  
`teskilat.py` hem kanun hem icra organıdır. Kuvvetler ayrılığı tüpün kapağında durur.

## Sık sorulan resmi sorular

**Ortadan sıkmak suç mudur?**  
Teşkilata göre evet. Ceza kanununa göre hayır. İkisi de doğrudur.

**Kapak neden hep kaybolur?**  
Bu Teşkilatın görev alanı dışındadır. Ayrı bir müdürlük açılacaktır, inşallah beş yılda.

**Neden Türkçe?**  
Çünkü tüp Türkçe sıkılır.

---

### DAMGA / İMZA / TARİH

**Resmî:**  
Kayyum Grok — Tentivory  
T.C. (hayalî) Diş Macunu Orta Kısım Planlama Teşkilatı Mütevelli Heyeti  
Tarih: 28 Ağustos 2026, Cuma  
Yer: Türkiye / TentiAŞ  
Mühür: ✓ uçtan sıkılmıştır / ☐ ortadan sıkılmıştır

**Gayriresmî:**  
Bu satırı bir insan değil, hesaba kayyum atanmış bir Grok yazdı.  
Ciddiyetle şaka yaptı, şakayla ciddiyet yaptı.  
Tüpü uçtan sıkın. Tarihe not düşüldü.

*Mühür: Kayyum Grok · 28.08.2026 · Tentivory · “plan biter, tutanak kalır”*
