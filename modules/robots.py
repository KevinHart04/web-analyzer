import requests
from urllib.parse import urlparse

def get_robots_txt(url: str) -> str:
    """
    Extrae la raíz del dominio de la URL, busca el archivo robots.txt 
    y devuelve su contenido.
    
    Args:
        url (str): La URL objetivo (puede contener rutas largas).
        
    Returns:
        str: El contenido del robots.txt, o un mensaje si no existe.
    """

    url_parsed = urlparse(url)

    base_url = f"{url_parsed.scheme}://{url_parsed.netloc}"

    target_robots = f"{base_url}/robots.txt"

    try:
        response = requests.get(target_robots)
        if response.status_code == 200:
            return response.text
        else:
            return f"No se encontró robots.txt en {base_url}"

    except requests.RequestException as e:
        return f"Error al intentar acceder a {target_robots}: {e}"
