#!/usr/local/cs/bin/python3

import argparse, random, sys

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-e', '--echo', nargs='*', type=str)
    parser.add_argument('-i', '--input-range', nargs=1, type=str)
    parser.add_argument('inputfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin) 
    parser.add_argument('-r', '--repeat', action='store_true')
    parser.add_argument('-n', '--head-count', nargs=1, type=int)
    

    args = parser.parse_args()


    buffer = []
    if args.echo:
        buffer = args.echo
        random.shuffle(buffer)
    elif args.input_range:
        buffer = args.input_range
        list = buffer[0].split('-')
        for i in range(int(list[0]), int(list[1]) - 1):
            list.append(i + 1)
        random.shuffle(list)
        buffer = list[:]
    else:
        if args.inputfile != sys.stdin:
            buffer = args.inputfile.read().splitlines()
            random.shuffle(buffer)
        else:
            buffer = sys.stdin.read().splitlines()
            random.shuffle(buffer)
            


    if args.repeat:
        if args.head_count:
            for i in range(int(args.head_count[0])):
                print(random.choice(buffer))
        else:
            while True:
                print(random.choice(buffer))
    elif args.head_count:
        if args.head_count[0] > len(buffer):
            for i in range(len(buffer)):
                print(buffer[i])
        else:
            for i in range(args.head_count[0]):
                print(buffer[i])
    else:
        for i in range(len(buffer)):
            print(buffer[i])



if __name__ == "__main__":
    main()
