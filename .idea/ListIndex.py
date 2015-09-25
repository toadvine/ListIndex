__author__ = 'benjamin_sanchez'

def main():
    a_toss = int(input())
    b_list = [int(x) for x in input().split()]
    sorted_b_list = b_list.sort()
    for x in sorted_b_list:
        print(b_list.index(), end=" ")


main()
