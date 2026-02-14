from http.client import HTTPException

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from container.salesbrochure_container import SalesBrochureContainer

app = FastAPI(title="LLM Sales Brochure API")


class URLRequest(BaseModel):
    """
    Request model for providing a base URL.
    """

    base_url: str


@app.post("/generate_prompt")
def get_links(data: URLRequest):
    """
    Endpoint to generate a prompt and fetch relevant links for the given URL.

    Args:
        data (URLRequest): Contains the base_url to scrape.

    Returns:
        dict: Contains company brochure details.
    """
    try:
        orchestrator = SalesBrochureContainer.create_orchestrator(data.base_url)
        company_brochure = orchestrator.orchestrate(data.base_url)
        return {"company_brochure": company_brochure}

    except Exception as e:
        # Raise HTTPException to return proper HTTP status code (500)
        raise HTTPException(status_code=500, detail=f"Error fetching links: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(
        host="127.0.0.1", port=8000, app="sales_brochure_fastapi:app", reload=True
    )
