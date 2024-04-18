import time
import requests
api_key = 'RGAPI-1aaa536d-ac29-4c67-b0b2-1823a448a8d4'


faker_url = 'https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/Hide%20on%20bush/KR1?api_key=RGAPI-1aaa536d-ac29-4c67-b0b2-1823a448a8d4'
oner_url = 
gumayusi_url = 
keria_url = 
zeus_url = 'https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/T1%20%EC%A0%9C%EC%9A%B0%EC%8A%A4/0102?api_key=RGAPI-1aaa536d-ac29-4c67-b0b2-1823a448a8d4'

t1_table = [["Player Name", "CS at 10 ", "Max Level Lead", "Outcome"]]



def max_level_lead(match_data):
  for participant in match_data["info"]["participants"]:
      if participant["puuid"] == faker_puuid:
          level_lead = participant["challenges"]["maxLevelLeadLaneOpponent"]
          return level_lead
                break
      else:
          print("No player found with this puuid")

def get_cs_at_10(match_data):
  for participant in match_data["info"]["participants"]:
      if participant["puuid"] == faker_puuid:
          CS_at_10 = participant["challenges"]["laneMinionsFirst10Minutes"]
          return CS_at_10
                break
      else:
          print("No player found with this puuid")


def get_player_matches(player_url):
  player_info = requests.get(player_url).json()
  player_puuid = player_info['puuid']
  player_games_url = (
    'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/%27' +
    player_puuid + 
    '%27/ids?start=0&count=100&api_key=' +
    api_key
    )
    
  match_ids = requests.get(player_games_url).json()
  return match_ids
               
def did_win(match_data):
  for participant in match_data["info"]["participants"]:
      if participant["puuid"] == faker_puuid:
          if participant["win"]:
            return "Win"
          else:
            return "Lose"
               break
      else:
          print("No player found with this puuid")
               
               
                      
def get_table_data(player_name, player_url, team_table):
  match_ids = get_player_matches(player_url)
  for match in match_ids:
    match_data_url = (
      "https://asia.api.riotgames.com/lol/match/v5/matches/" +
      match +
      "?api_key=" +
      api_key
    )
    match_data = requests.get(match_data_url).json()
    creep_score = get_cs_at_10(match_data)
    max_level = max_level_lead(match_data)
    outcome = did_win(match_data)
    team_table.append([player_name, creep_score, max_level, outcome])
  return

faker_matches = get_player_matches(faker_url)
len(faker_matches)  
     
     

match = 'KR_6991193145'     
match_data_url = (
      "https://asia.api.riotgames.com/lol/match/v5/matches/" +
      match +
      "?api_key=" +
      api_key
    )
    match_data = requests.get(match_data_url).json()
    creep_score = get_cs_at_10(match_data)
creep_score
     
     
     
     
            
# 
# faker_info = requests.get(faker_url).json()
# faker_info
# 
# faker_puuid = faker_info['puuid']
# 
# faker_puuid
# 
# 
# faker_games_url = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/%27OjM0_nzpr7rWBUpqFQBUeNhiKLpH-fcfSdSQm00VlJfzq-50HQN_cnySkMWlElws88EKxijnKtX6Ww%27/ids?start=0&count=100&api_key=RGAPI-1aaa536d-ac29-4c67-b0b2-1823a448a8d4'
# 
# match_ids = requests.get(faker_games_url).json()
# match_ids
# 
# 
# 
# match_data = requests.get('https://asia.api.riotgames.com/lol/match/v5/matches/KR_6995105556?api_key=RGAPI-1aaa536d-ac29-4c67-b0b2-1823a448a8d4').json()






