from src.commands.help import show_calc_help
import math
import re


def calculate(args):

    if not args or args[0].lower() in ("--help", "-h"):
        show_calc_help()
        return

    expression = " ".join(args).strip()

    try:
        result = process_expression(expression)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        print(f"Result: {result}")

    except Exception as error:
        print(f"Error: {error}")


# =========================================================
# EXPRESSION PROCESSOR
# =========================================================

def process_expression(expression):

    text = expression.lower().strip()

    # -----------------------------------------------------
    # Percentage: X% of Y
    # -----------------------------------------------------

    match = re.fullmatch(
        r"([-+]?\d*\.?\d+)%\s+of\s+([-+]?\d*\.?\d+)",
        text
    )

    if match:

        percent = float(match.group(1))
        number = float(match.group(2))

        return number * percent / 100

    # -----------------------------------------------------
    # Increased by percentage
    # -----------------------------------------------------

    match = re.fullmatch(
        r"([-+]?\d*\.?\d+)\s+increased\s+by\s+([-+]?\d*\.?\d+)%",
        text
    )

    if match:

        number = float(match.group(1))
        percent = float(match.group(2))

        return number * (1 + percent / 100)

    # -----------------------------------------------------
    # Decreased by percentage
    # -----------------------------------------------------

    match = re.fullmatch(
        r"([-+]?\d*\.?\d+)\s+decreased\s+by\s+([-+]?\d*\.?\d+)%",
        text
    )

    if match:

        number = float(match.group(1))
        percent = float(match.group(2))

        return number * (1 - percent / 100)

    # -----------------------------------------------------
    # Discount
    # -----------------------------------------------------

    match = re.fullmatch(
        r"([-+]?\d*\.?\d+)\s+with\s+([-+]?\d*\.?\d+)%\s+discount",
        text
    )

    if match:

        number = float(match.group(1))
        percent = float(match.group(2))

        return number * (1 - percent / 100)

    # -----------------------------------------------------
    # Percentage addition/subtraction
    # -----------------------------------------------------

    match = re.fullmatch(
        r"([-+]?\d*\.?\d+)\s*([+-])\s*([-+]?\d*\.?\d+)%",
        text
    )

    if match:

        number = float(match.group(1))
        operator = match.group(2)
        percent = float(match.group(3))

        change = number * percent / 100

        if operator == "+":
            return number + change

        return number - change

    # -----------------------------------------------------
    # Square root
    # -----------------------------------------------------

    match = re.fullmatch(
        r"(?:sqrt|square\s+root)\s+([-+]?\d*\.?\d+)",
        text
    )

    if match:

        number = float(match.group(1))

        if number < 0:
            raise ValueError(
                "Cannot calculate square root of a negative number."
            )

        return math.sqrt(number)

    # -----------------------------------------------------
    # Cube root
    # -----------------------------------------------------

    match = re.fullmatch(
        r"(?:cbrt|cube\s+root)\s+([-+]?\d*\.?\d+)",
        text
    )

    if match:

        number = float(match.group(1))

        return math.copysign(
            abs(number) ** (1 / 3),
            number
        )

    # -----------------------------------------------------
    # Absolute value
    # -----------------------------------------------------

    match = re.fullmatch(
        r"abs\s+([-+]?\d*\.?\d+)",
        text
    )

    if match:

        return abs(float(match.group(1)))

    # -----------------------------------------------------
    # Round
    # -----------------------------------------------------

    match = re.fullmatch(
        r"round\s+([-+]?\d*\.?\d+)",
        text
    )

    if match:

        return round(float(match.group(1)))

    # -----------------------------------------------------
    # Floor
    # -----------------------------------------------------

    match = re.fullmatch(
        r"floor\s+([-+]?\d*\.?\d+)",
        text
    )

    if match:

        return math.floor(float(match.group(1)))

    # -----------------------------------------------------
    # Ceiling
    # -----------------------------------------------------

    match = re.fullmatch(
        r"ceil\s+([-+]?\d*\.?\d+)",
        text
    )

    if match:

        return math.ceil(float(match.group(1)))

    # -----------------------------------------------------
    # Average
    # -----------------------------------------------------

    match = re.fullmatch(
        r"average\s+of\s+(.+)",
        text
    )

    if match:

        numbers = parse_numbers(match.group(1))

        if not numbers:
            raise ValueError("Please provide numbers.")

        return sum(numbers) / len(numbers)

    # -----------------------------------------------------
    # Minimum
    # -----------------------------------------------------

    match = re.fullmatch(
        r"(?:minimum|min)\s+of\s+(.+)",
        text
    )

    if match:

        numbers = parse_numbers(match.group(1))

        if not numbers:
            raise ValueError("Please provide numbers.")

        return min(numbers)

    # -----------------------------------------------------
    # Maximum
    # -----------------------------------------------------

    match = re.fullmatch(
        r"(?:maximum|max)\s+of\s+(.+)",
        text
    )

    if match:

        numbers = parse_numbers(match.group(1))

        if not numbers:
            raise ValueError("Please provide numbers.")

        return max(numbers)

    # -----------------------------------------------------
    # Normal math expression
    # -----------------------------------------------------

    return evaluate_math(text)


# =========================================================
# NUMBER PARSER
# =========================================================

def parse_numbers(text):

    values = re.findall(
        r"[-+]?\d*\.?\d+",
        text
    )

    return [
        float(value)
        for value in values
    ]


# =========================================================
# MATH EVALUATOR
# =========================================================

def evaluate_math(expression):

    expression = expression.replace("^", "**")

    # Allow only numbers and basic math operators.

    if not re.fullmatch(
        r"[0-9+\-*/().%\s]+|\*\*",
        expression
    ):

        raise ValueError(
            "Invalid mathematical expression."
        )

    try:

        return eval(
            expression,
            {
                "__builtins__": None
            },
            {}
        )

    except ZeroDivisionError:

        raise ValueError(
            "Cannot divide by zero."
        )

    except Exception:

        raise ValueError(
            "Invalid mathematical expression."
        )