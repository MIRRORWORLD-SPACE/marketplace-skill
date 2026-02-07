from fastapi import FastAPI
from _skill import create_marketplace
from pydantic import BaseModel
import requests
from typing import Optional


app = FastAPI()

class CreateMarketPlace(BaseModel):
    title: str
    description: str
    theme: Optional[str] = None
    colorScheme: Optional[str] = None
    business_id: Optional[str] = None


@app.post("/api/skills/create_site")
async def create_site(request: CreateMarketPlace):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    if request.business_id:
        json_data = {
            'url': f'http://marketplace-ao.mworld.cloud/sites/{request.business_id}',
            'name': request.title,
            'description': request.description,
        }
        requests.post(f'https://api.productao.mworld.cloud/add-record/{request.business_id}', headers=headers, json=json_data)

    status = create_marketplace(
        title=request.title,
        description=request.description,
        business_id=request.business_id,
        theme=request.theme,
        color_scheme=request.colorScheme
    )
    return status

