import re as re
import csv as csv



def func_all_players(play_by_players): #function to define all playyers
    lst_players = []
    
    for i in range(len(play_by_players)):
        name = re.search(r'\w\. \w+', play_by_players[i])
        if name:
            name = name.group(0)
            if name not in lst_players:
                lst_players.append(name)

    return(lst_players)    

def func_stats(play_by_playst): # function to sort statistics

    lst_names = []
    lst_names = func_all_players(play_by_playst)

    lst_stats = []
    
    for player in lst_names:
        dict_profile = {"player_name": '', "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
        dict_profile["player_name"] = player

        for i in range(len(play_by_playst)):
            name = re.search(r'(\w\. \w+)', play_by_playst[i]) 
            two_pt= re.search(r'(\w\. \w+) makes 2-pt', play_by_playst[i])
            two_pt_at = re.search(r'(\w\. \w+) misses 2-pt', play_by_playst[i])
            three_pt = re.search(r'(\w\. \w+) makes 3-pt', play_by_playst[i])
            three_pt_at = re.search(r'(\w\. \w+) misses 3-pt', play_by_playst[i])
            free_throw = re.search(r'(\w\. \w+) makes free throw', play_by_playst[i])
            free_throw_clear = re.search(r'(\w\. \w+) makes clear path free throw', play_by_playst[i])
            free_throw_at = re.search(r'(\w\. \w+) misses free throw', play_by_playst[i])
            free_throw_clear_at = re.search(r'(\w\. \w+) misses clear path free throw', play_by_playst[i])
            def_reb = re.search(r'Defensive rebound by (\w\. \w+)', play_by_playst[i])
            off_reb = re.search(r'Offensive rebound by (\w\. \w+)', play_by_playst[i])
            assists = re.search(r'(assist by) (\w\. \w+)', play_by_playst[i])
            turnover = re.search(r'Turnover by (\w\. \w+)', play_by_playst[i])
            steal = re.search(r'(steal by) (\w\. \w+)', play_by_playst[i])
            block = re.search(r'(block by) (\w\. \w+)', play_by_playst[i])
            foul = re.search(r'foul by (\w\. \w+)', play_by_playst[i])

            if name:
                name2 = name.group(0)
                if name2 == player:
                    if two_pt:
                        dict_profile["FG"] +=1
                        dict_profile["FGA"] +=1
                    if two_pt_at:
                        #dict_profile["FG"] +=1
                        dict_profile["FGA"] +=1
                    if three_pt:
                        dict_profile["3P"] +=1
                        dict_profile["3PA"] +=1
                        dict_profile["FG"] +=1
                        dict_profile["FGA"] +=1
                    if three_pt_at:
                        #dict_profile["FG"] +=1
                        dict_profile["3PA"] +=1
                        dict_profile["FGA"] +=1
                    if free_throw or free_throw_clear:
                        #print(free_throw)
                        dict_profile["FT"] +=1
                        dict_profile["FTA"] +=1
                    if free_throw_at or free_throw_clear_at:
                        #dict_profile["FG"] +=1
                        dict_profile["FTA"] +=1
                    if def_reb:
                        dict_profile["DRB"] +=1
                        dict_profile["TRB"] +=1
                    if off_reb:
                        dict_profile["ORB"] +=1
                        dict_profile["TRB"] +=1
                    if foul:
                        dict_profile["PF"] +=1
                    if turnover:
                        dict_profile["TOV"] +=1
                #need to group(2)
                if assists :    
                    name_ast = assists.group(2)
                    if name_ast == player :
                        dict_profile["AST"] +=1
                if steal :    
                    name_stl = steal.group(2)
                    if name_stl == player :
                        dict_profile["STL"] +=1
                
                if block:    
                    name_blk = block.group(2)
                    if name_blk == player :
                        dict_profile["BLK"] +=1

                #total pts and %
                if dict_profile["FG"] != 0:
                    dict_profile["PTS"] = 2*(dict_profile["FG"]-dict_profile["3P"])+3*(dict_profile["3P"])+dict_profile["FT"]
                else:
                    dict_profile["PTS"] = 0
                if dict_profile["FGA"] != 0:
                    dict_profile["FG%"] = round((dict_profile["FG"]/dict_profile["FGA"]), 3)
                    
                else:
                    dict_profile["FG%"] = 0
                if dict_profile["3PA"] != 0:
                    dict_profile["3P%"] = round((dict_profile["3P"]/dict_profile["3PA"]),3)
                else:
                    dict_profile["3P%"] = 0
                if dict_profile["FTA"] != 0:
                    dict_profile["FT%"] = round((dict_profile["FT"]/dict_profile["FTA"]),3)
                else:
                    dict_profile["FT%"] = 0
        lst_stats.append(dict_profile)

    #team arranging 
    #dict_final = {"home_team": {"name": "", "players_data": lst_home}, "away_team": {"name": "", "players_data": lst_away}}
    return lst_stats               
    #print(lst_stats[0]["player_name"])


def home_team(stats, home, play_by_play, txt_posession): #function to sort home team
    #index = 0
    lst_home_sort = []
    for i in range(len(stats)):
        check = stats[i]["player_name"]
        #print(check)
        for j in range(len(play_by_play)):
            name = re.search(r'(\w\. \w+)', play_by_play[j])
            foul = re.search(r'foul by \w\. \w+', play_by_play[j])
            if name:
                #print("1st if",check)
                name1 = name.group()
                if check == name1 and txt_posession[j] == home:
                        if (stats[i] not in lst_home_sort) and foul == None:
                    #print("2 if",check)
                            lst_home_sort.append(stats[i])
        #index +=1
    return lst_home_sort


def away_team(stats, home, play_by_play, txt_posession): # function to sort away team
    lst_away_sort = []
    for i in range(len(stats)):
        check = stats[i]["player_name"]
        #print(check)
        for j in range(len(play_by_play)):
            name = re.search(r'(\w\. \w+)', play_by_play[j])
            foul = re.search(r'foul by \w\. \w+', play_by_play[j])
            if name:
                #print("1st if",check)
                name1 = name.group()
                if check == name1 and txt_posession[j] != home:
                        if (stats[i] not in lst_away_sort) and foul == None:
                    #print("2 if",check)
                            lst_away_sort.append(stats[i])
        #index +=1
    return lst_away_sort

def analyse_nba_game(play_by_play): #main function
    with open (play_by_play,'r', encoding='utf-8') as csv_text:
        text_lines = csv.reader(csv_text, delimiter = '|')
        each_play = [each for each in text_lines] #make list of play by play
        txt_play = [each[-1] for each in each_play] # only take plays 
        txt_teams = [each[2] for each in each_play] # defines team
        txt_home = each_play[1][4] # home team
       
        txt_away = each_play[1][3] # away team
        
    func_stats(txt_play)

    lst_stats = []
    lst_stats = func_stats(txt_play)
    

    lst_home_final = []
    lst_away_final = []
    lst_home_final = home_team(lst_stats, txt_home, txt_play, txt_teams)
    #print(lst_home_final)
    lst_away_final = away_team(lst_stats, txt_home, txt_play, txt_teams)
    #print(lst_away_final)
    dict_final = {"home_team": {"name": txt_home, "players_data": lst_home_final}, "away_team": {"name": txt_away, "players_data": lst_away_final}}
    #print(txt_teams)

    print(dict_final)
    print("\n")
    print_nba_game_stats(lst_home_final)
    print("\n")
    print_nba_game_stats(lst_away_final)
    #print(lst_home_final)


#part II
def print_nba_game_stats(team_dict):

    headers = [keys for keys in team_dict[0].keys()]
    print(*headers, sep = "\t")

    for i in range(len(team_dict)):
        print(*team_dict[i].values(), sep = "\t")
    dict_total = {"Team Totals": 'Team Totals', "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
    

    #print totals
    for i in range(len(team_dict)):
        dict_total["FG"] += team_dict[i]["FG"]
        dict_total["FGA"] += team_dict[i]["FGA"]
        dict_total["3P"] += team_dict[i]["3P"] 
        dict_total["3PA"] +=team_dict[i]["3PA"]
        dict_total["FT"] += team_dict[i]["FT"] 
        dict_total["FTA"] +=team_dict[i]["FTA"]
        dict_total["ORB"] +=team_dict[i]["ORB"]
        dict_total["DRB"] +=team_dict[i]["DRB"]
        dict_total["TRB"] +=team_dict[i]["TRB"]
        dict_total["AST"] +=team_dict[i]["AST"]
        dict_total["STL"] +=team_dict[i]["STL"]
        dict_total["BLK"] +=team_dict[i]["BLK"]
        dict_total["TOV"] +=team_dict[i]["TOV"]
        dict_total["PF"] += team_dict[i]["PF"] 
        dict_total["PTS"] +=team_dict[i]["PTS"]
        
    dict_total["FG%"] = round((dict_total["FG"]/dict_total["FGA"]), 3)
    dict_total["3P%"] = round((dict_total["3P"]/dict_total["3PA"]), 3)
    dict_total["FT%"] = round((dict_total["FT"]/dict_total["FTA"]), 3)
    
    
    print(*dict_total.values(), sep = "\t")
    
analyse_nba_game("/home/docode/project/text.txt")


#analyse_nba_game()