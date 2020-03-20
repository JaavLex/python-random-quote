import random

def lol():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)

  print(quotes[rnd]),
  f = open("quotes.txt", "a")
  f.write(quotes[rnd])
  f.close()

if __name__== "__main__":
    rndprint = random.randint(0, 10)
    for x in range(rndprint):
        lol()
