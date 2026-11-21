# Lab 5 — Static Code Analysis Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program. It helps identify potential bugs, insecure coding patterns, maintainability problems, and style violations early in development. Fixing issues before deployment can make code safer, clearer, and easier to maintain.

## 2. What are the roles of Pylint, Bandit, and Flake8?

- **Pylint** checks code quality and common programming practices, including naming conventions, missing docstrings, unused variables, and other maintainability concerns.
- **Bandit** checks Python code for common security risks, such as unsafe evaluation, weak hashing, insecure random-number generation, and risky shell execution.
- **Flake8** checks Python style and formatting, including unused imports, whitespace, line length, and other PEP 8-related violations.

## 3. What issues were found in the original program?

The original e-commerce cart program had several issues. Bandit identified use of `eval()`, MD5 hashing, a predictable checkout PIN, and shell command execution. Pylint identified a mutable default list, missing docstrings, function naming issues, a global statement, and unused variables or imports. Flake8 reported a bare `except`, unused imports and variables, an incorrect comparison with `None`, a long line, and a missing final newline.

## 4. Which fixes were applied?

The unsafe `eval()` expression was replaced with a validated numeric discount rate. MD5 was replaced with SHA-256, checkout PIN generation was changed to use Python's `secrets` module, and shell execution was removed. The hard-coded payment secret was removed. The code was also updated to avoid a mutable default argument, handle item removal safely, use a context manager for receipt files, add docstrings, follow snake_case naming, remove unused code, and correct formatting.

## 5. What did you learn from the lab?

The lab showed that different static analysis tools identify different categories of problems. Bandit focused on security, Pylint highlighted code quality and maintainability, and Flake8 identified style issues. Running all three provided a more complete review than relying on only one tool. I also learned that a clean report should be verified by rerunning the tools after making changes.

## 6. What were the final results?

For the final version tested, Pylint reported a score of **10.00/10**, Bandit reported **no issues identified**, and Flake8 produced no output. These results indicate that the reported findings were resolved for the analyzed file.

## 7. How can static analysis be used in future projects?

Static analysis can be included in the development workflow and run before commits or as part of continuous integration. Running the tools regularly helps detect regressions early and encourages consistent coding and security practices.
