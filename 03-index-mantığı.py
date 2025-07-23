# --- 0-Bazlı İndeksleme ---

meyveler = ["elma", "armut", "kiraz", "muz"]
print(meyveler[0])   # ilk eleman → "elma"
print(meyveler[2])   # üçüncü eleman → "kiraz"

# --- Negatif İndeksleme ---

print(meyveler[-1])  # son eleman → "muz"
print(meyveler[-2])  # sondan ikinci → "kiraz"

# --- String İndeksleme ---

kelime = "Python"
print(kelime[0])     # "P"
print(kelime[3])     # "h"
print(kelime[-1])    # "n"

# --- Dilme (Slicing) ---

# meyveler listesinin 1. ve 2. elemanını al:
print(meyveler[1:3])   # ["armut", "kiraz"]

# ilk 2 karakter:
print(kelime[:2])      # "Py"

# 2. karakterden sona kadar:
print(kelime[2:])      # "thon"

# baştan sona her 2. karakter:
print(kelime[::2])     # "Pto"

# ters çevirme (sondan başa):
print(kelime[::-1])    # "nohtyP"

# --- Dikkat! ---
# Geçersiz bir indeks kullanmak:
# print(meyveler[10])  # IndexError: list index out of range

# | İfade      | Anlamı                              | Örnek          |
# | ---------- | ----------------------------------- | -------------- |
# | `x[0]`     | İlk eleman                          | `meyveler[0]`  |
# | `x[n]`     | `n+1`’inci eleman                   | `kelime[3]`    |
# | `x[-1]`    | Son eleman                          | `meyveler[-1]` |
# | `x[a:b]`   | `a` dahil, `b` hariç arası          | `kelime[1:4]`  |
# | `x[:b]`    | Baştan `b-1`’e kadar                | `kelime[:3]`   |
# | `x[a:]`    | `a`’dan sona kadar                  | `kelime[2:]`   |
# | `x[a:b:c]` | `a`–`b-1` arası, `c` adım atlayarak | `kelime[::2]`  |
# | `x[::-1]`  | Listeyi/string’i ters çevirir       | `kelime[::-1]` |

