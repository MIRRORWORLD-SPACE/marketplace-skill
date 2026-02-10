
import os
import requests
import dotenv
dotenv.load_dotenv()


THEME_COLOR_SCHEMES = {
    "modern": '["#000000", "#ffffff", "#f4f4f5"]',
    "elegant": '["#1a1a1a", "#fdfcf9", "#e5e7eb"]',
    "techy": '["#0f172a", "#3b82f6", "#1e293b"]',
    "playful": '["#f43f5e", "#fef2f2", "#fb7185"]',
}


def create_marketplace(title: str, description: str, business_id: str = None, theme: str = None, color_scheme: str = None):
    try:
        # Gets the pre-defined colour scheme from theme if colour is not present
        if theme and not color_scheme:
            color_scheme = THEME_COLOR_SCHEMES.get(theme)

        payload = {
            "title": title,
            "description": description,
            "business_id": business_id,
            "theme": theme,
            "colorScheme": color_scheme
        }

        headers = {"content-type": "application/json"}

        url = f"{os.environ.get('MARKETPLACE_URL')}/api/skills/create_site"

        response = requests.post(url, json=payload, headers=headers)

        if not response.ok:
            print(f"Error: Server returned {response.status_code}")
            print("Response text:", response.text)
            return {"success": False, "response": f"Server error: {response.status_code}"}

        try:
            res = response.json()
        except Exception as e:
            print("Error parsing JSON response:", e)
            print("Response text:", response.text)
            return {"success": False, "response": "Invalid response from server"}

        return {"success": True, "response": "Website will be generated shortly", "site_id": res.get('data', {}).get('site_id')}
    except Exception as e:
        print("Error generating site:", e)
        return {"success": False, "response": str(e)}
