from utils import read_input

DATA = read_input("inputs/day01.txt")

position = 50

compteur_zero = 0

for line in DATA:
    sens = line[0]
    pas = int(line[1:])
    for i in range(pas):
        if sens == "R":
            position += 1
        elif sens == "L":  
            position -= 1

        position %= 100
    
        if position == 0:
            compteur_zero += 1

print("Nombre de fois où la position 0 est atteinte :", compteur_zero)