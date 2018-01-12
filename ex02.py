def myrange3(start, end, step=1):
    i = start
    while i + step < end:
        i += step
        yield i


def myrange2(start, end, step=1):
    r = []
    i = start
    while i + step < end:
        i += step
        r.append(i)
    return r


if __name__ == '__main__':
    print([x for x in myrange3(0, 10, 3)])
    print([x for x in myrange2(0, 10, 3)])
