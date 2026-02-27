# AGENTS.md

## Development Rules

1. **One function per file**
   - Each standalone function must live in its own Python file.
   - Keep files small, focused, and single-purpose.

2. **Sensitive data must be git-ignored**
   - Never commit secrets or sensitive artifacts.
   - Examples: API keys, tokens, credentials, local env files, generated private datasets, and large downloaded outputs.
   - Ensure `.gitignore` is updated whenever new sensitive/generated paths are introduced.

3. **Keep this document up to date**
   - Update `AGENTS.md` whenever project structure, conventions, or workflow rules change.

4. **Reuse active runtime sessions**
   - Do not repeatedly establish a new notebook kernel or Python environment when one is already active and working.
   - Only restart or reconfigure the kernel/environment when there is a concrete execution/import failure that requires it.

5. **Strict typing and diagnostics are required**
   - Treat Pylance type warnings/errors as blockers for new or changed code.
   - Add explicit function return types and typed collections (avoid untyped `dict`/`list` in new logic).
   - Validate both runtime execution and static diagnostics before considering work complete.

## Project Architecture

```text
historicalStockDataDownload/
├── .gitignore
├── AGENTS.md
├── constants.py
├── main.ipynb
├── downloads/                  # legacy generated CSV outputs (git-ignored)
└── utils/
    ├── __init__.py
    ├── build_call_record.py
   ├── enforce_call_limit.py
   ├── get_max_available_share_price_data.py
   ├── print_header.py
    └── print_calls_made.py
```

## Notes

- `main.ipynb` is the main execution entry for this project.
- Utility logic is separated under `utils/` using the one-function-per-file convention.
- Current CSV exports are written to `/Users/kristopherpepper/Documents/jupyterProjects/historicalStockTrader/raw_data` via `OUTPUT_DIR` in `constants.py`.
