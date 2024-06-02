import sys

def main(args):
  if len(args) != 2: return print("Expected 2 args")
  x, n, m = 1, int(args[0]), int(args[1]) - 1
  #print(x, n, m)
  
  while True:
    print(x, end="")
    x = x + m - n if x + m > n else x + m
    if x == 1:
      break

if __name__ == "__main__":
  main(sys.argv[1:])
