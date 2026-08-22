from config import HF_API_KEY
import requests
import base64
import os
from PIL import Image

URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

VISION_MODEL = "meta-llama/Llama-3.2-11B-Vision-Instruct:sambanova"
TEXT_MODEL = "Qwen/Qwen2.5-7B-Instruct:together"


def image_url(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return "data:image/jpeg;base64," + data


def ask(model, messages, tokens=100):
    data = {
        "model": model,
        "messages": messages,
        "max_tokens": tokens,
        "temperature": 0.3
    }

    r = requests.post(URL, headers=HEADERS, json=data, timeout=120)

    if r.status_code != 200:
        return "Error: " + r.text

    return r.json()["choices"][0]["message"]["content"].strip()


def main():

    path = input("Enter image path: ").strip()

    if not os.path.exists(path):
        print("Image not found.")
        return

    try:
        Image.open(path).verify()
    except:
        print("Invalid image.")
        return

    # Basic caption
    caption = ask(
        VISION_MODEL,
        [{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Give a short caption for this image."
                },
                {
                    "type": "image_url",
                    "image_url": {"url": image_url(path)}
                }
            ]
        }]
    )

    print("\nBasic Caption:")
    print(caption)

    # Expand caption
    prompt = "Expand this image caption into a short description:\n" + caption

    description = ask(
        TEXT_MODEL,
        [{"role": "user", "content": prompt}],
        150
    )

    print("\nExpanded Description:")
    print(description)


if __name__ == "__main__":
    main()
