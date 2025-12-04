from utils import read_input

DATA = read_input("inputs/day02.txt")[0]

ranges = DATA.split(",")

total_sum = 0

# ----- Partie 1 -----
# for r in ranges:
#     start = int(r.split("-")[0])
#     end = int(r.split("-")[1])

#     for number in range(start, end + 1):
        
#         s_num = str(number)
        
#         longueur = len(s_num)
#         firstpart = s_num[:longueur//2]
#         secondpart = s_num[longueur//2:]

        
#         if firstpart == secondpart:
#             total_sum += number
#         else:
#             pass


# ----- Partie 2 -----
diviseur = 0

for r in ranges:
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])

    for number in range(start, end + 1):
        s_num = str(number)
        longueur = len(s_num)
        
        trouve = False 

        for taille_motif in range(1, (longueur // 2) + 1):
            
            if longueur % taille_motif != 0:
                continue

            motif = s_num[:taille_motif]
            
            nb_fois = longueur // taille_motif
            
            if motif * nb_fois == s_num:
                trouve = True
                break

        if trouve:
            total_sum += number

print("Somme totale partie 2 :", total_sum)