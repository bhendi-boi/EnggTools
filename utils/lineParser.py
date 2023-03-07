from typing import Tuple

def lineParser(input:str)->Tuple[float]:
    coordinates = [0,0,0]
    # removing spaces
    input = input.replace(" ", "")
    for i in range(len(input)):
        if input[i].lower() == "x":
            coordinates[0] = input[i-1]
        elif input[i].lower() == "y":
            coordinates[1] = input[i-1]
        elif input[i] == '=':
            coordinates[2] = input[i-1]
    return coordinates