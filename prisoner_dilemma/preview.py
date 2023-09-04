"""Preview Functions."""


def preview_html(html: str) -> None:
    """HTML a preview of the output.

    On macOS, displayed via Quicklook, otherwise the output is written to a file.
    """
    import platform
    from pathlib import Path

    # write to file
    outfile = Path(".out.html")
    with outfile.open("w") as file:
        file.write(html)

    # on macOS: open
    if platform.system() == "Darwin":
        import os

        # tempfile does not work with `qlmanage` for some reason
        os.system(f"qlmanage -p '{outfile.name}' &>/dev/null")
        outfile.unlink()  # remove file
    else:
        print(f"Output created as '{outfile.name}'.")
