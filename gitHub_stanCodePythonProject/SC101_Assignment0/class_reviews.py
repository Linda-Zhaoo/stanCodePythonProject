"""
File: class_reviews.py
Name: Linda Zhao
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1


def main():
    """
    The program would mostly separate into 3 parts.
    1st: Judge which class is user input. If it equal to -1 program end.
    2nd: Enter scored, if it first data of each class deal with the edge condition, else count compare the max and min
    score and count the average score.
    3nd: if user input -1, then print each class's max, min and avg score.
    """
    count_001 = 0
    count_101 = 0
    max_001 = -float('inf')
    min_001 = float('inf')
    max_101 = -float('inf')
    min_101 = float('inf')
    sum_001 = -float('inf')
    sum_101 = -float('inf')
    avg_001 = -float('inf')
    avg_101 = -float('inf')
    class_name = input('Which class? ')
    if class_name == str(EXIT):
        print('No class scores were entered')
    else:
        while True:
            if class_name == str(EXIT):
                break
            score = int(input('Score: '))
            if str('001') in class_name:
                if count_001 == 0:
                    count_001 += 1
                    max_001 = score
                    min_001 = score
                    sum_001 = score
                    avg_001 = sum_001/count_001
                else:
                    count_001 += 1
                    sum_001 += score
                    avg_001 = sum_001/count_001
                    if score > max_001:
                        max_001 = score
                    if score < min_001:
                        min_001 = score

            if str('101') in class_name:
                if count_101 == 0:
                    count_101 += 1
                    max_101 = score
                    min_101 = score
                    sum_101 = score
                    avg_101 = sum_101/count_101
                else:
                    count_101 += 1
                    sum_101 += score
                    avg_101 = sum_101/count_101
                    if score > max_101:
                        max_101 = score
                    if score < min_101:
                        min_101 = score
            class_name = input('Which class? ')

        print('==============SC001==============')
        if count_001 == 0:
            print('No score for SC001')
        else:
            print('Max (001): '+str(max_001))
            print('Min (001): '+str(min_001))
            print('Avg (001): ' + str(avg_001))
        print('==============SC101==============')
        if count_101 == 0:
            print('No score for SC101')
        else:
            print('Max (101): '+str(max_101))
            print('Min (101): '+str(min_101))
            print('Avg (101): ' + str(avg_101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
