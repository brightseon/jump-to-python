from functools import reduce
import sys

print(reduce(lambda acc, cur: acc + cur, range(1, len(sys.argv)), 0))
