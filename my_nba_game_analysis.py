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
    #three_pta
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
def analyse_nba_game(play_by_play_moves):

    
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
    return

all_players(txt_teams, txt_home, txt_play)


#analyse_nba_game()