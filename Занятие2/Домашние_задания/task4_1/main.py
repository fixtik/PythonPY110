def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i+1]

def len_(points: list):
    def d(pt):
        return ((pt[0][1] - pt[0][0]) ** 2 + (pt[1][1] - pt[1][0]) ** 2) ** 0.5
    return sum(map(d, pairwise(points)))

if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    print(len_(pts))

