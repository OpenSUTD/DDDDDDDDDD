import lib_d


def big_D(verbose=False):
    d = lib_d.D()
    if verbose:
        print("Created D:", d.get_time_created)
    return d.return_D()


def DDDDDDDDDD():
    a = [big_D() for i in range(int("1010", 2))]
    print(''.join(a))


if __name__ == "__main__":
    DDDDDDDDDD()
