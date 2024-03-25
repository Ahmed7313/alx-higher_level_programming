#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = sum(score * weight for score, weight in my_list)
    denominator = sum(weight for _, weight in my_list)
    return numerator / denominator if denominator else 0

if __name__ == "__main__":
    weight_average = __import__('100-weight_average').weight_average

    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
