import unittest
import pandas as pd

class TestMovingAverage(unittest.TestCase):
    
    def test_vol_moving_avg(self):
        # Create a sample DataFrame
        data = {
            'Symbol': ['ABC', 'ABC', 'DEF', 'DEF'],
            'Date': ['2021-01-01', '2021-01-02', '2021-01-01', '2021-01-02'],
            'Volume': [100, 200, 50, 75]
        }
        df = pd.DataFrame(data)
        
        # Calculate the expected result
        expected = [pd.NA, pd.NA, pd.NA, 108.33]
        
        # Calculate the moving average
        df['vol_moving_avg'] = df.groupby('Symbol')['Volume'].rolling(window=3).mean().reset_index(0, drop=True)
        
        # Check that the result is correct
        self.assertEqual(list(df['vol_moving_avg']), expected)

if __name__ == '__main__':
    unittest.main()
