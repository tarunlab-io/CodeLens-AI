from pydantic import BaseModel, Field
from typing import List, Optional

# --- Explain Schemas ---

class ComplexityInfo(BaseModel):
    complexity: str = Field(description="The Big-O notation, e.g., O(n), O(1)")
    explanation: str = Field(description="Beginner-friendly explanation of why it has this complexity")

class CodeElement(BaseModel):
    name: str = Field(description="Name of the function or variable")
    description: str = Field(description="Simple explanation of what it does")

class ExplanationResponse(BaseModel):
    summary: str = Field(description="A clear summary of what the code does")
    how_it_works: List[str] = Field(description="Step-by-step numbered explanation of how the code works")
    time_complexity: ComplexityInfo = Field(description="Time complexity analysis")
    space_complexity: ComplexityInfo = Field(description="Space complexity analysis")
    important_functions: List[CodeElement] = Field(description="List of important functions and their roles. Leave empty if none.")
    important_variables: List[CodeElement] = Field(description="List of important variables and their roles. Leave empty if none.")

# --- Improve Schemas ---

class ImprovementResponse(BaseModel):
    improved_code: str = Field(description="The refactored and improved source code in the same language")
    explanation: str = Field(description="A concise explanation of what was improved and why")
    changes: List[str] = Field(description="List of specific important changes made")

# --- Optimize Schemas ---

class OptimizationResponse(BaseModel):
    analysis: str = Field(description="Analysis of the current implementation and performance bottlenecks")
    original_time_complexity: str = Field(description="Time complexity of the original code")
    original_space_complexity: str = Field(description="Space complexity of the original code")
    optimized_time_complexity: str = Field(description="Time complexity of the optimized code, or same if no improvement possible")
    optimized_space_complexity: str = Field(description="Space complexity of the optimized code, or same if no improvement possible")
    optimized_code: Optional[str] = Field(description="The optimized source code. Null/empty if no meaningful optimization is possible")
    changes: List[str] = Field(description="List of specific optimizations made")
    no_optimization_possible: bool = Field(description="True if no meaningful optimization is possible, False otherwise")
