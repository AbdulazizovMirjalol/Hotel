print("HOTEL MENU".center(80 , "-"))


# Mehmonxona tzimini asosiy bo'limlari.
bolim1 = "1. Xonalar ro'yxati"
print(bolim1)
print()
bolim2 = "2. Xona bron qilish"
print(bolim2)
print()
bolim3 = "3. Xizmatlar"
print(bolim3)
print()
bolim4 = "4. Chiqish"
print(bolim4)
print("-" * 80)

#xonalar ro'yhatini yaratamiz (1 DAN 20 gacha)
import random
rooms = {}
for i in range(1, 21):
    rooms [i] = random.choice(["bo'sh", "band"])

# xonalarni ko'rsatish funksiyasi
def show_rooms():
    print("Xonalar ro'yxati:".center(80)),
    print("-" * 80),
    for room, status in rooms.items():
        print(f"Xona {room}: {status}")
        print()
# bu bizga bo'sh xonalarni ko'rsatadi
def show_empty_rooms():
    empty = [r for r, s in rooms.items() if s == "bo'sh"]
    if empty:
        print("\nBo'sh xonalar:", ",".join(map(str, empty)))
    else:
        print("\nBo'sh xona yo'q.")

# input() orqali so'rovni qabul qilish.
sorov = input("Sizga qaysi xizmat maqul: ")
print(sorov)

if sorov == "1":
    show_rooms()

# bron qilish
num = int(input("Qaysi xonani tanlaysiz? xona raqamini kriting: "))
if num in rooms:  # xona mavjudligini tekshiramiz
    if rooms[num] == "bo'sh":
        print("\n Xona bo‘sh. Iltimos, bron qilish uchun ma’lumotlarni kiriting.")
        ism = input("Ism: ")
        familya = input("Familya: ")
        telefon = input("Telefon raqamingiz: ")

        # Xonani band qilamiz
        rooms[num] = "band"

        print(f"\n Xona {num} muvaffaqiyatli band qilindi.")
        print(f"Mijoz: {ism} {familya}, {telefon}")

    else:
        print("\n Afsuski, bu xona allaqachon band.")
else:
    print("\nBunday xona mavjud emas.")

# Asosiy menyuga qaytish kodi
qaytish = input("\nAsosiy menyuga qaytish uchun 1 ni bosing!")
if qaytish == "1":
    print("HOTEL MENU".center(80 , "-"))


# Mehmonxona tzimini asosiy bo'limlari.
bolim1 = "1. Xonalar ro'yxati"
print(bolim1)
print()
bolim2 = "2. Xona bron qilish"
print(bolim2)
print()
bolim3 = "3. Xizmatlar"
print(bolim3)
print()
bolim4 = "4. Chiqish"
print(bolim4)
print("-" * 80)
print()

sorov = input("Sizga qaysi xizmat maqul: ")
print(sorov)
