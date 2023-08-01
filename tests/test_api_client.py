import unittest
from unittest.mock import patch
from utils import api_client

class TestAPIClient(unittest.TestCase):
    @patch('utils.api_client.requests.post')
    def test_api_request_with_retry(self, mock_post):
        # Mock successful API response
        response_json = {"data": "test"}
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = response_json

        url = "https://api.example.com/test"
        headers = {"Authorization": "Bearer TEST_API_KEY"}
        data = {"param": "value"}

        result = api_client.api_request_with_retry(url, headers=headers, data=data)

        mock_post.assert_called_once_with(url, headers=headers, data=data)
        self.assertEqual(result, response_json)

    @patch('utils.api_client.requests.post')
    def test_api_request_with_retry_retry_on_failure(self, mock_post):
        # Mock failed API response and successful retry
        response_json = {"data": "test"}
        mock_post.side_effect = [Exception(), Exception(), mock_post.return_value]
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = response_json

        url = "https://api.example.com/test"
        headers = {"Authorization": "Bearer TEST_API_KEY"}
        data = {"param": "value"}

        result = api_client.api_request_with_retry(url, headers=headers, data=data, max_retries=3)

        self.assertEqual(mock_post.call_count, 3)
        mock_post.assert_called_with(url, headers=headers, data=data)
        self.assertEqual(result, response_json)

if __name__ == '__main__':
    unittest.main()
