def show_help():

    print("""
Zary - Your Command-Line Toolkit

Usage:
  zary <command> [options]

Commands:

  calc
      Perform calculations.

  json
      Work with JSON files.

Options:

  --help
      Show help.

  --version
      Show version.

Examples:

  zary calc 20 + 30
  zary calc 20% of 500
  zary json format data.json
  zary json minify data.json
  zary json validate data.json
  zary json info data.json

Run:
  zary <command> --help

for detailed command help.
""")


# =========================================================
# CALCULATOR HELP
# =========================================================

def show_calc_help():

    print("""
Zary Calculator

Usage:
  zary calc <expression>

Operations:

  Basic arithmetic
      +   Addition
      -   Subtraction
      *   Multiplication
      /   Division
      %   Modulo
      ^   Power

  Percentages
      X% of Y
      X increased by Y%
      X decreased by Y%
      X + Y%
      X - Y%
      X with Y% discount

  Math functions
      sqrt X
      square root X
      cube root X
      cbrt X
      abs X
      round X
      floor X
      ceil X

  Statistics
      average of X Y Z
      minimum of X Y Z
      maximum of X Y Z

Examples:

  zary calc 20 + 30
  zary calc 20 * 30
  zary calc 20% of 500
  zary calc 500 increased by 20%
  zary calc 500 decreased by 20%
  zary calc 1000 with 20% discount
  zary calc sqrt 144
  zary calc cube root 27
  zary calc abs -25
  zary calc round 12.56
  zary calc average of 10 20 30
  zary calc minimum of 10 20 30
  zary calc maximum of 10 20 30

Options:

  --help
      Show calculator help.
""")


# =========================================================
# JSON MAIN HELP
# =========================================================

def show_json_help():

    print("""
Zary JSON Toolkit

Usage:
  zary json <action> <file>

Actions:

  format
      Format JSON with readable indentation.

  minify
      Remove unnecessary whitespace from JSON.

  validate
      Check JSON syntax and report detailed errors.

  info
      Show JSON structure and statistics.

Options:

  --help
      Show JSON help.

Examples:

  zary json format data.json
  zary json minify data.json
  zary json validate data.json
  zary json info data.json

Run:

  zary json <action> --help

for detailed action help.
""")


# =========================================================
# JSON FORMAT HELP
# =========================================================

def show_json_format_help():

    print("""
Zary JSON Format

Usage:
  zary json format <file>

Description:

  Format a JSON file using readable indentation.

Example:

  zary json format data.json

The formatted JSON is printed to the terminal.
""")


# =========================================================
# JSON MINIFY HELP
# =========================================================

def show_json_minify_help():

    print("""
Zary JSON Minify

Usage:
  zary json minify <file>

Description:

  Remove unnecessary whitespace from a JSON file
  while preserving its data.

Example:

  zary json minify data.json

The minified JSON is printed to the terminal.
""")


# =========================================================
# JSON VALIDATE HELP
# =========================================================

def show_json_validate_help():

    print("""
Zary JSON Validate

Usage:
  zary json validate <file>

Description:

  Check whether a JSON file is valid.

  Zary reports:

  - Syntax errors
  - Line and column numbers
  - Missing commas
  - Missing colons
  - Incorrect brackets
  - Unclosed strings
  - Invalid values
  - Duplicate keys
  - Other JSON structure problems

Examples:

  zary json validate data.json
  zary json validate config.json

Options:

  --help
      Show JSON validation help.
""")


# =========================================================
# JSON INFO HELP
# =========================================================

def show_json_info_help():

    print("""
Zary JSON Info

Usage:
  zary json info <file>

Description:

  Analyze a JSON file and display useful information.

  Zary can show:

  - File size
  - Root type
  - Number of objects
  - Number of arrays
  - Number of strings
  - Number of numbers
  - Number of booleans
  - Number of null values
  - Number of object keys
  - Maximum nesting depth

Example:

  zary json info data.json

Options:

  --help
      Show JSON information help.
""")