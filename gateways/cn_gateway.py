import asyncio
import httpx
from typing import Dict, Any, List

class CNGateway:
    def __init__(self, config: Dict[str, Any]):
        self.models = config.get("cn_models", [])

    async def _query_model(self, client: httpx.AsyncClient, model: Dict[str, Any], prompt: str) -> Dict[str, Any]:
        try:
            # Standardized payload wrapper for CN providers
            response = await client.post(
                model["endpoint"],
                json={"model": model["id"], "messages": [{"role": "user", "content": prompt}]},
                timeout=10.0
            )
            return {"model": model["id"], "status": "success", "data": response.json()}
        except Exception as e:
            return {"model": model["id"], "status": "error", "error": str(e)}

    async def query_all(self, prompt: str) -> List[Dict[str, Any]]:
        async with httpx.AsyncClient() as client:
            tasks = [self._query_model(client, model, prompt) for model in self.models]
            return await asyncio.gather(*tasks)
