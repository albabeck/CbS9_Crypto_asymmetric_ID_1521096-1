
from Crypto.Util.number import long_to_bytes
import gmpy2

c_hex = "ed924527ff3a43600e318248daa62a18307096f78f5ea899598eb5ce7de2adbd6565ce5cfe896dcee24521f615cedb8236ed642a1966592cac7cae40412a717594e75b58d610b9ca2ea8642c336b804357ca1f405f9b713a9f492f1a85b64e9601385fb872a1c9e487af698727359e91221c3e3acacd476ab374469daf586c11bf1a5eb09a957670be8b353c901868d86bf2fe9074361a2a54c73df56ca38d"
c = int(c_hex, 16)
e = 5

m, exact = gmpy2.iroot(c, e)

plaintext_bytes = long_to_bytes(int(m))
plaintext = plaintext_bytes.decode('utf-8')

print("Chiqqan plaintext:")
print(plaintext)

with open("RSA_cracked.txt", "w", encoding="utf-8") as f:
    f.write(plaintext)

print("\nPlaintext RSA_cracked.txt fayliga yozildi.")
