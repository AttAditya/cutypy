import sys

from importlib.metadata import version, PackageNotFoundError

from cutypy.discover import discover
from cutypy.format_file import format_file

def get_version():
  try:
    return version("cutypy")

  except PackageNotFoundError:

    return "0.0.0"

def main():
  args: list[str] = sys.argv[1:]
  check_mode = False
  target = "."

  if args:
    if args[0] in ("--version", "-v"):
      print(get_version())
      return

    if args[0] == "--check":
      check_mode = True

      if len(args) > 1:
        target = args[1]

    else:
      target = args[0]

  needs_format = False

  for path in discover(target):
    changed = format_file(path, check=check_mode)

    if changed:
      needs_format = True

  if check_mode and needs_format:
    raise SystemExit(1)

if __name__ == "__main__":
  main()

