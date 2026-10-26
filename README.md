# smarttoy

smarttoy is an early-stage Python/FastAPI project for a planned research assistant. The current service exposes a greeting endpoint. Research, web search, report generation, and export are planned work.

## Current implementation

- `app/main.py` defines a FastAPI application with `GET /`.
- `models/models.py` defines Pydantic request and response models for the planned research API. These models are not connected to API routes yet.
- `clients/supabase_client.py` contains a minimal Supabase client wrapper. The greeting route does not use it.
- `tests/test_models.py` tests the Pydantic models.

## Planned work

The intended workflow is to generate search queries, gather and evaluate sources, synthesize a cited report, and export it. The research route, agent loop, integrations, and exports are not implemented yet. See the [roadmap](ROADMAP.md) and [GitHub issues](https://github.com/ashwinjohn3/smarttoy/issues) for the work ahead.

## Setup

Python 3.11 or newer is required by `pyproject.toml`. No API keys are needed to run the current greeting endpoint.

```bash
git clone https://github.com/ashwinjohn3/smarttoy.git
cd smarttoy
python3.11 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pip install uvicorn
python -m uvicorn app.main:app --reload
```

The service runs at `http://localhost:8000`, with interactive API documentation at `http://localhost:8000/docs`. `uvicorn` is installed separately because it is not listed in `requirements.txt`.

### API example

```bash
curl http://localhost:8000/
```

```json
{"message":"Hello, I am SmartToy!"}
```

There is currently no `POST /api/v1/research` endpoint.

### Tests

```bash
python -m pip install pytest
python -m pytest tests/ -v
```

`pytest` is in the `pyproject.toml` development dependency group, but not in `requirements.txt`. There is no configured coverage plugin or unit/integration test marker selection.

## Repository layout

```text
app/main.py                  FastAPI application and greeting route
models/models.py             Research request and response models
clients/supabase_client.py   Minimal Supabase client wrapper
tests/test_models.py         Model tests
agents/ and tools/           Package placeholders
pyproject.toml               Project metadata and dependencies
requirements.txt             Compiled runtime requirements
ROADMAP.md                   Submission tasks and planned work
```

## License

This project is licensed under the [MIT License](LICENSE).
