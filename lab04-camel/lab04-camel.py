class Room:

    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []

    room = Room("Estás en la entrada, hay una sala de estar al oeste", None, None, None, 1)
    room_list.append(room)

    room = Room("Estás en la sala de estar, puedes ir a la entrada hacia el este, o ir hacia la cocina por el norte", 2, 0, None, 6)
    room_list.append(room)

    room = Room("Estás en la cocina, puedes ir a la sala de estar por el norte o al dormitorio por el sur", 1, None, 3, None)
    room_list.append(room)

    room = Room("Estás en el dormitorio, puedes ir a la cocina por el norte o al pasillo sur por el este", 2, 4, None, None)
    room_list.append(room)

    room = Room("Estás en el pasillo sur, puedes ir al pasillo norte por el norte, puedes ir al dormitorio por el oeste o al baño por el este", 6, 5, None, 3)
    room_list.append(room)

    room = Room("Estás en el baño, puedes ir al pasillo sur por el oeste", None, None, None, 4)
    room_list.append(room)

    room = Room("Estás en el pasillo norte, puedes ir al pasillo sur por el sur, o a la sala de estar por el este", None, 1, 4, None)
    room_list.append(room)

    current_room = 0

    done = False

    while not done:
        quit = input("Introduce 'Si' si quieres salir del juego: ").lower()
        if quit == "si": done = True

        print()
        print(room_list[current_room].description)

        decision = input("A donde quieres ir: ").lower()
        next_room = current_room

        if decision in ["n", "north", "norte"]:
            next_room = room_list[current_room].north
            if handleNones(next_room): current_room = next_room
        elif decision in ["e", "east", "este"]:
            next_room = room_list[current_room].east
            if handleNones(next_room): current_room = next_room
        elif decision in ["s", "south", "sur"]:
            next_room = room_list[current_room].south
            if handleNones(next_room): current_room = next_room
        elif decision in ["w", "o", "west", "oeste"]:
            next_room = room_list[current_room].west
            if handleNones(next_room): current_room = next_room
        else:
            print("Esa no es una dirección válida")

        current_room = next_room



def handleNones(next_room):
    if next_room == None:
        print("No puedes ir en esa dirección")
        return False
    else: return True

main()