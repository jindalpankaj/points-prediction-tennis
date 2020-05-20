# import pandas as pd
# import glob
# from operator import itemgetter
#

# data = pd.read_csv("data\pbp_matches_atp_main_archive.csv")
# data.head(10)
# data.shape
# pd.options.display.max_columns = 12
# data.head(10)
# data.dtypes
# data['draw'].describe()
# data['tour'].describe()
# # dropping irrelevant columns
# data = data.drop(columns=['draw', 'tny_name', 'adf_flag', 'wh_minutes', 'tour'])
# data.dtypes
#
# # removing all rows where there was a tie-break to avoid confusion
# data['tiebreak'] = ['Yes' if x.find('/') != -1 else 'No' for x in data['pbp']]
# data[data['tiebreak'] == 'Yes'].loc[10880,'pbp']
# # data.loc[10880]
# data.loc[9834]
# name_1 = data.loc[9834,'server1']
# name_2 = data.loc[9834,'server2']
#
# # replacing all Double Faults with R, and all Aces with S
# data['pbp2'] = [x.replace("D", "R") for x in data['pbp']]
# data['pbp2'] = [x.replace("A", "S") for x in data['pbp2']]
#
# scoreline = data.loc[9834,'pbp2']

####
# player_1 = 1
# player_2 = 2
#
# # flip(player_1, player_2)
# def flip(player_num_1, player_num_2):
#     global player_1
#     global player_2
#     # temp_player = player_num_1
#     player_1 = player_num_2
#     player_2 = player_num_1
#
#
# # sequential points won by player 1 or 2? generating this info through this function
# def get_scoreline12(scoreline):
#     scoreline12 = []
#     num_tiebreak_serve_change = 0
#     for point in scoreline:
#         if point == 'S':
#             scoreline12.append(player_1)
#         elif point == 'R':
#             scoreline12.append(player_2)
#         else:
#             pass
#         if point == "/":
#             num_tiebreak_serve_change += 1
#             # new_scoreline.append('/')
#         if point == ";" or point == "/":
#             flip(player_1, player_2)
#         if point == '.':
#             if num_tiebreak_serve_change % 2 == 0:  # flip only if even
#                 flip(player_1, player_2)
#             num_tiebreak_serve_change = 0  # reset value
#     return scoreline12


#########################################################

# from score_games_sets import *
# del sgs
# importlib.reload(score_games_sets)

# update score in a normal game through this function
# def score_normal_game(current_scoreline, point_winner):
#     points_range = ["0", "15", "30", "40", "A", "W"]
#     last_point = current_scoreline[-1]
#     p1 = last_point[0:last_point.find("-")]
#     p2 = last_point[last_point.find("-") + 1:]
#     p1 = points_range.index(p1)
#     p2 = points_range.index(p2)
#     p1_new = p1
#     p2_new = p2
#     if p1 < 3 or p2 < 3 or (p1 == p2):
#         if point_winner == 1:
#             p1_new = p1 + 1
#         elif point_winner == 2:
#             p2_new = p2 + 1
#     if p1 == 3 and p2 < 3 and point_winner == 1:
#         p1_new = 5
#     if p2 == 3 and p1 < 3 and point_winner == 2:
#         p2_new = 5
#     if p1 == 4:
#         if point_winner == 1:
#             p1_new = 5
#         if point_winner == 2:
#             p1_new = 3
#     if p2 == 4:
#         if point_winner == 2:
#             p2_new = 5
#         if point_winner == 1:
#             p2_new = 3
#
#     new_point = str(points_range[p1_new]) + "-" + str(points_range[p2_new])
#     current_scoreline.append(new_point)
#     if p1_new == 5:
#         return [current_scoreline, 1]
#     elif p2_new == 5:
#         return [current_scoreline, 2]
#     else:
#         return [current_scoreline, 0]


# t = ["0-0"]
# score_normal_game(t, 1)

# def score_tiebreak_game(current_tiebreak_score, point_winner):
#     last_point = current_tiebreak_score[-1]
#     p1 = last_point[0:last_point.find("-")]
#     p2 = last_point[last_point.find("-") + 1:]
#     p1 = int(p1)
#     p2 = int(p2)
#     if point_winner == 1:
#         p1 = p1 + 1
#         if p1 > 6 and (p1 - p2 >= 2):
#             p1 = 'W'
#     elif point_winner == 2:
#         p2 = p2 + 1
#         if p2 > 6 and (p2 - p1 >= 2):
#             p2 = 'W'
#     new_point = str(p1) + "-" + str(p2)
#     current_tiebreak_score.append(new_point)
#     if p1 == 'W':
#         return [current_tiebreak_score, 1]
#     elif p2 == 'W':
#         return [current_tiebreak_score, 2]
#     else:
#         return [current_tiebreak_score, 0]


