from collections import defaultdict


def solution(genres: list[str], plays: list[int]) -> list[int]:
    genres_play = defaultdict(int)
    genres_rank = defaultdict(list)
    result = []

    for index, (genre, play) in enumerate(zip(genres, plays)):
        genres_play[genre] += play
        genres_rank[genre].append((index, play))

    for key in genres_rank:
        genres_rank[key].sort(key=lambda x: x[1], reverse=True)

    for genre in sorted(genres_play.items(), key=lambda x: x[1], reverse=True):
        result.extend([item[0] for item in genres_rank[genre[0]][:2]])

    return result
