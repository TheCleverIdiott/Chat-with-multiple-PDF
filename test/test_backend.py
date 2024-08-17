import unittest
from backend import comp_process

class TestCompProcess(unittest.TestCase):
    def test_process_with_valid_inputs(self):
        # Example test case with mock inputs
        apikey = "test-api-key"
        pdfs = ["sample.pdf"]
        question = "What is the content of the PDF?"
        result = comp_process(apikey, pdfs, question)
        self.assertIsNotNone(result)
    
    def test_process_with_invalid_inputs(self):
        apikey = ""
        pdfs = []
        question = ""
        result = comp_process(apikey, pdfs, question)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
