def solution(participant, completion):
    players = {}

    for participant_name in participant:
        if participant_name in players:
            players[participant_name] += 1
            continue

        players[participant_name] = 1

    for completion_name in completion:
        if completion_name not in players:
            return completion_name

        players[completion_name] -= 1

    for players_name in players:
        if players[players_name] != 0:
            return players_name

    return 'no retired players!'


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
