import requests
from PIL import Image, ImageEnhance
from io import BytesIO
from config import HF_API_KEY

MODEL = "runwayml/stable-diffusion-v1-5"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def generate_image(prompt):
    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    image = Image.open(BytesIO(response.content))
    return image

def post_process(image):
    image = ImageEnhance.Brightness(image).enhance(1.2)
    return image

def main():
    prompt = input("Enter image prompt: ")

    image = generate_image(prompt)
    image = post_process(image)

    image.show()

if __name__ == "__main__":
    main()