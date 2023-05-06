import unittest
import pandas as pd

class TestMovingAverage(unittest.TestCase):
    
    def test_vol_moving_avg(self):
        # Create a sample DataFrame
        self.df = pd.DataFrame({
            'Symbol': ['AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL'],
            'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08'],
            'Adj Close': [100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0]
        })
        self.expected = pd.Series([pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, 125.0])

    def test_rolling_median(self):
        result = self.df.groupby('Symbol')['Adj Close'].rolling(window=3).median().reset_index(0, drop=True)
        self.assertTrue(self.expected.equals(result))

if __name__ == '__main__':
    unittest.main()
