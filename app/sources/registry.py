from __future__ import annotations

from pydantic import BaseModel, Field


class SourceCatalogEntry(BaseModel):
    name: str
    url: str
    category: str
    country: str
    reliability: float = Field(0.5, ge=0, le=1)
    description: str


REGION_PRIORITY = ["Tunisia", "Africa", "Europe", "Asia", "Global"]

OFFICIAL_SOURCE_CATALOG = [
    SourceCatalogEntry(name="ANETI", url="https://www.aneti.tn/", category="government", country="Tunisia", reliability=0.95, description="Tunisian public employment agency."),
    SourceCatalogEntry(name="Wuzzuf", url="https://wuzzuf.net/", category="job_board", country="Egypt", reliability=0.83, description="Egypt-focused employment platform."),
    SourceCatalogEntry(name="RemoteOK", url="https://remoteok.com/", category="job_board", country="Global", reliability=0.85, description="Public remote-work listings."),
    SourceCatalogEntry(name="Wellfound", url="https://wellfound.com/", category="startup_jobs", country="Global", reliability=0.88, description="Startup jobs and company information."),
    SourceCatalogEntry(name="Official company career pages", url="https://www.google.com/search?q=official+company+career+pages", category="official", country="Global", reliability=0.97, description="Primary source for a company's own vacancies."),
    SourceCatalogEntry(name="Government labor portals", url="https://ilostat.ilo.org/", category="statistics", country="Global", reliability=0.96, description="International Labour Organization statistics."),
]
