import json
import os


def run(filename):
    try:
        # -------------------------------------------------
        # FILE CHECK
        # -------------------------------------------------

        if not filename:
            print("Error: Please provide a JSON file.")
            print()
            print("Usage:")
            print("  zary json info data.json")
            return

        if not os.path.isfile(filename):
            print(f"Error: File not found: {filename}")
            return

        # -------------------------------------------------
        # FILE SIZE
        # -------------------------------------------------

        try:
            file_size = os.path.getsize(filename)
        except OSError as error:
            print(f"Error: Could not read file information: {error}")
            return

        # -------------------------------------------------
        # READ FILE
        # -------------------------------------------------

        try:
            text = read_file(filename)

        except UnicodeDecodeError:
            print("Error: File is not valid UTF-8 or supported Unicode encoding.")
            return

        except PermissionError:
            print(f"Error: Permission denied: {filename}")
            return

        except OSError as error:
            print(f"Error: Could not read file: {error}")
            return

        # -------------------------------------------------
        # EMPTY FILE
        # -------------------------------------------------

        if not text.strip():
            print("Error: The JSON file is empty.")
            return

        # -------------------------------------------------
        # PARSE JSON
        # -------------------------------------------------

        try:
            data = json.loads(text)

        except json.JSONDecodeError as error:
            print("Invalid JSON.")
            print(f"Line: {error.lineno}, Column: {error.colno}")
            print(f"Error: {error.msg}")
            return

        # -------------------------------------------------
        # ANALYZE
        # -------------------------------------------------

        stats = {
            "objects": 0,
            "arrays": 0,
            "strings": 0,
            "numbers": 0,
            "booleans": 0,
            "nulls": 0,
            "keys": 0,
            "max_depth": 0,
        }

        analyze_value(data, 1, stats)

        # -------------------------------------------------
        # ROOT TYPE
        # -------------------------------------------------

        root_type = get_type_name(data)

        # -------------------------------------------------
        # DISPLAY
        # -------------------------------------------------

        print()
        print("JSON Information")
        print("================")
        print()

        print(f"File: {filename}")
        print(f"Size: {format_size(file_size)}")
        print()

        print(f"Root type: {root_type}")
        print()

        print("Statistics")
        print("----------")

        print(f"Objects: {stats['objects']}")
        print(f"Arrays: {stats['arrays']}")
        print(f"Strings: {stats['strings']}")
        print(f"Numbers: {stats['numbers']}")
        print(f"Booleans: {stats['booleans']}")
        print(f"Nulls: {stats['nulls']}")
        print()

        print(f"Object keys: {stats['keys']}")
        print(f"Maximum depth: {stats['max_depth']}")

    except KeyboardInterrupt:
        print()
        print("Operation cancelled.")

    except Exception as error:
        print(f"Error: {error}")


# =========================================================
# FILE READER
# =========================================================

def read_file(filename):
    """
    Read JSON files using common Unicode encodings.

    Supported:
      - UTF-8
      - UTF-8 BOM
      - UTF-16 LE
      - UTF-16 BE
      - UTF-32 LE
      - UTF-32 BE
    """

    with open(filename, "rb") as file:
        raw = file.read()

    # UTF-8 BOM
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw[3:].decode("utf-8")

    # UTF-32 LE
    if raw.startswith(b"\xff\xfe\x00\x00"):
        return raw[4:].decode("utf-32-le")

    # UTF-32 BE
    if raw.startswith(b"\x00\x00\xfe\xff"):
        return raw[4:].decode("utf-32-be")

    # UTF-16 LE
    if raw.startswith(b"\xff\xfe"):
        return raw[2:].decode("utf-16-le")

    # UTF-16 BE
    if raw.startswith(b"\xfe\xff"):
        return raw[2:].decode("utf-16-be")

    # Standard UTF-8
    return raw.decode("utf-8")


# =========================================================
# RECURSIVE JSON ANALYZER
# =========================================================

def analyze_value(value, depth, stats):

    # Track maximum depth
    if depth > stats["max_depth"]:
        stats["max_depth"] = depth

    # -----------------------------------------------------
    # OBJECT
    # -----------------------------------------------------

    if isinstance(value, dict):

        stats["objects"] += 1
        stats["keys"] += len(value)

        for child in value.values():
            analyze_value(child, depth + 1, stats)

        return

    # -----------------------------------------------------
    # ARRAY
    # -----------------------------------------------------

    if isinstance(value, list):

        stats["arrays"] += 1

        for child in value:
            analyze_value(child, depth + 1, stats)

        return

    # -----------------------------------------------------
    # BOOLEAN
    # -----------------------------------------------------

    # bool must be checked before int because
    # Python considers bool a subclass of int.
    if isinstance(value, bool):

        stats["booleans"] += 1
        return

    # -----------------------------------------------------
    # STRING
    # -----------------------------------------------------

    if isinstance(value, str):

        stats["strings"] += 1
        return

    # -----------------------------------------------------
    # NUMBER
    # -----------------------------------------------------

    if isinstance(value, (int, float)):

        stats["numbers"] += 1
        return

    # -----------------------------------------------------
    # NULL
    # -----------------------------------------------------

    if value is None:

        stats["nulls"] += 1
        return


# =========================================================
# TYPE DETECTION
# =========================================================

def get_type_name(value):

    if isinstance(value, dict):
        return "Object"

    if isinstance(value, list):
        return "Array"

    if isinstance(value, bool):
        return "Boolean"

    if isinstance(value, str):
        return "String"

    if isinstance(value, (int, float)):
        return "Number"

    if value is None:
        return "Null"

    return "Unknown"


# =========================================================
# FILE SIZE FORMATTER
# =========================================================

def format_size(size):

    if size < 1024:
        return f"{size} bytes"

    if size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"

    if size < 1024 * 1024 * 1024:
        return f"{size / (1024 * 1024):.2f} MB"

    return f"{size / (1024 * 1024 * 1024):.2f} GB"