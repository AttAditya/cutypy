import tomllib

from pathlib import Path

from cutypy.models.args import Args

from langex.core.functions import autosig

@autosig
def version_interference(args: Args) -> Args:
  if not args.version_check:
    return args

  pyproject = Path("pyproject.toml")

  with pyproject.open("rb") as f:
    data = tomllib.load(f)

  version = data["project"]["version"]
  print(version)

  return Args()

