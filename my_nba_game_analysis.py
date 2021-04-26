import re as re
import csv as csv

with open ('text.txt','r', encoding='utf-8') as csv_text:
    text_lines = csv.reader(csv_text, delimiter = '|')
    each_play = [each for each in text_lines] #make list of play by play
    txt_play = [each[-1] for each in each_play] # only take plays 
    txt_teams = [each[2] for each in each_play] # defines team
    txt_home = each_play[1][4] # home team
    #print(txt_teams)
    #print(txt_home)
    #print(txt_play)
    #patterns
    
    #two_ptt = 
    #two_ptta
    #three_pt
    #three_ptad
    #free_throw
    #def_reb
    #off_reb
    #assists
    #turnover
    #steal
def all_players(team, home, play_by_play):
    lst_home = []
    lst_away = []

    index = 0
    #name = ""
    #name_pattern = re.compile(r'[A-Z]\. [a-zA-Z]+')
    for i in range(len(play_by_play)):
        name = re.search(r'\w\. \w+', play_by_play[i])
        foul = re.search(r'foul by \w\. \w+', play_by_play[i])
        #print(foul.group(0))
        if name:
            #if foul:
            #    foul = foul.group(0)
            name = name.group(0)
            #print(foul)
            if team[index] == home:
                #print("home index")
                if (name not in lst_home) and foul ==None:
                    lst_home.append(name)
            else:
                #print("away index")
                if (name not in lst_away) and foul ==None:
                    lst_away.append(name)
        index+=1
    print(lst_away)
    print(end  = '\n')
    print(lst_home)

#def all_player_stats():
#    return
#
#def all_player_match():
#    return
#
def analyse_nba_game(play_by_play, lst_home, lst_away):

    {"player_name": '', "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
    for i in range(len(play_by_play)):
        name = re.search(r'\w\. \w+', play_by_play[i])
        foul = re.search(r'foul by \w\. \w+', play_by_play[i])
        two_pt= re.search(r'\w\. \w+ makes 2-pt', play_by_play[i])
        two_pt_at = re.search(r'\w\. \w+ misses ', play_by_play[i])
        three_pt = re.search(r'\w\. \w+ makes 3-pt', play_by_play[i])
        three_pt_at = re.search(r'\w\. \w+ misses 3-pt', play_by_play[i])
        free_throw = re.search(r'\w\. \w+ makes free throw', play_by_play[i])
        free_throw_at = re.search(r'\w\. \w+ misses free throw', play_by_play[i])
        def_reb = re.search(r'Defensive rebound by \w\. \w+', play_by_play[i])
        off_reb = re.search(r'Offensive rebound by \w\. \w+', play_by_play[i])
        assists = re.search(r'assist by \w\. \w+', play_by_play[i])
        turnover = re.search(r'Turnover by \w\. \w+', play_by_play[i])
        steal = re.search(r'steal by \w\. \w+', play_by_play[i])
        foul = re.search(r'foul by \w\. \w+', play_by_play[i])


        #print(foul.group(0))
        if name:
            name = name.group(0)
            #print(foul)
            if team[index] == home:
                #print("home index")
                if (name not in lst_home) and foul ==None:
                    lst_home.append(name)
            else:
                #print("away index")
                if (name not in lst_away) and foul ==None:
                    lst_away.append(name)
        index+=1
    return

all_players(txt_teams, txt_home, txt_play)


#analyse_nba_game()