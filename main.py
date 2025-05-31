from extract import extract_jobs
from transform import transform_jobs
from load import load_jobs
from prefect import flow

@flow(name="ETL de Ofertas Laborales")
def etl_flow():
    extracted_data = extract_jobs()
    if extracted_data:
        transformed_data = transform_jobs(extracted_data)
        load_jobs(transformed_data)
    else:
        print("No se encontraron datos para procesar.")

if __name__ == "__main__":
    etl_flow()
