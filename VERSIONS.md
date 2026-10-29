# Versions

Resolved in `uv.lock` on 2026-10-29. The repository previously declared no dependencies or versions (the README suggested `pip install numpy matplotlib opencv-python pyserial` unpinned).

| Component | Version | Note |
|---|---|---|
| Python | 3.13 (`.python-version`) | `requires-python >=3.13`; course code was written for Python 3.6 (old bytecode was tracked) |
| numpy | 2.5.4 | |
| scipy | 1.18.1 | used by `collision_checker.py` |
| matplotlib | 3.11.2 | |
| opencv-python | 5.0.0.93 | |
| pyserial | 3.5 | |

Dev: pytest, ruff. Not installed: the CARLA simulator and its Python API (required by `spwaningcar.py` and the course projects).
