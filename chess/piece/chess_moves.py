def move_knight_turn_one(coordinate):
    bottom= ['a', 'b', 'c', 'd', 'e' ,'f' ,'g', 'h']

    possible_moves = []
    position_start = coordinate
    position_bottom = position_start[:-1]
    position_top= int(position_start[1:])

    top_one = position_top + 1
    top_two = position_top + 2
    down_one = position_top - 1
    down_two = position_top - 2

    # Pega o indice de correto de cada letra para 2 casas ou 1 casa 
    for index , content in enumerate(bottom):
        if content == position_bottom:
            left_one = index - 1
            left_two = index - 2
            right_one = index + 1
            right_two = index + 2

    # A partir do indice localiza qual é a letra a direita ou esquerda
    for index ,content in enumerate(bottom):
        if left_one == index:
            left_one_letter = content
        if left_two == index:
            left_two_letter = content
        if right_one == index:
            right_one_letter = content
        if right_two == index:
            right_two_letter = content 
    
    # Adiciona a lista com 1 movimento a esquerda
    if left_one >= 0 and left_one <= 7:
        if down_two >= 1 and down_two <= 8:
            one_left_dow_two = left_one_letter + str(down_two)
            possible_moves.append(one_left_dow_two)
        if top_two >= 1 and top_two <= 8:
            one_left_two_top = left_one_letter + str(top_two)
            possible_moves.append(one_left_two_top)

    # Adiciona a lista com 2 movimentos a esquerda
    if left_two >= 0 and left_two <= 7:
        if down_one >= 1 and down_one <= 8:
            two_left_one_down = left_two_letter + str(down_one)
            possible_moves.append(two_left_one_down)
        if top_one >= 1 and top_one <= 8:
            two_left_one_top = left_two_letter + str(top_one)
            possible_moves.append(two_left_one_top)
    
    # Adiciona a lista com 1 movimento a direita
    if right_one >= 0 and right_one <= 7:
        if down_two >= 1 and down_two <= 8:
            one_right_down_two = right_one_letter + str(down_two)
            possible_moves.append(one_right_down_two)
        if top_two >= 1 and top_two <= 8:
            one_right_top_two = right_one_letter + str(top_two)
            possible_moves.append(one_right_top_two)

    # Adiciona a lista com 2 movimentos a direita
    if right_two >= 0 and right_two <=7:
        if down_one >= 1 and down_one <= 8:
            two_right_dow_two = right_two_letter + str(down_one)
            possible_moves.append(two_right_dow_two)
        if top_one >= 1 and top_one <= 8:
            two_right_top_two = right_two_letter + str(top_one)
            possible_moves.append(two_right_top_two)

    return(possible_moves)

def move_knight_turn_two(data):
    resposta = data

    turn_two = []
    for c in resposta:
        turn_two.append(move_knight_turn_one(c))

    return turn_two