from helper_functions.add_list import add_list
import unittest
import pandas as pd 
from pandas.util.testing import assert_frame_equal

df = pd.DataFrame(
    {"a":
    [1,2,3,4]
    }
    )
series = pd.Series([5,6,7,8])
name = "b"
expected = pd.DataFrame(
            {"a":
            [1,2,3,4],
            "b":
            [5,6,7,8]
            }
            )


class Test_Module_Func(unittest.TestCase):
    def test_add_list1(self):
        assert_frame_equal(expected, add_list(df,series,name))





if __name__ == '__main__':
    unittest.main()