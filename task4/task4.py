import sys

def main(args):
  if len(args) != 1: return print("Expected 1 arg")
  with open(args[0], 'r') as file:
    line = file.readline()
    elems = list(map(int, line.strip().split()))
  
  elems.sort()
  median = elems[len(elems) // 2]
  print(sum(abs(el - median) for el in elems))

if __name__ == "__main__":
  main(sys.argv[1:])
