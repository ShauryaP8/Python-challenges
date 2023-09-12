class GarageDoor:
    def __init__(self):
        self.state = "CLOSED"
        self.blocked = False

    def process_command(self, command):
        if self.blocked:
            if command == "BLOCK_CLEARED":
                self.blocked = False
                self.state = "OPEN" if self.state == "EMERGENCY_OPENING" else "CLOSED"
        else:
            if command == "button_clicked":
                if self.state == "CLOSED" or self.state == "OPEN":
                    self.state = "OPENING" if self.state == "CLOSED" else "CLOSING"
                elif self.state == "OPENING":
                    self.state = "STOPPED_WHILE_OPENING"
                elif self.state == "CLOSING":
                    self.state = "STOPPED_WHILE_CLOSING"
            elif command == "cycle_complete":
                if self.state == "OPENING":
                    self.state = "OPEN"
                elif self.state == "CLOSING":
                    self.state = "CLOSED"
            elif command == "block_detected":
                if self.state == "CLOSING":
                    self.state = "EMERGENCY_OPENING"
                    self.blocked = True

    def __str__(self):
        return f"Door: {self.state}"


def main():
    commands = [
        "button_clicked",
        "cycle_complete",
        "button_clicked",
        "button_clicked",
        "button_clicked",
        "button_clicked",
        "button_clicked",
        "cycle_complete",
    ]

    garage_door = GarageDoor()
    for command in commands:
        garage_door.process_command(command)
        print(garage_door)
        print(f"> {command}.")

    # Bonus Challenge
    bonus_commands = [
        "button_clicked",
        "cycle_complete",
        "button_clicked",
        "block_detected",
        "button_clicked",
        "cycle_complete",
        "button_clicked",
        "block_cleared",
        "button_clicked",
        "cycle_complete",
    ]

    garage_door = GarageDoor()
    for command in bonus_commands:
        garage_door.process_command(command)
        print(garage_door)
        print(f"> {command}.")


if __name__ == "__main__":
    main()
