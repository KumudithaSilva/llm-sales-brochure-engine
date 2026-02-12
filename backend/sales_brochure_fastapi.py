from fastapi import FastAPI
from pydantic import BaseModel

from components.sales_brochure import SalesBrochure

app = FastAPI(title="LLM Sales Brochure API")

class URLRequest(BaseModel):
    base_url: str

@app.post("/fetch_links")
def get_links(data: URLRequest):
    sb = SalesBrochure()
    try:
        links = sb.fetch_links(data.base_url)
        return {"links": links}
    except Exception as e:
        return {"error": str(e), "links": []}
    
    # uvicorn sales_brochure_fastapi:app --reload