from random import shuffle

def main():
    friends = [input() for _ in range(int(input()))]
    shuffle(friends)

    friends_copy = friends[1:] + list(friends[0])

    secret_friend_list = list(zip(friends, friends_copy))

    for pair in secret_friend_list:
        print(*pair, sep=' - ')


main()