transactions_aed = [23.45, 67.89, 12.34, 78.90, 11.22, 33.44, 55.66, 77.88, 99.0]

transactions_usd = []


i = 0

while i <= len(transactions_aed) - 1:
    item_usd = transactions_aed[i] * 0.27
    print("Converting value", transactions_aed[i])
    transactions_usd.append(item_usd)
    i += 1


for transaction in transactions_aed:
    item_usd = transaction * 0.27
    print("Converting value", transaction)
    transactions_usd.append(item_usd)

lst = [2, 4, 5, 6]

for number in lst:
    if number % 2 == 0:
        print(number *2)



print(transactions_usd)