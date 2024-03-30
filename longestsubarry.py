from itertools import count
import re


def pickingNumbers(a):
    ls =[]
    
    for i in range(len(a)):
        row = []
        for j in range(len(a)):
            if(abs(a[i] - a[j]) <= 1):
                row.append(a[j])
        ls.append(row)

    

    return ls

a = [1,1,2,2,4,4,5,5,5]



def climbingLeaderboard(ranked, player):
    scores = set(ranked)
    leaderboard  = sorted(scores, reverse= True)
    l = len(leaderboard)
    rank = [] 
    for p in player: 
        while (l > 0) and (p >= leaderboard[l-1]):
            l -= 1 
        rank.append(l+1)
    return rank


ranked= [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]
print(climbingLeaderboard(ranked, player)) 



def repeatedString(s, n):
    S = (s * (n//len(s) + 1))[:n]
    c = S.count('a')
    print(c)
     
print(repeatedString('aba', 10))



