# Drill: Minimal Test Harness

Timebox: 20 minutes

## Task

Given one of the API drills, write just enough tests to drive the implementation.

Do not build a full framework. Pretend the interviewer has given you one file and asks you to show how you think about correctness.

## Suggested starting point

```python
import pytest


@pytest.mark.asyncio
async def test_happy_path():
    ...
```

## Requirements

- Mock HTTP responses instead of depending on a live API.
- Test one happy path.
- Test one error path.
- Test one edge case.
- Keep fixtures minimal.

## Follow-up prompts an interviewer might add

- How would you test retries without sleeping?
- How would you test pagination stopped at the right time?
- How would you test that secrets were not logged?
- Which tests would you skip in a 30-minute interview?

## Things to explain aloud

- What behavior is worth testing first.
- What you are intentionally not testing.
- Where you would add integration tests outside the interview.
