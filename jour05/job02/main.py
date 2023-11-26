def draw_rectangle(width, height):
    # Dessiner la ligne supérieure
    top_bottom_line = '|' + '-' * (width - 2) + '|'
    print(top_bottom_line)
    
    # Dessiner les lignes intermédiaires
    for i in range(height - 2):
        middle_lines = '|' + ' ' * (width - 2) + '|'
        print(middle_lines)

    # Dessiner la ligne inférieure si la hauteur est supérieure à 1
    if height > 1:
        print(top_bottom_line)

# Test de la fonction avec les dimensions fournies
draw_rectangle(10, 6)
