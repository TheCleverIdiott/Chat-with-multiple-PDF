import unittest
from unittest.mock import patch
from backend import comp_process

class TestCompProcess(unittest.TestCase):
    
    @patch('backend.external_api_call')  # Mocking the external API call
    def test_process_with_valid_inputs(self, mock_external_api_call):
        # Set up the mock to return a specific response
        mock_external_api_call.return_value = {"summary": "This is a sample summary of the PDF content."}

        apikey = "test-api-key"
        pdfs = ["sample.pdf"]
        question = "What is the content of the PDF?"

        result = comp_process(apikey, pdfs, question)

        # Assertions
        self.assertIsNotNone(result)
        self.assertIn("summary", result)
        self.assertEqual(result["summary"], "This is a sample summary of the PDF content.")

    def test_process_with_invalid_inputs(self):
        apikey = ""
        pdfs = []
        question = ""

        result = comp_process(apikey, pdfs, question)

        # Assertions
        self.assertIsNone(result)

    def test_process_with_missing_api_key(self):
        apikey = None
        pdfs = ["sample.pdf"]
        question = "What is the content of the PDF?"

        result = comp_process(apikey, pdfs, question)

        # Assertions
        self.assertIsNone(result)

    @patch('backend.external_api_call')  # Mocking the external API call
    def test_process_with_invalid_file_type(self, mock_external_api_call):
        mock_external_api_call.return_value = None  # Simulate failure due to invalid file type

        apikey = "test-api-key"
        pdfs = ["sample.txt"]  # Invalid file type
        question = "What is the content of the file?"

        result = comp_process(apikey, pdfs, question)

        # Assertions
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
