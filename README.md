# Test AI Coding Helpers

Would be interesting to compare commercial and FOSS tools on a known codebase.

## Setup at home

Cloud:
deepseek-v3.1:671b-cloud

Local, `Continue.dev`
nomic-embed-text:latest
qwen2.5-coder:14b
codellama:34b

To try:

- Qwen3 Coder (480B) (cloud available with ollama) for `Agent` and `Chat`, Qwen2.5-coder for `Autocomplete`.
- Different agents to compare how they work.

## Further integrations

Automate for dev/prod. Use up-to-date tools (e.g.`uv`, `ruff`), automated documentation generation, build and maitain release versions, integration with GitHub/smooth work with local resources.


## test_0

The script in `main.py` has 2 numerical arguments. In the project sub-directory, `lib` there will be implementation of the function in `calc.py` processing the arguments: `def get_sum(num1, num2)`:

- check whether the arguemtns are numeric (catch exception, print error message if any is)
- calculate sum of the arguments, print out: "Sum of {arg1} and {arg2} is {sum}"

The function get_sum() should be callable by outside code, to be used as a library later.

### Tests

Using Pytest, create unit tests for the function "get_sum()" described above.

### CI/CD

Create GitHub Actions workflow to:

- run tests on push and pull requests
- run `ruff` on committ

### Issues

Having a sub-directory, missing `pyproject.toml` for GitHub actions. Moving up. Other projects are separate tools, or wrapped in `main.py`.
Remove/Add `ruff` after migration.