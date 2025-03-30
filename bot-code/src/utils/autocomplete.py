import difflib


def suggest_command(cmd, commands, cutoff=0.8):

    closest_matches = difflib.get_close_matches(
        cmd, commands, n=1, cutoff=cutoff)

    if closest_matches:

        return closest_matches[0]

    return None
