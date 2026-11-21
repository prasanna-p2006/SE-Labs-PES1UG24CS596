# Static Code Analysis — Issue Table

**Project:** E-commerce Cart System  
**Lab:** Lab 5 — Static Code Analysis

| No. | Issue identified | Tool / type | Original location | Description | Fix applied |
|---:|---|---|---|---|---|
| 1 | Unsafe `eval()` usage | Bandit — Medium severity | `calculateDiscountedTotal()` | Evaluating a string as Python code can execute unintended expressions. | Replaced expression evaluation with a numeric discount rate validated to be between `0` and `1`. |
| 2 | Weak MD5 hash | Bandit — High severity | `generateItemHash()` | MD5 is not suitable for security-sensitive hashing. | Replaced MD5 with SHA-256 using `hashlib.sha256()`. |
| 3 | Predictable PIN generation | Bandit — Low severity | `generateCheckoutPin()` | The standard `random` generator is not intended for security-sensitive values. | Used `secrets.randbelow()` to generate a four-digit PIN. |
| 4 | Shell command execution | Bandit — High severity | `exportCartReceipt()` | `os.system()` can introduce command-injection risk when strings are combined. | Removed shell execution and printed the receipt confirmation with `print()`. |
| 5 | Hard-coded payment secret | Security review | `main()` | A credential-like value was embedded in source code and printed. | Removed the hard-coded secret and its print statement. |
| 6 | Mutable default argument | Pylint — Warning | `addItemToCart()` | A default list can be shared between function calls. | Changed the default to `None` and initialized a list inside the function. |
| 7 | Bare `except` block | Flake8 / Pylint / Bandit | `removeItemFromCart()` | Catching all exceptions can hide errors; an empty handler also suppresses failures. | Used `cart_items.pop(item_id, None)` to safely remove an item if present. |
| 8 | Global statement and naming convention | Pylint | Sales counter and `addItemToCart()` | Pylint flagged the global statement and nonconforming module-level name. | Replaced the global numeric variable with `sales_state = {"total_sales": 0.0}` and updated the value through the dictionary. |
| 9 | Missing docstrings and non-snake-case names | Pylint | Module and functions | The module and functions lacked documentation, and function names did not follow the expected naming style. | Added a module docstring and function docstrings; renamed functions using snake_case. |
| 10 | Unused imports and variables | Flake8 / Pylint | Multiple locations | Unused imports and assigned variables made the code less clear. | Removed unused imports and variables. |
| 11 | Incorrect `None` comparison and unnecessary branching | Flake8 / Pylint | `checkCartStatus()` | Compared a value to `None` with `==` and used a verbose conditional. | Used `is not None` and returned the boolean condition directly. |
| 12 | File handling and formatting issues | Flake8 / Pylint | `exportCartReceipt()` and file ending | The original code did not explicitly specify file encoding or use a context manager; it also had a long line and missing final newline. | Used `with open(..., encoding="utf-8")`, formatted lines, and ensured the file ends with a newline. |

## Verification results

For the final version tested, the reported results were:

- **Pylint:** `10.00/10`
- **Bandit:** `No issues identified`
- **Flake8:** no output, indicating no reported violations for the analyzed file.

These results apply to the version of `ecommerce_cart_system.py` used during the reported runs. Rerun the tools if the file changes.
