# Zary

**Zary - Your Command-Line Toolkit**

Zary is a lightweight command-line toolkit designed to make everyday tasks simple from the terminal.

The goal is simple:

> **If a normal person can say it, Zary should understand it.**

Zary currently provides a natural-language-friendly calculator and a JSON toolkit, with more utilities planned for future releases.

---

## Features

### Calculator

Perform everyday calculations directly from the command line.

```powershell
zary calc 20 + 30
```

```text
Result: 50
```

Percentage calculations:

```powershell
zary calc 20% of 500
zary calc 500 increased by 20%
zary calc 500 decreased by 20%
zary calc 1000 with 20% discount
```

Math functions:

```powershell
zary calc sqrt 144
zary calc cube root 27
zary calc abs -25
zary calc round 12.56
zary calc floor 12.9
zary calc ceil 12.1
```

Statistics:

```powershell
zary calc average of 10 20 30
zary calc minimum of 10 20 30
zary calc maximum of 10 20 30
```

---

## JSON Toolkit

Zary includes several JSON utilities.

### Format JSON

Format JSON with readable indentation:

```powershell
zary json format data.json
```

### Minify JSON

Remove unnecessary whitespace:

```powershell
zary json minify data.json
```

### Validate JSON

Check JSON syntax and receive detailed error information:

```powershell
zary json validate data.json
```

Validation can identify problems such as:

* Missing commas
* Missing colons
* Incorrect brackets
* Unclosed strings
* Invalid JSON values
* Single quotes
* Trailing commas
* Extra JSON data
* Empty files
* Duplicate object keys

### JSON Information

Analyze the structure of a JSON file:

```powershell
zary json info data.json
```

The information command can report:

* File size
* Root type
* Number of objects
* Number of arrays
* Number of strings
* Number of numbers
* Number of booleans
* Number of null values
* Number of object keys
* Maximum nesting depth

---

## Help

Show general help:

```powershell
zary --help
```

Calculator help:

```powershell
zary calc --help
```

JSON help:

```powershell
zary json --help
```

Individual JSON command help:

```powershell
zary json format --help
zary json minify --help
zary json validate --help
zary json info --help
```

---

## Version

Check the installed version:

```powershell
zary --version
```

Example:

```text
Zary v0.1.0
```

---

## Installation

Zary is distributed as a standalone Windows executable, so end users do not need to install Python.

After installation, you can use:

```powershell
zary
```

from PowerShell or Command Prompt.

The installer also creates a Zary shortcut that launches Zary through Windows PowerShell.

---

## Development Setup

### Requirements

For development and building Zary:

* Windows
* Python 3.14+
* PyInstaller 6.22.3
* Git

Clone the repository:

```powershell
git clone https://github.com/toolzary/zary.git
```

Enter the project:

```powershell
cd zary
```

Install the build dependency:

```powershell
python -m pip install -r requirements.txt
```

---

## Build

Zary includes a PowerShell build script.

Run:

```powershell
.\build.ps1
```

The script builds:

```text
dist\zary.exe
```

You can also build manually:

```powershell
python -m PyInstaller --onefile --name zary zary.py
```

---

## Project Structure

```text
zary/
│
├── assets/
│   ├── logo.ico
│   └── logo.svg
│
├── installer/
│   └── zary.iss
│
├── src/
│   ├── __init__.py
│   │
│   └── commands/
│       ├── __init__.py
│       ├── calc.py
│       ├── help.py
│       ├── version.py
│       │
│       └── json/
│           ├── __init__.py
│           ├── format.py
│           ├── info.py
│           ├── minify.py
│           └── validate.py
│
├── .gitignore
├── build.ps1
├── requirements.txt
├── zary.py
└── zary.spec
```

---

## Design Philosophy

Zary is being developed around a simple idea:

**Command-line tools should be powerful without being complicated.**

Instead of forcing users to remember complicated syntax, Zary aims to understand commands that resemble normal language.

For example:

```text
20% of 500
```

is more natural for many users than having to remember a specialized calculator syntax.

The same philosophy will guide future Zary commands.

---

## Roadmap

Planned areas include:

* More calculator operations
* Unit conversion
* More developer utilities
* More file utilities
* Improved command discovery
* Better error messages
* Additional JSON tools
* Configuration support
* AI-assisted commands
* More cross-platform support

The roadmap may change as Zary develops.

---

## Contributing

Contributions, suggestions, bug reports, and feature ideas are welcome.

If you find a problem or have an idea for Zary, open an issue or submit a pull request.

---

## License

License information will be added in a future release.

---

## Author

**Toolzary**

Zary is part of the Toolzary ecosystem of lightweight online and developer utilities.

---

**Zary - Your Command-Line Toolkit**
