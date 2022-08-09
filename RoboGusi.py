import random as r

hp = 0
coins = 0
damage = 0
arm = 0

def printParameters():
    print("У тебя {0} жизней, {1} урона, {2} фёшбошювов и {3} защиты.".format(hp, damage, coins, arm))

def printHp():
    print("У тебя", hp, "жизней.")

def printCoins():
    print("У тебя", coins, "фёшбошювов.")

def printDamage():
    print("У тебя", damage, "урона.")

def printArm():
    print("У тебя", arm, "зашиты.")

def meetShop():
    global hp
    global damage
    global coins
    global arm

    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print("Я не выдаю кредитов!")
        return False

    weaponLvl = r.randint(1, 6)
    weaponDmg = r.randint(1, 11) * weaponLvl
    weapons = ["Деревянный меч", "Железныйм меч", "Копьё", "Мечь с зазубренными", "Лук", "Арбалет"]
    weaponRarities = ["[испорченное]", "[Обычное]", "[не обычное]", "[редкое]", "[эпическое]", "[легендарное]"]
    weaponRarity = weaponRarities[weaponLvl - 6]
    weaponCost = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)

    oneHpCost = 4
    threeHpCost = 12

    armorLvl = r.randint(1, 6)
    armorDmg = r.randint(1, 11) * armorLvl
    armors = ["кожанный доспех", "железный доспех", "Кожанный доспех с железными ставнями", "Облегчённый доспех", "тяжёлый доспех"]
    armorRarities = ["[испорченное]", "[Обычное]", "[не обычное]", "[редкое]", "[эпическое]", "[легендарное]"]
    armorRarity = armorRarities[armorLvl - 6]
    armorCost = r.randint(3, 10) * armorLvl
    armor = r.choice(armors)

    print("На пути тебе встретился торговец!")
    printParameters()
    
    while input("Что ты будешь делать (зайти/уйти): ").lower() == "зайти":
        print("1) Одна единица здоровья -", oneHpCost, "фёшбошювов;")
        print("2) Три единицы здоровья -", threeHpCost, "фёшбошювов;")
        print("3) {0} {1} - {2} фёшбошювов - урон {3}".format(weaponRarity, weapon, weaponCost, weaponDmg))
        print("4) {0} {1} - {2} фёшбошювов - защита {3}".format(armorRarity, armor, armorCost, armorDmg))
        print("///\nУйти\n///")

        choice = input("Что хочешь приобрести: ")
        if choice == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
        elif choice == "2":
            if buy(threeHpCost):
                hp += 3
                printHp()
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        elif choice == "4":
            if buy(armorCost):
                arm = armorDmg
        else:
            print("У меня такого нет...")

def meetMonster():
    global hp
    global coins
    global damage
    global arm

    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl * 2 - 1
    monsterDmg = monsterLvl 
    monsters = ["усталый камень", "Вор", "Пьянная деревенщина", "Позорный волк", "Дитя 10"]

    monster = r.choice(monsters)

    print("Блуждая по миру, ты встретил - {0}, у него {1} уровень, {2} жизней и {3} урона.".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()

    while monsterHp > 0:
        choice = input("(атака/бег): ").lower()

        if choice == "атака":
            monsterHp -= damage
            print("Атаковав врага, ты оставил ему ", monsterHp, "здоровья.")
        elif choice == "бег":
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print("Ты убежал сверкая пятками!\nПохоже что от удивления твой противник остался далеко позади...")
                break
            else:
                print("Пытаясь убежать, ты незаметил как оступился и упал. Этого времени хватило что бы")
        else:
            continue

        if monsterHp > 0:
            monsterDmg -= arm
            hp -= monsterDmg
            print("Вражина ударила тебя, оставив", hp, "здоровья.")
            monsterDmg += arm
        if hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl
        coins += loot
        print("Ты смог одолеть его! Рядом оказалось пару коробочек в которых", loot, "фёшбошювов")
        printCoins()
    
def meetHardMonster():
    global hp
    global coins
    global damage
    global arm

    monsterLvl = r.randint(4, 7)
    monsterHp = monsterLvl * 2 - 1
    monsterDmg = monsterLvl 
    monsters = ["Голем", "Существо из пробирки", "Страж деревни", "Стая волков", "Дитя 11"]

    monster = r.choice(monsters)

    print("///\nБлуждая по миру, ты набрёк на себя - {0}, с {1} уровень, {2} жизней и {3} урона.".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()

    while monsterHp > 0:
        choice = input("(атака/бег): ").lower()

        if choice == "атака":
            monsterHp -= damage
            print("Атаковав, ты оставил ", monsterHp, "здоровья.")
        elif choice == "бег":
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print("Ты убежал сверкая пятками! Вот это да!\nПохоже что от удивления твой противник остался далеко позади!")
                break
            else:
                print("Пытаясь убежать, ты незаметил как оступился и упал. Этого времени хватило что бы")
        else:
            continue

        if monsterHp > 0:
            monsterDmg -= arm
            hp -= monsterDmg
            print("Вражина ударила тебя, оставив", hp, "здоровья.")
            monsterDmg += arm
        if hp <= 0:
            break
    else:
        loot = r.randint(1, 3) * monsterLvl
        coins += loot
        print("Ты смог одолеть его! Рядом не приметно лежал сундук с", loot, "фёшбошювов")
        printCoins()
    
def initGame(initHp, initCoins, initDamage, initArm):
    global hp
    global coins
    global damage
    global arm

    hp = initHp
    coins = initCoins
    damage = initDamage
    arm = initArm

    print("Ты решил отправится изучат и позновать мир.\nПопрощавшись со своими знакомыми ты отправился на встеру своим преключениям...\n ///\n ///")
    printParameters()

def ivent():
    iv  = r.randint (0, 3)

    if iv == 0:
        input("///\nНа поляне ты встретил странного парня, который наблюдал за звёздами и что то саписывал на бумагу. Рядом видно немного свёртков бумаги, из чего можно сделать вывод что он тут давно. Похоже он не заметил тебя. \nНе решаясь отвлечь его, ты продолжил свой путь...\n///")

    elif iv == 1:
        input("///\nПутешествуя, ты пришёл на пляж.\nНа пляжу были крабы и они танцевали.\nЗаметив тебя, они начали танцевать в твою сторону. Кажется ты им понравился!\n[Получин бонус: Крабовое просветление]")


def gameLoop():
    situation = r.randint(0, 100)

    if situation == 0:
        meetShop()
    elif situation == 10:
        meetShop()
    elif situation == 20:
        meetShop()
    elif situation == 30:
        meetShop()
    elif situation == 40:
        meetShop()
    elif situation == 50:
        meetShop()
    elif situation == 60:
        meetShop()
    elif situation == 70:
        meetShop()
    elif situation == 80:
        meetShop()
    elif situation == 90:
        meetShop()
    elif situation == 1:

        meetMonster()
    elif situation == 11:
        meetMonster()
    elif situation == 21:
        meetMonster()
    elif situation == 31:
        meetMonster()
    elif situation == 41:
        meetMonster()
    elif situation == 51:
        meetHardMonster()
    elif situation == 61:
        meetMonster()
    elif situation == 71:
        meetMonster()
    elif situation == 81:
        meetMonster()
    elif situation == 91:
        meetHardMonster()
    elif situation == 99:
        ivent()
    else:
        input("Бродим...")

initGame(5, 5, 2, 1)

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет): ").lower() == "да":
            initGame(5, 5, 2, 1)
        elif choice == "нет":
            break
        else:
            continue
