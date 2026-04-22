# mini project - car start/stop game
# bool se track karo car started hai ya nahi
started = False

while True:  # infinite loop - quit pe break karega
    command = input("Command (start/stop/quit): ").lower()

    if command == "quit":
        break

    elif command == "start":
        if started:
            print("Already started!")
        else:
            started = True
            print("Car started ✓")

    elif command == "stop":
        if not started:
            print("Already stopped!")
        else:
            started = False
            print("Car stopped ✓")

    else:
        print("Unknown command")
