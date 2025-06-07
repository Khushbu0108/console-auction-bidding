import art
print(art.logo)

loop = True
aution_details ={}

while loop:
    Name = (input("What's your name?: "))
    price = (input ("What's your bid?: $"))

    aution_details[Name] = price

    choice = input("Do yo want to pass any other bidder to bid on? Say \"Yes or \"No").lower()

    if choice == "no":
        highest_bid = max(aution_details.values())
        for Name, price in aution_details.items():
            if price == highest_bid:
                print(f"The winner of this aution is {Name} with the bid of ${highest_bid}")
        break
    if choice == "yes":
        print("\n" * 100)
        continue






