import itertools

# Talabalarning baholarini keltiruvchi ro'yxat
talabalar = [
    {"ism": "Ali", "baholar": [85, 90, 78]},
    {"ism": "Vali", "baholar": [90, 85, 92]},
    {"ism": "Hasan", "baholar": [78, 92, 88]},
    {"ism": "Husan", "baholar": [88, 78, 90]},
    {"ism": "Tohir", "baholar": [92, 88, 85]},
]

# Baholar bo'yicha talabalarni guruhlash
guruhlar = itertools.groupby(sorted(talabalar, key=lambda x: max(x["baholar"])), key=lambda x: max(x["baholar"]))

# Har bir guruh uchun baholarning o'rtacha qiymatini hisoblash
for baholar, guruh in guruhlar:
    baholarlar = [talaba["baholar"] for talaba in guruh]
    o'rtacha_baholar = sum(baholarlar) / len(baholarlar)
    print(f"Baholar {baholar} bo'yicha talabalarning o'rtacha baholar {o'rtacha_baholar}")
