from apikey import api_key
import requests

def rankinfo(id):
        url2 = (
            f"https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}"
            + "?api_key="
            + api_key
        )
        rank_info = requests.get(url2)
        rank_info = rank_info.json()
        return rank_info

def lastmatchinfo(puuid):
    url1=(
        f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20'
        +'&api_key='
        +api_key
    )
    matches_ids=requests.get(url1)
    resp2= matches_ids.json()
    match_url = (
        f'https://europe.api.riotgames.com/lol/match/v5/matches/{resp2[0]}'
        +'?api_key='
        +api_key
    )
    match_info = requests.get(match_url)
    resp = match_info.json()
    user_index = resp["metadata"]["participants"].index(puuid)
    return resp,user_index
 

def last_match(resp,user_index):
    champion=resp["info"]["participants"][user_index]["championName"]
    kills = resp["info"]["participants"][user_index]["kills"]
    deaths = resp["info"]["participants"][user_index]["deaths"]
    assists = resp["info"]["participants"][user_index]["assists"]
    damage_to_champion = resp["info"]["participants"][user_index]["totalDamageDealtToChampions"]
    damage_taken = resp["info"]["participants"][user_index]["totalDamageTaken"]
    healing = resp["info"]["participants"][user_index]["totalHeal"]
    true_damage_to_champion = resp["info"]["participants"][user_index]["trueDamageDealtToChampions"]
    visionscore = resp["info"]["participants"][user_index]["visionScore"]
    goldEarned = resp["info"]["participants"][user_index]["goldEarned"]
    miniony = resp["info"]["participants"][user_index]["totalMinionsKilled"]
    czas = resp["info"]["participants"][user_index]["timePlayed"]
    minuty = czas / 60
    goldperminute = round(goldEarned / minuty, 1)
    cs = round(miniony / minuty, 1)
    cs=f'{miniony} ({cs})'
    kda = round((kills + assists) / deaths, 1)
    return kda,champion,visionscore,goldEarned,goldperminute,damage_to_champion,true_damage_to_champion,damage_taken,healing,cs
    

def rank(rank):
    try:
        division = rank[0]["tier"]
        tier = rank[0]["rank"]
        lp = rank[0]["leaguePoints"]
        wins = rank[0]["wins"]
        losses = rank[0]["losses"]
        played = wins + losses
        wr = round(wins / played * 100, 1)
        wr = f"Winrate: {wr}%  {wins}W {losses}L"
    except Exception:
        division = 'unranked'
        tier = ''
        lp = ''
        wins =''
        losses =''
        wr = ''
    return division,tier,lp,wr


def maestria(id):
    url2 = (
        f"https://eun1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{id}"
        + "?api_key="
        + api_key
    )
    maestria_info = requests.get(url2)
    maestria_info = maestria_info.json()
    champ_id = maestria_info[0]["championId"]
    x = champ_id

    def get_champ_name(_id):
        all_champions_id = {
            1: "Annie",
            2: "Olaf",
            3: "Galio",
            4: "Twisted Fate",
            5: "Xin Zhao",
            6: "Urgot",
            7: "LeBlanc",
            8: "Vladimir",
            9: "Fiddlesticks",
            10: "Kayle",
            11: "Master Yi",
            12: "Alistar",
            13: "Ryze",
            14: "Sion",
            15: "Sivir",
            16: "Soraka",
            17: "Teemo",
            18: "Tristana",
            19: "Warwick",
            20: "Nunu & Willump",
            21: "Miss Fortune",
            22: "Ashe",
            23: "Tryndamere",
            24: "Jax",
            25: "Morgana",
            26: "Zilean",
            27: "Singed",
            28: "Evelynn",
            29: "Twitch",
            30: "Karthus",
            31: "Cho'Gath",
            32: "Amumu",
            33: "Rammus",
            34: "Anivia",
            35: "Shaco",
            36: "Dr.Mundo",
            37: "Sona",
            38: "Kassadin",
            39: "Irelia",
            40: "Janna",
            41: "Gangplank",
            42: "Corki",
            43: "Karma",
            44: "Taric",
            45: "Veigar",
            48: "Trundle",
            50: "Swain",
            51: "Caitlyn",
            53: "Blitzcrank",
            54: "Malphite",
            55: "Katarina",
            56: "Nocturne",
            57: "Maokai",
            58: "Renekton",
            59: "JarvanIV",
            60: "Elise",
            61: "Orianna",
            62: "Wukong",
            63: "Brand",
            64: "LeeSin",
            67: "Vayne",
            68: "Rumble",
            69: "Cassiopeia",
            72: "Skarner",
            74: "Heimerdinger",
            75: "Nasus",
            76: "Nidalee",
            77: "Udyr",
            78: "Poppy",
            79: "Gragas",
            80: "Pantheon",
            81: "Ezreal",
            82: "Mordekaiser",
            83: "Yorick",
            84: "Akali",
            85: "Kennen",
            86: "Garen",
            89: "Leona",
            90: "Malzahar",
            91: "Talon",
            92: "Riven",
            96: "Kog'Maw",
            98: "Shen",
            99: "Lux",
            101: "Xerath",
            102: "Shyvana",
            103: "Ahri",
            104: "Graves",
            105: "Fizz",
            106: "Volibear",
            107: "Rengar",
            110: "Varus",
            111: "Nautilus",
            112: "Viktor",
            113: "Sejuani",
            114: "Fiora",
            115: "Ziggs",
            117: "Lulu",
            119: "Draven",
            120: "Hecarim",
            121: "Kha'Zix",
            122: "Darius",
            126: "Jayce",
            127: "Lissandra",
            131: "Diana",
            133: "Quinn",
            134: "Syndra",
            136: "AurelionSol",
            141: "Kayn",
            142: "Zoe",
            143: "Zyra",
            145: "Kai'sa",
            147: "Seraphine",
            150: "Gnar",
            154: "Zac",
            157: "Yasuo",
            161: "Vel'Koz",
            163: "Taliyah",
            166: "Akshan",
            164: "Camille",
            201: "Braum",
            202: "Jhin",
            203: "Kindred",
            222: "Jinx",
            223: "TahmKench",
            234: "Viego",
            235: "Senna",
            236: "Lucian",
            238: "Zed",
            240: "Kled",
            245: "Ekko",
            246: "Qiyana",
            254: "Vi",
            266: "Aatrox",
            267: "Nami",
            268: "Azir",
            350: "Yuumi",
            360: "Samira",
            412: "Thresh",
            420: "Illaoi",
            421: "Rek'Sai",
            427: "Ivern",
            429: "Kalista",
            432: "Bard",
            497: "Rakan",
            498: "Xayah",
            516: "Ornn",
            517: "Sylas",
            526: "Rell",
            518: "Neeko",
            523: "Aphelios",
            555: "Pyke",
            875: "Sett",
            711: "Vex",
            777: "Yone",
            887: "Gwen",
            876: "Lillia",
        }
        return all_champions_id.get(_id)

    champ_name = get_champ_name(int(x))
    level = maestria_info[0]["championLevel"]
    punkty = maestria_info[0]["championPoints"]
    print(
        f"Twoj czempion z najwieksza iloscia punktow to {champ_name}\nPoziom Maestrii: {level}\nIlość punktów: {punkty}"
    )