def read_input(filename):
    with open(filename, 'r') as f:
        # Retourne une liste de lignes nettoyées (sans le \n à la fin)
        return [line.strip() for line in f.readlines()]



if __name__ == "__main__":
    data = read_input("inputs/day01.txt")
    
    print(data)