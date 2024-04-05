"""
Base routes for the API.

The routes in this module serve a very basic purpose, such as health checks and
version information.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from pypacter_api import get_version
from langdetect import detect
from language_detection import detect_language


router = APIRouter()


@router.get("/health", tags=["health"])
async def health() -> JSONResponse:
    """
    Health check.

    Returns:
        A JSON response indicating the health of the API.
    """
    return JSONResponse(content={"status": "ok"})


@router.get("/version", tags=["version"])
async def version() -> JSONResponse:
    """
    Get the version of the API.

    Returns:
        A JSON response containing the version of the API.
    """
    return JSONResponse(content={"version": get_version()})

@router.post("/detect-language", tags=["Language"])
async def detect_language_api(code_snippet: str):
    """
    Endpoint to detect the language of a code snippet.
    Accepts a POST request with a JSON payload containing the code snippet.
    
    Args:
    The code snippet to analyze.

    Returns:
    A dictionary containing the detected language.
    """
    language = detect_language(code_snippet)
    return {"language": language}
