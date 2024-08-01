# codellamaAssistant
codellama:
A large language model that can use text prompts to generate and discuss code.

Example prompts

Ask questions
ollama run codellama:7b-instruct 'You are an expert programmer that writes simple, concise code and explanations. Write a python function to generate the nth fibonacci number.'
Fill-in-the-middle (FIM) or infill
ollama run codellama:7b-code '<PRE> def compute_gcd(x, y): <SUF>return result <MID>'
Fill-in-the-middle (FIM) is a special prompt format supported by the code completion model can complete code between two already written code blocks. Code Llama expects a specific format for infilling code:

<PRE> {prefix} <SUF>{suffix} <MID>
<PRE>, <SUF> and <MID> are special tokens that guide the model.

Code review
ollama run codellama '
Where is the bug in this code?

def fib(n):
    if n <= 0:
        return n
    else:
        return fib(n-1) + fib(n-2)
'
Writing tests
ollama run codellama "write a unit test for this function: $(cat example.py)"
Code completion
ollama run codellama:7b-code '# A simple python function to remove whitespace from a string:'