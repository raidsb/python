"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

    The player with the highest score is ranked number 

    on the leaderboard.
    Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

Example


The ranked players will have ranks , , , and , respectively. If the player's scores are , and , their rankings after each game are , and . Return

.

Function Description

Complete the climbingLeaderboard function in the editor below.

climbingLeaderboard has the following parameter(s):

    int ranked[n]: the leaderboard scores
    int player[m]: the player's scores

Returns

    int[m]: the player's rank after each new score
https://www.hackerrank.com/challenges/one-month-preparation-kit-climbing-the-leaderboard/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three 
"""
def climbingLeaderboard(ranked, player):
    results = []
    for score in player:
        ranked.append(score)
        ranked = sorted(list(set(ranked)), reverse=True)
        results.append(ranked.index(score) + 1)
    return results

# The right one, it doesn't exceeds timelimit --> using the binary search
def climbingLeaderboard(ranked, player):
    unique_scores = sorted(set(ranked), reverse=True)
    results = []

    j = len(unique_scores) - 1
    for score in player:
        while j >= 0:
            if score >= unique_scores[j]:
                j -= 1
            else:
                results.append(j + 1 + 1)
                break
        else:
            results.append(0 + 1)
        unique_scores.insert(j + 1, score)  # Insert Alice's score into the list

    return results