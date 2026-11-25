import os
from pathlib import Path


LINE = 'fix: 04:04. Removed my null dereference. After four hours, my "cannot happen" comment has been demoted from system prompt to supporting evidence.'

assert 1 <= len(LINE) <= 195

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
