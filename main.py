"""User-facing CLI interface. Using Google python-fire."""

import fire
from lib.calc import get_sum


def main():
    """CLI interface for library functions."""
    try:
        fire.Fire(get_sum)
    except (TypeError, ValueError) as e:
        print(f"Error: Please provide numeric arguments. {e}")


if __name__ == "__main__":
    main()
