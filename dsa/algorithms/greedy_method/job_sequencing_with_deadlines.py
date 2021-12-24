from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Job:
    job_id: int
    profit: int
    deadline: int

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Job):
            return Job.job_id == Job.job_id
        return False


def sequencing_job(jobs: List[Job], number_of_slots: int) -> List[Job]:
    """Return the exact sequence of jobs which maximise the outputs.

    :param jobs: Input jobs.
    :param number_of_slots: Number of execution slots
    :return: Sequenced jobs
    """
    # It is assumed that all jobs take an equal amount of time to execute,
    # and that job_ids of the input jobs start from 1 and are sequential

    jobs.sort(key=lambda element: element.profit)

    execution_timeline = [0] * number_of_slots

    scheduled_jobs: List[Job] = []

    for job in jobs:
        if job.deadline > len(execution_timeline) - 1:
            continue
        place_in_schedule = job.deadline - 1
        while place_in_schedule > 0:
            if execution_timeline[place_in_schedule] == 0:
                scheduled_jobs.append(job)
                break
            else:
                place_in_schedule -= 1

    return scheduled_jobs
