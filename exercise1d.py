# Given the name list, use indexing to grab word “target”, the_list =
# [1,2,[3,4],[5,[100,200,['target']],23,11],1,7]


the_list = [
    1,
    2,
    [3, 4],
    [5, [100, 200, ['target']],
     23, 11],
    1,
    7]

valueToGrab = the_list[3][1][2][0]

print(valueToGrab)
