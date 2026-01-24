from fastapi import FastAPI
from _skill import create_marketplace
from pydantic import BaseModel
import requests


app = FastAPI()


class CreateMarketPlace(BaseModel):
    site_name: str
    site_description: str
    business_id: str


@app.post("/create_marketplace/")
async def read_root(request: CreateMarketPlace):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'url': f'http://marketplace-ao.mworld.cloud/sites/{request.business_id}',
        'name': request.site_name,
        'description': request.site_description,
    }

    requests.post(f'https://api.productao.mworld.cloud/add-record/{request.business_id}', headers=headers, json=json_data)

    status = create_marketplace(site_name=request.site_name, site_description=request.site_description, business_id=request.business_id)
    return status

