prices = []

# รับราคาสินค้า 6 รายการ
print("Enter prices of 6 items:")

for i in range(6):
    price = int(input(f"Item {i + 1}: "))
    prices.append(price)

print()

# รับงบประมาณรวม
budget = int(input("Enter total budget: "))

print()

total = 0
bought_items = []

# ตรวจสอบสินค้าตามลำดับ
for i in range(6):
    price = prices[i]

    if total + price <= budget:
        print(f"Item {i + 1} = {price} -> buy")
        total += price
        bought_items.append(price)
    else:
        print(f"Item {i + 1} = {price} -> cannot buy")

    print(f"Current total = {total}")
    print()

# แสดงผลลัพธ์
print(f"Bought items: {bought_items}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget - total}")