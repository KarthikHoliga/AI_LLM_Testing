import time
from typing import Dict, Any

class LLMAgent:
    def __init__(self, model_name: str = "gemini-1.5-flash", timeout: float = 2.0):
        self.model_name = model_name
        self.timeout = timeout

    def generate_response(self, prompt: str) -> Dict[str, Any]:
        start_time = time.time()
        
        # Guardrail: empty prompt check
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty")

        # Simulated response logic
        if "error" in prompt.lower():
            return {
                "status": "error",
                "message": "Model failed to process request.",
                "latency_sec": round(time.time() - start_time, 4),
            }

        # Simulated success response
        time.sleep(0.1) # Simulate network latency
        return {
            "status": "success",
            "model": self.model_name,
            "output": f"Processed response for: '{prompt}'",
            "tokens_used": len(prompt.split()) + 10,
            "latency_sec": round(time.time() - start_time, 4),
        }
