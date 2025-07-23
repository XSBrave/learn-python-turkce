# ---------- Python String (str) Metotları ----------

metin = "  Merhaba Python Dünyası!  "

# 1. lower() → Küçük harfe çevirir
print(metin.lower())  # "  merhaba python dünyası!  "

# 2. upper() → Büyük harfe çevirir
print(metin.upper())  # "  MERHABA PYTHON DÜNYASI!  "

# 3. strip() → Baş ve sondaki boşlukları siler
print(metin.strip())  # "Merhaba Python Dünyası!"

# 4. replace("a", "x") → Harf veya kelime değiştirir
print(metin.replace("a", "*"))  # "  Merh*b* Python Düny*sı!  "

# 5. split(" ") → Boşluklara göre ayırır, liste döner
print(metin.split())  # ['Merhaba', 'Python', 'Dünyası!']

# 6. startswith("  M") → Belirli karakterle başlıyor mu?
print(metin.startswith("  M"))  # True

# 7. endswith("!  ") → Belirli karakterle bitiyor mu?
print(metin.endswith("!  "))  # True

# 8. find("Python") → İçinde arar, bulursa index (sıra) döner
print(metin.find("Python"))  # 10

# 9. len(metin) → Uzunluğu verir (kaç karakter?)
print(len(metin))  # 27

# 10. capitalize() → İlk harfi büyük yapar
print(metin.strip().capitalize())  # "Merhaba python dünyası!"

# 11. title() → Her kelimenin baş harfi büyük
print(metin.strip().title())  # "Merhaba Python Dünyası!"

# 12. count("a") → Kaç tane "a" var sayar
print(metin.count("a"))  # 3

# 13. isdigit() → Sadece rakamlardan mı oluşuyor?
print("12345".isdigit())  # True
print("12a3".isdigit())   # False

# 14. isalpha() → Sadece harflerden mi oluşuyor?
print("Merhaba".isalpha())  # True
print("Merhaba1".isalpha()) # False


# | Metot          | Ne işe yarar?                           | Örnek                               |
# | -------------- | --------------------------------------- | ----------------------------------- |
# | `lower()`      | Tüm harfleri küçültür                   | `"Ali".lower()` → `"ali"`           |
# | `upper()`      | Tüm harfleri büyütür                    | `"Ali".upper()` → `"ALI"`           |
# | `strip()`      | Kenarlardaki boşlukları temizler        | `"  ali  ".strip()` → `"ali"`       |
# | `replace()`    | Metin içinde değişiklik yapar           | `"ali".replace("a", "b")`           |
# | `split()`      | Kelimelere böler                        | `"a b c".split()` → `["a","b","c"]` |
# | `find()`       | Aranan değerin başlangıç indexini döner | `"ali".find("l")` → `1`             |
# | `startswith()` | Belirli ifadeyle başlıyor mu?           | `"ali".startswith("a")` → `True`    |
# | `endswith()`   | Belirli ifadeyle bitiyor mu?            | `"ali".endswith("i")` → `True`      |
# | `count()`      | Kaç tane geçtiğini bulur                | `"ali".count("a")` → `1`            |
# | `capitalize()` | İlk harfi büyütür                       | `"ali".capitalize()` → `"Ali"`      |
# | `title()`      | Her kelimenin baş harfi büyük           | `"ali veli".title()` → `"Ali Veli"` |
# | `isdigit()`    | Sadece rakam mı?                        | `"123".isdigit()` → `True`          |
# | `isalpha()`    | Sadece harf mi?                         | `"abc".isalpha()` → `True`          |