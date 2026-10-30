import os
from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams

faithfulness_metric = GEval(
    name="Faithfulness",
    criteria="Determine if the actual output aligns with the retrieval context.",
    evaluation_params=[
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.RETRIEVAL_CONTEXT,
    ],
    model="gemini-1.5-flash",
)

def test_refund_answer():
    test_case = LLMTestCase(
        input="What is your refund policy?",
        actual_output="We offer a 30-day full refund for all purchase orders.",
        retrieval_context=["Our refund policy guarantees a full refund within 30 days of purchase."],
    )
    assert_test(test_case, [faithfulness_metric])
