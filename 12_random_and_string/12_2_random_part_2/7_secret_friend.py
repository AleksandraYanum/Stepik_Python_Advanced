from random import shuffle

def main():
    friends = [input() for _ in range(int(input()))]
    shuffle(friends)

    secret_friend_list = []
    for i in range(len(friends)):
        print(f"{friends[i - 1]} - {friends[i]}")


main()