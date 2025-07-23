# Python'daki temel veri türleri örneklerle anlatılmıştır:

# ----------- TAM SAYI (int) -----------
# Ondalıklı olmayan sayılardır.
sayi1 = 10
sayi2 = -5
print("int örneği:", sayi1 + sayi2)  # Sonuç: 5

# ----------- ONDALIKLI SAYI (float) -----------
# Noktalı yazılır (virgül değil!)
sayi3 = 3.14
sayi4 = -0.5
print("float örneği:", sayi3 + sayi4)  # Sonuç: 2.64

# ----------- METİN (string - str) -----------
# Tırnak içindeki her şey bir string’dir.
isim = "Ahmet"
soyad = 'Yılmaz'
print("str örneği:", isim + " " + soyad)  # Sonuç: Ahmet Yılmaz

# ----------- DOĞRU/YANLIŞ (boolean - bool) -----------
# Sadece True (doğru) veya False (yanlış) değer alır.
dogruMu = True
yanlisMi = False
print("bool örneği:", dogruMu)  # Sonuç: True
print("Karşılaştırma örneği (5 > 3):", 5 > 3)  # Sonuç: True

# ----------- VERİ TÜRÜNÜ GÖRÜNTÜLEME (type) -----------
# Bir değişkenin hangi türde olduğunu gösterir.
print("sayi1 türü:", type(sayi1))     # <class 'int'>
print("sayi3 türü:", type(sayi3))     # <class 'float'>
print("isim türü:", type(isim))       # <class 'str'>
print("dogruMu türü:", type(dogruMu)) # <class 'bool'>


# | Tür     | Açıklama            | Örnek           |
# | ------- | ------------------- | --------------- |
# | `int`   | Tam sayı            | `10`, `-5`      |
# | `float` | Ondalıklı sayı      | `3.14`, `-0.5`  |
# | `str`   | Metin (yazı)        | `"Merhaba"`     |
# | `bool`  | Doğru/Yanlış değeri | `True`, `False` |