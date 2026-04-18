def compact(text: str):
  compactions = {}
  compaction_id = 0
  cmp_text = ""
  i = 0
  n = len(text)
  is_compacting = False
  quote = ""
  triple = False
  cmp_temp = ""

  while i < n:
    c = text[i]

    if not is_compacting:
      if c in ("'", '"'):
        if i + 2 < n and text[i] == text[i+1] == text[i+2]:
          quote = c
          triple = True
          is_compacting = True
          cmp_temp = c * 3
          i += 3
          continue
        else:
          quote = c
          triple = False
          is_compacting = True
          cmp_temp = c
          i += 1
          continue
      else:
        cmp_text += c
        i += 1
        continue
    else:
      cmp_temp += c

      if triple:
        if i + 2 < n and text[i] == text[i+1] == text[i+2] == quote:
          cmp_temp += quote * 2
          i += 3
          compaction_id += 1
          key = f"__STR_{compaction_id}__"
          compactions[key] = cmp_temp
          cmp_text += key
          is_compacting = False
          cmp_temp = ""
          continue
        else:
          i += 1
          continue
      else:
        if c == '\\' and i + 1 < n:
          cmp_temp += text[i+1]
          i += 2
          continue

        if c == quote:
          compaction_id += 1
          key = f"__STR_{compaction_id}__"
          compactions[key] = cmp_temp
          cmp_text += key
          is_compacting = False
          cmp_temp = ""
          i += 1
          continue

        i += 1

  return cmp_text, compactions

def expand(text: str, compactions: dict):
  for k, v in compactions.items():
    text = text.replace(k, v)

  return text

