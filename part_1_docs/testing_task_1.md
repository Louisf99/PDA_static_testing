### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # Wrong operator has been used should be == instead of =
      return True
    else # else needs a : after it e.g 'else:'
      return False
   

  dif highest_card(self, card1 card2):# dif should be changed to def and a "," should be between card1 and card2 
  if card1.value > card2.value: # this line should be indented thus should line 29 - 31 should then be indented by 1 tab aswell
    return card # should be return card1 
  else:
    return card2
  


def cards_total(self, cards): #  this line should be indented thus should line 36 - 38 should then be indented by 1 tab aswell
  total # Should be total = 0 
  for card in cards:
    total += card.value
    return "You have a total of" + total # total needs to be converted to string in order to use string interpolation and the return statement should not be indented but should be one less indent
  
```
