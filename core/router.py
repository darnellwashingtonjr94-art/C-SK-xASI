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
        # Work Level 1: Gather all info together (Parallel fan-out to AI Models 1–10)
        cn_results, sk_results = await asyncio.gather(
            self.cn_gateway.query_all(prompt),
            self.sk_gateway.query_all(prompt)
        )
        all_responses = cn_results + sk_results

        # Work Level 2: State accurate answer (Pivot translation & ensemble consensus)
        pivoted_outputs = []
        for res in all_responses:
            raw_text = str(res.get("data", ""))
            pivoted_text = await self.translator.pivot_to_target(raw_text, "ko")
            pivoted_outputs.append({
                "model": res.get("model"),
                "status": res.get("status"),
                "content": pivoted_text
            })

        # Synthesize model responses into a consolidated answer state
        valid_responses = [p["content"] for p in pivoted_outputs if p["status"] == "success"]
        synthesized_answer = "\n---\n".join(valid_responses) if valid_responses else "No valid model responses."

        # Work Level 3: Check answer (CN data compliance & SK cultural localization verification)
        compliance_checked = await self.cn_compliance.process_data({"data": synthesized_answer})
        final_verified_answer = await self.k_localization.process_data(compliance_checked)

        return {
            "status": "completed",
            "work_level_1_gathered_count": len(all_responses),
            "work_level_2_accurate_state": {
                "synthesized_answer": synthesized_answer,
                "individual_model_outputs": pivoted_outputs
            },
            "work_level_3_checked_answer": final_verified_answer
        }
