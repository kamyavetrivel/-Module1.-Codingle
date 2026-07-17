from huggingface_hub import InferenceClient
from datetime  import datetime
from PIL import Image
from config import HF_API_KEY
MODELS =[ 
    "ByteDance/SDXL-Lighting",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwaym1/stable-diffusion-v1-5",
    ]
client= InferenceClient(api_key=HF_API_KEY)
print(f"primary model:{MODELS[0]}")
print("Type 'quit' to exit\n")
while True:
    prompt =input("Enter prompt: ").strip()
    if prompt.lower() in ["quit","exit","q"]:
        break
    if not prompt:
        continue 
    print("Generating....")
    Image= None 
    for model in MODELS:
        try:
            image=client.text_to_image(prompt,model=model)
            break
        except Exception:
            print(f" Executing next...")
            continue
    if Image:
        timestamp= datetime.now().strftime("%Y%m%d_%H%M%S")
        filename= f"generated_{timestamp}.png"
        image.save(filename)
        print(f" Saved: {filename}")
        image.show()
        print()
    else:
        print("Error: All models failes. Check your API key.\n")
    print("Goodbye!")


