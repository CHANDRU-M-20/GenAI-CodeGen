from model import LLM

genai_model = LLM("gemini-1.5-pro")
print("LLM initialized successfully.")
llm = genai_model.get_llm()
response = llm.invoke("What is the capital of France?")
print(response.content)

