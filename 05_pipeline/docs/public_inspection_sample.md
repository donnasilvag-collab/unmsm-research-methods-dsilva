# Public inspection guide

The complete 48-record public benchmark is already included in the source workbook, so a reduced sample is not published as a separate dataset. A second extract could create ambiguity about which file is authoritative.

To inspect the first five records without changing the source, run from `05_pipeline/`:

```powershell
python -c "import pandas as pd; d=pd.read_csv('data/public_repo_security_benchmark.csv'); print(d[['record_id','stratum','repository_url']].head().to_string(index=False))"
```

Use the workbook sheets `LEEME`, `Diccionario`, `Metodologia`, `Trazabilidad`, and `Calidad` before interpreting a row. Public URLs support source inspection, not company ranking. The four composite variables are observability proxies and must not be treated as internal maturity assessments.
