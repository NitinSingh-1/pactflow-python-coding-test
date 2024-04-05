import unittest
from pypacter.language_detection import detect_language

class TestLanguageDetection(unittest.TestCase):
    """
    Test case for the language detection function.
    """

    def test_detect_language_functionality(self):
        """
        Test the detect_language function with a simple code snippet.
        """
        # Creating a simple Python code snippet
        python_code_snippet = "print('Hello, world!')"
        
        # Calling the detect_language function for output
        detected_language = detect_language(python_code_snippet )
        
        # Printing the language detected
        print("Detected language:", detected_language)

if __name__ == "__main__":
    unittest.main()