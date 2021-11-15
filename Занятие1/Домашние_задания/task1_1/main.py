if __name__ == "__main__":

    def zip_(list_: list):
        return list(zip(range(len(list_)), list_))

    lisr = [1,2,3,4,5,6,7]

    print(zip_(lisr))