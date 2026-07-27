from huggingface_hub import InferenceClient
from datetime import datetime
from config import HF_API_KEY

client = InferenceClient(api_key=HF_API_KEY)

MODEL = "ByteDance/SDXL-Lightning"

print("Text-to-Image Payload Customization")
print("Type 'quit' to exit.\n")

while True:
    prompt = input("Enter prompt: ").strip()

    if prompt.lower() == "quit":
        break

    image = client.text_to_image(
        prompt,
        model=MODEL,
        parameters={
            "num_inference_steps": 20,
            "guidance_scale": 7.5
        }
    )

    filename = f"generated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

    image.save(filename)
    print("Saved:", filename)
    image.show()

print("GoodbyeEe")