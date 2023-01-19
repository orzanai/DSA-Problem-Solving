"""
Considering the final scores for a competition, the score of the second competitor is to be determined. Points are given as 2 3 6 6 5.
First check how many participants.
Then take the scores as input.
And find the second.

Example input:
5
2 3 6 6 5

"""

def second_place():
    """
    takes competitors and scores as integer inputs, eliminates duplicates.
    comps: number of competitors
    scores: list of scores
    returns: second place of the list
    """
    
    comps = int(input("Input number of competitiors"))
    scores = []
    for comp in range(comps):
        scores.append(int(input("Input scores")))
    second = list(set(sorted(scores)))
    
    return second[-2]
