import json
import re


OPENING = {"{": "}", "[": "]"}
CLOSING = {"}": "{", "]": "["}


def run(filename):
    try:
        text = read_file(filename)

        # Empty/whitespace-only file
        if not text.strip():
            print("Invalid JSON.")
            print("Error: The file is empty.")
            return

        # Zary structural analysis
        structural_error = analyze_structure(text)

        if structural_error:
            print("Invalid JSON.")
            print(
                f"Line: {structural_error['line']}, "
                f"Column: {structural_error['column']}"
            )
            print(f"Error: {structural_error['message']}")

            if structural_error.get("detail"):
                print(structural_error["detail"])

            return

        # Python JSON parser performs final syntax validation
        try:
            data = json.loads(text)

        except json.JSONDecodeError as error:
            print("Invalid JSON.")
            print(f"Line: {error.lineno}, Column: {error.colno}")
            print(f"Error: {friendly_error(error, text)}")

            show_context(text, error.lineno)

            return

        # Duplicate keys â€” object-aware
        duplicates = find_duplicate_keys(text)

        print("Valid JSON.")

        if duplicates:
            print()
            print("Warning: Duplicate keys found:")

            for item in duplicates:
                print(
                    f'  "{item["key"]}" '
                    f'(line {item["line"]}, '
                    f'first used on line {item["first_line"]})'
                )

    except FileNotFoundError:
        print(f"Error: File not found: {filename}")

    except PermissionError:
        print(f"Error: Permission denied: {filename}")

    except UnicodeDecodeError:
        print("Invalid JSON.")
        print(
            "Error: File is not valid UTF-8 or supported Unicode encoding."
        )

    except OSError as error:
        print(f"Error: {error}")


# =========================================================
# FILE READER
# =========================================================

def read_file(filename):
    with open(filename, "rb") as file:
        raw = file.read()

    # UTF-8 BOM
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw[3:].decode("utf-8")

    # UTF-32 LE BOM
    if raw.startswith(b"\xff\xfe\x00\x00"):
        return raw[4:].decode("utf-32-le")

    # UTF-32 BE BOM
    if raw.startswith(b"\x00\x00\xfe\xff"):
        return raw[4:].decode("utf-32-be")

    # UTF-16 LE BOM
    if raw.startswith(b"\xff\xfe"):
        return raw[2:].decode("utf-16-le")

    # UTF-16 BE BOM
    if raw.startswith(b"\xfe\xff"):
        return raw[2:].decode("utf-16-be")

    # Standard UTF-8
    return raw.decode("utf-8")


# =========================================================
# STRUCTURE ANALYZER
# =========================================================

def analyze_structure(text):
    stack = []

    in_string = False
    escape = False

    line = 1
    column = 0

    for char in text:

        if char == "\n":
            line += 1
            column = 0
            continue

        column += 1

        # Inside JSON string
        if in_string:

            if escape:
                escape = False
                continue

            if char == "\\":
                escape = True
                continue

            if char == '"':
                in_string = False
                continue

            continue

        # Start of JSON string
        if char == '"':
            in_string = True
            continue

        # Single quotes are not valid JSON strings
        if char == "'":
            return {
                "line": line,
                "column": column,
                "message": "Single quotes are not allowed.",
                "detail": (
                    'JSON strings and property names must use double quotes (").'
                ),
            }

        # Opening brackets
        if char in OPENING:
            stack.append((char, line, column))
            continue

        # Closing brackets
        if char in CLOSING:

            if not stack:
                return {
                    "line": line,
                    "column": column,
                    "message": "Unexpected closing bracket.",
                    "detail": (
                        f"Found '{char}' but there is no matching "
                        "opening bracket."
                    ),
                }

            opening, open_line, open_column = stack[-1]
            expected = OPENING[opening]

            if char != expected:
                return {
                    "line": line,
                    "column": column,
                    "message": "Incorrect closing bracket.",
                    "detail": (
                        f"Found '{char}', but expected '{expected}'.\n"
                        f"The '{opening}' opened on line "
                        f"{open_line}, column {open_column}."
                    ),
                }

            stack.pop()

    # String was never closed
    if in_string:
        return {
            "line": line,
            "column": column,
            "message": "Unclosed string.",
            "detail": (
                'A string was started but never closed with a double quote (").'
            ),
        }

    # Bracket was never closed
    if stack:
        opening, open_line, open_column = stack[-1]
        expected = OPENING[opening]

        return {
            "line": line,
            "column": column + 1,
            "message": "Unclosed bracket.",
            "detail": (
                f"Expected '{expected}' to close the '{opening}' "
                f"opened on line {open_line}, column {open_column}."
            ),
        }

    return None


