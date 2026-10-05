# Multition AI

Technical scaffold cho AI service của Multition. Repo này chỉ thiết lập Python
3.12, FastAPI, Pydantic Settings, test, lint, type checking, Docker và CI. Chưa
có model, ranking, RAG, embeddings hoặc agent loop.

## Chạy local

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
uvicorn multition_ai.main:app --reload --port 8000
```

```bash
curl http://localhost:8000/health
```

## Kiểm tra

```bash
ruff check .
mypy src
pytest
```

Các capability AI sẽ được thiết kế sau. Khi triển khai, model provider cần nằm
sau interface riêng, output phải được validate và feature phải có evaluation
trước khi được bật trong production.
