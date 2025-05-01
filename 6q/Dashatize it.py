def dashatize(n):
    new_str = ''
    for i, num in enumerate(str(n)):
        if int(num) % 2 != 0:

            new_str += f'-{num}-'
        else:
            new_str += num

    result = new_str.replace("--", "-")
    return result.strip('-')



print(dashatize(274))  # ,"2-7-4", "Should return 2-7-4")
print(dashatize(5311))  # ,"5-3-1-1", "Should return 5-3-1-1")
print(dashatize(86320))  # ,"86-3-20", "Should return 86-3-20")
print(dashatize(974302))  # ,"9-7-4-3-02", "Should return 9-7-4-3-02")
