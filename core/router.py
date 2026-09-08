import asyncio
from typing import Dict, Any, List
from gateways.cn_gateway import CNGateway
from gateways.sk_gateway import SKGateway
from core.translator import PivotTranslator
from data_pipeline.c_compliance import CNCompliancePipeline
from data_pipeline.k_localization import KLocalizationPipeline

class CrossBorderRouter:
    def __init__(self, config: Dict[str, Any]):
        self.cn_gateway = CNGateway(config)
        self.sk_gateway = SKGateway(config)
        self.translator = PivotTranslator()
        self.cn_compliance = CNCompliancePipeline()
        self.k_localization = KLocalizationPipeline()

    async def orchestrate(self, prompt: str) -> Dict[str, Any]:
        # Work Level 1: Fan-out prompt to all 10 Asian models simultaneously
        cn_results, sk_results = await asyncio.gather(
            self.cn_gateway.query_all(prompt),
            self.sk_gateway.query_all(prompt)
        )
        raw_responses = cn_results + sk_results

        # Work Level 2: State accurate answer / Pivot translation processing
        pivoted_responses = []
        for res in raw_responses:
            pivoted_res = await self.translator.pivot_to_target(str(res), "ko")
            pivoted_responses.append(pivoted_res)

        # Work Level 3: Check answer / Compliance & localization verification
        verified_cn = [await self.cn_compliance.process_data({"data": r}) for r in cn_results]
        verified_sk = [await self.k_localization.process_data({"data": r}) for r in sk_results]

        return {
            "status": "completed",
            "total_models_queried": len(raw_responses),
            "ensemble_outputs": {"cn_node": verified_cn, "sk_node": verified_sk}
        }
