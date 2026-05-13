# LLMEval - Comprehensive LLM Evaluation Framework

A Python-based testing framework for evaluating Large Language Model (LLM) responses and Retrieval-Augmented Generation (RAG) systems. Built on top of the [RAGAS](https://docs.ragas.io/) framework, this project provides a suite of metrics to assess the quality, relevance, and accuracy of LLM outputs.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Available Metrics](#available-metrics)
- [Running Tests](#running-tests)
- [Configuration](#configuration)
- [Test Data](#test-data)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Overview

LLMEval provides a comprehensive testing suite for evaluating LLM and RAG system performance. It integrates with multiple evaluation metrics to measure:

- **Context Precision**: How well retrieved contexts match the query
- **Context Recall**: How comprehensively contexts answer the questions
- **Faithfulness**: Whether responses are grounded in provided contexts
- **Response Relevance**: How relevant responses are to user queries
- **Topic Adherence**: How well multi-turn conversations stay on topic
- **Rubrics-based Scoring**: Custom 1-5 scale evaluation

The framework leverages Anthropic's Claude models via the RAGAS library for intelligent evaluation.

## Features

✅ **Multiple Evaluation Metrics** - Context precision, recall, faithfulness, relevance, and more
✅ **RAG System Testing** - Complete RAG pipeline evaluation
✅ **Parametrized Tests** - Run same test with multiple datasets
✅ **Async Support** - Efficient async test execution
✅ **Custom Scoring** - Rubrics-based evaluation with customizable criteria
✅ **Data-Driven** - JSON-based test data for easy management
✅ **Production-Ready** - Comprehensive error handling and timeouts
✅ **Industry-Standard Structure** - Following Python best practices

## Prerequisites

Before you begin, ensure you have the following:

1. **Python 3.9+** - [Download Python](https://www.python.org/downloads/)
2. **Anthropic API Key** - Required for Claude model access
   - Sign up at [Anthropic Console](https://console.anthropic.com)
   - Copy your API key from the dashboard
3. **Internet Connection** - For API calls and model inference

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/LLMEval.git
cd LLMEval
```

### 2. Create Virtual Environment

```bash
# Using Python 3.11 (recommended)
python3.11 -m venv .venv311

# Activate virtual environment
source .venv311/bin/activate  # On macOS/Linux
# or
.venv311\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# .env
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_MODEL=claude-sonnet-4-6  # Optional, defaults to claude-sonnet-4-6
```

Or export as environment variables:

```bash
export ANTHROPIC_API_KEY=your_api_key_here
export ANTHROPIC_MODEL=claude-sonnet-4-6
```

## Quick Start

### Run All Tests

```bash
# Discover and collect tests
pytest --collect-only

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_context_precision.py -v

# Run with logging
pytest -v -s
```

### Run Specific Metrics

```bash
# Test context precision
pytest tests/test_context_precision.py

# Test context recall with parametrized data
pytest tests/test_context_recall_integration.py -v

# Test faithfulness metric
pytest tests/test_faithfulness.py

# Test response relevance
pytest tests/test_response_relevance.py

# Test rubrics scoring
pytest tests/test_rubrics.py

# Test topic adherence in multi-turn conversations
pytest tests/test_topic_adherence.py
```

## Project Structure

```
LLMEval/
├── src/
│   └── llmeval/                    # Main package
│       ├── __init__.py
│       ├── main.py                 # Entry point
│       └── utils.py                # Utility functions
│
├── tests/                          # Test suite
│   ├── __init__.py
│   ├── fixtures/                   # Test data files
│   │   ├── parametrization_data.json
│   │   ├── faithfulness_parametrization_data.json
│   │   └── responseRelevance_data.json
│   ├── test_context_precision.py
│   ├── test_context_recall.py
│   ├── test_context_recall_integration.py
│   ├── test_faithfulness.py
│   ├── test_response_relevance.py
│   ├── test_rubrics.py
│   ├── test_topic_adherence.py
│   └── test_dataset_generation.py
│
├── conftest.py                     # Pytest fixtures and configuration
├── pytest.ini                      # Pytest configuration
├── .env                            # Environment variables (create this)
├── .gitignore
├── README.md                       # This file
└── requirements.txt                # Python dependencies
```

## Available Metrics

### 📊 1. Context Precision (`test_context_precision.py`)

**Purpose**: Measures how well the retrieved contexts are relevant to the query.

**What it evaluates**:
- Does each retrieved document contain information relevant to the query?
- What percentage of context chunks are actually useful?
- Reduces false-positive retrieval results

**Score**: 0-1 (higher is better)

**Test Type**: Single-turn evaluation

```bash
pytest tests/test_context_precision.py -v
```

---

### 📊 2. Context Recall (`test_context_recall.py`)

**Purpose**: Measures whether all relevant information needed to answer a query is present in the retrieved contexts.

**What it evaluates**:
- Are all necessary facts/information in the retrieved documents?
- Can the question be fully answered from the contexts provided?
- Useful for detecting missing information

**Score**: 0-1 (higher is better)

**Test Type**: Single-turn evaluation with reference data

**Threshold**: > 0.7 required to pass

```bash
pytest tests/test_context_recall.py -v
```

---

### 📊 3. Faithfulness (`test_faithfulness.py`)

**Purpose**: Measures whether the response is grounded in the provided context without hallucinations.

**What it evaluates**:
- Are all claims in the response supported by the context?
- Does the response avoid making up information?
- Is the response factually consistent with provided documents?

**Score**: 0-1 (higher is better)

**Test Type**: Parametrized test with multiple datasets

**Threshold**: > 0.8 required to pass

```bash
pytest tests/test_faithfulness.py -v
```

**Test Data**: `tests/fixtures/faithfulness_parametrization_data.json`

---

### 📊 4. Response Relevance (`test_response_relevance.py`)

**Purpose**: Measures how relevant the generated response is to the input query.

**What it evaluates**:
- Does the response address the user's question?
- Is the response focused or does it contain irrelevant information?
- How well does the response match user intent?

**Score**: 0-1 (higher is better)

**Test Type**: Parametrized test with embedding-based similarity

**Threshold**: > 0.8 required to pass

**Components**:
- Uses HuggingFace embeddings for semantic similarity
- Compares response to original query

```bash
pytest tests/test_response_relevance.py -v
```

**Test Data**: `tests/fixtures/responseRelevance_data.json`

---

### 📊 5. Topic Adherence (`test_topic_adherence.py`)

**Purpose**: Evaluates whether multi-turn conversations maintain focus on specified topics.

**What it evaluates**:
- Does the conversation stay on the specified topics?
- Are responses relevant across multiple turns?
- Prevents topic drift in long conversations

**Score**: 0-1 (higher is better)

**Test Type**: Multi-turn conversation evaluation

**Threshold**: > 0.8 required to pass

```bash
pytest tests/test_topic_adherence.py -v
```

**Example**: Evaluates a multi-turn conversation about Selenium WebDriver course to ensure all responses relate to course topics.

---

### 📊 6. Rubrics Score (`test_rubrics.py`)

**Purpose**: Custom 1-5 scale evaluation based on defined rubric criteria.

**What it evaluates**:
- **Score 1**: Incorrect, irrelevant, does not align with ground truth
- **Score 2**: Partially matches, includes significant errors or omissions
- **Score 3**: Generally aligns, may lack detail or have minor inaccuracies
- **Score 4**: Mostly accurate, aligns well with minor issues
- **Score 5**: Fully accurate, complete alignment with ground truth

**Score**: 1-5 (higher is better)

**Test Type**: Custom rubrics-based grading

**Threshold**: > 4 required to pass (excellent quality)

```bash
pytest tests/test_rubrics.py -v
```

**Example**: Evaluates whether "The Eiffel Tower is situated in Paris" accurately answers "Where is the Eiffel Tower located?"

---

### 🔧 7. Context Recall Integration (`test_context_recall_integration.py`)

**Purpose**: Parametrized context recall testing with multiple datasets.

**What it evaluates**:
- Same as Context Recall but with multiple test cases
- Batch testing of recall across different queries

**Score**: 0-1 per test case

**Test Type**: Parametrized multi-dataset evaluation

**Threshold**: > 0.7 required per test case

```bash
pytest tests/test_context_recall_integration.py -v
```

**Test Data**: `tests/fixtures/parametrization_data.json`

---

### 🔨 8. Dataset Generation (`test_dataset_generation.py`)

**Purpose**: Generate synthetic test datasets from documents using RAGAS TestsetGenerator.

**What it evaluates**:
- Creates question-context pairs from documents
- Generates reference answers
- Useful for creating training/testing data

**Test Type**: Data generation (not graded)

```bash
pytest tests/test_dataset_generation.py -v
```

**Note**: Requires document files in specified directory.

## Running Tests

### Basic Commands

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_context_precision.py

# Run specific test function
pytest tests/test_rubrics.py::test_rubric_score

# Run tests matching a pattern
pytest -k "context" -v

# Show print statements
pytest -v -s

# Stop on first failure
pytest -x

# Show the last N lines of output
pytest -v --tb=short
```

### Advanced Options

```bash
# Run with specific asyncio mode
pytest -v --asyncio-mode=auto

# Generate HTML report
pytest --html=report.html

# Measure test coverage
pytest --cov=src/llmeval tests/

# Run tests in parallel (requires pytest-xdist)
pytest -n auto

# Run with markers
pytest -m asyncio -v

# Collect tests without running
pytest --collect-only -q
```

### Parametrized Tests

Some tests run with multiple datasets:

```bash
# View which parametrized tests will run
pytest tests/test_faithfulness.py --collect-only -v

# Expected output shows multiple get_data variants
```

## Configuration

### pytest.ini

The `pytest.ini` file configures pytest behavior:

```ini
[pytest]
testpaths = tests              # Where to find tests
python_files = test_*.py       # Test file naming pattern
asyncio_mode = auto            # Async test support
pythonpath = src               # Add src to Python path
filterwarnings =
    ignore::DeprecationWarning # Suppress deprecation warnings
```

### .env File

Create `.env` in project root for environment variables:

```env
# Required
ANTHROPIC_API_KEY=sk-ant-your-api-key-here

# Optional (defaults to claude-sonnet-4-6)
ANTHROPIC_MODEL=claude-sonnet-4-6
```

### conftest.py

Defines shared pytest fixtures:

```python
@pytest.fixture
def llm_wrapper():
    """Provides a RAGAS-wrapped LLM for tests"""
    # Initializes Anthropic client
    # Returns LangchainLLMWrapper
```

## Test Data

### Data Structure

Test data files are JSON arrays of objects:

```json
[
  {
    "question": "How many articles are there in the Selenium Webdriver course?",
    "reference": "63"
  },
  {
    "question": "What are the requirements for the course?",
    "reference": "The course requires basic programming knowledge"
  }
]
```

### Available Datasets

- `tests/fixtures/parametrization_data.json` - Context recall test data
- `tests/fixtures/faithfulness_parametrization_data.json` - Faithfulness test data
- `tests/fixtures/responseRelevance_data.json` - Response relevance test data

### Adding New Test Data

1. Create a new JSON file in `tests/fixtures/`
2. Follow the data structure above
3. Reference it in your test:

```python
filename = "tests/fixtures/your_data.json"

@pytest.mark.parametrize("get_data",
                         load_test_data(filename),
                         indirect=True)
async def test_your_metric(llm_wrapper, get_data):
    # Your test
    pass
```

## Dependencies

### Core Dependencies

- **ragas** (>=0.0.x) - LLM evaluation framework
- **langchain** - LLM integration framework
- **langchain-anthropic** - Anthropic Claude integration
- **langchain-community** - Community integrations
- **langchain-huggingface** - HuggingFace embeddings
- **pytest** (>=9.0.0) - Testing framework
- **pytest-asyncio** - Async test support
- **python-dotenv** - Environment variable management
- **requests** - HTTP client for API calls
- **pandas** - Data manipulation (via dependencies)

### Development Dependencies

- **pytest-cov** - Coverage reporting
- **pytest-html** - HTML test reports
- **pytest-xdist** - Parallel test execution

### Installation

```bash
# Install all dependencies
pip install -r requirements.txt

# Or install specific components
pip install ragas langchain langchain-anthropic pytest-asyncio
```

## Utility Functions

### `llmeval.utils` Module

#### `get_llm_response(test_data)`

Queries the external LLM API and retrieves response and context.

```python
from llmeval.utils import get_llm_response

response_dict = get_llm_response({
    "question": "What is Python?",
    "chat_history": []
})

# Returns:
# {
#     "answer": "Python is a programming language...",
#     "retrieved_docs": [
#         {"page_content": "..."},
#         {"page_content": "..."}
#     ]
# }
```

#### `load_test_data(filename)`

Loads test data from JSON file.

```python
from llmeval.utils import load_test_data

data = load_test_data("tests/fixtures/parametrization_data.json")
# Returns list of test cases
```

## Troubleshooting

### Common Issues

#### 1. API Key Not Found

**Error**: `ANTHROPIC_API_KEY is not set`

**Solution**:
```bash
# Set environment variable
export ANTHROPIC_API_KEY=sk-ant-...

# Or create .env file with key
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
```

#### 2. Timeout Errors

**Error**: `Timed out waiting for context precision score (30s)`

**Causes**:
- Network connectivity issues
- API is slow or overloaded
- Query is too complex

**Solutions**:
- Check internet connection
- Check Anthropic API status
- Increase timeout in test code
- Simplify test queries

#### 3. Import Errors

**Error**: `ModuleNotFoundError: No module named 'llmeval'`

**Solution**:
```bash
# Verify pytest.ini has correct pythonpath
# Should include: pythonpath = src

# Or run pytest from project root:
cd /path/to/LLMEval
pytest tests/
```

#### 4. Async Errors

**Error**: `RuntimeError: no running event loop`

**Solution**:
```bash
# Ensure pytest-asyncio is installed
pip install pytest-asyncio

# Run with asyncio mode
pytest --asyncio-mode=auto -v
```

## Test Results Interpretation

### Passing Tests

```
PASSED tests/test_context_precision.py::test_context_precision
```
✅ Metric score meets or exceeds the minimum threshold

### Failing Tests

```
FAILED tests/test_faithfulness.py::test_faithfulness[get_data0]
AssertionError: assert 0.65 > 0.8
```
❌ Metric score is below the required threshold

### Skipped Tests

```
SKIPPED tests/test_rubrics.py::test_rubric_score - ANTHROPIC_API_KEY is not set
```
⏭️ Test was skipped (usually due to missing configuration)

## Example Test Output

```
============================= test session starts ==============================
platform darwin -- Python 3.11.13, pytest-9.0.3
rootdir: /Users/username/LLMEval
configfile: pytest.ini
asyncio_mode: Mode.AUTO

collected 9 items

tests/test_context_precision.py::test_context_precision PASSED         [ 11%]
tests/test_context_recall.py::test_context_recall PASSED               [ 22%]
tests/test_context_recall_integration.py::test_context_recall_parametrized[get_data0] PASSED [ 33%]
tests/test_context_recall_integration.py::test_context_recall_parametrized[get_data1] PASSED [ 44%]
tests/test_faithfulness.py::test_faithfulness[get_data0] PASSED         [ 55%]
tests/test_response_relevance.py::test_response_relevance[get_data0] PASSED [ 66%]
tests/test_rubrics.py::test_rubric_score PASSED                        [ 77%]
tests/test_topic_adherence.py::test_topic_adherence PASSED             [ 88%]
tests/test_dataset_generation.py::test_dataset_generation PASSED       [ 99%]

======================== 9 passed in 45.23s ==============================
```

## Performance Tips

### Optimize Test Execution

1. **Run tests in parallel** (requires pytest-xdist):
   ```bash
   pip install pytest-xdist
   pytest -n auto
   ```

2. **Skip slow tests**:
   ```bash
   pytest -m "not slow"
   ```

3. **Cache embeddings** for response relevance tests

4. **Use smaller models** for testing (configure in .env):
   ```env
   ANTHROPIC_MODEL=claude-haiku-3  # Faster, cheaper
   ```

## Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork** the repository
2. **Create a branch** for your feature: `git checkout -b feature/new-metric`
3. **Write tests** for your new metric
4. **Update test data** as needed
5. **Submit a pull request**

### Adding New Metrics

1. Create `tests/test_your_metric.py`
2. Add test data to `tests/fixtures/`
3. Update this README with metric description
4. Run all tests to ensure nothing breaks:
   ```bash
   pytest -v
   ```

## License

This project is licensed under the MIT License. See LICENSE file for details.

## References

- [RAGAS Documentation](https://docs.ragas.io/)
- [Anthropic Claude Documentation](https://docs.anthropic.com)
- [LangChain Documentation](https://python.langchain.com/)
- [Pytest Documentation](https://docs.pytest.org/)

## Support

For issues, questions, or suggestions:

1. Check [Troubleshooting](#troubleshooting) section
2. Review test logs and error messages
3. Check RAGAS and Anthropic documentation
4. Create an issue on GitHub

## Changelog

### Version 1.0.0 (May 2026)

- ✅ Initial release
- ✅ 7 evaluation metrics
- ✅ Parametrized test support
- ✅ Multi-turn conversation evaluation
- ✅ Custom rubrics scoring
- ✅ Comprehensive test suite
- ✅ Industry-standard project structure

---

**Made with ❤️ for LLM evaluation**

Last Updated: May 11, 2026
