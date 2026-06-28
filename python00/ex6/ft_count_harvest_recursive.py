def ft_count_harvest_recursive():
    def helper(day):
        if (day > 1):
            helper(day - 1)
        print("Day",    day)
    day = int(input("Days until harvest: "))
    helper(day)
