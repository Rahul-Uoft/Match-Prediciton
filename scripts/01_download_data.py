#### Preamble ####
# Purpose: Downloads data for T1 players and Gen G players from Riots API
# Author: Rahul Gopeesingh
# Date: 30 March 2024
# Contact: rahul.gopeesingh@mail.utoronto.ca



import os
import time
import requests
import csv
import pandas as pd

#this is the api_key used to access the riot games api. It is valid for 24 hours and can be refreshed at any time. 
#It is also free to create an account however this step must be complete in order to reproduce this project.
api_key = 'RGAPI-b1752f55-73af-4d04-b466-936ed04a914f'



#the following 10 urls are obtained from the riot games api by doing a query on the account api using the players in-game names and tags. 
faker_url = 'https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Hide%20on%20bush/KR1?api_key=' + api_key
oner_url = 'https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Oner/KR222?api_key=' + api_key
gumayusi_url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/T1%20Gumayusi/KR1?api_key="  + api_key
keria_url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Keria/%EB%A0%88%EB%82%98%ED%83%80?api_key=" + api_key
zeus_url = 'https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/T1%20%EC%A0%9C%EC%9A%B0%EC%8A%A4/0102?api_key=' + api_key


kiin_url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/kiin/KR1?api_key=" + api_key
canyon_url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/JUGKlNG/KR1?api_key=" + api_key
chovy_url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/%ED%97%88%EA%B1%B0%EB%8D%A9/0303?api_key=" + api_key
peyz_url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Peyz/KR11?api_key=" + api_key
lehends_url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Lehends/KR1?api_key=" + api_key


#the match data is given in a json file as a dictionary, in it contains the maximum level lead which is obtained by looping through all the player ids, puuids and referencing it with the correct puuid obtained earlier. Then we return the max level lead for this player.
#The same is done for get_cs_at_10 function and the did_win function below


def max_level_lead(match_data, player_puuid):
  for participant in match_data["info"]["participants"]:
    if participant["puuid"] == player_puuid:
      level_lead = participant["challenges"]["maxLevelLeadLaneOpponent"]
      return level_lead


def get_cs_at_10(match_data, player_puuid):
  for participant in match_data["info"]["participants"]:
     if participant["puuid"] == player_puuid:
        CS_at_10 = participant["challenges"]["laneMinionsFirst10Minutes"]
        return CS_at_10

     

               
def did_win(match_data, player_puuid):
  for participant in match_data["info"]["participants"]:
      if participant["puuid"] == player_puuid:
          if participant["win"]:
            return "Win"
          else:
            return "Lose"

               
#this function works by first getting a list of match ids of the player and then obtaining the match data on which the above 3 functions are called,
#then we add such data to the team's table using the append function.
#the sleep function is used as we are only able to make 100 requests from the api at a time.


def add_table_data(player_name, team_table, player_url):
    player_info = requests.get(player_url).json()
    player_puuid = player_info['puuid']
    player_games_url = (
        'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/%27' +
        player_puuid +
        '%27/ids?start=0&count=30&api_key=' +
        api_key
    )
    match_ids = requests.get(player_games_url).json()
    i = 1
    for match in match_ids:
          try:
                match_data_url = (
                    "https://asia.api.riotgames.com/lol/match/v5/matches/" +
                    match +
                    "?api_key=" +
                    api_key
                )
                match_data = requests.get(match_data_url).json()
                creep_score = get_cs_at_10(match_data, player_puuid)
                max_level = max_level_lead(match_data, player_puuid)
                outcome = did_win(match_data, player_puuid)
                team_table.append([player_name, creep_score, max_level, outcome])
                print(i)
                i += 1
          except Exception as e:
            print(f"Error processing match {match}: {e}")



#make two tables and add the player games to these tables.

     
t1_table = [["Player Name", "CS at 10", "Max Level Lead", "Outcome"]]
add_table_data("Zeus", t1_table, zeus_url)
time.sleep(120)
add_table_data("Oner", t1_table, oner_url)
time.sleep(120)
add_table_data("Faker", t1_table,faker_url)    
time.sleep(120)
add_table_data("Gumayusi", t1_table, gumayusi_url)     
time.sleep(120)
add_table_data("Keria", t1_table, keria_url)
print (t1_table)

geng_table = [["Player Name", "CS at 10", "Max Level Lead", "Outcome"]]
time.sleep(120)
add_table_data("Kiin", geng_table, kiin_url)
time.sleep(120)
add_table_data("Canyon", geng_table, canyon_url)
time.sleep(120)
add_table_data("Chovy", geng_table, chovy_url)
time.sleep(120)
add_table_data("Peyz", geng_table, peyz_url)
time.sleep(120)
add_table_data("Lehends", geng_table, lehends_url)
print (geng_table)

#save the two tables as the csv files
t1_df = pd.DataFrame(t1_table[1:], columns = t1_table[0])
t1csvfilepath = "/Users/rahulgopeesingh/Documents/Match Prediction/data/raw_data/t1rawdata.csv"
geng_df = pd.DataFrame(geng_table[1:], columns = geng_table[0])
gengcsvfilepath = "/Users/rahulgopeesingh/Documents/Match Prediction/data/raw_data/gengrawdata.csv"    
     
t1_df.to_csv(t1csvfilepath, index = False)
geng_df.to_csv(gengcsvfilepath, index = False)
