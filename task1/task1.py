import sys

def generate_circular_path(n, m):
    circular_array = list(range(1, n + 1))
    path = []
    current_index = 0

    while True:
        path.append(circular_array[current_index])
        next_index = (current_index + m - 1) % n
        if next_index == 0:
            break
        current_index = next_index

    return ''.join(map(str, path))

if name == "__main__":
    if len(sys.argv) != 3:
        print("incorrect input, expected 2 args")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    result = generate_circular_path(n, m)
    print(result)
