import random

# XONALAR MA'LUMOTI

rooms = {
    i: {"status": random.choice(["bo'sh", "band"]), "client": None}
    for i in range(1, 21)
}

clients = {}



# XONALAR RO'YXATi

def show_rooms():
    print("\n" + "XONALAR RO'YXATI".center(80, "-"))
    for r, info in rooms.items():
        print(f"Xona {r}: {info['status']}")
    print("-" * 80)

    tanlov = input("Xonani bron qilishni xohlaysizmi? (ha/yo'q): ").lower()
    if tanlov == "ha":
        book_room()
    else:
        print("Bron qilinmadi.")



# XONA BRON QILISH

def book_room():
    print("\n" + "BRON QILISH".center(80, "-"))

    # Bo'sh xonalar ro'yxati
    empty = [r for r, info in rooms.items() if info["status"] == "bo'sh"]

    if not empty:
        print("Hozircha bo'sh xonalar yo'q!")
        return

    print("Bo'sh xonalar:", ", ".join(map(str, empty)))

    try:
        tanlov = int(input("Qaysi xonani band qilasiz? "))
    except:
        print("Faqat raqam kiriting!")
        return

    if tanlov not in empty:
        print("Xato: bu xona mavjud emas yoki band!")
        return

    # Mijoz ma'lumotlari
    ism = input("Ism: ")
    familya = input("Familya: ")
    telefon = input("Telefon raqam: ")

    # Ma'lumotni saqlash
    rooms[tanlov]["status"] = "band"
    rooms[tanlov]["client"] = f"{ism} {familya}"

    clients[tanlov] = {
        "ism": ism,
        "familya": familya,
        "telefon": telefon,
        "xona": tanlov
    }

    print(f"\n{tanlov}-Xona muvaffaqiyatli band qilindi!")
    print(f"Mijoz: {ism} {familya}, tel: {telefon}")



# XIZMATLAR

def services():
    print("\n" + "XIZMATLAR".center(80, "-"))
    print("1. Internet xizmati")
    print("2. Tozalov xizmati")
    print("3. Ovqat buyurtma")
    print("4. Orqaga qaytish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        print("\n🌐 Internet xizmati yoqildi (20 000 so'm/kun).")
    elif tanlov == "2":
        print("\n🧹 Tozalov xizmati chaqirildi (10 daqiqada keladi).")
    elif tanlov == "3":
        print("\n🍴 Ovqat buyurtma qabul qilindi (15-25 daqiqa).")
    elif tanlov == "4":
        return
    else:
        print("Noto‘g‘ri tanlov!")



# ADMIN KIRISH

def admin_login():
    parol = "0000"
    kirit = input("\nAdmin parolini kiriting: ")

    if kirit == parol:
        admin_menu()
    else:
        print("Xato parol!")



# ADMIN MENYUSI

def admin_menu():
    while True:
        print("\n" + "ADMIN PANEL".center(80, "-"))
        print("1. Barcha mijozlar ro'yxati")
        print("2. Xonadagi mijozni tekshirish")
        print("3. Xonani bo'shatish")
        print("4. Chiqish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            show_clients()
        elif tanlov == "2":
            check_by_room()
        elif tanlov == "3":
            free_room()
        elif tanlov == "4":
            break
        else:
            print("Xato tanlov!")



# MIJOZLAR RO‘YXATI

def show_clients():
    print("\n" + "MIJOZLAR RO'YXATI".center(80, "-"))

    if not clients:
        print("Hozircha hech qanday mijoz yo'q!")
        return

    for xona, info in clients.items():
        print(f"Xona {xona}: {info['ism']} {info['familya']} | Tel: {info['telefon']}")

    print("-" * 80)



# XONADA MIJOZ BOR-YO'QLIGINI TEKSHIRISH

def check_by_room():
    try:
        r = int(input("Qaysi xona raqamini tekshirasiz? "))
    except:
        print("Faqat raqam kiriting!")
        return

    if r not in rooms:
        print("Bunday xona mavjud emas!")
        return

    if rooms[r]["status"] == "bo'sh":
        print("Bu xona bo‘sh.")
        return

    info = clients.get(r)
    print("\n" + "MIJOZ MA'LUMOTI".center(80, "-"))
    print(f"Ism: {info['ism']}")
    print(f"Familya: {info['familya']}")
    print(f"Telefon: {info['telefon']}")
    print(f"Xona: {r}")
    print("-" * 80)



# XONANI BO‘SHATISH

def free_room():
    try:
        r = int(input("Qaysi xonani bo'shatasiz? "))
    except:
        print("Faqat raqam kiriting!")
        return

    if r not in rooms:
        print("Bunday xona mavjud emas!")
        return

    rooms[r]["status"] = "bo'sh"
    rooms[r]["client"] = None

    if r in clients:
        del clients[r]

    print(f"Xona {r} bo'shatildi!")



# ASOSIY MENYU

def back_to_menu():
    input("\nAsosiy menuga qaytish uchun Enter bosing...")


while True:
    print("\n" + "HOTEL MENYU".center(80, "-"))
    print("1. Xonalar ro'yxati")
    print("2. Xona bron qilish")
    print("3. Xizmatlar")
    print("4. Chiqish")
    print("5. Admin panel")
    print("-" * 80)

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        show_rooms()
        back_to_menu()
    elif tanlov == "2":
        book_room()
        back_to_menu()
    elif tanlov == "3":
        services()
        back_to_menu()
    elif tanlov == "4":
        print("\nMehmonxonamizdan foydalanganingiz uchun rahmat!")
        break
    elif tanlov == "5":
        admin_login()
    else:
        print("Xato tanlov!")
