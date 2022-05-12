#from replit import clear
#from art import logo

# HINT: You can call clear() to clear the output in the console.

#print(logo)

dict = {}
question = True


# Find highest ValueError
def find_highest(bidding_record):
    highest = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest:
            highest = bid_amount

            winner = bidder
    print(f"Winner is {winner}!")


# Collect all bidders info
while question:
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))  # Note: the input is a string, not an int!
    dict[name] = bid
    question = input("Are there any other bidders? Type yes or no: ")

    if question == "yes":
        #clear()
        continue

    else:
        find_highest(dict)







