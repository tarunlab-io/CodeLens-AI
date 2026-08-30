import os
from google import genai
from google.genai import types
from utils.schemas import ExplanationResponse, ImprovementResponse, OptimizationResponse
from prompts.explain import EXPLAIN_PROMPT
from prompts.improve import IMPROVE_PROMPT
from prompts.optimize import OPTIMIZE_PROMPT

class LLMService:
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        if not self.api_key or self.api_key == "your_api_key_here":
            raise ValueError("API Key not found or is default. Please set GEMINI_API_KEY in the .env file.")
        
        # Initialize the GenAI client
        self.client = genai.Client(api_key=self.api_key)
        self.model_name = 'gemini-3.6-flash' # Using 3.6-flash as required by the 2026 API update
    
    def explain_code(self, code: str, language: str) -> ExplanationResponse:
        prompt = EXPLAIN_PROMPT.format(language=language, code=code)
        
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ExplanationResponse,
                temperature=0.2, # Low temperature for more factual explanations
            ),
        )
        # The genai SDK automatically parses to a pydantic model if response_schema is provided as one in config.
        # Wait, the latest google-genai SDK response.parsed contains the parsed object if schema was provided.
        # Let's ensure we return the parsed Pydantic object.
        if hasattr(response, 'parsed') and response.parsed:
             return response.parsed
        else:
             # Fallback if parsed isn't populated automatically, though it should be.
             return ExplanationResponse.model_validate_json(response.text)

    def improve_code(self, code: str, language: str) -> ImprovementResponse:
        prompt = IMPROVE_PROMPT.format(language=language, code=code)
        
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ImprovementResponse,
                temperature=0.3,
            ),
        )
        if hasattr(response, 'parsed') and response.parsed:
             return response.parsed
        return ImprovementResponse.model_validate_json(response.text)

    def optimize_code(self, code: str, language: str) -> OptimizationResponse:
        prompt = OPTIMIZE_PROMPT.format(language=language, code=code)
        
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=OptimizationResponse,
                temperature=0.2,
            ),
        )
        if hasattr(response, 'parsed') and response.parsed:
             return response.parsed
        return OptimizationResponse.model_validate_json(response.text)