# =========================================================
# FRIENDLY ERROR ENGINE
# =========================================================

def friendly_error(error, text):

    message = error.msg.lower()
    line_text = get_line(text, error.lineno).strip()

    # Python 3.14 can report trailing commas using
    # "Illegal trailing comma before end of object/array"
    if "trailing comma" in message:
        return "Trailing comma is not allowed in JSON."

    if "illegal trailing comma" in message:
        return "Trailing comma is not allowed in JSON."

    # Missing comma
    if "expecting ',' delimiter" in message:

        if line_text.endswith(("]", "}")):
            return (
                "Possible missing comma or incorrect structure "
                "near this location."
            )

        return "Missing comma between JSON properties or values."

    # Missing colon
    if "expecting ':' delimiter" in message:
        return "Missing ':' after a JSON property name."

    # Invalid property name
    if "expecting property name enclosed in double quotes" in message:

        if line_text.endswith(","):
            return "Trailing comma is not allowed in JSON."

        if "'" in line_text:
            return "JSON property names must use double quotes."

        return (
            "Expected a JSON property name enclosed in double quotes."
        )

    # Invalid value
    if "expecting value" in message:

        if re.search(
            r":\s*(yes|no|none|undefined|nan|infinity|truee|falsee)\s*,?\s*$",
            line_text,
            re.IGNORECASE,
        ):
            return (
                "Invalid JSON value. Use true, false, null, "
                "a number, a string, object, or array."
            )

        if line_text.endswith(","):
            return "Trailing comma is not allowed in JSON."

        return "A valid JSON value was expected."

    # Extra content after valid JSON
    if "extra data" in message:
        return (
            "Extra data found after the end of the JSON document. "
            "A JSON file must contain exactly one complete JSON value."
        )

    # Invalid control character
    if "invalid control character" in message:
        return (
            "Invalid control character inside a JSON string. "
            "Check for an unescaped line break or special character."
        )

    # Unterminated string
    if "unterminated string" in message:
        return (
            "A string was started but was not properly closed."
        )

    # Invalid escape
    if "invalid \\escape" in message:
        return (
            "Invalid escape sequence inside a JSON string."
        )

    # Invalid Unicode escape
    if "invalid \\u" in message:
        return (
            "Invalid Unicode escape sequence. "
            "Use four hexadecimal digits after \\u."
        )

    return error.msg


# =========================================================
# DUPLICATE KEY DETECTOR
# =========================================================

def find_duplicate_keys(text):
    """
    Detect duplicate keys only inside the same JSON object.

    The same key in different objects is allowed.
    """

    duplicates = []

    object_stack = []

    in_string = False
    escape = False

    line = 1
    column = 0

    index = 0

    while index < len(text):

        char = text[index]

        if char == "\n":
            line += 1
            column = 0
            index += 1
            continue

        column += 1

        # Inside a string
        if in_string:

            if escape:
                escape = False

            elif char == "\\":
                escape = True

            elif char == '"':
                in_string = False

            index += 1
            continue

        # Start of string
        if char == '"':

            start_line = line

            end = index + 1
            escaped = False

            while end < len(text):

                current = text[end]

                if escaped:
                    escaped = False

                elif current == "\\":
                    escaped = True

                elif current == '"':
                    break

                end += 1

            key = text[index + 1:end]

            after = end + 1

            # Skip whitespace
            while after < len(text) and text[after].isspace():
                after += 1

            # If followed by ":" then this string is a property name
            if after < len(text) and text[after] == ":":

                if object_stack:

                    current_object = object_stack[-1]

                    if key in current_object:

                        duplicates.append({
                            "key": key,
                            "line": start_line,
                            "first_line": current_object[key],
                        })

                    else:
                        current_object[key] = start_line

            index = end + 1
            continue

        # Opening object
        if char == "{":
            object_stack.append({})
            index += 1
            continue

        # Closing object
        if char == "}":

            if object_stack:
                object_stack.pop()

            index += 1
            continue

        index += 1

    return duplicates


# =========================================================
# ERROR CONTEXT
# =========================================================

def show_context(text, line_number):

    lines = text.splitlines()

    if 1 <= line_number <= len(lines):

        print()
        print("Context:")

        start = max(1, line_number - 1)
        end = min(len(lines), line_number + 1)

        for number in range(start, end + 1):

            marker = ">" if number == line_number else " "

            print(
                f"{marker} {number:>4} | {lines[number - 1]}"
            )


# =========================================================
# UTILITIES
# =========================================================

def get_line(text, line_number):

    lines = text.splitlines()

    if 1 <= line_number <= len(lines):
        return lines[line_number - 1]

    return ""
