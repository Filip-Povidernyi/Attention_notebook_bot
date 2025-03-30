import sys
from rich.console import Console
from ..persistence.storage import save_data

console = Console()


def auto_save_on_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            console.print("\nExiting due to user interruption. Saving data before exit... Goodbye!",
                          style="steel_blue")
            if "book" in kwargs and "notes" in kwargs:
                save_data(kwargs["book"], kwargs["notes"])
            elif "book" in kwargs:
                save_data(kwargs["book"], None)
            elif "notes" in kwargs:
                save_data(None, kwargs["notes"])
            sys.exit(1)
        except Exception as e:
            console.print(
                f"\n[ERROR] {e}\nSaving data before exit...", style="steel_blue")
            if "book" in kwargs and "notes" in kwargs:
                save_data(kwargs["book"], kwargs["notes"])
            elif "book" in kwargs:
                save_data(kwargs["book"], None)
            elif "notes" in kwargs:
                save_data(None, kwargs["notes"])
            sys.exit(1)
    return wrapper
