import sys

from src.commands.help import (
    show_help,
    show_calc_help,
    show_json_help,
    show_json_format_help,
    show_json_minify_help,
    show_json_validate_help,
    show_json_info_help
)

from src.commands.version import show_version
from src.commands.calc import calculate

from src.commands.json.format import run as format_json
from src.commands.json.minify import run as minify_json
from src.commands.json.validate import run as validate_json
from src.commands.json.info import run as info_json


def main():

    args = sys.argv[1:]

    # =====================================================
    # NO COMMAND
    # =====================================================

    if not args:
        show_help()
        return

    command = args[0].lower()
    command_args = args[1:]

    # =====================================================
    # GLOBAL OPTIONS
    # =====================================================

    if command in ("--help", "-h"):
        show_help()
        return

    if command in ("--version", "-v"):
        show_version()
        return

    # =====================================================
    # CALCULATOR
    # =====================================================

    if command == "calc":

        if not command_args:
            show_calc_help()
            return

        if command_args[0].lower() in ("--help", "-h"):
            show_calc_help()
            return

        calculate(command_args)
        return

    # =====================================================
    # JSON
    # =====================================================

    if command == "json":

        # zary json
        if not command_args:
            show_json_help()
            return

        json_action = command_args[0].lower()
        json_args = command_args[1:]

        # zary json --help
        if json_action in ("--help", "-h"):
            show_json_help()
            return

        # -------------------------------------------------
        # JSON FORMAT
        # -------------------------------------------------

        if json_action == "format":

            if not json_args:
                show_json_format_help()
                return

            if json_args[0].lower() in ("--help", "-h"):
                show_json_format_help()
                return

            json_file = " ".join(json_args)

            format_json(json_file)
            return

        # -------------------------------------------------
        # JSON MINIFY
        # -------------------------------------------------

        if json_action == "minify":

            if not json_args:
                show_json_minify_help()
                return

            if json_args[0].lower() in ("--help", "-h"):
                show_json_minify_help()
                return

            json_file = " ".join(json_args)

            minify_json(json_file)
            return

        # -------------------------------------------------
        # JSON VALIDATE
        # -------------------------------------------------

        if json_action == "validate":

            if not json_args:
                show_json_validate_help()
                return

            if json_args[0].lower() in ("--help", "-h"):
                show_json_validate_help()
                return

            json_file = " ".join(json_args)

            validate_json(json_file)
            return

        # -------------------------------------------------
        # JSON INFO
        # -------------------------------------------------

        if json_action == "info":

            if not json_args:
                show_json_info_help()
                return

            if json_args[0].lower() in ("--help", "-h"):
                show_json_info_help()
                return

            json_file = " ".join(json_args)

            info_json(json_file)
            return

        # -------------------------------------------------
        # UNKNOWN JSON ACTION
        # -------------------------------------------------

        print(f"Unknown JSON action: {json_action}")
        print('Run "zary json --help" for help.')
        return

    # =====================================================
    # UNKNOWN COMMAND
    # =====================================================

    print(f"Unknown command: {command}")
    print('Run "zary --help" for help.')


if __name__ == "__main__":
    main()