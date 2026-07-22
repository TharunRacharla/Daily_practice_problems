"""This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
 implement a function rand5() that returns an integer from 1 to 5 (inclusive)."""
import random
def ran7():
    return  random.randint(1, 7)

def ran5():
    num = ran7()
    if num in range(1, 6):
        return num
    else:
        return ran5()

print(ran5())

