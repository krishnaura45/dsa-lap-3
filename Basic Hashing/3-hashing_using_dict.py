# Hashing using dictionary

def mapHash() -> None:
    arr = list(map(int, input().split()))

    # Precompute
    mpp = {}

    for num in arr:
        mpp[num] = mpp.get(num, 0) + 1

    # Iterate in sorted order (like C++ map)
    for key in sorted(mpp):
        print(f"{key} --> {mpp[key]}")

    q = int(input())

    while q > 0:
        num = int(input())

        # Fetch
        freq = mpp.get(num,0)
        print(f"Frequency of {num} --> {freq}")

        q -= 1


def mapHash2() -> None:
    arr = list(map(int, input().split()))

    # Precompute
    mpp = {}

    for num in arr:
        mpp[num] = mpp.get(num, 0) + 1

    # Iterate (like C++ unordered map)
    for key in mpp:
        print(f"{key} --> {mpp[key]}")

    q = int(input())

    while q > 0:
        num = int(input())

        # Fetch
        freq = mpp.get(num,0)
        print(f"Frequency of {num} --> {freq}")

        q -= 1


if __name__ == "__main__":
    # mapHash()
    mapHash2()