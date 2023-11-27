




















def ligne_insert(n):
    hastag =  "#" * n ; i=0
    encadrement = "-" * (n+1)
    print(f"+{encadrement}+")
    while i <=n:
        new_hastag = hastag[:n-i] + " " + hastag[n-i:]
        print(f"|{new_hastag}|")
        i += 1
    print(f"+{encadrement}+")

ligne_insert(3)