import logging
import sys

import click
import toml

from deplodocker.formatter import formatter
from deplodocker.loader import loader
from deplodocker.stainer import stainer

logger = logging.getLogger(__name__)


@click.command(help="Select lock file to work with or use stdin as source")
@click.argument("src", type=click.File("r"), default=sys.stdin)
@click.option("-d", "--dst", help="result file [default=stdout]", type=click.File("w"), default=sys.stdout)
@click.option("-i", "--input-format", help="format of input lock file [default=poetry]", type=str, default="poetry")
@click.option(
    "-o",
    "--output-format",
    help="format of output file [default=requirements.txt]",
    type=str,
    default="requirements.txt",
)
@click.option("-s", "--section", help="Section of lock file (multiple) [default=<all>]", multiple=True)
def main(src, dst, input_format, output_format, section):
    with src:
        try:
            data = toml.loads(src.read())
        except (toml.TomlDecodeError, TypeError, FileNotFoundError) as e:
            logger.error(e)
            exit(1)

    dst.write(formatter(stainer(loader(data, input_format), section), output_format))


if __name__ == "__main__":
    main()
