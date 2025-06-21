def query_ai(prompt, history):
    # Demo: Bisa diintegrasikan ke OpenAI/Gemini/LLM lokal
    # Untuk sekarang, balas echo markdown
    code_example = "```python\nprint('Hello, world!')\n```"
    return f"**Prompt diterima:**\n\n{prompt}\n\n---\nContoh kode Python:\n{code_example}\n\n*Integrasi AI asli bisa ditambahkan di sini*"