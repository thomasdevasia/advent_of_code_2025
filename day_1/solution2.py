# read from input.txt
def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()


# solution function
def move_dial(input_lines, start_pos):
    pos = start_pos
    print(f"Starting position: {pos}")
    count_zero = 0
    for item in input_lines:
        print("---------------------------------------")
        dir, steps = item[:1], int(item[1:])
        for _ in range(steps):
            if dir == "R":
                pos += 1
            if dir == "L":
                pos -= 1
            
            if pos > 99:
                pos = 0
            if pos < 0:
                pos = 99
            
            if pos == 0:
                count_zero += 1

        print(f"Moving {dir} by {steps} steps to position {pos}")
        # print(f"Dial wrapped around, landed on 0 {temp} times")
        print(f"Total count of times landed on 0 so far: {count_zero}")
    return count_zero


start_pos = 50
input_lines = read_input("input.txt")
# input_lines = read_input("input_test.txt")
print(input_lines)
res = move_dial(input_lines, start_pos)
print(f"Number of times dial landed on 0: {res}")
