"""Preview Functions."""

import os
import platform
from pathlib import Path


def preview_html(html: str) -> None:
    """HTML a preview of the output.

    On macOS, displayed via Quicklook, otherwise the output is written to a file.
    """
    # write to file
    outfile = Path(".out.html")
    with outfile.open("w") as file:  # pylint: disable=W1514
        file.write(html)

    # on macOS: open in quicklook
    if platform.system() == "Darwin":
        # tempfile does not work with `qlmanage` for some reason
        os.system(f"qlmanage -p '{outfile.name}' &>/dev/null")
        outfile.unlink()  # remove file
    # other OS: just point out the browser
    else:
        print(f"Output created as '{outfile.name}'.")
