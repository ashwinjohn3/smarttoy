from datetime import datetime
from enum import Enum
from typing import Annotated, List, Optional

from pydantic import BaseModel, Field, HttpUrl

ResearchSessionId = Annotated[str, 
    Field(pattern=r'^r-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
]

SourceId = Annotated[str,
    Field(pattern=r'^s-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
]

class ResearchStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class SearchProvider(str, Enum):
    TAVILY = "TAVILY"

class ExportFormat(str, Enum):
    MARKDOWN = "MARKDOWN"

class Language(str, Enum):
    ENGLISH = "en"
    
# Request Models 

class ResearchConfig(BaseModel):
    include_academic_sources: bool = False
    date_filter: str | None = None  # "past_week", "past_month", "past_year"
    max_sources_per_query: int = 5
    language: Language = Language.ENGLISH
    
class CreateResearchRequest(BaseModel):
    question: Annotated[str, Field(min_length=10, max_length=1000)]
    max_iterations: Annotated[int, Field(default=3, ge=1, le=10)]
    relevance_threshold: Annotated[float, Field(default=0.6, ge=0.0, le=1.0)]
    search_provider: SearchProvider = SearchProvider.TAVILY
    export_format: ExportFormat = ExportFormat.MARKDOWN
    research_config: ResearchConfig | None = None
    
class ExportRequest(BaseModel):
    format: ExportFormat
    # TODO: config: Optional[Dict[str, Any]] = None

# Response Models 
class ProgressInfo(BaseModel):
    queries_generated: int
    sources_found: int
    sources_evaluated: int
    sources_above_threshold: int

class ResearchSessionResponse(BaseModel):
    research_session_id: ResearchSessionId
    status: ResearchStatus
    question: str
    current_iteration: Optional[int] = None
    max_iterations: int
    progress: Optional[ProgressInfo] = None
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    
class SourceResponse(BaseModel):
    source_id: SourceId
    title: str
    url: HttpUrl
    snippet: str | None
    relevance_score: float | None
    quality_score: float | None
    domain: str | None
    retrieved_at: datetime
    
class ReportResponse(BaseModel):
    content: str
    format: str
    word_count: int
    sources_cited: int
    
class ExportInfo(BaseModel):
    format: ExportFormat
    url: Optional[HttpUrl] = None
    exported_at: datetime | None = None

class ResearchMetrics(BaseModel): 
    total_queries: int
    total_sources_found: int
    sources_used: int
    iterations_used: int
    total_duration_seconds: int

class ResearchResultsResponse(BaseModel):
    session_id: ResearchSessionId
    status: ResearchStatus
    question: str
    report: ReportResponse
    sources: List[SourceResponse]
    export: ExportInfo | None = None
    metrics: ResearchMetrics
    completed_at: datetime
    
class IterationResponse(BaseModel):
    iteration_number: int
    status: str
    reasoning: str | None = None
    queries_generated: int
    sources_found: int
    sources_above_threshold: int
    decision: str | None = None
    started_at: datetime
    completed_at: datetime | None = None
    duration_seconds: int | None = None
    
class SessionListItem(BaseModel): 
    session_id: ResearchSessionId
    question: str
    status: ResearchStatus
    created_at: datetime
    completed_at: datetime | None = None
    sources_count: int
    
class PaginationInfo(BaseModel):
    total: int
    limit: int
    offset: int 
    has_more: bool
    
class SessionListResponse(BaseModel): 
    sessions: List[SessionListItem]
    pagination: PaginationInfo
    