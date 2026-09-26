# Global Opportunity & Market Intelligence Agent

This repository is a professional MVP for a global opportunity intelligence system that monitors jobs, internships, apprenticeships, and business opportunities across countries with a strong focus on Africa first, then Europe, Asia, and the world.

## Mission

Identify and validate:
- real opportunity signals across job boards and company career pages;
- company activity, sectors and mission;
- market-demand evolution by country and skill;
- high-potential business and startup opportunities.

## Principles

- No fabricated data
- Every data point is traceable
- Cross-verification before trust
- Confidence scores are displayed
- Sources are preserved and linked

## Regional priority

1. Tunisia
2. Morocco, Algeria, Egypt, Libya and the rest of Africa
3. Europe: France, Germany, Spain, Italy and others
4. Asia: Japan, Qatar, Saudi Arabia, China and others
5. Rest of the world

## MVP stack

- FastAPI backend
- Pydantic models
- Source registry and confidence scoring
- Data validation and market analysis
- Sample dataset for onboarding
- CI workflow with pytest

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API

- `/health`
- `/summary`
- `/jobs`
- `/market`
- `/countries`
- `/sources`

## License

MIT
