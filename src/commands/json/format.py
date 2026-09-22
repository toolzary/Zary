import json
import os


def run(file_path):
    """Format a JSON file with readable indentation."""

    if not file_path:
        print("Error: Please provide a JSON file path.")
        return

    file_path = file_path.strip()

    # Remove surrounding quotes
    if len(file_path) >= 2:
        if (
            (file_path[0] == '"' and file_path[-1] == '"')
            or
            (file_path[0] == "'" and file_path[-1] == "'")
        ):
            file_path = file_path[1:-1]

    file_path = os.path.abspath(os.path.expanduser(file_path))

    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    if not os.path.isfile(file_path):
        print(f"Error: Path is not a file: {file_path}")
        return

    try:
        # Read raw bytes
        with open(file_path, "rb") as file:
            raw_data = file.read()

        # Decode based on BOM
        if raw_data.startswith(b"\xef\xbb\xbf"):
            text = raw_data[3:].decode("utf-8")

        elif raw_data.startswith(b"\xff\xfe\x00\x00"):
            text = raw_data[4:].decode("utf-32-le")

        elif raw_data.startswith(b"\x00\x00\xfe\xff"):
            text = raw_data[4:].decode("utf-32-be")

        elif raw_data.startswith(b"\xff\xfe"):
            text = raw_data[2:].decode("utf-16-le")

        elif raw_data.startswith(b"\xfe\xff"):
            text = raw_data[2:].decode("utf-16-be")

        else:
            text = raw_data.decode("utf-8")

        data = json.loads(text)

        print(
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False
            )
        )

    except json.JSONDecodeError as error:
        print("Error: Invalid JSON.")
        print(f"Line: {error.lineno}, Column: {error.colno}")
        print(f"Message: {error.msg}")

    except UnicodeDecodeError:
        print("Error: File encoding is not supported.")

    except PermissionError:
        print(f"Error: Permission denied: {file_path}")

    except OSError as error:
        print(f"Error: Could not read file: {error}")

    except Exception as error:
        print(f"Error: {error}")