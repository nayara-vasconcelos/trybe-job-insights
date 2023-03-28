from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    all_max_salaries = [
        int(job["max_salary"])
        for job in read(path)
        if job["max_salary"].isdigit()
    ]
    return max(all_max_salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    all_min_salaries = [
        int(job["min_salary"])
        for job in read(path)
        if job["min_salary"].isdigit()
    ]
    return min(all_min_salaries)


def convert_salary_to_int(
    min_salary_key: Union[int, str], max_salary_key: Union[int, str]
) -> tuple:
    if isinstance(min_salary_key, int) and isinstance(max_salary_key, int):
        return (min_salary_key, max_salary_key)
    min_salary_is_valid = (
        isinstance(min_salary_key, str) and min_salary_key.isdigit()
    )
    max_salary_is_valid = (
        isinstance(max_salary_key, str) and max_salary_key.isdigit()
    )
    if min_salary_is_valid and max_salary_is_valid:
        return (int(min_salary_key), int(max_salary_key))
    else:
        raise ValueError(
            "'min_salary' and 'max_salary' values must be valid integers."
        )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    int_salary = salary
    # verifica type de salário
    if isinstance(int_salary, str) and int_salary.isdigit():
        int_salary = int(int_salary)
    if not (isinstance(int_salary, int)):
        raise ValueError("'salary' isn't a valid integer")
    # verifica se as chaves "min_salary" e "max_salary existem"
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError("'max_salary' and 'min_salary' keys are required.")
    # converte os valores da chave se for necessário e possível
    (min_salary, max_salary) = convert_salary_to_int(
        job["min_salary"], job["max_salary"]
    )
    if min_salary > max_salary:
        raise ValueError(
            "'max_salary' value must be greater than 'min_salary' value."
        )
    it_matches = min_salary <= int_salary <= max_salary
    return it_matches


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            continue
    return filtered_jobs


if __name__ == "__main__":
    min_salary = get_min_salary("data/jobs.csv")
    print(min_salary)
    max_salary = get_max_salary("data/jobs.csv")
    print(max_salary)
    jobs = read("data/jobs.csv")
    filtered_jobs = filter_by_salary_range(jobs, 1000)
    print(filtered_jobs)
