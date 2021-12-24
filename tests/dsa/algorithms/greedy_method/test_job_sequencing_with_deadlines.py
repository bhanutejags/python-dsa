from dsa.algorithms.greedy_method.job_sequencing_with_deadlines import (
    Job,
    sequencing_job,
)


def test_schedule_job():
    jobs = [
        Job(job_id=1, deadline=1, profit=10),
        Job(job_id=2, deadline=3, profit=40),
        Job(job_id=3, deadline=1, profit=5),
        Job(job_id=4, deadline=4, profit=34),
    ]
    sequencing_job(jobs, number_of_slots=3)
