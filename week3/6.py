p = int(input())
x = int(input())
y = int(input())
full_price = x + y / 100
full_price *= (1 + p / 100)
full_price = round(full_price, 4)
print(int(full_price), int(full_price * 100 % 100))
