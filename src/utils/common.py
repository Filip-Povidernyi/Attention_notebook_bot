"""
Common utility functions for the application.

This module provides helper functions that can be reused across different parts 
of the app.
"""

def print_help(commands: dict[str, str]):
    """Prints a formatted list of available commands and their descriptions."""
    # Find the longest command
    max_length = max(len(cmd) for cmd in commands)
    
    print('\nAvailable commands:')
    for cmd, desc in commands.items():
        # Align descriptions
        print(f"  <{cmd}>".ljust(max_length + 6) + f"- {desc}")