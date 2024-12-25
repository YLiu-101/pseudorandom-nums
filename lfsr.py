def next_lfsr(state):
    newbit = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7)) & 1
    return (state >> 1) | (newbit << 127)

def main():
    state = (1 << 127) | 1
    orig_state = state
    counter = 0
    length = len(bin(state)[2:])
    while(True):
        # print("{:08b}".format(state),f"size {len(bin(state)[2:])}")
        print(state & 1,end='')
        state = next_lfsr(state)
        counter+=1
        if (state == orig_state):
            print(f"Ended after {counter} iterations with size {length} binary number")
            break

if __name__ == "__main__":
    main()