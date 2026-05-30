.PHONY: test eval-fast eval-full lint clean coverage

test:
	pytest tests/ -v --tb=short

eval-fast:
	pytest tests/test_context_precision.py tests/test_rubrics.py -v

eval-full:
	pytest tests/ -v --tb=long -s

lint:
	ruff check src/ tests/
	mypy src/llmeval/

coverage:
	pytest --cov=src/llmeval --cov-report=xml
	coverage-badge -o coverage.svg -f

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -f coverage.xml .coverage
