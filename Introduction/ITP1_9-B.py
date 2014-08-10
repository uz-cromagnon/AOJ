while True:
    data = raw_input()
    if data == '-':
        break

    num = int(raw_input())

    for x in xrange(0, num):
        shuffle_point = int(raw_input())
        upper_seq = data[:shuffle_point]
        data = data[shuffle_point:] + upper_seq

    print data
