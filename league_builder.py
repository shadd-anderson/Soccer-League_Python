import csv


# Creates the letters for the parents by accepting a list of players and the name of the team
def welcome_letters(team_list):
    # Letter template
    letter = "Dear {},\n" \
             "Welcome to the league! We're excited for {} to officially join the {}. Please be aware the first " \
             "practice will be on Thursday, January 17th, at 5:00pm. Can't wait to meet you and get started on a " \
             "great season!\n" \
             "GOOOOOOOOO {}!!!!"

    # Loops through list of players and formats the template with required parameters
    for team_name in team_list:
        for team_player in team_list[team_name]:
            with open("{}.txt".format(team_player['name'].replace(" ", "_")), "w") as file:
                file.write(letter.format(team_player['guardians'], team_player['name'], team_name, team_name.upper()))


# We don't want this to run when it imports!
if __name__ == '__main__':
    players_list = []
    experienced = []
    non_experienced = []

    teams = {'Sharks': [], 'Dragons': [], 'Raptors': []}

    # Fills the players_list with each individual player from the soccer_players.csv file
    with open('soccer_players.csv', newline='') as player_file:
        players = csv.DictReader(player_file, delimiter=',')
        rows = list(players)
        for row in rows:
            players_list.append({'name': row['Name'],
                                 'height': row['Height (inches)'],
                                 'experience': row['Soccer Experience'],
                                 'guardians': row['Guardian Name(s)']})

    # Splits players into experienced/non-experienced
    for player in players_list:
        if player['experience'] == "YES":
            experienced.append(player)
        else:
            non_experienced.append(player)

    # Equally divides experienced players across 3 teams
    # TODO: Allow for more than 3 hard-coded teams
    for index, player in enumerate(experienced):
        if index % 3 == 0:
            teams['Sharks'].append(player)
        elif index % 3 == 1:
            teams['Dragons'].append(player)
        else:
            teams['Raptors'].append(player)

    # Equally divides non-experienced players across 3 teams
    # TODO: Allow for more than 3 hard-coded teams
    for index, player in enumerate(non_experienced):
        if index % 3 == 0:
            teams['Raptors'].append(player)
        elif index % 3 == 1:
            teams['Dragons'].append(player)
        else:
            teams['Sharks'].append(player)

    # Creates the teams.txt file with rosters
    with open('teams.txt', 'w') as team_file:
        for team in teams:
            team_file.write("{}\n".format(team))
            for player in teams[team]:
                team_file.write("{}, {}, {}\n".format(player['name'], player['experience'], player['guardians']))
            team_file.write("\n")

    # Creates all welcome letters
    welcome_letters(teams)
