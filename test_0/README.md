# Example CLI tool using module Fire

The script in `main.py` has 2 numerical arguments. In the project sub-directory, `lib` there will be implementation of the function in `calc.py` processing the arguments: `def get_sum(num1, num2)`:

- check whether the arguemtns are numeric (catch exception, print error message if any is)
- calculate sum of the arguments, print out: "Sum of {arg1} and {arg2} is {sum}"

The function get_sum() should be callable by outside code, to be used as a library later.

## Tests

Using Pytest, create unit tests for the function "get_sum()" described above.

## CI/CD

Create GitHub Actions workflow to:

- run tests on push and pull requests
- run `ruff` on committ
