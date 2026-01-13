# Codex Learning Plan

## Overview
This plan teaches Python fundamentals alongside practical LLM development, then builds toward agent systems you can apply to any future workflow.

## Phase 1: Python + LLM Foundations (Weeks 1-3)
Goal: refresh Python and understand how LLMs work at a practical level.
- Python refresh: variables, functions, lists/dicts, classes, file IO, virtual environments.
- LLM basics: tokens, context windows, transformer intuition, hallucinations.
- Prompting basics: instruction vs context, few-shot prompts, structured outputs.
Deliverables:
- A simple CLI script that sends a prompt and prints JSON output.
- A short note describing what causes hallucinations and how to reduce them.

## Phase 2: LLM APIs + RAG (Weeks 4-6)
Goal: build reliable apps using hosted LLMs.
- Use an LLM API (OpenAI/Anthropic/etc.).
- Learn retries, rate limits, and cost tracking.
- Embeddings + vector search for retrieval-augmented generation (RAG).
Deliverables:
- Q&A over a small set of local docs.
- A text-to-JSON extractor for structured data.

## Phase 3: Agent Basics (Weeks 7-9)
Goal: learn the agent loop and tool use.
- Agent loop: plan -> act (tools) -> observe -> refine -> finalize.
- Tool integrations: files, APIs, databases.
- Guardrails: validation, tool permissions, and human-in-the-loop checks.
Deliverables:
- A small agent that can call tools and update its plan.

## Phase 4: Reliability + Evaluation (Weeks 10-12)
Goal: make agent systems reliable and testable.
- Evaluation datasets (good/bad examples).
- Output validation with schemas.
- Failure handling and retries.
- Monitoring for latency, cost, quality.
Deliverables:
- A prompt test suite.
- A reliability report with failure patterns.

## Phase 5: Capstone Agent Framework (Weeks 13-16)
Goal: build a reusable agent template.
- An agent runner that takes a goal, selects tools, executes, validates, and reports.
Deliverable:
- A reusable agent starter template.

## Tools and Language
- Primary language: Python.
- Optional later: TypeScript for web integrations.

## Weekly cadence
- 2-3 short theory blocks.
- 1 hands-on build.
- 1 review/reflection session.

## First steps (Week 1)
- Install VS Code Python extension.
- Verify Python install.
- Create a project folder and virtual environment.
- Write and run a basic Python script.
