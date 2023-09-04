"""Preview Functions."""

def preview_html(html: str) -> None:
    """HTML a preview of the output.

    On macOS, displayed via Quicklook, otherwise the output is written to a file.
    """
    import os
    import platform
    from pathlib import Path

    filename = ".out.html"
    with Path(filename).open("w") as file:
        file.write(html)


    if platform.system() == "Darwin":
        os.system(f"qlmanage -p '{filename}' &>/dev/null")
    else:
        print(f"Output created as '{filename}'.")
