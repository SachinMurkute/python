"""
Question:

Andrea and Maria each have an array of integers. Andrea want to change her array to match Maria's
for each elemnt of her array, she can increment or decrement one digit in one item in one move
How many moves will take Adrea to take Maria's array. NO reordering of digits is allowed.
For example, consider 2 arrays,
Andrea =[123,543]
Maria = [231,271]

For the first integer, Andrea can increment the 1 twice to achieve 3. The 2's are equal already. 
finally she decrement her 3 twice to equal 1. It took 4 moves to reach her goal. for the second integer,
she decrement 5 three times, increment 4 three times and 3 six times, it took 12 moves to convert the second array element
In total, it took 16 moves to convert both values comprising the complete array.

Function description:
Complete the function minimumMoves() in the editor below. The function must return the integer number of moves to convert Andreas array to match Maria's array.

minimumMoves function has the following paramerts:
a[a[0],...,a[n-1]]:     Andreas array of integers
m[m[0],...,m[n-1]]:     Maria array of integers

Constraints:
1 <= n <=10^5       
1<= a[i],m[i]<=10^9
The lenghts of a and m are equal, |a| =|m|
The elements a[i] and m[i] have an equal number of digits.

"""
def minimum_moves(list1, list2):
    """
    Returns Minimun moves required
    :param list1: list
    :param list2: list
    :return: int
    """
    moves = 0
    for i in range(0, len(list1)):  # type: int
        num1 = list1[i]  # type: int
        num2 = list2[i]
        while num1 != 0:
            digit1 = num1 % 10
            digit2 = num2 % 10
            num1 = num1 / 10
            num2 = num2 / 10
            moves += digit1 - digit2 if digit1 > digit2 else digit2 - digit1
    return moves


if __name__ == "__main__":
    A = [123, 436, 657]
    B = [999, 634, 657]
    min_moves = minimum_moves(A, B)
    print("Minimum Moves Requires: {}".format(min_moves))
