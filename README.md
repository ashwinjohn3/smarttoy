# smarttoy - Deep Research Agent

An AI-powered deep research agent that autonomously searches the web, synthesizes information from multiple sources, and exports structured research reports.

## Overview

smarttoy is a web service that conducts comprehensive research on any topic by:
- Generating diverse, targeted search queries using LLM
- Iteratively searching the web and extracting content
- Evaluating source relevance and quality
- Synthesizing findings into coherent, well-cited reports
- Exporting results to Google Docs, Notion, or Markdown

## Architecture

The system follows a ReAct (Reasoning + Acting) pattern:

1. **Query Generation**: LLM generates diverse search queries from the research question
2. **Search & Extraction**: Executes searches and extracts clean content from web pages
3. **Evaluation**: Scores each source for relevance and quality
4. **Synthesis**: Combines sources into a comprehensive report with citations
5. **Export**: Publishes the report to the chosen platform

### Key Components

- **API Layer** (`app/`): FastAPI endpoints for research requests
- **Agent Core** (`agents/`): Research orchestration, query generation, evaluation, synthesis
- **Tools** (`tools/`): Search API, content extraction, export integrations
- **Utils** (`utils/`): Configuration, logging, helpers

## Setup

### Prerequisites

- Python 3.9+
- API keys for:
  - LLM provider (OpenAI/Anthropic)
  - Search service (Tavily/SerpAPI/Brave)
  - Export service (Google Docs/Notion)

### Installation

```bash
# Clone the repository
git clone https://github.com/ashwinjohn3/smarttoy.git
cd smarttoy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Running the Service

```bash
# Start the development server
uvicorn app.main:app --reload

# The API will be available at http://localhost:8000
# API documentation at http://localhost:8000/docs
```

## API Usage

### Conduct Research

```bash
curl -X POST http://localhost:8000/api/v1/research \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What are the latest developments in quantum computing?",
    "max_iterations": 3,
    "export_format": "google_docs"
  }'
```

### Response Format

```json
{
  "question": "What are the latest developments in quantum computing?",
  "report": "# Quantum Computing Developments\n\n## Executive Summary...",
  "sources": [
    {
      "title": "IBM Unveils 433-Qubit Quantum Processor",
      "url": "https://example.com/article",
      "snippet": "IBM announced their new Osprey processor...",
      "relevance_score": 0.95,
      "retrieved_at": "2025-01-15T10:30:00Z"
    }
  ],
  "iterations_used": 2,
  "export_url": "https://docs.google.com/document/d/...",
  "completed_at": "2025-01-15T10:35:00Z"
}
```

## Development

### Project Structure

```
smarttoy/
├── app/                    # API layer
│   ├── __init__.py
│   ├── main.py            # FastAPI application
│   ├── models.py          # Pydantic models
│   └── api/
│       └── routes.py      # API endpoints
├── agents/                 # Agent logic
│   ├── __init__.py
│   ├── research_agent.py  # Main ReAct loop
│   ├── query_generator.py # Search query generation
│   ├── evaluator.py       # Source relevance scoring
│   ├── synthesizer.py     # Report generation
│   └── state.py           # State management
├── tools/                  # External integrations
│   ├── __init__.py
│   ├── search_tool.py     # Web search API
│   ├── content_extractor.py # Web scraping
│   ├── google_docs_exporter.py
│   └── notion_exporter.py
├── utils/                  # Utilities
│   ├── __init__.py
│   ├── config.py          # Configuration
│   └── logging.py         # Structured logging
├── tests/                  # Test suite
└── requirements.txt
```

### Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=app --cov=agents --cov=tools

# Run specific test categories
pytest tests/ -m unit
pytest tests/ -m integration
```

## License

MIT

## Contributing

Issues and pull requests are welcome! Please see the project board for planned features and improvements.
