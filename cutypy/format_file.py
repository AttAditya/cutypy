from pathlib import Path

from cutypy.rules.format.mls_compact import compact, expand

from cutypy.rules.format.blank_lines import format_text as blank_lines
from cutypy.rules.format.double_blanks import format_text as double_blanks
from cutypy.rules.format.eof_newline import format_text as eof_newline
from cutypy.rules.format.import_sort import format_text as import_sort
from cutypy.rules.format.indentation import format_text as indentation
from cutypy.rules.format.line_endings import format_text as line_endings

from cutypy.rules.format.declaration_spacing import (
  format_text as declaration_spacing,
)

from cutypy.rules.format.leading_blank_lines import (
  format_text as leading_blank_lines,
)

from cutypy.rules.format.trailing_commas import (
  format_text as trailing_commas,
)

from cutypy.rules.format.trailing_spaces import (
  format_text as trailing_spaces,
)

def format_text(text: str) -> str:
  text, compactions = compact(text)
  text = blank_lines(text)
  text = line_endings(text)
  text = trailing_spaces(text)
  text = import_sort(text)
  text = indentation(text)
  text = leading_blank_lines(text)
  text = declaration_spacing(text)
  text = trailing_commas(text)
  text = double_blanks(text)
  text = eof_newline(text)
  text = expand(text, compactions)

  return text

def format_file(path: Path, check: bool = False) -> bool:
  original = path.read_text()
  formatted = format_text(original)

  if formatted == original:
    return False

  if check:
    print(f"{path} needs formatting")

    return True

  path.write_text(formatted)
  print(f"formatted {path}")

  return True

