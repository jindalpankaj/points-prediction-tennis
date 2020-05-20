# --------------------------------------------------------
# importing any needed libraries
import pandas as pd
import numpy as np
# import importlib
# import data_gather as dg
import pickle

# -----------------------------------------------------------
# functionalities to get points by 12 instead of SR

# sequential points won by player 1 or 2? generating this info through this function
def get_scoreline12(scoreline):
    player_1 = 1
    player_2 = 2
    # flip(player_1, player_2)
    def flip(player_num_1, player_num_2):
        nonlocal player_1
        nonlocal player_2
        # temp_player = player_num_1
        player_1 = player_num_2
        player_2 = player_num_1
    scoreline12 = []
    num_tiebreak_serve_change = 0
    for point in scoreline:
        if point == 'S':
            scoreline12.append(player_1)
        elif point == 'R':
            scoreline12.append(player_2)
        else:
            pass
        if point == "/":
            num_tiebreak_serve_change += 1
            # new_scoreline.append('/')
        if point == ";" or point == "/":
            flip(player_1, player_2)
        if point == '.':
            if num_tiebreak_serve_change % 2 == 0:  # flip only if even
                flip(player_1, player_2)
            num_tiebreak_serve_change = 0  # reset value
    return scoreline12

# --------------------------------------------------------
# get previous N points
pbp_data = pd.read_csv("data\pbp_matches_atp_main_archive.csv")
# pd.options.display.max_columns = 12

# dropping irrelevant columns
pbp_data = pbp_data.drop(columns=['draw', 'adf_flag', 'wh_minutes', 'tour'])
# replacing all Double Faults with R, and all Aces with S
pbp_data['pbp_SR'] = [x.replace("D", "R") for x in pbp_data['pbp']]
pbp_data['pbp_SR'] = [x.replace("A", "S") for x in pbp_data['pbp_SR']]
pbp_data['pbp_12'] = [get_scoreline12(x) for x in pbp_data['pbp_SR']]

pbp_data['num_points'] = pbp_data['pbp_12'].str.len() # <- better than -> [len(x) for x in data['pbp_12']]
pbp_data['date2'] = pd.to_datetime(pbp_data['date'], format='%d %b %y')
pbp_data.loc[pbp_data['winner'] == 1, 'loser_name'] = pbp_data['server2']
pbp_data.loc[pbp_data['winner'] == 2, 'loser_name'] = pbp_data['server1']
pbp_data['winner_name'] = pbp_data['server1']
pbp_data.loc[pbp_data['winner'] == 2, 'winner_name'] = pbp_data.loc[pbp_data['winner'] == 2, 'server2']

# there are some duplicate pbp_id records. keeping only unique:
pbp_data.drop_duplicates(subset=['pbp_id'], keep='first', inplace=True)

# don't really need the following 2 for the purpose of prediction
# data['my_score'] = [dg.score_the_match(x)[1] for x in data['pbp_12']]
# data['detailed_score'] = [dg.score_the_match(x)[0] for x in data['pbp_12']]

# if some processing done on data and if it needs to be saved/loaded to save time
# pickle.dump(data, open("df_data.dat", "wb"))
# data = pickle.load(open("df_data.dat", "rb"))

# num_matches = len(pbp_data)


# --------------------------------------------------------
# get player ranks, and surface of the match

    # cannot directly use data from matches csv files because there is no easy way to map
    # matches from both data and matches files.
    # read atp_players_rankings csv file and player info files to match player names with ID
    # get player 1 and player 2 ranks for all rows in data df for the date in data df

    # Update: not using the above now. Merging with matches data using multiple columns.

# player_info = pd.read_csv("https://raw.githubusercontent.com/jindalpankaj/tennis_atp/master/atp_players.csv",
#                           header=None,
#                           index_col=None,
#                           # since this csv file does not have column names
#                           names=["player_id", "firstname", "lastname", "handed",
#                                  "unparsed_dob", "country"])
#                           # not parsing now because we do not need date of birth
#                           # parse_dates=['dob_yyyymmdd'], date_parser=cached_date_parser
# player_info.info()
# player_info['fullname'] = player_info['firstname'].fillna('') + " " + player_info['lastname'].fillna('')
#
# rankings = pd.read_csv("https://raw.githubusercontent.com/jindalpankaj/tennis_atp/master/atp_rankings_10s.csv")
# rankings.info()
# rankings = rankings.rename(columns={'player': 'player_id'})
# rankings.info()
# rankings = rankings.merge(player_info[['player_id', 'fullname']], on='player_id', how='left')
# rankings['ranking_date2'] = pd.to_datetime(rankings['ranking_date'], format='%Y%m%d')
#

# merging matches from 2011-2015 to data Df
all_url = list()
for i in range(2011,2016):
    temp_url = "https://raw.githubusercontent.com/jindalpankaj/tennis_atp/master/atp_matches_" + str(i) + ".csv"
    all_url.append(temp_url)

matches = pd.DataFrame()
container = list()
for url_itr in all_url:
    df = pd.read_csv(url_itr,
                     index_col=None,
                     header=0)
    container.append(df)
matches = pd.concat(container)
del(all_url, container)

# pbp_data.info()

pbp_data = pbp_data.merge(matches[['winner_name', 'loser_name', 'score', 'winner_rank', 'loser_rank', 'surface']],
                      on=['winner_name', 'loser_name', 'score'], how='left')

