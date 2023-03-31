def find_outlier(integers):
    for int in integers:
        if integers[int] % 2:
            print(integers[int])
            return int



print(find_outlier([21, 4, 0, 100, 4, 11, 2602, 36, 11]))