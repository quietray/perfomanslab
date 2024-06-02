import sys

def main(args):
  if len(args) != 2: return print("Expected 2 args")
  with open(args[0], 'r') as file:
    lines = file.readlines()
    center = tuple(map(float, lines[0].strip().split()))
    radius = int(lines[1].strip())

  with open(args[1], 'r') as file:
    lines = file.readlines()
    points = [tuple(map(float, line.strip().split())) for line in lines]

  #print(points)
  r2 = radius**2
  for point in points:
    d2 = (center[0] - point[0])**2 + (center[1] - point[1])**2
    #print(point, r2, d2)
    if d2 > r2: print(2)
    elif d2 < r2: print(1)
    else: print(0)

if __name__ == "__main__":
  main(sys.argv[1:])
