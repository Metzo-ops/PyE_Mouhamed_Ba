from re import S


def moy(fichier):
    S = 0
    print("salam")
    for line in fichier:
        S = S + line
        print("nice")

        moy1 = S/len(fichier)
        print(moy1)