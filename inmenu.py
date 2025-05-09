menu = {"pho":74.3,
        "com suon":56.3476,
        "pizza":100.38746,
        "bun mam":34.2,
        "nuoc mia":10.3847,
        "ga chien":83.352}
        
order = []
total = 0

#tao hinh menu
print (f"{'MENU':-^20}")

for key,value in menu.items():
    print (f"{key:10}:  ${value:.2f}")

print (f"{'END':-^20}")

#dieu kien in menu
while True:
    chon = input("Order food (q to quit): ").lower()
    if chon == "q":
        break
    elif menu.get(chon) is not None: #mot cau hien nhien:
        order.append(chon)

#luu y cau lenh menu.get(chon)
for chon in order:
    total += total + menu.get(chon)
    print (chon, end = ", ")

print ()
print (f"Your total is: ${total:.2f}")