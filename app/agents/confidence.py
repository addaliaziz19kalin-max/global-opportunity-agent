from __future__ import annotations

from collections import Counter

from app.models import JobOpportunity, MarketInsight, SolutionIdea


def calculate_confidence(job: JobOpportunity) -> float:
    base_score = 0.30
    if job.source_url:
        base_score += 0.15
    if job.source_name:
        base_score += 0.10
    if job.required_skills:
        base_score += min(len(job.required_skills) * 0.02, 0.15)
    if job.description:
        base_score += 0.10
    if job.country in {"Tunisia", "Morocco", "Algeria", "Egypt", "Libya"}:
        base_score += 0.05
    return round(min(base_score, 1.0), 2)


def cross_validate(jobs: list[JobOpportunity]) -> list[JobOpportunity]:
    for job in jobs:
        job.confidence = calculate_confidence(job)
    return jobs


def analyze_market_by_country(jobs: list[JobOpportunity]) -> list[MarketInsight]:
    by_country: dict[str, list[JobOpportunity]] = {}
    for job in jobs:
        by_country.setdefault(job.country, []).append(job)

    insights: list[MarketInsight] = []
    for country, country_jobs in by_country.items():
        skill_counter = Counter()
        for job in country_jobs:
            for skill in job.required_skills:
                skill_counter[skill.lower()] += 1

        top_skills = [skill for skill, _ in skill_counter.most_common(5)]
        company_counter = Counter(job.company.lower() for job in country_jobs)

        insights.append(
            MarketInsight(
                country=country,
                top_skills=top_skills,
                hiring_trends=[
                    f"High demand visible for {top_skills[0]}" if top_skills else "Hiring activity visible",
                    f"{len(country_jobs)} opportunities identified",
                ],
                most_active_sectors=[sector for sector, _ in company_counter.most_common(3)],
                average_confidence=round(sum(job.confidence for job in country_jobs) / len(country_jobs), 2),
            )
        )
    return insights


def generate_solution_ideas(jobs: list[JobOpportunity]) -> list[SolutionIdea]:
    skill_counter = Counter()
    for job in jobs:
        for skill in job.required_skills:
            skill_counter[skill.lower()] += 1

    ideas: list[SolutionIdea] = []
    for skill, count in skill_counter.most_common(5):
        ideas.append(
            SolutionIdea(
                title=f"AI workflow for {skill.title()} teams",
                problem=f"Companies continue to face hiring and execution bottlenecks around {skill.lower()} skills.",
                opportunity=f"There is a recurring need to improve workflows and productivity around {skill.lower()}.",
                target_market="Tech-driven employers and SMEs",
                suggested_solution=f"Build an automated hiring, assessment, and workflow platform focused on {skill.lower()} capability and staff productivity.",
                evidence=[
                    f"Appears in {count} role definitions",
                    "Repeated demand across multiple markets",
                ],
            )
        )
    return ideas
