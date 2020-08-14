from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# for n in range(1000):
# list of rooms visited
player = Player(world.starting_room)
visited = [0]
# order of visits from each specific room visited
    # key: room, value: a list of rooms that have been visited from 'key room'
room_order = {}
for i in range(500):
    room_order[i] = []

travel_path = []
while len(set(visited)) < 500:
    # directions = player.current_room.get_exits()
    # player.travel(directions[0])
    # if player.current_room.id not in visited:
    #     visited.append(player.current_room.id)
    #     num_visits += 1
    #     visited.[player.current_room.id] = num_visits

# rules for each new room
# first: get the rooms I can access from the room I am in.
    reachable = [player.current_room.get_room_in_direction(i).id for i in player.current_room.get_exits()]
    # Dictionary of rooms with exit directions
    room_direction = {player.current_room.get_room_in_direction(i).id: i for i in player.current_room.get_exits()}
#1 is there a room i can go to that has not been visited?
    # then go there
    been_there = list(set(reachable) & set(visited))
    not_visited = list(set(reachable) - set(been_there))
    if len(not_visited) > 0:
        next_room = random.choice(not_visited)
        direction = room_direction[next_room]
        room_order[player.current_room.id].append(next_room)
        room_order[next_room].append(player.current_room.id)
        player.travel(direction)
        travel_path.append(direction)

    
#2 when there is no new room but only one direction to go:
    # go there
    elif len(not_visited) == 0 and len(reachable) == 1:
        next_room = reachable[0]
        direction = room_direction[next_room]
        room_order[player.current_room.id].append(next_room)
        room_order[next_room].append(player.current_room.id)
        player.travel(direction)
        travel_path.append(direction)

#3 when there are no new rooms but multiple directions:
    # which room-visit is the oldest?
        #go to that one.
    else:
        next_room = room_order[player.current_room.id][0]
        direction = room_direction[next_room]
        player.travel(direction)
        travel_path.append(direction)

    visited.append(player.current_room.id)
# if len(travel_path) < 974:
#     print(f"Smaller than 974: {len(travel_path)} moves") 
#     print(travel_path)
       
# else:
#     print(n)

# print(len(travel_path))
# print(travel_path)

