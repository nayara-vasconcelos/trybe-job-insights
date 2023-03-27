from functools import lru_cache
from typing import List, Dict
import csv

# Referências:
# - Documentação: https://docs.python.org/3/library/
# - Repositórios das aulas 1, 2 3 da seção 1 do módulo de CS
# - Course da Trybe: dias 1, 2 3 da seção 1 do módulo de CS
# - Site W3 schools: https://www.w3schools.com/python/


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    if not path.endswith(".csv"):
        raise ValueError("Invalid file format")

    content = []
    try:
        with open(path, mode="r", encoding="utf-8") as csv_file:
            content = list(
                csv.DictReader(csv_file, delimiter=",", quotechar='"')
            )
    except FileNotFoundError:
        print("File not found!")
    return content


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    job_types = set()
    [job_types.add(job["job_type"]) for job in read(path)]
    ordered_job_types = sorted(list(job_types))
    return ordered_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]
    return filtered_jobs


if __name__ == "__main__":
    jobs = read("data/jobs.csv")
    print(jobs[0])
    job_types = get_unique_job_types("data/jobs.csv")
    print(job_types)
    filtered_jobs = filter_by_job_type(jobs, "full")
    print(filtered_jobs)
