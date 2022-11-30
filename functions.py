from apikey import api_key
import requests


name = input('Wprowadź nazwe swojego summonera: ')
name = str(name.replace(' ', '%20'))

def kda(name):
    url1 = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
    name_api_link = url1 +"?api_key="+api_key
    player_info = requests.get(name_api_link)
    resp1 = player_info.json()
    player_puuid = resp1['puuid']
    url2=f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{player_puuid}/ids?start=0&count=20'+'&api_key='+api_key
    matches_ids=requests.get(url2)
    resp2= matches_ids.json()
    match_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{resp2[0]}'+'?api_key='+api_key
    match_info = requests.get(match_url)
    resp3 = match_info.json()
    user_index=resp3['metadata']['participants'].index(player_puuid)
    kills=resp3['info']['participants'][user_index]['kills']
    deaths=resp3['info']['participants'][user_index]['deaths']
    assists=resp3['info']['participants'][user_index]['assists']
    kda=round((kills+assists)/deaths,1)
    print(kda)

def CS(name):
    url1 = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
    name_api_link = url1 +"?api_key="+api_key
    player_info = requests.get(name_api_link)
    resp1 = player_info.json()
    player_puuid = resp1['puuid']
    url2=f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{player_puuid}/ids?start=0&count=20'+'&api_key='+api_key
    matches_ids=requests.get(url2)
    resp2= matches_ids.json()
    match_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{resp2[0]}'+'?api_key='+api_key
    match_info = requests.get(match_url)
    resp3 = match_info.json()
    user_index=resp3['metadata']['participants'].index(player_puuid)
    miniony=resp3['info']['participants'][user_index]['totalMinionsKilled']
    czas=resp3['info']['participants'][user_index]['timePlayed']
    minuty=czas/60
    cs=round(miniony/minuty,1)
    print(cs)


#nie dziala huj
def rank(name):
    url1 = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
    name_api_link = url1 +"?api_key="+api_key
    player_info = requests.get(name_api_link)
    resp1 = player_info.json()  
    player_id = resp1['id']
    url2=f'https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/{player_id}'+'?api_key='+api_key
    info=requests.get(url2)
    resp=info.json()
    division=resp['tier']
    rank=resp['rank']
    lp=resp['leaguePoints']
    ranga=f'{division} {rank} {lp} LP '
    
    print(ranga)


#rank(name=name)

url1 = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
name_api_link = url1 +"?api_key="+api_key
player_info = requests.get(name_api_link)
resp1 = player_info.json()  
player_id = resp1['id']
url2=f'https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/{player_id}'+'?api_key='+api_key
info=requests.get(url2)
resp=info.json()
division=resp['tier']
rank=resp['rank']
lp=resp['leaguePoints']
ranga=f'{division} {rank} {lp} LP '

print(ranga)




