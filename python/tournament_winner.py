"""
Given an array of pairs representing the teams that have competed against eachother and an array containing
the results of each competition, write a function that returns the winner of the tournament. The input arrays are named
competions and results. The competitions array has elemens in the form of [home_team, away_team], where each team is a
string of at most 30 characters representing the name of the team. The results array contains information about the winner
of each corresponding competition in the competitions array. Specifically, results[i] denotes the winner of competitions[i]
where a 1 in the results array means that the home team in the corresponding competition won and a 0 means that the away team won.

It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams
exactly once. Each tournament will have at least two teams.
"""

def tournament_winner(competitions, results):
    """
    :type competitions: List[List[str]]
    :type results: List[List[int]]
    """
    teams = {}

    for home, away in competitions:
        teams[home] = 0
        teams[away] = 0

    for i in range(len(competitions)):
        home, away = competitions[i]
        if results[i] == 1:
            teams[home] += 1
        else:
            teams[away] += 1

    winner = max(teams, key=teams.get)
    return winner

"""
It iterates through the competitions and results arrays to update the number of wins for each team. Then it uses 
the max() function with the key parameter set to the teams.get method to find the team with the most wins and returns
 that team's name as the tournament winner.
"""