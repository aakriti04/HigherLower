import random
from game_data import data
import art

def getDataVal():
  data_size= len(data)
  index=random.randint(0,data_size-1)
  return index

def returnInfo(index):
  info=f"{data[index]['name']},a {data[index]['description']}, from {data[index]['country']}"
  return info

def getFollowers(index):
  return data[index]['follower_count']

def incrementScore(oldScore):
  newScore=oldScore+1
  return newScore

def printMsgAndScore(msg,finalScore):
  print(f"{msg} : {finalScore}")

def importLogoAndClear():
  print(art.logo)


def playGame():
  a_val=getDataVal()
  b_val=getDataVal()
  endGame=False
  score=0
  while not endGame:
    while(b_val==a_val):
      b_val=getDataVal()

    print(f"Compare A: {returnInfo(a_val)}.")
    print(art.vs)
    print(f"Against B: {returnInfo(b_val)}.")

    a_foll=getFollowers(a_val)
    b_foll=getFollowers(b_val)
    if a_foll>b_foll:
      expected="A"
    else:
      expected="B"
    actual=input("Who has more followers? Type 'A' or 'B': ")
    print("userinput: ",actual)
    if actual.upper()==expected:
      a_val=b_val
      score=incrementScore(score)
      importLogoAndClear()
      printMsgAndScore(msg="You're right! Current score",finalScore=score)
    else:
      importLogoAndClear()
      printMsgAndScore(msg="Sorry, that's wrong. Final score",finalScore=score)
      endGame=True
if __name__ == '__main__':
    importLogoAndClear()
    playGame()

