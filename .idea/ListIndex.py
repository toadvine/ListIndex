__author__ = 'benjamin_sanchez'

def main():
    a_toss = int(input())
    b_list = [int(x) for x in input().split()]
    c_list = list(b_list)
    c_list.sort()
    for x in c_list:
        print(b_list.index(x) + 1, end=" ")


main()
