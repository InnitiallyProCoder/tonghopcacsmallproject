import random
#┌─────────┐┌─────────┐┌─────────┐
#│  ●   ●  ││  ●   ●  ││  ●   ●  │
#│         ││    ●    ││         │
#│  ●   ●  ││  ●   ●  ││  ●   ●  │
#└─────────┘└─────────┘└─────────┘

running = True
total = 0
dice_art = {1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘"),
}

playagain = ""
while running:
    number_of_dice = 0
    dices = []
    while number_of_dice not in range(1,7):
        number_of_dice = int(input("Nhap so xuc xac ban muon roll (tu 1 den 6 xuc xac): "))

    while len(dices) < number_of_dice:
        dice = random.randint(1, 6)
        dices.append(dice)

    comp = random.choice(dices)

    player = input (f"Chon tai hay xiu (tai/xiu): ").lower()

    for dice in dices:
        total += dice

    for i in range(5):
        for die in dices:
            print (dice_art[die][i], end = "")
        print()



    print (f"Xuc xac do ra la: {dices}")
    if total % 2 != 0:
        print (f"Tong la: {total}. La xiu")
        if player == "xiu":
            print(f"Ban chon: {player}")
            print(f"Ban da chien thang")
        else:
            print(f"Ban chon: {player}")
            print(f"Ban da thua")
    else:
        print(f"Tong la: {total}. La tai")
        if player == "tai":
            print(f"Ban chon: {player}")
            print(f"Ban da chien thang")
        else:
            print(f"Ban chon: {player}")
            print(f"Ban da thua")
    print()

    while playagain != "co" and playagain != "khong":
        playagain = input("Choi tiep khong? (co/khong): ").lower()

    print()
    if playagain == "khong":
        break






