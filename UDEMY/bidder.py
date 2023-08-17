# from replit import clear

from art import logo
print(logo)


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"Winner is {winner} with a winning bid of ${highest_bid}")

while not bidding_finished:

  name = input("What is your name? ")
  price = input("What is your bid? $")
  bids[name] = int(price)
  should_continue = input("Are there any more bidders? Type yes or no")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    continue




# goto https://pythontutor.com/render.html#mode=display

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
  
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid:
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"Winner is {winner} with a winning bid of ${highest_bid}")

# bids = {
#   "Craigo": 123,
#   "Barry": 32
# }
# find_highest_bidder(bids)