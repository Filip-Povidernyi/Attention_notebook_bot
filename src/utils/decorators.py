import sys
import atexit
from ..persistence.storage import save_data

def auto_save_on_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\n[INFO] Program interrupted by user. Saving data before exit...")
            if "book" in kwargs and "notes" in kwargs:
                save_data(kwargs["book"], kwargs["notes"])
            elif "book" in kwargs:
                save_data(kwargs["book"], None)
            elif "notes" in kwargs:
                save_data(None, kwargs["notes"])
            sys.exit(1)  
        except Exception as e:
            print(f"\n[ERROR] {e}\nSaving data before exit...")
            if "book" in kwargs and "notes" in kwargs:
                save_data(kwargs["book"], kwargs["notes"])
            elif "book" in kwargs:
                save_data(kwargs["book"], None)
            elif "notes" in kwargs:
                save_data(None, kwargs["notes"])
            sys.exit(1)  
    return wrapper