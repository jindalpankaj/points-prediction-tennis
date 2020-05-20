# update score in a normal game
points_range = ["0", "15", "30", "40", "A", "W"]
def score_normal_game(current_scoreline, point_winner):
    # current_scoreline = ["0-0"]
    # point_winner = 2
    last_point = current_scoreline[-1]
    p1 = last_point[0:last_point.find("-")]
    p2 = last_point[last_point.find("-") + 1:]
    p1 = points_range.index(p1)
    p2 = points_range.index(p2)
    p1_new = p1
    p2_new = p2
    if p1 < 3 or p2 < 3 or (p1 == p2):
        if point_winner == 1:
            p1_new = p1 + 1
        elif point_winner == 2:
            p2_new = p2 + 1
    if p1 == 3 and p2 < 3 and point_winner == 1:
        p1_new = 5
    if p2 == 3 and p1 < 3 and point_winner == 2:
        p2_new = 5
    if p1 == 4:
        if point_winner == 1:
            p1_new = 5
        if point_winner == 2:
            p1_new = 3
    if p2 == 4:
        if point_winner == 2:
            p2_new = 5
        if point_winner == 1:
            p2_new = 3

    new_point = str(points_range[p1_new]) + "-" + str(points_range[p2_new])
    current_scoreline.append(new_point)
    if p1_new == 5:
        return [current_scoreline, 1]
    elif p2_new == 5:
        return [current_scoreline, 2]
    else:
        return [current_scoreline, 0]

# t = ["0-0"]
# score_normal_game(t, 1)

def score_tiebreak(current_tiebreak_score, point_winner):
    # current_tiebreak_score = t
    last_point = current_tiebreak_score[-1]
    p1 = last_point[0:last_point.find("-")]
    p2 = last_point[last_point.find("-") + 1:]
    p1 = int(p1)
    p2 = int(p2)
    if point_winner == 1:
        p1 = p1 + 1
        if p1 > 6 and (p1 - p2 >= 2):
            p1 = 'W'
    elif point_winner == 2:
        p2 = p2 + 1
        if p2 > 6 and (p2 - p1 >= 2):
            p2 = 'W'
    new_point = str(p1) + "-" + str(p2)
    current_tiebreak_score.append(new_point)
    if p1 == 'W':
        return [current_tiebreak_score, 1]
    elif p2 == 'W':
        return [current_tiebreak_score, 2]
    else:
        return [current_tiebreak_score, 0]

# t = ["0-0"]
# score_tiebreak(t,1)
# score_tiebreak(t,2)

### score sets
def score_set(current_set_score, game_winner):
    # current_set_score = t
    # global set_winner
    # if set_winner == 1 or set_winner == 2:
    #     return("The set has ended.")
    # else:
    last_game = current_set_score[-1]
    p1 = last_game[0:last_game.find("-")]
    p2 = last_game[last_game.find("-") + 1:]
    p1 = int(p1)
    p2 = int(p2)
    if game_winner == 1:
        p1 = p1 + 1
        if (p1 == 6 and p2 < 5) or (p1 == 7):
            set_winner = 1
    elif game_winner == 2:
        p2 = p2 + 1
        if (p2 == 6 and p1 < 5) or (p2 == 7):
            set_winner = 2
    new_game = str(p1) + "-" + str(p2)
    current_set_score.append(new_game)
    return [current_set_score, set_winner]

# set_winner = 0
# t = ["0-0"]
# score_set(t,1)
# score_set(t,2)