import time
import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from config import HF_API_KEY

    # List of models to try
MODELS = [
        "black-forest-labs/FLUX.1-schnell",
        "stabilityai/stable-diffusion-xl-base-1.0",
        "runwayml/stable-diffusion-v1-5",
        "CompVis/stable-diffusion-v1-4",
    ]

    # Request headers
HEADERS = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Accept": "image/png"
    }


def generate_image_from_text(prompt):
        payload = {
            "inputs": prompt
        }

        last_error = None

        for model in MODELS:

            print(f"\nTrying model: {model}")

            url = f"https://api-inference.huggingface.co/models/{model}"

            for attempt in range(3):

                try:
                    response = requests.post(
                        url,
                        headers=HEADERS,
                        json=payload,
                        timeout=120
                    )

                except requests.RequestException as e:
                    last_error = str(e)
                    continue

                content_type = response.headers.get("Content-Type", "").lower()

                if response.status_code == 503:
                    try:
                        estimated = response.json().get("estimated_time", 5)
                    except Exception:
                        estimated = 5

                    print(f"Model loading... Waiting {estimated} seconds.")
                    time.sleep(estimated + 1)
                    continue

                if response.status_code == 200 and "application/json" not in content_type:
                    try:
                        image = Image.open(BytesIO(response.content)).convert("RGB")
                        return image
                    except Exception as e:
                        last_error = f"Couldn't decode image: {e}"
                        break

                try:
                    error_message = response.json()
                except Exception:
                    error_message = response.text

                last_error = f"Status {response.status_code}: {error_message}"
                print(last_error)
                break

        raise Exception(last_error or "Image generation failed.")

def post_process_image(image):
        image = ImageEnhance.Brightness(image).enhance(1.2)
        image = ImageEnhance.Contrast(image).enhance(1.3)
        image = ImageEnhance.Sharpness(image).enhance(1.5)
        image = image.filter(ImageFilter.GaussianBlur(radius=1))
        return image


def main():
        print("=" * 70)
        print("AI Image Generator + Post Processing")
        print("=" * 70)

        while True:
            prompt = input("\nEnter image prompt (or type 'exit'): ").strip()

            if prompt.lower() == "exit":
                print("Goodbye!")
                break

            try:
                print("\nGenerating image...")
                image = generate_image_from_text(prompt)

                print("Applying post-processing...")
                processed = post_process_image(image)

                processed.show()

                save = input("\nSave image? (yes/no): ").strip().lower()

                if save == "yes":
                    filename = input("Enter filename: ").strip()

                    if filename == "":
                        filename = "generated_image"

                    processed.save(f"{filename}.png")
                    print(f"Saved as {filename}.png")

                print("\n" + "-" * 70)

            except Exception as e:
                print(f"\nError: {e}")

if __name__ == "__main__":
        main()