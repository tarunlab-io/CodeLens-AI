IMPROVE_PROMPT = """
You are an expert programmer.
Your task is to improve the following {language} code while preserving its exact intended functionality.

Analyze the code for:
- Readability
- Naming conventions
- Maintainability
- Code structure
- Unnecessary repetition
- Obvious bugs or edge cases
- Language-specific best practices for {language}

Instructions:
- Do NOT make arbitrary changes that alter the intended behavior of the original program.
- Return the improved source code.
- Provide a concise explanation of what was improved and why.
- Provide a list of specific important changes made.

Here is the source code:
```
{code}
```
"""
