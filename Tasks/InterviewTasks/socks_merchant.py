# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar


def count_socks_pairs(socks):
    colors = {}
    for sock in socks:
        if sock not in colors.keys():
            colors[sock] = 1
        else:
            colors[sock] += 1
    pairs = 0
    for color in colors:
        pairs += colors[color] // 2
    return pairs


if __name__ == '__main__':
    socks_list = [10, 20, 20, 10, 10, 30, 50, 10, 20, 60, 10, 20, 50]
    result = count_socks_pairs(socks_list)
    print(result)

