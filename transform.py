from prefect import task

@task
def transform_jobs(extracted_jobs):
    transformed_jobs = []
    for job in extracted_jobs:
       
        transformed_jobs.append(job)
    return transformed_jobs

if __name__ == "__main__":

    sample_data = [
        {"title": " Python Developer ", "description": "", "location": "Lima, Peru ", "link": "link1", "date": "2025-05-29"},
        {"title": "Senior Python Engineer", "description": "", "location": "San Isidro, Lima ", "link": "link2", "date": "2025-05-28"}
    ]
    transformed_data = transform_jobs(sample_data)
    print("Datos transformados:")
    for job in transformed_data:
        print(job)
