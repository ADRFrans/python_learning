# Learning Plan

A beginner-friendly path from Python foundations to building a small LLM, then on to APIs and agents. You do the coding; I review and guide unless you ask for code.

## How we'll use this plan

- You work through steps in order.
- After each milestone, we log progress in history.md.
- If something feels too fast or too slow, we adjust and update this plan.

## Pace guidelines

- Aim for 3 to 5 short sessions per week (30 to 60 minutes each).
- Focus on one topic at a time until it feels comfortable.
- Build tiny things early and often.

## Phase 1: Python Foundations (Complete)

Goal: build core Python fluency needed for LLM work.

Topics
- Variables, functions, lists/dicts, classes, control flow.
- File I/O, parsing, JSON.
- Modules/imports, basic error handling.

Checkpoints
- You can read/write files and parse data.
- You can structure code into functions and modules.

## Phase 2: Build a Small LLM from Scratch (Current)

Goal: understand how an LLM works by building a tiny model end-to-end.

Lessons (suggested sequence)
- Text data + tokenization (character-level).
- Bigram model (counts -> probabilities).
- Sampling text from probabilities.
- Simple neural model (optional, pure Python).
- Tiny neural net (numpy).
- Evaluate loss + overfitting basics.
- Save/load model parameters.
- Tiny transformer (PyTorch, optional).

Deliverables
- A char-level bigram model that can generate text.
- A tiny neural model that improves over bigram.
- A short write-up on what changes improved output.

## Phase 3: LLM APIs + RAG

Goal: build reliable apps using hosted LLMs.

Topics
- LLM API usage.
- Retries, rate limits, cost tracking.
- Embeddings + vector search (RAG).

Deliverables
- Q&A over a small set of local docs.
- A text-to-JSON extractor for structured data.

## Phase 4: Agent Basics

Goal: learn the agent loop and tool use.

Topics
- Agent loop: plan -> act -> observe -> refine -> finalize.
- Tool integrations: files, APIs, databases.
- Guardrails and human-in-the-loop checks.

Deliverables
- A small agent that can call tools and update its plan.

## Phase 5: Reliability + Evaluation

Goal: make agent systems reliable and testable.

Topics
- Evaluation datasets.
- Output validation.
- Failure handling and retries.
- Monitoring for latency, cost, quality.

Deliverables
- A prompt test suite.
- A reliability report with failure patterns.

## Phase 6: Capstone Agent Framework

Goal: build a reusable agent template.

Deliverable
- An agent runner that takes a goal, selects tools, executes, validates, and reports.

## Tools and Language

- Primary language: Python.
- Optional later: TypeScript for web integrations.

## Session continuity

- When you ask "Where did we leave off" or for "next steps", I will read both history.md and LearningPlan.md before answering.
- Response format: short recap of the last session completed, then next steps.
- I will update history.md and LearningPlan.md during the session (as needed) and at the end of each session without prompting.
- At logical checkpoints, I will prompt you to update your git repo (status/add/commit, and push if desired).
- I will also surface git commands at random moments for practice (status/diff/add/commit/push).
- Next step rule: The first time you ask for "next step(s)" in a session, I will follow the current Next step in history.md. If you ask again in the same session, I will advance to the next logical step and update both history.md and LearningPlan.md.
