from random import shuffle

def main():
    friends = [input() for _ in range(int(input()))]
    shuffle(friends)

    friends_copy = friends.copy()
    friends_copy = friends_copy[1:]
    friends_copy.append(friends[0])

    secret_friend_list = list(zip(friends, friends_copy))

    for pair in secret_friend_list:
        for i in range(1, len(pair)):
            print(f"{pair[i - 1]} - {pair[i]}")


main()