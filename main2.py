from openai import OpenAI
client = OpenAI()

response = client.response.create(
    modal = "gpt-4o",
    input = "What is the capital of France?",
)

print(response.output_text)