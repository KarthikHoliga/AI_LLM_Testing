# Lab 01: Pytest Basics for LLM Applications

## Overview
Built unit and integration test coverage for an LLM API client wrapper using Pytest.

## Key Pytest Features Used
- **Fixtures (`@pytest.fixture`)**: Reusable setup logic for instantiating the LLM client across multiple tests.
- **Exception Assertions (`pytest.raises`)**: Validated boundary conditions and edge-cases (e.g., empty prompt inputs throwing `ValueError`).
- **Parameterized Testing (`@pytest.mark.parametrize`)**: Automated testing across multiple prompt lengths without duplicating test code.
- **Schema & Latency Assertions**: Verified structural payload fields (`status`, `tokens_used`) and response SLA thresholds (`latency_sec < timeout`).
