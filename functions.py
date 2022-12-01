from apikey import api_key
import requests
import json

name = input('Wprowadź nazwe swojego przywolywacza: ')
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
    print(f'KDA {kda}')

def champion(name):
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
    champ=resp3['info']['participants'][user_index]['championName']
    info=resp3['info']['participants'][user_index]
    print(info)

def visionscore(name):
    url1 = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
    name_api_link = url1 +"?api_key="+api_key
    player_info = requests.get(name_api_link)
    resp1 = player_info.json()
    player_puuid =resp1['puuid']
    url2=f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{player_puuid}/ids?start=0&count=20'+'&api_key='+api_key
    matches_ids=requests.get(url2)
    resp2= matches_ids.json()
    match_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{resp2[0]}'+'?api_key='+api_key
    match_info = requests.get(match_url)
    resp3 = match_info.json()
    user_index=resp3['metadata']['participants'].index(player_puuid)
    vs=resp3['info']['participants'][user_index]['visionScore']
    print(f'Punkty wizji: {vs}')

def gold(name):
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
    goldEarned=resp3['info']['participants'][user_index]['goldEarned']
    czas=resp3['info']['participants'][user_index]['timePlayed']
    minuty=czas/60
    goldperminute=round(goldEarned/minuty,1)
    print(f'Zdobyte złoto: {goldEarned}\nZłoto na minutę: {goldperminute}')


def damage(name):
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
    damage_to_champion=resp3['info']['participants'][user_index]['totalDamageDealtToChampions']
    damage_taken=resp3['info']['participants'][user_index]['totalDamageTaken']
    healing=resp3['info']['participants'][user_index]['totalHeal']
    true_damage_to_champion=resp3['info']['participants'][user_index]['trueDamageDealtToChampions']
    print(f'Zadane obrazenia graczą: {damage_to_champion}\nOtrzymane obrazenia: {damage_taken}\nCalkowite leczenie: {healing}\nZadane obrażenia nieuchronne: {true_damage_to_champion}')

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
    index=resp3['metadata']['participants'].index(player_puuid)
    miniony=resp3['info']['participants'][index]['totalMinionsKilled']
    czas=resp3['info']['participants'][index]['timePlayed']
    minuty=czas/60
    cs=round(miniony/minuty,1)
    print(f'CS {cs}')


def rank(name):
    url1 = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
    name_api_link = url1 +"?api_key="+api_key
    player_info = requests.get(name_api_link)
    resp1 = player_info.json()
    player_id = resp1['id']
    url2 =f'https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/{player_id}'+'?api_key='+api_key
    rank_info=requests.get(url2)
    rank_info=rank_info.json()
    ranga=(rank_info)
    division=ranga[0]['tier']
    tier=ranga[0]['rank']
    lp=ranga[0]['leaguePoints']
    ranga_informacje=f'{division} {tier} {lp}LP'
    wins=ranga[0]['wins']
    losses=ranga[0]['losses']
    played=wins+losses
    wr = round(wins/played*100,1)
    wr=f'Winrate: {wr}%'
    print(f'{ranga_informacje} \n{wr}')



#print(f'=======\nObecna ranga\n=======')
#rank(name=name)
#print(f'=======\nStatystyki z ostatniej gry\n=======')
#champion(name=name)
#kda(name=name)
#CS(name=name)
#print('=======')   





# https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/_pj7SWuX6ln_mAFfdQy8uh9tYRygVilOIHtxWquVDFwxNGqH4fW8fWIW5g?api_key=RGAPI-62ac970f-d313-4e55-a95e-59b6ef103018
