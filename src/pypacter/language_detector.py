from langdetect import detect

def detect_language(code_snippet):
    """
    Detects the programming language of the code snippet.
    Args:
    The code snippet to analyze.
    Returns:
    The detected programming language.
    """
    try:
        language = detect(code_snippet)
        return language
    except:
        return "Not Known"