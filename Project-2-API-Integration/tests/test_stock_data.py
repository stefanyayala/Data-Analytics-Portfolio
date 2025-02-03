import unittest
from unittest.mock import patch, MagicMock
import os
import sys
from src.stock_data import StockData

# Add the src directory to the system path so we can import src modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestStockData(unittest.TestCase):

    def setUp(self):
        """Set up before each test"""
        # Sample values for the test
        self.api_key = "your_api_key"  # Replace with your actual API key
        self.stock_symbol = "your_stock_symbol"
        self.stock_data = StockData(self.stock_symbol, self.api_key)

    @patch('src.stock_data.requests.get')  # Mocking requests.get method
    def test_fetch_data(self, mock_get):
        """Test fetching stock data"""
        # Mock the API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "Time Series (Daily)": {
                "2025-01-01": {"1. open": "150", "2. high": "155", "3. low": "149", "4. close": "152", "5. volume": "1000000"}
            }
        }
        mock_get.return_value = mock_response

        data = self.stock_data.fetch_data()

        # Check that the data returned is not None and has the expected structure
        self.assertIsNotNone(data)
        self.assertIn("Time Series (Daily)", data)

    @patch('src.stock_data.requests.get')  # Mocking requests.get method
    def test_process_data(self, mock_get):
        """Test processing the fetched data"""
        # Mock the API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "Time Series (Daily)": {
                "2025-01-01": {"1. open": "150", "2. high": "155", "3. low": "149", "4. close": "152", "5. volume": "1000000"},
                "2025-01-02": {"1. open": "152", "2. high": "157", "3. low": "151", "4. close": "154", "5. volume": "1200000"}
            }
        }
        mock_get.return_value = mock_response

        # Fetch the data (mocked) and process it
        self.stock_data.fetch_data()  # Ensure we have raw data
        df = self.stock_data.process_data()

        # Assertions: Ensure the processed data is valid
        self.assertIsNotNone(df)
        self.assertEqual(df.shape[0], 2)  # Check if it has 2 rows (for two days in the mock)
        self.assertEqual(df.columns.tolist(), ['Open', 'High', 'Low', 'Close', 'Volume'])

    def tearDown(self):
        """Clean up after each test"""
        raw_file_path = f"../data/raw/{self.stock_symbol}.json"
        processed_file_path = f"../data/processed/{self.stock_symbol}.csv"
        if os.path.exists(raw_file_path):
            os.remove(raw_file_path)
        if os.path.exists(processed_file_path):
            os.remove(processed_file_path)

if __name__ == '__main__':
    unittest.main()
