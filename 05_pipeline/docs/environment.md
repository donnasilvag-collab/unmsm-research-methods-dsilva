# Validated execution environment

This record describes the environment used for the repository checks on 9 August 2026. It is evidence of one successful local execution, not a claim that every compatible platform has been tested.

| Component | Validated value |
| --- | --- |
| Operating system | Microsoft Windows 11 Pro |
| Shell | Windows PowerShell |
| Python | 3.12.13 |
| Git | 2.54.0.windows.1 |
| DVC | 3.67.1 |
| MLflow | 3.1.4 |
| pandas | 2.3.3 |
| NumPy | 2.0.2 |
| Matplotlib | 3.10.8 |
| openpyxl | 3.1.5 |
| PyYAML | 6.0.3 |
| SciPy | 1.16.1 |
| statsmodels | 0.14.5 |
| Compute path | CPU only; no GPU is required |

The dependencies are pinned in [`../requirements.txt`](../requirements.txt). The GitHub Actions workflow also passed on Linux with Python 3.12, which checks that the documented commands are not limited to the local Windows path.

The local course workspace has a deeply nested path. Windows could not load a compiled statsmodels extension when the virtual environment was addressed through that full path, so the complete synthetic analysis was also executed through a temporary short-path junction. The junction changed only the access path, not the repository files, Python environment, parameters, or outputs. A short clone path avoids this operating-system limitation.

Docker remains unverified because no Docker engine was available in the local review environment. The repository therefore keeps the Docker item open rather than presenting the container as tested.

## Environment setup

Run from `05_pipeline/`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

No credential, API key, external database, or GPU is required to rebuild the committed public benchmark.
