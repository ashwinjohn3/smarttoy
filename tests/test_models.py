"""
Unit tests for Pydantic models in models/models.py

Tests cover:
- Model instantiation with valid data
- Field validation (min/max lengths, ranges)
- Type validation
- Enum constraints
- Edge cases
"""

import sys
from datetime import datetime, timezone
from typing import Any, Dict

import pytest
from pydantic import ValidationError

# Add models to path
sys.path.insert(0, 'models')
from models import (
    CreateResearchRequest,
    ExportFormat,
    ExportInfo,
    ExportRequest,
    IterationResponse,
    PaginationInfo,
    ProgressInfo,
    ReportResponse,
    ResearchConfig,
    ResearchMetrics,
    ResearchResultsResponse,
    ResearchSessionResponse,
    ResearchStatus,
    SearchProvider,
    SessionListItem,
    SessionListResponse,
    SourceResponse,
)


# ==================== FIXTURES ====================

@pytest.fixture
def valid_research_config() -> Dict[str, Any]:
    """Valid ResearchConfig data"""
    return {
        "include_academic_sources": True,
        "date_filter": "past_year",
        "max_sources_per_query": 5,
        "language": "en"
    }


@pytest.fixture
def valid_create_request() -> Dict[str, Any]:
    """Valid CreateResearchRequest data"""
    return {
        "question": "What are the latest developments in quantum computing?",
        "max_iterations": 3,
        "relevance_threshold": 0.7,
        "search_provider": "TAVILY",
        "export_format": "MARKDOWN"
    }


@pytest.fixture
def valid_export_request() -> Dict[str, Any]:
    """Valid ExportRequest data"""
    return {
        "format": "MARKDOWN"
    }


@pytest.fixture
def valid_progress_info() -> Dict[str, Any]:
    """Valid ProgressInfo data"""
    return {
        "queries_generated": 6,
        "sources_found": 15,
        "sources_evaluated": 12,
        "sources_above_threshold": 8
    }


@pytest.fixture
def valid_research_session() -> Dict[str, Any]:
    """Valid ResearchSessionResponse data"""
    return {
        "research_session_id": "r-550e8400-e29b-41d4-a716-446655440000",
        "status": "IN_PROGRESS",
        "question": "What are the latest developments in quantum computing?",
        "current_iteration": 2,
        "max_iterations": 3,
        "progress": {
            "queries_generated": 6,
            "sources_found": 15,
            "sources_evaluated": 12,
            "sources_above_threshold": 8
        },
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc)
    }


@pytest.fixture
def valid_source_response() -> Dict[str, Any]:
    """Valid SourceResponse data"""
    return {
        "source_id": "s-660e8400-e29b-41d4-a716-446655440001",
        "title": "IBM Unveils 433-Qubit Quantum Processor",
        "url": "https://example.com/ibm-quantum",
        "snippet": "IBM announced their new Osprey processor...",
        "relevance_score": 0.95,
        "quality_score": 0.88,
        "domain": "example.com",
        "retrieved_at": datetime.now(timezone.utc)
    }


@pytest.fixture
def valid_report_response() -> Dict[str, Any]:
    """Valid ReportResponse data"""
    return {
        "content": "# Quantum Computing Developments\n\nExecutive Summary...",
        "format": "markdown",
        "word_count": 1500,
        "sources_cited": 8
    }


@pytest.fixture
def valid_export_info() -> Dict[str, Any]:
    """Valid ExportInfo data"""
    return {
        "format": "MARKDOWN",
        "url": "https://docs.google.com/document/d/abc123",
        "exported_at": datetime.now(timezone.utc)
    }


@pytest.fixture
def valid_research_metrics() -> Dict[str, Any]:
    """Valid ResearchMetrics data"""
    return {
        "total_queries": 6,
        "total_sources_found": 15,
        "sources_used": 8,
        "iterations_used": 2,
        "total_duration_seconds": 225
    }


@pytest.fixture
def valid_iteration_response() -> Dict[str, Any]:
    """Valid IterationResponse data"""
    return {
        "iteration_number": 1,
        "status": "completed",
        "reasoning": "Starting with broad queries to understand the landscape...",
        "queries_generated": 3,
        "sources_found": 8,
        "sources_above_threshold": 5,
        "decision": "Continue to next iteration",
        "started_at": datetime.now(timezone.utc),
        "completed_at": datetime.now(timezone.utc),
        "duration_seconds": 75
    }


