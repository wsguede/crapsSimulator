# python craps maker
show_dice = True
# starting money
money = 200.00


dice_one_list = []
dice_two_list = []
outcome_list = []

# function to roll dice, and save outcome
# returns added value of the dice
def roll_dice():
  from random import randrange
  dice_one = randrange(6000) % 6+1
  dice_two = randrange(6000) % 6+1
  if show_dice:
    print("[%s][%s]" % (dice_one, dice_two))
  roll_value = dice_one + dice_two
  dice_one_list.append(dice_one)
  dice_two_list.append(dice_two)
  outcome_list.append(roll_value)
  return roll_value


# run
  # while money > 0 and iteration < 100
  # make bets in order of importance
    # if point is set -- bet pass
    # else bet iron cross

iteration = 0
point = 0
while money > 0 and (point > 0 or iteration < 100):
  # TODO make bets
  outcome = roll_dice()
  # point not set
  if point == 0:
    if outcome == 7 or outcome == 11:
      # odds = 1:1
      # win
      print("winner winner chicken dinner")
    elif outcome == 2 or outcome == 3 or outcome == 12:
      # lose
      print("lose - craps")
    else:
      point = outcome
  else:
    # point is set
    if outcome == 7:
      # lose
      print("seven out - new shooter!!")
      point = 0
    elif outcome == point:
      # odds
      #   pass: 1:1
      #   pass_odds
      #     4/10: 2:1
      #      5/9: 3:2
      #      6/8: 6:5
      # win
      print("point matched! WIN")
      point = 0
    else:
      # place bets (multi roll)
      #   odds:
      #     4/10: 9:5
      #      5/9: 7:5
      #      6/8: 7:6
      # field bet (per roll)
      #   odds:
      #     3/4/9/10/11: 1:1
      #      2: 2:1
      #     12: 3:1
      # check for side bets
      print(".")
  iteration += 1
else:
  print("DONE! We finished with $%.2f in %i iterations" % (money, iteration))
