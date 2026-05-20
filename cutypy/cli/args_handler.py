from os import getcwd

from sys import argv

from cutypy.models.args import Args

from langex.core.functions import autosig

class MODES:
  SOLVE = "solve"
  CHECK = "check"

@autosig
def get_cli_args(_: None) -> Args:
  args = Args()
  args.base_path = getcwd()
  recv = [*argv[1:]]
  mode = MODES.SOLVE

  if not recv:
    args.solve_paths.append(".")

  for arg in recv:
    if arg in ["-c", "--check"]:
      mode = MODES.CHECK
      continue

    if arg in ["-s", "--solve", "--"]:
      mode = MODES.SOLVE
      continue

    if mode == MODES.CHECK:
      args.check_paths.append(arg)
    else:
      args.solve_paths.append(arg)

  return args

