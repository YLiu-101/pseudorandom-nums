state = (1 << 127) | 1
orig_state = state
counter = 0
length = len(bin(state)[2:])
while(True):
    # print("{:08b}".format(state),f"size {len(bin(state)[2:])}")
    print(state & 1,end='')
    newbit = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7)) & 1
    state = (state >> 1) | (newbit << (127))
    counter+=1
    if (state == orig_state):
        print(f"Ended after {counter} iterations with size {length} binary number")
        break

