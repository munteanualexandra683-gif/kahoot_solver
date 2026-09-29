import os
import pyautogui
from google import genai
from PIL import Image

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE"))

MODELS = [
    "gemini-3.5-flash-lite",
    "gemini-3.8-flash",
    "gemini-3.7-flash",
]

def get_kahoot_answer(screenshot):
    last_error = None
    screenshot.thumbnail((800, 800))

    for model in MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=[
                    screenshot,
                    "CRITICAL: Output ONLY the exact text or color of the correct Kahoot answer. Do not write a single word of explanation. Zero context. Maximum 3 words."
                ],
            )
            return response.text.strip()

        except Exception as exc:
            last_error = exc
            print(f"[{model} busy, switching...]")

    raise RuntimeError(f"All models failed. Last error: {last_error}")

print("==========================================")
print("          KAHOOT HELPER SCRIPT            ")
print("==========================================")

while True:
    user_input = input("Press ENTER for answer (or 'q' to quit): ")

    if user_input.lower() == "q":
        break

    screenshot = pyautogui.screenshot()

    try:
        result = get_kahoot_answer(screenshot)
        print(f"\nANSWER: {result}\n")

    except Exception as exc:
        print(f"\nRequest failed: {exc}\n")
