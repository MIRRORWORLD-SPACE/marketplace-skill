
import os
import requests
import dotenv
dotenv.load_dotenv()


def create_marketplace(site_name:str, site_description: str, business_id: str):
    try:
        payload = {
            "title": site_name,
            "description": site_description,
            "business_id": business_id
        }

        headers = {"content-type": "application/json"}

        url = f"{os.environ.get('URL')}/api/skills/create_site"

        response = requests.post(url, json=payload, headers=headers)

        res = response.json()

        if response.ok:
            return {"success": True, "response": "Website will be generated shortly", "site_id": res['data']['site_id']}
    except Exception as e:
        print("Error generating image:", e)
        return {"success": False, "response": str(e)}
