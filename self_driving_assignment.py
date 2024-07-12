

def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabput(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

def navigate():
    start_engine()

navigate()

destination = input("Where do you want to go: ").strip().lower()


move_forward()

if destination == "library":
    turn("left")
    print(f"We have arrived at the {destination}")
elif destination == "tech park":
    turn("right")
    print(f"We have arrived at the {destination}")
elif destination in ["hospital", "mall", "airport", "university", "stadium"]:
    print("entering the roundabout")
    if destination == "hospital":
        print("taking exit number 1 from the roundabout")
        print(f"We have arrived at the {destination}")
    elif destination == "mall":
        print("taking exit number 2 from the roundabout")
        move_forward
        turn("right")
        print(f"We have arrived at the {destination}")
    else:
        print("taking exit number 3 from the roundabout")
        print(f"We have arrived at the {destination}")
elif destination in ["university", "stadium"]:   
    print("taking exit number 4 from the roundabout")
    move_forward()
    if destination == "university":
        turn("left")
        print(f"We have arrived at the {destination}")
    else:
        turn("right")
        print(f"We have arrived at the {destination}")
else:
    print("Error: Destination not recognized.")

stop_engine()



