import function



def DetectClicked(x, y):
    ligne = 0
    colone = 0
    cercle_pos = None

    if y <= 240:
        ligne = 1
        if x <= 240:
            colone = 1
            cercle_pos = (120, 120)
        elif x <= 480:
            colone = 2
            cercle_pos = (360, 120)
        else:
            colone = 3
            cercle_pos = (600, 120)

    elif y <= 480:
        ligne = 2
        if x <= 240:
            colone = 1
            cercle_pos = (120, 360)
        elif x <= 480:
            colone = 2
            cercle_pos = (360, 360)
        else:
            colone = 3
            cercle_pos = (600, 360)

    else:
        ligne = 3
        if x <= 240:
            colone = 1
            cercle_pos = (120, 600)
        elif x <= 480:
            colone = 2
            cercle_pos = (360, 600)
        else:
            colone = 3
            cercle_pos = (600, 600)

    if ligne and colone:
        function.Moov(ligne, colone)
        return cercle_pos

    return None
