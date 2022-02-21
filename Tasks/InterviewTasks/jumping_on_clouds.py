# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.


def jumping_on_clouds(clouds):
    cumulus = 0
    current_cloud = 0
    steps = 0
    while current_cloud < len(clouds)-2:
        current_cloud += 2 if clouds[current_cloud+2] == cumulus else 1
        steps += 1
    steps += 1 if current_cloud < len(clouds)-1 else 0
    return steps


if __name__ == '__main__':
    clouds_list = [0, 0, 1, 0, 0, 1, 0]
    result = jumping_on_clouds(clouds_list)
    print(result)