# Best Run-
# Shortest Path:
travel_path = ['n', 's', 's', 'w', 'e', 'n', 'w', 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'n', 'w', 'w', 's', 'n', 'w', 's', 's', 's', 'w', 'w', 'w', 's', 'w', 'n', 's', 'e', 'n', 'e', 'e', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'e', 's', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 's', 's', 's', 's', 's', 's', 's', 's', 'w', 'e', 'n', 'e', 'e', 's', 's', 'e', 'w', 's', 'w', 'e', 'n', 'n', 'n', 'w', 's', 'n', 'w', 'n', 'n', 'n', 'w', 's', 's', 's', 'n', 'n', 'w', 's', 'w', 'e', 's', 'w', 'e', 'n', 'n', 'e', 'n', 'e', 'n', 'n', 'w', 's', 'w', 's', 'w', 's', 'n', 'e', 'n', 'w', 'w', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 'w', 's', 's', 'w', 'e', 's', 's', 'n', 'w', 'w', 'e', 'e', 'n', 'n', 'w', 'e', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 's', 's', 's', 'e', 'w', 's', 'e', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 'e', 'e', 'n', 'w', 'w', 'n', 's', 'w', 'w', 'w', 's', 'w', 's', 'n', 'e', 'n', 'e', 'e', 'n', 'w', 'w', 'n', 'w', 'e', 's', 'e', 'n', 'n', 'w', 'n', 'w', 'e', 'e', 'n', 'w', 'n', 's', 'w', 'e', 'e', 'e', 'e', 'e', 'n', 'w', 'w', 'e', 'e', 'e', 's', 'n', 'n', 'w', 'w', 'w', 'w', 'e', 'n', 'w', 'n', 'n', 's', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 's', 'n', 'w', 'e', 'e', 'e', 'n', 's', 's', 'e', 'e', 'e', 'n', 'w', 'w', 'e', 'n', 'w', 'e', 's', 'e', 's', 'e', 'e', 'e', 'e', 'e', 'e', 's', 's', 'e', 'w', 's', 'e', 's', 'n', 'w', 's', 'w', 'w', 'w', 'e', 's', 'w', 'e', 's', 's', 's', 's', 'w', 's', 'w', 's', 'n', 'e', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 's', 'n', 'n', 'w', 'n', 's', 'e', 'e', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n', 'w', 'n', 'w', 'e', 'n', 'w', 'e', 'n', 'w', 'w', 's', 'n', 'e', 'e', 'n', 'n', 'e', 'e', 's', 'e', 'e', 's', 'e', 'n', 'e', 's', 's', 'n', 'n', 'w', 's', 'w', 's', 's', 's', 's', 'e', 'w', 'n', 'n', 'n', 'e', 's', 's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'e', 'w', 'n', 'w', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 's', 's', 's', 'n', 'e', 's', 's', 's', 'e', 's', 'e', 'e', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'n', 'e', 'e', 'n', 'e', 'e', 's', 's', 's', 's', 'n', 'n', 'e', 'w', 'n', 'n', 'e', 'w', 'w', 's', 's', 'n', 'n', 'w', 's', 'w', 'w', 'w', 's', 's', 's', 's', 'n', 'n', 'w', 's', 'n', 'e', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 'n', 'e', 'n', 'e', 'n', 'e', 'n', 'n', 'n', 's', 'e', 'n', 'n', 'e', 'e', 'n', 's', 'e', 'n', 's', 'e', 'w', 'w', 'w', 'n', 's', 'w', 's', 's', 'w', 's', 's', 'w', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 's', 'w', 'n', 'n', 'e', 'n', 'n', 's', 's', 'w', 'n', 'n', 's', 's', 's', 's', 's', 'e', 'e', 'n', 'e', 'n', 'e', 'n', 'e', 'e', 'e', 'e', 'w', 'n', 'e', 'w', 's', 'w', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'w', 's', 'n', 'w', 'n', 'e', 'n', 'n', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 's', 's', 'e', 'n', 'e', 'w', 's', 'w', 'w', 's', 's', 'w', 's', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'w', 'w', 'n', 'w', 's', 'n', 'w', 'w', 's', 'e', 's', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 's', 'e', 'e', 's', 'n', 'e', 'w', 'w', 'w', 's', 's', 'e', 'n', 's', 'e', 'w', 'w', 's', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'w', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 'w', 's', 'e', 'w', 'n', 'n', 'w', 's', 's', 'n', 'n', 'n', 'w', 'w', 'n', 'w', 'n', 'n', 'w', 'w', 'w', 'w', 'n', 's', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 'n', 'n', 'n', 'n', 'w', 'e', 'n', 'n', 's', 's', 's', 's', 's', 'w', 'n', 'n', 's', 's', 'w', 'w', 'w', 's', 'w', 'e', 'n', 'w', 'e', 'e', 'e', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 'e', 'e', 's', 'w', 'w', 'e', 'e', 'e', 's', 'e', 'e', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'e', 'e', 'n', 'n', 'n', 'w', 'w', 'n', 'w', 'e', 's', 'e', 'n', 's', 'e', 's', 's', 'w', 'n', 's', 'e', 's', 'e', 'n', 's', 'e', 'n', 'n', 'n', 'n', 'e', 'e', 'e', 'n', 'n', 'n', 'e', 'n', 'n', 's', 'e', 'n', 'n', 's', 'e', 'e', 'w', 's', 'n', 'w', 's', 'w', 's', 'w', 'n', 'n', 's', 's', 's', 'w', 'n', 'n', 'n', 'w', 'w', 's', 's', 's', 'w', 'w', 'w', 'n', 'w', 'n', 'n', 'w', 'e', 's', 's', 'e', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 's', 'w', 'e', 'n', 'w', 'w', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'e', 'n', 'n', 's', 'w', 'n', 's', 'e', 's', 'e', 'e', 'n', 'n', 's', 's', 'w', 's', 'e', 'w', 'n', 'n', 'n', 'n', 'e', 'n', 'w', 'w', 'e', 'e', 's', 'e', 'n', 'e', 'e', 'w', 'w', 's', 's', 's', 's', 'e', 's', 'e', 'n', 'e', 'n', 's', 'e', 'e', 'w', 'n', 's', 'w', 'w', 's', 'e', 'w', 'w', 's', 'e', 'w', 'w', 'n', 's', 'w', 'w', 's', 'e', 'e', 'w', 'w', 's', 'w', 'n', 'n', 'w', 'n', 'w', 'e', 'e', 'w', 's', 'e', 's', 's', 'e', 's', 's', 's', 'n', 'w', 's', 'w', 'e', 's', 'w', 'w', 'n', 's', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 'w', 's', 'w', 'w', 'w', 'n']



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in travel_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(travel_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")




#######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
