import requests
from rich.table import Table

def analyze_headers(url: str) -> Table:
    """
    Realiza una petición a la URL, extrae las cabeceras HTTP y 
    las formatea en una tabla visual.
    
    Args:
        url (str): La dirección web objetivo.
        
    Returns:
        Table: Un objeto Table de la librería Rich listo para ser impreso.
    """
    
    headers = requests.head(url).headers

    tabla = Table(title=f"Cabeceras HTTP de {url}", border_style="green")
    tabla.add_column("Cabecera", style="cyan", justify="right")
    tabla.add_column("Valor", style="magenta")

    for header, value in headers.items():
        tabla.add_row(header, value)

    return tabla
