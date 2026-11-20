
from groq import generate_response
# from hf import generate_response

def prompt_engineering_activity():
    print("Welcome to the AI Prompt Engineering Tutorial!")

    vague_prompt = input("Enter a vague prompt: ")
    print("\nAI's response to vague prompt:")
    print(generate_response(vague_prompt))

    specific_prompt = input("\nMake your prompt more specific: ")
    print("\nAI's response to specific prompt:")
    print(generate_response(specific_prompt))

    contextual_prompt = input("\nAdd context to your specific prompt: ")
    print("\nAI's response to contextual prompt:")
    print(generate_response(contextual_prompt))

    print("\n--- Reflection ---")
    print("1. How did the AI's response change when the prompt became more specific?")
    print("2. How did the AI's response improve when context was added?")
    print("3. Which prompt gave the most relevant response? Why?")

if __name__ == "__main__":
    prompt_engineering_activity()
