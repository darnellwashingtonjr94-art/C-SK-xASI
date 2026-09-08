import pytest
from core.router import CrossBorderRouter

@pytest.fixture
def sample_config():
    return {
        "cn_models": [{"id": "qwen-max", "endpoint": "https://httpbin.org/post"}],
        "sk_models": [{"id": "solar-pro", "endpoint": "https://httpbin.org/post"}]
    }

@pytest.mark.asyncio
async def test_cross_border_router_3level_pipeline(sample_config):
    router = CrossBorderRouter(sample_config)
    result = await router.orchestrate("Test cross-border prompt")
    
    assert result["status"] == "completed"
    assert result["work_level_1_gathered_count"] == 2
    assert "synthesized_answer" in result["work_level_2_accurate_state"]
    assert result["work_level_3_checked_answer"]["k_localized"] is True
