
import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Python API Client")
API_BASE_URL = os.getenv("API_BASE_URL")
DEMO_API_KEY = os.getenv("DEMO_API_KEY")


def get_post(post_id):
    if not API_BASE_URL:
        print("Error: API_BASE_URL is missing.")
        return

    if not DEMO_API_KEY:
        print("Error: DEMO_API_KEY is missing.")
        return

    url = f"{API_BASE_URL}/posts/{post_id}"

    # Demonstration only: JSONPlaceholder does not
    # require or validate this header.
    headers = {
        "X-Demo-Key": DEMO_API_KEY
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()
        post = response.json()

        print("\n--- Post Details ---")
        print("ID:", post["id"])
        print("Title:", post["title"])
        print("Body:", post["body"])

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)

    except ValueError:
        print("Error: Invalid JSON response.")


def main():
    print(f"=== {APP_NAME} ===")

    try:
        post_id = int(input("Enter a post ID (1-100): "))

        if not 1 <= post_id <= 100:
            print("Please enter a number from 1 to 100.")
            return

        get_post(post_id)

    except ValueError:
        print("Please enter a valid whole number.")


if __name__ == "__main__":
    main()