# t = ["0-0"]
# score_tiebreak_game(t,1)
# score_tiebreak_game(t,2)

##############################################
# score sets
# def score_set(current_set_score, game_winner):
#     set_winner = 0
#     last_game = current_set_score[-1]
#     p1 = last_game[0:last_game.find("-")]
#     p2 = last_game[last_game.find("-") + 1:]
#     p1 = int(p1)
#     p2 = int(p2)
#     if game_winner == 1:
#         p1 = p1 + 1
#         if (p1 == 6 and p2 < 5) or (p1 == 7):
#             set_winner = 1
#     elif game_winner == 2:
#         p2 = p2 + 1
#         if (p2 == 6 and p1 < 5) or (p2 == 7):
#             set_winner = 2
#     new_game = str(p1) + "-" + str(p2)
#     current_set_score.append(new_game)
#     return [current_set_score, set_winner]


# set_winner = 0
# t = ["0-0"]
# score_set(t,1)
# score_set(t,2)


#########################################################
# score the match

# def score_the_match(scoreline12):
#     save_set_score = []
#     game_score = ['0-0']
#     set_score = ['0-0']
#     match_score = []
#     # set_winner = 0
#     for points in scoreline12:
#         if set_score[-1] == '6-6':
#             [game_score, game_winner] = score_tiebreak_game(game_score, points)
#         else:
#             [game_score, game_winner] = score_normal_game(game_score, points)
#         # print("Game Score: ", game_score)
#         # print("Game winner = ", game_winner)
#         if game_winner != 0:
#             # print("Game Score: ", game_score)
#             # print("Game winner = ", game_winner)
#             # print("Set Score: ", set_score)
#             # print("Set winner = ", set_winner)
#             [set_score, set_winner] = score_set(set_score, game_winner)
#             save_set_score.append(set_score[-1])
#             save_set_score.append(game_score[1:])
#             # print("Set Score: ", set_score)
#             # print("Last entry of set-score: ", set_score[-1])
#             # print("Set winner = ", set_winner)
#             if set_winner != 0:
#                 set_winner = 0
#                 match_score.append(set_score[-1])
#                 # save_set_score.append(set_score[1:])
#                 # save_set_score.append(game_score)
#                 set_score = ['0-0']
#             game_score = ['0-0']
#     return [save_set_score, match_score]


# name_1, name_2
# match_score
# save_set_score



####################################################################
# process more data from Jeff Sackmann's repositories
# def readATPMatches(dirname):
#     """Reads ATP matches but does not parse time into datetime object"""
#     allFiles = glob.glob(dirname + "/atp_matches_" + "????.csv")
#     matches = pd.DataFrame()
#     container = list()
#     for filen in allFiles:
#         df = pd.read_csv(filen,
#                          index_col=None,
#                          header=0)
#         container.append(df)
#     matches = pd.concat(container)
#     return matches


####################################################################
# get h2h
# def geth2hforplayer(matches,name):
#     """get all head-to-heads of the player"""
#     matches = matches[(matches['winner_name'] == name) | (matches['loser_name'] == name)]
#     h2hs = {}
#     for index, match in matches.iterrows():
#         if (match['winner_name'] == name):
#             if (match['loser_name'] not in h2hs):
#                 h2hs[match['loser_name']] = {}
#                 h2hs[match['loser_name']]['l'] = 0
#                 h2hs[match['loser_name']]['w'] = 1
#             else:
#                 h2hs[match['loser_name']]['w'] = h2hs[match['loser_name']]['w']+1
#         elif (match['loser_name'] == name):
#             if (match['winner_name'] not in h2hs):
#                 h2hs[match['winner_name']] = {}
#                 h2hs[match['winner_name']]['w'] = 0
#                 h2hs[match['winner_name']]['l'] = 1
#             else:
#                 h2hs[match['winner_name']]['l'] = h2hs[match['winner_name']]['l']+1
#
#     #create list
#     h2hlist = []
#     for k, v in h2hs.items():
#         h2hlist.append([k, v['w'],v['l']])
#     #sort by wins and then by losses + print
#     #filter by h2hs with more than 6 wins:
#     #h2hlist = [i for i in h2hlist if i[1] > 6]
#     if (len(h2hlist) == 0):
#         return ''
#     else:
#         return sorted(h2hlist, key=itemgetter(1,2))
#         #for h2h in h2hlist:
#         #    print(name+';'+h2h[0]+';'+str(h2h[1])+';'+str(h2h[2]))
#