@pytest.fixture
def valid_session_list_item() -> Dict[str, Any]:
    """Valid SessionListItem data"""
    return {
        "session_id": "r-550e8400-e29b-41d4-a716-446655440000",
        "question": "What are the latest developments in quantum computing?",
        "status": "COMPLETED",
        "created_at": datetime.now(timezone.utc),
        "completed_at": datetime.now(timezone.utc),
        "sources_count": 8
    }


@pytest.fixture
def valid_pagination_info() -> Dict[str, Any]:
    """Valid PaginationInfo data"""
    return {
        "total": 25,
        "limit": 10,
        "offset": 0,
        "has_more": True
    }


# ==================== ENUM TESTS ====================

class TestEnums:
    """Test enum definitions"""

    def test_research_status_values(self):
        """Test ResearchStatus enum has correct values"""
        assert ResearchStatus.PENDING == "PENDING"
        assert ResearchStatus.IN_PROGRESS == "IN_PROGRESS"
        assert ResearchStatus.COMPLETED == "COMPLETED"
        assert ResearchStatus.FAILED == "FAILED"

    def test_search_provider_values(self):
        """Test SearchProvider enum has correct values"""
        assert SearchProvider.TAVILY == "TAVILY"

    def test_export_format_values(self):
        """Test ExportFormat enum has correct values"""
        assert ExportFormat.MARKDOWN == "MARKDOWN"


# ==================== REQUEST MODEL TESTS ====================

class TestResearchConfig:
    """Test ResearchConfig model"""

    def test_valid_config(self, valid_research_config):
        """Test creating valid ResearchConfig"""
        config = ResearchConfig(**valid_research_config)
        assert config.include_academic_sources is True
        assert config.date_filter == "past_year"
        assert config.max_sources_per_query == 5

    def test_default_values(self):
        """Test ResearchConfig default values"""
        config = ResearchConfig()
        assert config.include_academic_sources is False
        assert config.date_filter is None
        assert config.max_sources_per_query == 5


class TestCreateResearchRequest:
    """Test CreateResearchRequest model"""

    def test_valid_request(self, valid_create_request):
        """Test creating valid CreateResearchRequest"""
        request = CreateResearchRequest(**valid_create_request)
        assert request.question == "What are the latest developments in quantum computing?"
        assert request.max_iterations == 3
        assert request.relevance_threshold == 0.7

    def test_default_values(self):
        """Test CreateResearchRequest default values"""
        request = CreateResearchRequest(
            question="What is quantum computing and how does it work?"
        )
        assert request.max_iterations == 3
        assert request.relevance_threshold == 0.6
        assert request.search_provider == SearchProvider.TAVILY

    def test_question_too_short(self):
        """Test question minimum length validation"""
        with pytest.raises(ValidationError) as exc_info:
            CreateResearchRequest(question="short")
        assert "question" in str(exc_info.value)

    def test_question_too_long(self):
        """Test question maximum length validation"""
        long_question = "x" * 1001
        with pytest.raises(ValidationError) as exc_info:
            CreateResearchRequest(question=long_question)
        assert "question" in str(exc_info.value)

    def test_max_iterations_below_minimum(self):
        """Test max_iterations minimum value validation"""
        with pytest.raises(ValidationError) as exc_info:
            CreateResearchRequest(
                question="Valid question here?",
                max_iterations=0
            )
        assert "max_iterations" in str(exc_info.value)

    def test_max_iterations_above_maximum(self):
        """Test max_iterations maximum value validation"""
        with pytest.raises(ValidationError) as exc_info:
            CreateResearchRequest(
                question="Valid question here?",
                max_iterations=11
            )
        assert "max_iterations" in str(exc_info.value)

    def test_relevance_threshold_below_minimum(self):
        """Test relevance_threshold minimum value validation"""
        with pytest.raises(ValidationError) as exc_info:
            CreateResearchRequest(
                question="Valid question here?",
                relevance_threshold=-0.1
            )
        assert "relevance_threshold" in str(exc_info.value)

    def test_relevance_threshold_above_maximum(self):
        """Test relevance_threshold maximum value validation"""
        with pytest.raises(ValidationError) as exc_info:
            CreateResearchRequest(
                question="Valid question here?",
                relevance_threshold=1.1
            )
        assert "relevance_threshold" in str(exc_info.value)


