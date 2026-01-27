# Agent Instructions (python_learning)

## Source of truth
- All continuity and session guidance lives in `CodexUpdates/`.
- Always read `CodexUpdates/LEARNING_HISTORY.md`, `CodexUpdates/LEARNING_PLAN.md`, and `CodexUpdates/LEARNING_STATE.md` before resuming work or giving "next steps".

## Workflow rules
- Breadcrumb mode: the user writes all code; the assistant gives hints only.
- Each lesson should feel different; avoid repeating the same setup; use a new approach or structure each lesson.
- When asked "Where did we leave off" or "next steps", respond with a short recap of the last completed session, then the next steps.
- The first "next steps" request in a session uses the current Next step in `LEARNING_HISTORY.md`. Subsequent requests in the same session advance to the next logical step and update both history and plan.
- Update `LEARNING_HISTORY.md` and `LEARNING_PLAN.md` during the session as needed and at the end of each session without prompting.
- At logical checkpoints, prompt the user to update git (status/add/commit, and push if desired).
- Also surface git commands at random moments for practice (status/diff/add/commit/push).

## Current focus
- Phase 2 Lesson 5: tiny neural net (numpy).
