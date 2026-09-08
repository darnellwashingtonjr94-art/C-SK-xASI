import yaml
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.router import CrossBorderRouter

app = FastAPI(title="C-SK-xASI Cross-Border API", version="1.0.0")

# Load configuration
with open("config/models_config.yaml", "r") as f:
    config = yaml.safe_load(f)

router = CrossBorderRouter(config)

class QueryRequest(BaseModel):
    prompt: str

@app.post("/v1/orchestrate")
async def execute_pipeline(request: QueryRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    result = await router.orchestrate(request.prompt)
    return result
