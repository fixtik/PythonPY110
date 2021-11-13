if __name__ == "__main__":
    str_ = "1q2w3e4r5t6y"
    chars = ''.join(filter(str.isalpha, str_))

    print("".join(chars))
