def draw_triangle(height):

    height = int(input("Veuillez renseigner la hauteur du triangle"))
    
    # Dessus du triangle
    for i in range(height - 1):
        # Calculez les espaces pour le côté gauche et la partie intérieure du triangle
        left_space = ' ' * (height - i - 1)
        inner_space = ' ' * (2 * i)

        # Dessine les côté du triangle
        if i == 0:
            # Le chapeau du triangle
            print(left_space + '/' + '\\' + left_space)
        else:
            # Le corps du triangle
            print(left_space + '/' + inner_space + '\\' + left_space)

    # Dessine la base du triangle
    print('/' + '_' * (2 * height - 2) + '\\')

draw_triangle(0)
