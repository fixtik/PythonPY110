def geom_progress(start: int = 1, step: int = 2):
    value = start
    while True:
        yield value
        value *= step

if __name__ == "__main__":
    # Write your solution here
    g_p = geom_progress(5)
    for _ in range(10):
        print(next(g_p))
