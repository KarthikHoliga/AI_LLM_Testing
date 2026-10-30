# Lab 02: Multi-Metric Evaluation with DeepEval

## Overview
Evaluated RAG outputs using multi-metric assertions (`GEval` for Faithfulness + `AnswerRelevancyMetric`).

## Metrics Summary
- **Faithfulness (`GEval`)**: Measures whether the `actual_output` is factually supported by the `retrieval_context`.
- **Answer Relevancy (`AnswerRelevancyMetric`)**: Measures how directly the `actual_output` addresses the original user `input`.

## Test Scenarios & Results
1. **Passing Case (`test_refund_answer_success`)**:
   - Both `Faithfulness` and `Answer Relevancy` met the `>= 0.7` score threshold.
2. **Failing Edge-Case (`test_refund_answer_irrelevant`)**:
   - `Answer Relevancy` dropped below `0.7` because the response drifted to shipping details.
   - `assert_test` caught the relevancy failure and generated structured reasoning logs.
