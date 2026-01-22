from fastapi import FastAPI
from _skill import create_marketplace
from pydantic import BaseModel


app = FastAPI()


class CreateMarketPlace(BaseModel):
    site_name: str
    site_description: str
    business_id: str


@app.post("/create_marketplace/")
async def read_root(request: CreateMarketPlace):
    status = create_marketplace(site_name=request.site_name, site_description=request.site_description, business_id=request.business_id)

    print(status)
    return status

