########################################################################################
# SECTION: Imports
########################################################################################
# std
import logging
import sys
from argparse import ArgumentParser, Namespace
from datetime import datetime
from pathlib import Path

# 3rd
from PIL import Image

# local


########################################################################################
# SECTION: Functions
########################################################################################
def parse_cli() -> Namespace:
    stamp = datetime.now().isoformat(timespec="seconds").replace(":", "-")
    parser = ArgumentParser()
    parser.add_argument(
        "images", nargs="+", help="Paths to images to convert; glob expressions (**/*.png) are acceptable."
    )
    parser.add_argument(
        "-o", "--output", default=f"build/{stamp}", help="Directory where converted images will be written."
    )
    parser.add_argument(
        "-v", "--verbose", default=2, action="count", help="Verbosity of output, add -vvv for more text."
    )
    parser.add_argument("-W", "--width", default=300, help="Width of resized image in pixels.")
    parser.add_argument("-H", "--height", default=300, help="Height of resized image in pixels.")
    return parser.parse_args()


def setup_logger(verbosity: int):
    levels = [logging.CRITICAL, logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG]
    verbosity = max(verbosity, 0)
    verbosity = min(verbosity, len(levels) - 1)
    logging.basicConfig(stream=sys.stdout, format="%(message)s", level=levels[verbosity])


def main():
    # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize
    args = parse_cli()
    setup_logger(args.verbose)

    output = Path(args.output)
    output.unlink(missing_ok=True)
    output.mkdir(parents=True)
    images = (path.absolute() for expr in args.images for path in Path().glob(expr) if path.is_file())

    for image in images:
        logging.info(f"Converting: {image!r}")
        with Image.open(image) as img:
            resized = img.resize((args.width, args.height), Image.Resampling.BICUBIC)
            resized.save(output / image.name)


########################################################################################
# SECTION: EntryPoints
########################################################################################
if __name__ == "__main__":
    main()
