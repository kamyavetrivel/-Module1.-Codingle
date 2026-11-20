
from groq import generate_response
# from hf import generate_response

def run_activity():
    category = input("Enter a category (e.g., fruit, city, animal): ").strip()
    item = input(f"Enter a {category}: ").strip()

    print("\n--- ZERO-SHOT ---")
    zero_prompt = f"Is {item} a {category}? Answer yes or no."
    print(f"Prompt: {zero_prompt}")
    print("Response:", generate_response(zero_prompt, temperature=0.3, max_tokens=1024))

    print("\n--- ONE-SHOT ---")
    one_prompt = f"""Check if the item belongs to the category.

Example:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Now try:
Category: {category}
Item: {item}
Answer:"""
    print("Response:", generate_response(one_prompt, temperature=0.3, max_tokens=1024))

    print("\n--- FEW-SHOT ---")
    few_prompt = f"""Check if the item belongs to the category.

Example 1:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Example 2:
Category: fruit
Item: carrot
Answer: No, carrot is a vegetable.

Example 3:
Category: vehicle
Item: bicycle
Answer: Yes, bicycle is a vehicle.

Now try:
Category: {category}
Item: {item}
Answer:"""
    print("Response:", generate_response(few_prompt, temperature=0.3, max_tokens=1024))

    print("\n--- CREATIVE FEW-SHOT ---")
    creative_prompt = f"""Write a one-sentence story using the given word.

Example 1:
Word: moon
Story: The moon winked at the lovers as they shared their first kiss.

Example 2:
Word: computer
Story: The computer sighed as another cup of coffee was spilled on its keyboard.

Word: {item}
Story:"""
    print("Response:", generate_response(creative_prompt, temperature=0.7, max_tokens=1024))

    print("\n--- REFLECTION QUESTIONS ---")
    print("1. How were the responses different in each approach?")
    print("2. Which approach gave the most helpful or creative response?")
    print("3. How did the examples guide the AI's answer?")
    print("4. How can you use these techniques in your own tasks?")

if __name__ == "__main__":
    run_activity()
