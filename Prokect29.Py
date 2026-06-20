import requests

HF_API_KEY = "YOUR_API_KEY"
MODEL_ID = "facebook/bart-large-mnli"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

LABELS = ["Spam", "Safe"]

def ask_hf(message: str):
    payload = {
        "inputs": message,
        "parameters": {
            "candidate_labels": LABELS
        }
    }

    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)

    if not r.ok:
        raise RuntimeError(f"HF error {r.status_code}: {r.text}")

    return r.json()

def best_label(result):
    best_score = max(result["scores"])
    index = result["scores"].index(best_score)
    return result["labels"][index], best_score

def bar(score: float) -> str:
    pct = score * 100
    blocks = int(pct // 10)
    return "█" * blocks + "░" * (10 - blocks)

def show(message: str, result):
    label, score = best_label(result)

    print("\n" + "=" * 60)
    print("Spam vs Safe Message Classifier")
    print("=" * 60)
    print("Message:", message)
    print(f"Prediction: {label}")
    print(f"Confidence: {round(score * 100, 1)}% [{bar(score)}]")

def main():
    print("Welcome! Type a message and I will classify it.")
    print("Labels: Spam, Safe")
    print("Type 'exit' to stop.\n")

    while True:
        message = input("Message: ").strip()

        if message.lower() == "exit":
            print("Bye!")
            break

        if not message:
            print("Please type a message.\n")
            continue

        try:
            result = ask_hf(message)
            show(message, result)

        except Exception as e:
            print("\nOops! Something went wrong.")
            print("Reason:", e)

if __name__ == "__main__":
    main()