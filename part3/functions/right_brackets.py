def bracket_check(test_string):
    left = 0
    right = 0
    count = 0
    n = len(test_string)

    for i in range(n):
        if test_string[i] == "(":
            left += 1
        elif test_string[i] == ")":
            right += 1
        if left < right:
            print("NO")
            count = 1
            break
    if count == 0:
        if right == left:
            print("YES")
        else:
            print("NO")