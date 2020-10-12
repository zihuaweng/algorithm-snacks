# https://leetcode.com/discuss/interview-question/861453/

def items(s, start_indices, end_indices):
    """

        0 1 2 3 4 5 6 7 8 9
        * * | * * * | * * *
    l  -1-1 2 2 2 2 6 6 6 6
    r   2 2 2 6 6 6 6 -1-1-1 
    s   1 2 2 3 4 5 5 6 7 8  
    """
    res = []
    
    n = len(s)
    left = [0] * n
    right = [0] * n
    stars = [0] * n

    prev_left = -1
    for i in range(n):
        if s[i] == '|':
            prev_left = i
        left[i] = prev_left

    prev_right = -1
    for i in range(n-1, -1, -1):
        if s[i] == '|':
            prev_right = i
        right[i] = prev_right

    star = 0
    for i in range(n):
        if s[i] == '*':
            star += 1
        stars[i] = star

    for start, end in zip(start_indices, end_indices):
        start -= 1
        end -= 1
        idx_stars_s = right[start]
        idx_stars_e = left[end]
        if idx_stars_e <= idx_stars_s:
            res.append(0)
            continue
        num_stars = stars[idx_stars_e] - stars[idx_stars_s]
        res.append(num_stars)

    return res 
    

print(items("|**|*|*", [1, 1], [5, 6]))     # [2,3]
print(items("*|*|", [1], [3]))              # [0]
print(items("*|*|*|", [1], [6]))            # [2]
print(items("*|**|***|", [1,2,4,1], [4,6,6,9])) # [0, 2, 0, 5]
         