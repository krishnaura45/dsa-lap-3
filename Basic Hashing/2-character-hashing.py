# hashing alphabets 
def alphaHash() -> None:
    # single string input
    s = input().strip()

    # Precompute
    hash_arr = [0] * 26

    for ch in s:
        hash_arr[ord(ch) - ord('a')] += 1

    # Fetch
    q = int(input())

    for _ in range(q):
        ch = input().strip()

        freq = hash_arr[ord(ch) - ord('a')]

        print(f"Frequency of {ch} --> {freq}")

# hashing all characters 
def charHash() -> None:
    # single string input
    s = input().strip()

    # Precompute
    hash_arr = [0] * 256

    for ch in s:
        hash_arr[ord(ch)] += 1

    # Fetch
    q = int(input())

    for _ in range(q):
        ch = input().strip()

        freq = hash_arr[ord(ch)]

        print(f"Frequency of {ch} --> {freq}")


# optimal for hashing characters
from collections import Counter
def opt_charHash():
    s = input().strip()

    freq = Counter(s)

    q = int(input())

    for _ in range(q):
        ch = input().strip()
        print(f"Frequency of {ch} --> {freq[ch]}")


if __name__=="__main__":
    # sample input for func 1:
    # maadam
    # 4
    # m
    # a
    # d
    # s

    # CALLING function 1
    # alphaHash()

    # sample input for func 2:
    # maad@M4
    # 6
    # m
    # a
    # M
    # 4
    # @
    # S

    # CALLING function 2
    charHash()