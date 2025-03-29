from model import LLM

genai_model = LLM()
print("LLM initialized successfully.")
response = genai_model.llm.invoke("What is the capital of France?")
print(response)

