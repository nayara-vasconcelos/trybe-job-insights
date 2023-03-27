from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    industries = set()
    [
        industries.add(job["industry"])
        for job in read(path)
        if len(job["industry"]) > 0
    ]
    ordered_industries = sorted(list(industries))
    return ordered_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_industries = [job for job in jobs if job["industry"] == industry]
    return filtered_industries


if __name__ == "__main__":
    jobs = read("data/jobs.csv")
    print(jobs[0])
    industries = get_unique_industries("data/jobs.csv")
    print(industries)
    filtered_industries = filter_by_industry(jobs, industries[0])
    print(filtered_industries)
