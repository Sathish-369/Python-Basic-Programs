

amount = int(input("Enter the amount: "))

if amount <1000:
    discount = amount*0.02
    print("Discount added", discount)
elif amount < 5000:
    discount = amount *0.4
    print("Double Discount added", discount)
else:
    discount = amount*0.10
    print("Discount O Discount", discount)

print("Net payable: ", amount-discount)