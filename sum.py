class InvalidArgumentsCount(Exception):
    pass


class InvalidArguments(Exception):
    pass


def my_sum(*nums):
    if len(nums) < 2:
        raise InvalidArgumentsCount("INVALID_ARGUMENTS_COUNT")
    if not (all([type(i) in [int, float] for i in nums])):
        raise InvalidArguments("INVALID_ARGUMENTS")
    res = 0
    for num in nums:
        res += num
    return res


try:
    print(my_sum(1))
except Exception as err:
    print(err)

try:
    print(my_sum(1, 2, "2"))
except Exception as err:
    print(err)

try:
    print(my_sum(3, 1, 2, 4, 1, -1.31))
except Exception as err:
    print(err)
