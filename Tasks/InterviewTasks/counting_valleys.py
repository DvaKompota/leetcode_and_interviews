# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path


def count_valleys(path_string):
    valley_started = False
    valley_ended = False
    level = 0
    valleys_traversed = 0
    for step in path_string:
        level += 1 if step.upper() == 'U' else -1
        valley_started = True if level < 0 and not valley_started else valley_started
        valley_ended = True if level == 0 and valley_started else valley_ended
        if valley_started and valley_ended:
            valleys_traversed += 1
            valley_started = valley_ended = False
    return valleys_traversed


if __name__ == '__main__':
    path = 'UDDDUDUU'
    result = count_valleys(path)
    print(result)
