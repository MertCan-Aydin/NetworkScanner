# 🔍 ARP Network Scanner (Python)

Bu küçük ama etkili Python aracı, yerel ağınızdaki cihazları ARP protokolü kullanarak tarar ve IP-MAC eşleşmelerini listeler. Özellikle ağ güvenliği, penetrasyon testleri ve etik hacking çalışmaları için ideal bir başlangıç aracıdır.

---

## 🚀 Özellikler

- Basit ve sade bir arayüz
- Belirli bir IP aralığını ARP ile tarar
- IP ve MAC adreslerini listeler
- Scapy kullanarak paket düzeyinde ağ analizi
- Komut satırından çalıştırılır

---

## ⚙️ Gereksinimler

- Python 3.x
- [Scapy](https://scapy.net/) kütüphanesi

Kurulum:
```bash
# Sanal ortam önerilir ama zorunlu değildir
python3 -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

# Gerekli kütüphaneyi yükleyin
pip install scapy
```

---

## 💻 Kullanım

Script'i aşağıdaki gibi çalıştırabilirsin:

```bash
python3 NetworkScanner.py -i 192.168.1.1/24
```

🔹 `-i` veya `--ipaddress` parametresiyle hedef IP aralığını belirtmelisin.  
CIDR (örneğin `/24`) biçiminde girilmesi önerilir.

---

## 📌 Örnek Çıktı

```
IP                      MAC Address
----------------------------------------
192.168.1.1             aa:bb:cc:dd:ee:ff
192.168.1.14            00:11:22:33:44:55
192.168.1.25            78:45:c4:89:6a:1e
```

---

## 🛡️ Uyarı

🔐 Bu script yalnızca **eğitim**, **test** ve **yetkili ağlar üzerinde kullanım** içindir. İzinsiz ağ taramaları yasa dışıdır ve etik dışıdır.

---

