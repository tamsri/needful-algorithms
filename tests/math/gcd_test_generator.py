import pandas as pd
import numpy as np
import math
FILE_PATH = 'gcd_test.csv'
TEST_N = 3000000
RANGE_N = 10000

def main():
    a_list = [int(a_num*RANGE_N) for a_num in np.random.rand(TEST_N)]
    b_list = [int(b_num*RANGE_N) for b_num in np.random.rand(TEST_N)]

    gcd_ans = []
    for a, b in zip(a_list, b_list):
        ans = math.gcd(a, b)
        gcd_ans.append(ans)
    data = {
            'a': a_list,
            'b': b_list,
            'c': gcd_ans
            }
    df = pd.DataFrame(data)
    df.to_csv('gcd.csv', index_label='id')

if __name__ == '__main__':
    main()
