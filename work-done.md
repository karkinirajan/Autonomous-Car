# Work done: Autonomous-Car

Branch: `chore/modernize` (local, not pushed). Date: 2026-10-29.

## What was there
A collection of self-driving-car course work (Coursera): 4 course folders of notes, PDFs, quizzes, notebooks and assignment code (458 tracked files, 173 PDFs), plus root scripts (`Bicycle.py`, `kineticsBicycle.py`, `spwaningcar.py`, `motor.py`). No dependency file, no tests, no CI. Compiled Python 3.6 bytecode was tracked.

## Step 1: your uncommitted work, committed as-is
- `motor.py`: rewritten from a script that moved a motor on import into an importable module with `send_motor_command`, argparse CLI, bounds checks, and a zero-speed stop in `finally`.
- `README.md`: added Repository Layout and Local Experiments sections.
- `.vscode/settings.json`: interpreter path made workspace-relative.
- New `.gitignore`; removed tracked `__pycache__/*.pyc` files.

## Step 2: modernization changes by file
| File | Before | Change |
|---|---|---|
| `pyproject.toml`, `uv.lock`, `.python-version` | absent | New uv project, Python 3.13; numpy, scipy, matplotlib, opencv-python, pyserial; pytest/ruff config |
| `State_Estimation_.../Week_5/c2m5_assignment_files/rotations.py` | `skew_symmetric` crashed with "inhomogeneous shape" on the (3,1) vectors that `Quaternion.to_mat` passes it (NumPy >= 1.24), so `to_mat` and anything built on it could not run | `skew_symmetric` reshapes its input to (3,). One added line; all other course code untouched |
| `motor.py` | one over-long line, formatting | Wrapped/formatted by ruff; no behavior change |
| `tests/test_motor.py`, `test_priority_dict.py`, `test_rotations.py`, `test_cutils.py` | absent | New: 21 tests |
| `.github/workflows/ci.yml` | absent | New: uv sync, ruff, pytest |
| `README.md` | pip install line, no test docs | Replaced install with `uv sync`; added Testing section and TOC entry |
| `VERSIONS.md`, `work-done.md` | absent | New |

## Not changed, on purpose
- Course folders, notebooks, PDFs, and assignment code were not renamed, moved, or reformatted: notebooks use relative paths and the files are course-provided. The folder structure already follows the course/week curriculum.
- Ruff is scoped to `motor.py` and `tests/` (`[tool.ruff] include`); linting the course-supplied code would fail on style that is not ours to rewrite. This is a deliberate scope, not a lowered gate.

## Verification (actual runs)
- `uv run pytest -q`: 21 passed.
- `uv run ruff check .` and `ruff format --check .`: clean (within the scope above).
- Not run: notebooks, `spwaningcar.py` and `Codes/Course4FinalProject` (need CARLA and course data).

## Needs your attention
- Redistributing course PDFs/slides may be restricted by the course provider; check before keeping the repo public.
- Nothing pushed. To publish: `git push -u origin chore/modernize`
