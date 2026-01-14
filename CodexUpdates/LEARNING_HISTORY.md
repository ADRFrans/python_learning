# Codex Learning History

## Session 2026-01-13
- Prompt: "I want an indepth learning plan for LLMs and AI agents." | Response: Provided phased plan and clarified meaning of agents.
- Prompt: "Where do we start? IDE?" | Response: Recommended VS Code, Python, and tooling setup.
- Prompt: "Create .md files to track progress + history." | Response: Created LEARNING_STATE.md and LEARNING_HISTORY.md.
- Prompt: "Add Learning Plan.md" | Response: Created LEARNING_PLAN.md with phased roadmap.
- Prompt: "Start first step" | Response: Guided Python install and venv setup.
- Result: Python 3.14.2 installed; venv activated; first script ran.
- Prompt: "I want to type all code; breadcrumb mode." | Response: Switched to hints-only guidance.

## Lesson 1 (Variables, collections, functions, main guard)
- Prompt: "print the steps for me again" | Response: Provided breadcrumb steps for Lesson 1.
- Prompt: "give me a hint for step 4" | Response: Explained how to define a function and return a value.
- Prompt: "what is the __name__ == \"__main__\"?" | Response: Explained main guard purpose.
- Prompt: "check out the file i just created" | Response: Found file; fixed f-string quoting guidance.
- Prompt: "snake case or camel case?" | Response: Recommended snake_case for vars/functions, CamelCase for classes.

## Lesson 2 (Control flow + loops)
- Prompt: "let's start the next lesson 2" | Response: Provided control flow + loops breadcrumbs.
- Prompt: "check out the src directory" | Response: Confirmed Lesson_2.py exists and reviewed code.
- Prompt: "why does the total_odd function not work?" | Response: Explained != vs ! and noted odds/even totals.
- Prompt: "am i good to move to the next lesson" | Response: Approved; noted minor cleanup options.

## Lesson 3 (Input, strings, validation)
- Prompt: "im ready" | Response: Provided input/validation breadcrumbs.
- Prompt: "check it out in src directory" | Response: Reviewed Lesson_3.py; suggested minor fix for negative age.

## Lesson 4 (Functions + file I/O)
- Prompt: "alright check out src" | Response: Reviewed Lesson_4.py; suggested saving to data/profile.txt and guarding file reads.

## Lesson 5 (Lists of dicts + aggregation + randomness)
- Prompt: "for this i want to create a random list generating function, what is the import for math" | Response: Explained imports for random and math.
- Prompt: "checkout lesson 5" | Response: Reviewed; noted skill list vs single skill, total skills counting, random.choice.
- Prompt: "hint on how to add more then one skill" | Response: Suggested random.sample or repeated random.choice.
- Prompt: "change only that portion and add a comment" | Response: Updated skills selection to multi-skill with comment.
- Prompt: "does sample pick a random amount of skills" | Response: Explained random k with randint.
- Prompt: "just do the random skills" | Response: Clarified options; updated to exactly 2 skills.
- Prompt: "checkout the entire file now" | Response: Confirmed updates and readiness to proceed.

## Lesson 6 (Modules + imports)
- Prompt: "How do I import from another file?" | Response: Explained from utils import syntax and file structure.
- Prompt: "re check" | Response: Found functions still in Lesson 6; advised moving to utils.
- Result: utils.py contains is_even/sum_evens; Lesson 6 imports and prints sum.

## Lesson 7 (File parsing + stats)
- Prompt: "Done check lesson_7" | Response: Suggested skipping blanks and computing stats.
- Result: Added count/sum/min/max/avg functions.

## Lesson 8 (Word frequency)
- Prompt: "not getting each word" | Response: Identified utils.py mixup and dictionary logic.
- Prompt: "hint for build_dictionary" | Response: Explained counting pattern.
- Result: Word counts working; moved list scope; text file contains sample sentences.

## Lesson 9 (Exceptions + input)
- Prompt: "need a hint for step 2" | Response: Provided while-true try/except pattern.
- Result: Input validation for two numbers; arithmetic outputs with divide-by-zero guard.

## Lesson 10 (Classes)
- Prompt: "constructor in python" | Response: Explained __init__.
- Result: Profile class with summary; created multiple instances.

## Lesson 11 (List of objects + filter)
- Prompt: "How do I work with the list and the objects inside?" | Response: Explained has_skill and loop.
- Result: Method name mismatch remains (has_skills vs has_skill).

## Lesson 12 (JSON save/load)
- Prompt: "Step 3 I have no idea" | Response: Gave json.dump example.
- Result: JSON saved to data/profiles.json and loaded back.

## Session wrap-up
- Prompt: "rename all the lesson files" | Response: Renamed to descriptive filenames.
- What was learned: modules/imports, file parsing, word frequency, exceptions, classes, JSON I/O.
- Next session: fix Lesson 11 method name; start Lesson 13 (HTTP requests).
