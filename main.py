import urllib2
import csv

from bs4 import BeautifulSoup
quote_page = 'http://www.premierinjuries.com/injury-table.php'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
injury_table = soup.find('table', attrs={'class': 'injury-table'})
#with open('index.csv', 'a') as csv_file:

rows = injury_table.find_all('tr')

with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for row in rows :
        #print row['class'][0]
        if(row['class'][0]=='heading') :
            team_name=row.text.strip()
            name = team_name[0:team_name.rindex(' ')]
            injury_count = team_name[team_name.rindex(' '):len(team_name)-5]
            # print 'Team Name:' + name
            # print 'Injury Count:' + injury_count
            writer.writerow([])
            writer.writerow([])
            writer.writerow([name.upper(),injury_count])
        i=0
        if(i==injury_count) :
            pass
        if(row['class'][0]=='player-row') :
            player = row.text.strip()
            player=player.splitlines()
            #print player
            #print 'Player\tReason\tFurther Detail\t\t\tPotential Return\tCondition\tStatus'
            writer.writerow([player[0][6:],player[1][6:],player[2][14:],player[3][16:],player[4][9:],player[5][6:]])

            # print 'Player: '+ player[0][6:]
            # print 'Reason: '+ player[1][6:]
            # print 'Further Detail: ' + player[2][14:]
            # print 'Potential Return: ' + player[3][16:]
            # print 'Condition: ' + player[4][9:]
            # print 'Status: ' + player[5][6:]
            # print '\n'






#for link in soup.find_all('a'):
# with open('index.csv', 'a') as csv_file:


#     for entry in injury_table.find_all('tr',attrs={'class':'heading'}):
#         # player = players.text.strip()
#         # print player
#         team_name=entry.find('th').text.strip()

#         name = team_name[0:team_name.rindex(' ')]
#         injury_count = team_name[team_name.rindex(' '):len(team_name)-5]
#         writer = csv.writer(csv_file)
#         writer.writerow([name, injury_count])

#     players = injury_table.find_all('tr',attrs={'class':'player-row'})
#     for player_row in players :
#         player = player_row.text.strip()
#         writer = csv.writer(csv_file)
#         writer.writerow([player])



#print entry.parent
# player_row = entry.parent.find_all('tr',attrs={'class':'player-row'})
# print player_row




# for entry in injury_table.find_all('tr'):
#     team_name=entry.find('tr',attrs={'class':'heading'})

#     # name = team_name[0:team_name.rindex(' ')]
#     # injury_count = team_name[team_name.rindex(' '):len(team_name)-5]
#     # print name
#     # print injury_count
#     print team_name


    #print entry.parent
    #print name
    #print injury_count


