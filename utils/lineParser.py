from typing import Tuple


def lineParser(input: str) -> Tuple[float]:
    coordinates = [0, 0, 0]
    # removing spaces
    input = input.replace(" ", "")
    for i in range(len(input)):
        if input[i].lower() == "x":
            if input[i - 2] == "-":
                coordinates[0] = -1 * float(input[i - 1])
            else:
                coordinates[0] = float(input[i - 1])
        elif input[i].lower() == "y":
            if input[i - 2] == "-":
                coordinates[1] = -1 * float(input[i - 1])
            else:
                coordinates[1] = float(input[i - 1])
        elif input[i] == "=":
            # ax + by = c
            if input[-1] != "0":
                if input[i + 1] == "-":
                    coordinates[2] = -1 * float(input[i + 2])
                else:
                    coordinates[2] = float(input[i + 1])
            # ax + by = 0
            elif input[i-1] == "y":
                coordinates[2] = 0
            # ax + by + c = 0
            else:
                coordinates[2] = float(input[i - 1])
    return coordinates
