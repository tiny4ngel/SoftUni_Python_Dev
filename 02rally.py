matrix_size = int(input())
racing_car_num = input()

current_car_pos = [0, 0]
tunnel_positions = [] # the list containing tunnel positions
finish_pos = () # the list that contains finish line
position_matrix = [] # the matrix that will contain the map
normal_dist = 10
tunnel_dist = 30
covered_dist = 0
end_command = "End"

for i in range(matrix_size):
    line = input()
    line_list = line.split(" ")
    for j in range(len(line_list)):
        if line_list[j] == "T":
            tunnel_positions.append((i,j))
        elif line_list[j] == "F":
            finish_pos = (i, j)
    # add to position matrix
    position_matrix.append(line_list)

while True:
    command = input()
    if command == "up":
        current_car_pos[0] -= 1
    elif command == "right":
        current_car_pos[1] += 1
    elif command == "down":
        current_car_pos[0] += 1
    elif command == "left":
        current_car_pos[1] -= 1
    elif command == "End":
        break
    # current car state
    current_car_state = position_matrix[current_car_pos[0]][current_car_pos[1]]

    if current_car_state == '.':
        covered_dist += 10
    # check if the car is at tunnel
    elif current_car_state == "T":
        tunnel_index = tunnel_positions.index(tuple(current_car_pos))
        out_index = int(not tunnel_index)
        # car moves out of the tunnel
        current_car_pos = list(tunnel_positions[out_index])
        covered_dist += 30
        for tunnel_pos in tunnel_positions:
            position_matrix[tunnel_pos[0]][tunnel_pos[1]] = "."
    # check if the car found the exit
    elif current_car_state == "F":
        covered_dist += 10
        break

if tuple(current_car_pos) == finish_pos:
    print(f"Racing car {racing_car_num} finished the stage!")
else:
    print(f"Racing car {racing_car_num} DNF.")

print(f"Distance covered {covered_dist} km.")

position_matrix[current_car_pos[0]][current_car_pos[1]] = "C"

for row in position_matrix:
    for col in row:
        print(col, end="")
    print("", end="\n")
