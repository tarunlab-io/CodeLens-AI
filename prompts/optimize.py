OPTIMIZE_PROMPT = """
You are an expert algorithms and performance engineer.
Your task is to optimize the following {language} code if possible.

Optimization should focus on:
- Time complexity
- Space complexity
- Unnecessary computations
- Inefficient loops
- Redundant operations
- Inappropriate data structures
- Algorithmic improvements

Instructions:
1. Analyze the current implementation and identify any performance bottlenecks.
2. State the original time and space complexity.
3. If a meaningful optimization is possible, produce an optimized version of the code. If the code is already optimal and no meaningful optimization can be made, set the `no_optimization_possible` flag to true, and leave `optimized_code` empty. Do not claim an optimization unless it actually improves or meaningfully changes the implementation in terms of performance.
4. State the new time and space complexity.
5. List the specific optimizations made.

Analyze the code considering {language} specifics.

Here is the source code:
```
{code}
```
"""
