def rankTeams(self, votes: List[str]) -> str:
    num_teams = len(votes[0])
    freq = {team: [0] * num_teams for team in votes[0]}

    for vote in votes:
        for idx, team in enumerate(vote):
            freq[team][
                idx] -= 1  # We use negative because we want to sort in descending order later

    return ''.join(sorted(freq.keys(), key=lambda x: freq[x] + [x]))
