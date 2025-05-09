import random

# ● ┌ ─ ┐ │ └ ┘

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

num_of_dice = 0
dice = []
total = 0
n=0

num_of_dice = int(input("Enter the number of dice: "))

for die in range(num_of_dice):
    die = dice.append(random.randint(1,6))

for line in range(5):
    for die in dice:
        print (dice_art.get(die)[line], end= "")
    print()

for die in dice:
    total += die

print (f"Your dice is: {dice}")
print (f"Total is: {total}")