# I get around 1500 null values for winner rank, loser rank, and surface.
# This number should not be so high, but for the sake of saving time, I am
# not pursuing this right now. Digging depeer into this, we can gain more
# data points.
# For now, I am not dropping anything, but this needs further rigorous checking.

# --------------------------------------------------------
# get surface of match
# maybe in v2 as it would need matching of the two csv data files and there is no readily available ID
# that can be utilized for this purpose. Hence, this task would take sort of a soft-matching involving
# matching tourney dates (+/- 7 days) with the match date of data_df, along with player names, some sort
# name matching of tourneys by sub-stringing city names from tourney, and more such things.
# Alternatively, data downloaded from scorecard.com website can also be utilized as it contains
# exact dates and player names (in a different format though)

# Update: matched using the matches csv files


# --------------------------------------------------------
# get h2h
# add this in v2
    # todo: write a function to output h2h of 2 players
    # todo: inputs will be the date till which h2h is needed, and the 2 players names

# --------------------------------------------------------
# get who is serving this point (the point that is supposed to be predicted)
# maybe add this in v2


# --------------------------------------------------------
# preparing data for ML

def generate_lagged_variables(match_index):
    shifted_df = pd.DataFrame()
    shifted_df['point_number'] = np.arange(1, pbp_data.loc[match_index, 'num_points'] + 1)
    shifted_df['point_winner'] = pbp_data.loc[match_index, 'pbp_12']
    shifted_df['pbp_id'] = pbp_data.loc[match_index, 'pbp_id']
    shifted_df['player_1'] = pbp_data.loc[match_index, 'server1']
    shifted_df['player_2'] = pbp_data.loc[match_index, 'server2']
    shifted_df['winner'] = pbp_data.loc[match_index, 'winner']
    shifted_df['surface'] = pbp_data.loc[match_index, 'surface']
    if pbp_data.loc[match_index, 'winner'] == 1:
        shifted_df['player_1_rank'] = pbp_data.loc[match_index, 'winner_rank']
        shifted_df['player_2_rank'] = pbp_data.loc[match_index, 'loser_rank']
    elif pbp_data.loc[match_index, 'winner'] == 2:
        shifted_df['player_1_rank'] = pbp_data.loc[match_index, 'loser_rank']
        shifted_df['player_2_rank'] = pbp_data.loc[match_index, 'winner_rank']
    else:
        print("Ranks not found!")
    # variable to decide how many previous points we consider for prediction
    # maybe passed as a parameter later on
    N = 20
    for x in range(N, 0, -1):
        column_name = 'pw_lag' + str(x)
        shifted_df[column_name] = shifted_df['point_winner'].shift(x)
    # to drop rows with NaN values (the first N rows for each match)
    # shifted_df.dropna(inplace=True) # not doing this for now, can do it later, if needed
    # also remember that dropna would also drop even other rows where surface, ranks
    # fields have NA values. So probably, do not do this.
    return shifted_df

# pbp_data.loc[1, 'pbp_SR']
# pbp_data.loc[1, 'pbp_12']
#
# pbp_data.loc[pbp_data['pbp_id'] == 2239568, 'pbp_SR']
# pbp_data.loc[pbp_data['pbp_id'] == 2239568, 'pbp_12']


num_matches = len(pbp_data)
final_ml_data = pd.DataFrame()

for j in range(0, num_matches): # replace 1 by num_matches
    print(f'Match number: ',j)
    # concat. ignore index renumbers the index from 0 till end, instead of restarting it from 0 every since time a new dataframe is concated.
    final_ml_data = pd.concat([final_ml_data, generate_lagged_variables(j)], ignore_index=True)

pickle.dump(final_ml_data, open("final_ml_data.dat", "wb"))

# This way might be faster, in case you have to do it again.
final_ml_list = list()
for j in range(0, num_matches): # replace 1 by num_matches
    print(f'Match number: {j}')
    df = generate_lagged_variables(j)
    final_ml_list.append(df)
    # concat. ignore index renumbers the index from 0 till end, instead of restarting it from 0 every since time a new dataframe is concated.
final_ml_list_df = pd.concat(final_ml_list, ignore_index=True)

# Check for last point in a match == winner field
match_counter = 0
for j in range(0, len(final_ml_data)):
    if j == len(final_ml_data) - 1:
        # print(j)
        print(f"Match number: {match_counter} is being checked... ")
        match_counter += 1
        if final_ml_data.loc[j, 'point_winner'] == final_ml_data.loc[j, 'winner']:
            pass#print(f"Match number {match_counter} with pbp_id {final_ml_data.loc[j, 'pbp_id']} checked. No error.")
        else:
            print(f"Error in match number: {match_counter}. "
                  f"pbp_id is {final_ml_data.loc[j, 'pbp_id']}")
    elif (final_ml_data.loc[j+1, 'point_number'] - final_ml_data.loc[j, 'point_number'] != 1):
        # print(j)
        print(f"Match number: {match_counter} is being checked... ")
        match_counter += 1
        if final_ml_data.loc[j, 'point_winner'] == final_ml_data.loc[j, 'winner']:
            pass#print(f"Match number {match_counter} with pbp_id {final_ml_data.loc[j, 'pbp_id']} checked. No error.")
        else:
            print(f"Error in match number: {match_counter}. "
                  f"pbp_id is {final_ml_data.loc[j, 'pbp_id']}")



# --------------------------------------------------------
# train ML model
# Maybe in a separate file using the final_ml_data from this table