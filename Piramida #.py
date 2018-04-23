wysokosc_piramidy = int(input("Podaj wysokość piramidy :"))
for x in range(wysokosc_piramidy):
    print(" "*(wysokosc_piramidy-1-x)+"#"*(2*x+1))