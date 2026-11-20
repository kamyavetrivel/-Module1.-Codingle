
from groq import generate_response
# from hf import generate_response

import time

def temperature_prompt_activity():
    print("=" * 80)
    print("PROMPT ENGINEERING: TEMPERATURE AND INSTRUCTIONS")
    print("=" * 80)

    print("\n" + "-" * 40)
    print("PART 1: TEMPERATURE EXPLORATION")
    print("-" * 40)

    base_prompt = input("Enter a creative prompt: ").strip()

    print("\nGenerating responses using different temperatures...")

    print("\n--- LOW TEMPERATURE (0.1) ---")
    print(generate_response(base_prompt, temperature=0.1, max_tokens=512))
    time.sleep(1)

    print("\n--- MEDIUM TEMPERATURE (0.5) ---")
    print(generate_response(base_prompt, temperature=0.5, max_tokens=512))
    time.sleep(1)

    print("\n--- HIGH TEMPERATURE (0.9) ---")
    print(generate_response(base_prompt, temperature=0.9, max_tokens=512))
    time.sleep(1)

    print("\n" + "-" * 40)
    print("PART 2: INSTRUCTION-BASED PROMPTS")
    print("-" * 40)

    topic = input("Enter a topic: ").strip()

    instructions = [
        f"Summarize the main facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10-year-old child.",
        f"Write a pro and con list about {topic}.",
        f"Create a fictional news headline from 2050 about {topic}.",
    ]

    for i, instruction in enumerate(instructions, 1):
        print(f"\n--- INSTRUCTION {i}: {instruction} ---")
        print(generate_response(instruction, temperature=0.7, max_tokens=512))
        time.sleep(1)

    print("\n" + "-" * 40)
    print("PART 3: CREATE YOUR OWN PROMPT")
    print("-" * 40)

    custom_instruction = input("Enter your own prompt: ").strip()

    try:
        custom_temp = float(input("Enter a temperature (0.1 to 1.0): ").strip())

        if not (0.1 <= custom_temp <= 1.0):
            print("Invalid temperature. Using 0.7.")
            custom_temp = 0.7

    except ValueError:
        print("Invalid input. Using temperature 0.7.")
        custom_temp = 0.7

    print(f"\n--- YOUR PROMPT WITH TEMPERATURE {custom_temp} ---")
    print(generate_response(custom_instruction, temperature=custom_temp, max_tokens=512))

    print("\n" + "-" * 40)
    print("REFLECTION QUESTIONS")
    print("-" * 40)
    print("1. How did temperature affect creativity and variety?")
    print("2. Which instruction gave the most useful result?")
    print("3. How can you use temperature and instructions in real tasks?")
    print("4. What surprised you about the AI's responses?")

if __name__ == "__main__":
    temperature_prompt_activity()
