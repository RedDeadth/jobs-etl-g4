import requests
from bs4 import BeautifulSoup
import time
import random
from prefect import task

@task
def extract_jobs():
    url = "https://www.linkedin.com/jobs/search/?keywords=python"
    headers = {"User-Agent": "Mozilla/5.0"}
    print(f"Intentando acceder a la URL: {url}")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Respuesta recibida con código de estado: {response.status_code}")
        soup = BeautifulSoup(response.text, 'html.parser')
        print("HTML analizado correctamente.")

        job_cards = soup.select(".base-search-card__info")
        print(f"Se encontraron {len(job_cards)} ofertas laborales.")

        jobs_data = []

        for job_card in job_cards:
            title_tag = job_card.select_one(".base-search-card__title")
            location_tag = job_card.select_one(".job-search-card__location")
            link_tag = job_card.select_one(".hidden-nested-link")
            date_tag = job_card.select_one("time.job-search-card__listdate")

            job = {
                "title": title_tag.text.strip() if title_tag else None,
                "description": "",
                "location": location_tag.text.strip() if location_tag else None,
                "link": link_tag["href"].strip() if link_tag else None,
                "date": date_tag["datetime"] if date_tag and date_tag.has_attr("datetime") else None
            }
            print(f"Información extraída: {job}")
            jobs_data.append(job)
            time.sleep(random.uniform(1, 3))

        return jobs_data

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []

if __name__ == "__main__":
    extracted_data = extract_jobs()
    if extracted_data:
        print(f"Se extrajeron {len(extracted_data)} ofertas.")
    else:
        print("No se pudieron extraer ofertas de empleo.")
