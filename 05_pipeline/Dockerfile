FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD dvc repro \
    && python src/run_experiments.py \
    && python src/generate_synthetic_fieldwork.py \
    && python src/score_fieldwork.py --input fieldwork/synthetic/survey_responses_synthetic.csv --output-dir fieldwork/synthetic --synthetic \
    && python src/generate_synthetic_analysis.py \
    && python src/score_fieldwork.py --input fieldwork/synthetic/association_demo/survey_responses_analysis_synthetic.csv --output-dir fieldwork/synthetic/association_demo --synthetic \
    && python src/analyze_synthetic_fieldwork.py --synthetic
