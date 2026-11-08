import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN: ")

    for player in players:
        if player.nationality == "FIN":
            points = player.goals + player.assists
            print(f"{player.name:20} {player.team:15} "
                  f"{player.goals} + {player.assists} = {points}")
            
if __name__ == "__main__":
    main()