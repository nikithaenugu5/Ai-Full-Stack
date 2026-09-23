import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"Give the answer in 2 lines only to explain a 5 years old baby."
        },
        {
            "role":"user",
            "content":"Define Ai"
        }
    ]
)
print(response["message"]["content"])