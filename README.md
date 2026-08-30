# CodeLens AI

## Overview
CodeLens AI is a Generative AI–powered developer tool designed to analyze, explain, enhance, and optimize source code in clear, accessible language. It provides interactive insights into program logic, identifies potential improvements, and helps users understand algorithmic complexity, making it a practical solution for both aspiring developers and experienced professionals.

## Features
- **AI Code Explanation**: Breaks down complex code into simple, beginner-friendly concepts.
- **Time Complexity & Space Complexity**: Analyzes and prominently displays the Big-O notations with clear explanations.
- **Important Functions and Variables**: Identifies and describes the purpose of key structural elements in the code.
- **Multi-language Support**: Fully supports Python, C++, Java, and JavaScript.
- **Code Improvement**: Suggests readability, naming, and maintainability improvements while preserving intended functionality.
- **Code Optimization**: Identifies performance bottlenecks and suggests optimized implementations where meaningful.

## Tech Stack
- **Python**: Core backend logic.
- **Streamlit**: Interactive user interface.
- **Google Gemini API**: Powerful Large Language Model (via `google-genai`) for analysis and generation using structured outputs.

## Project Structure
- `app.py`: Main Streamlit application entry point and UI layout.
- `services/`: Contains `llm_service.py` to handle communication with the Google Gemini API.
- `prompts/`: Contains structured prompt files (`explain.py`, `improve.py`, `optimize.py`) for consistent AI responses.
- `utils/`: Contains `schemas.py` for Pydantic data models (structured output schemas) and `validators.py` for input validation.
- `examples/`: Contains `example_codes.py` with pre-defined code snippets for testing.

## Setup

1. **Clone the repository** (if applicable) or download the project files.
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

The application requires an API key to communicate with the LLM. 

1. Create a file named `.env` in the root directory.
2. Open the `.env.example` file and copy its contents into `.env`.
3. Replace `your_api_key_here` with your actual Google Gemini API key.

```
GEMINI_API_KEY=your_real_key_here
```

## Run

To start the application, run the following Streamlit command in your terminal:

```bash
streamlit run app.py
```

## How It Works
1. The user selects a programming language and pastes their code snippet into the UI.
2. The user clicks "Explain Code", "Improve Code", or "Optimize Code".
3. The Streamlit app validates the input and calls the `LLMService`.
4. `LLMService` utilizes specific prompts and Pydantic schemas to request structured JSON data from the Gemini API.
5. The Gemini API processes the code according to the language and prompt.
6. The application parses the structured response and dynamically displays it in visually separated UI components (cards, metrics, expanders).

## Usage
1. Open the application in your browser (usually `http://localhost:8501`).
2. Select your desired programming language from the dropdown menu.
3. Paste your code or use one of the provided examples.
4. Click the **Explain Code** button to get a beginner-friendly breakdown, including time/space complexity and key variables/functions.
5. (Optional) Click **Improve Code** to receive suggestions for better readability and maintainability.
6. (Optional) Click **Optimize Code** to see if the algorithm can be made more efficient in terms of time or space complexity.

