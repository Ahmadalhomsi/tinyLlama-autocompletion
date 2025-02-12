import ollama

word = "characteri"

response = ollama.chat(model="tinyllama", messages=[
    {"role": "system", "content": "Your task is to complete the missing Turkish words. Examples:\n"
                                  "Incomplete word: comput\n"
                                  "Completed word: computer\n"
                                  "Incomplete word: telepho\n"
                                  "Completed word: telephone\n"},
    {"role": "user", "content": f"Incomplete word: {word}\nCompleted word:"}
])

print(response['message']['content'])
