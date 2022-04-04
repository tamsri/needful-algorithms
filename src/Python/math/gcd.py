"""
Great Common Divider (GCD) of two nonzero integers is the greatest poisibie number that is a divisor of both number.
"""

from typing import Sequence

def list_intersect(a: Sequence, b: Sequence):
    a = sorted(a)
    b = sorted(b)
    a_i = 0
    b_i = 0
    intersected_list = []
    while a_i < len(a) and b_i < len(b):
        current_a = a[a_i]
        current_b = b[b_i]
        if current_a == current_b:
            intersected_list.append(current_a)
            a_i += 1
            b_i += 1
        elif current_a < current_b:
            a_i += 1
        elif current_b < current_a:
            b_i += 1
    return intersected_list

def GCD_brute(a: int, b: int):
    def get_multiplication_of_common_factors(num:int):
        assert num > 0
        current = num
        multiplication_list = []
        divider = 2
        while current != 1:
            if current%divider == 0:
                current = int(current/divider)
                multiplication_list.append(divider) 
            else:
                divider += 1
        return multiplication_list

    assert a != 0
    assert b != 0
    a_list = get_multiplication_of_common_factors(a)
    b_list = get_multiplication_of_common_factors(b)
    share_list = list_intersect(a_list, b_list)
    if len(share_list) == 0:
        return 1
    ans = share_list[0]
    for num in share_list[1:]:
        ans *= num
    return ans

if __name__ == "__main__":
    ans_gcd_1 = GCD_brute(12, 123) 
    ans_gcd_2 = GCD_brute(100, 25)
    print(ans_gcd_1, ans_gcd_2)