import pytest
from agent_sim import LLMAgent

# 1. Pytest Fixture: Initializes the agent instance cleanly before tests
@pytest.fixture
def agent():
    return LLMAgent(model_name="gemini-1.5-flash", timeout=2.0)

# 2. Test Success Flow & Schema Validation
def test_generate_response_schema(agent):
    response = agent.generate_response("Explain quantum computing in one sentence.")
    
    assert response["status"] == "success"
    assert response["model"] == "gemini-1.5-flash"
    assert isinstance(response["output"], str)
    assert response["tokens_used"] > 0
    assert response["latency_sec"] < agent.timeout

# 3. Test Error Scenario / Edge Case
def test_empty_prompt_raises_value_error(agent):
    with pytest.raises(ValueError, match="Prompt cannot be empty"):
        agent.generate_response("   ")

# 4. Parameterized Tests: Run multiple prompts through the same test function
@pytest.mark.parametrize("prompt, expected_token_min", [
    ("What is AI?", 10),
    ("Summarize the history of space exploration in detail", 15),
])
def test_token_usage_scaling(agent, prompt, expected_token_min):
    response = agent.generate_response(prompt)
    assert response["tokens_used"] >= expected_token_min