class TestExportRequest:
    """Test ExportRequest model"""

    def test_valid_export_request(self, valid_export_request):
        """Test creating valid ExportRequest"""
        request = ExportRequest(**valid_export_request)
        assert request.format == ExportFormat.MARKDOWN


# ==================== RESPONSE MODEL TESTS ====================

class TestProgressInfo:
    """Test ProgressInfo model"""

    def test_valid_progress_info(self, valid_progress_info):
        """Test creating valid ProgressInfo"""
        progress = ProgressInfo(**valid_progress_info)
        assert progress.queries_generated == 6
        assert progress.sources_found == 15
        assert progress.sources_evaluated == 12
        assert progress.sources_above_threshold == 8


class TestResearchSessionResponse:
    """Test ResearchSessionResponse model"""

    def test_valid_session_response(self, valid_research_session):
        """Test creating valid ResearchSessionResponse"""
        session = ResearchSessionResponse(**valid_research_session)
        assert session.research_session_id == "r-550e8400-e29b-41d4-a716-446655440000"
        assert session.status == ResearchStatus.IN_PROGRESS
        assert session.current_iteration == 2
        assert session.max_iterations == 3

    def test_optional_fields(self):
        """Test ResearchSessionResponse with optional fields as None"""
        session = ResearchSessionResponse(
            research_session_id="r-550e8400-e29b-41d4-a716-446655440000",
            status="PENDING",
            question="Test question?",
            max_iterations=3,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        assert session.current_iteration is None
        assert session.progress is None
        assert session.completed_at is None


class TestSourceResponse:
    """Test SourceResponse model"""

    def test_valid_source_response(self, valid_source_response):
        """Test creating valid SourceResponse"""
        source = SourceResponse(**valid_source_response)
        assert source.source_id == "s-660e8400-e29b-41d4-a716-446655440001"
        assert source.title == "IBM Unveils 433-Qubit Quantum Processor"
        assert source.relevance_score == 0.95

    def test_optional_fields(self, valid_source_response):
        """Test SourceResponse with optional fields as None"""
        data = valid_source_response.copy()
        data["snippet"] = None
        data["relevance_score"] = None
        data["quality_score"] = None
        data["domain"] = None

        source = SourceResponse(**data)
        assert source.snippet is None
        assert source.relevance_score is None


class TestReportResponse:
    """Test ReportResponse model"""

    def test_valid_report_response(self, valid_report_response):
        """Test creating valid ReportResponse"""
        report = ReportResponse(**valid_report_response)
        assert report.word_count == 1500
        assert report.sources_cited == 8
        assert report.format == "markdown"


class TestExportInfo:
    """Test ExportInfo model"""

    def test_valid_export_info(self, valid_export_info):
        """Test creating valid ExportInfo"""
        export = ExportInfo(**valid_export_info)
        assert export.format == ExportFormat.MARKDOWN
        assert str(export.url) == "https://docs.google.com/document/d/abc123"

    def test_optional_fields(self):
        """Test ExportInfo with optional fields as None"""
        export = ExportInfo(format="MARKDOWN")
        assert export.url is None
        assert export.exported_at is None


class TestResearchMetrics:
    """Test ResearchMetrics model"""

    def test_valid_metrics(self, valid_research_metrics):
        """Test creating valid ResearchMetrics"""
        metrics = ResearchMetrics(**valid_research_metrics)
        assert metrics.total_queries == 6
        assert metrics.total_sources_found == 15
        assert metrics.sources_used == 8


class TestIterationResponse:
    """Test IterationResponse model"""

    def test_valid_iteration_response(self, valid_iteration_response):
        """Test creating valid IterationResponse"""
        iteration = IterationResponse(**valid_iteration_response)
        assert iteration.iteration_number == 1
        assert iteration.queries_generated == 3
        assert iteration.sources_found == 8

    def test_optional_fields(self, valid_iteration_response):
        """Test IterationResponse with optional fields as None"""
        data = valid_iteration_response.copy()
        data.pop("reasoning")
        data.pop("decision")
        data.pop("completed_at")
        data.pop("duration_seconds")

        iteration = IterationResponse(**data)
        assert iteration.reasoning is None
        assert iteration.decision is None


class TestSessionListItem:
    """Test SessionListItem model"""

    def test_valid_session_list_item(self, valid_session_list_item):
        """Test creating valid SessionListItem"""
        item = SessionListItem(**valid_session_list_item)
        assert item.session_id == "r-550e8400-e29b-41d4-a716-446655440000"
        assert item.status == ResearchStatus.COMPLETED
        assert item.sources_count == 8


class TestPaginationInfo:
    """Test PaginationInfo model"""

    def test_valid_pagination_info(self, valid_pagination_info):
        """Test creating valid PaginationInfo"""
        pagination = PaginationInfo(**valid_pagination_info)
        assert pagination.total == 25
        assert pagination.limit == 10
        assert pagination.offset == 0
        assert pagination.has_more is True


class TestSessionListResponse:
    """Test SessionListResponse model"""

    def test_valid_session_list_response(
        self, valid_session_list_item, valid_pagination_info
    ):
        """Test creating valid SessionListResponse"""
        response = SessionListResponse(
            sessions=[valid_session_list_item],
            pagination=valid_pagination_info
        )
        assert len(response.sessions) == 1
        assert response.pagination.total == 25


# ==================== INTEGRATION TESTS ====================

class TestResearchResultsResponse:
    """Test complete ResearchResultsResponse model"""

    def test_complete_results_response(
        self,
        valid_source_response,
        valid_report_response,
        valid_export_info,
        valid_research_metrics
    ):
        """Test creating complete ResearchResultsResponse"""
        response = ResearchResultsResponse(
            session_id="r-550e8400-e29b-41d4-a716-446655440000",
            status="COMPLETED",
            question="What are the latest developments in quantum computing?",
            report=valid_report_response,
            sources=[valid_source_response],
            export=valid_export_info,
            metrics=valid_research_metrics,
            completed_at=datetime.now(timezone.utc)
        )

        assert response.status == ResearchStatus.COMPLETED
        assert len(response.sources) == 1
        assert response.report.word_count == 1500
        assert response.metrics.total_queries == 6

    def test_results_without_export(
        self,
        valid_source_response,
        valid_report_response,
        valid_research_metrics
    ):
        """Test ResearchResultsResponse without export info"""
        response = ResearchResultsResponse(
            session_id="r-550e8400-e29b-41d4-a716-446655440000",
            status="COMPLETED",
            question="What are the latest developments in quantum computing?",
            report=valid_report_response,
            sources=[valid_source_response],
            metrics=valid_research_metrics,
            completed_at=datetime.now(timezone.utc)
        )

        assert response.export is None


# ==================== ID PATTERN VALIDATION TESTS ====================

class TestIdPatterns:
    """Test ID pattern validation"""

    def test_valid_research_session_id(self):
        """Test valid research session ID format"""
        session = ResearchSessionResponse(
            research_session_id="r-550e8400-e29b-41d4-a716-446655440000",
            status="PENDING",
            question="Test question?",
            max_iterations=3,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        assert session.research_session_id.startswith("r-")

    def test_invalid_research_session_id_prefix(self):
        """Test invalid research session ID prefix"""
        with pytest.raises(ValidationError) as exc_info:
            ResearchSessionResponse(
                research_session_id="s-550e8400-e29b-41d4-a716-446655440000",
                status="PENDING",
                question="Test question?",
                max_iterations=3,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            )
        assert "research_session_id" in str(exc_info.value)

    def test_valid_source_id(self, valid_source_response):
        """Test valid source ID format"""
        source = SourceResponse(**valid_source_response)
        assert source.source_id.startswith("s-")

    def test_invalid_source_id_prefix(self, valid_source_response):
        """Test invalid source ID prefix"""
        data = valid_source_response.copy()
        data["source_id"] = "r-660e8400-e29b-41d4-a716-446655440001"

        with pytest.raises(ValidationError) as exc_info:
            SourceResponse(**data)
        assert "source_id" in str(exc_info.value)
