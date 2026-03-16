import requests
from rich.console import Console

console = Console()

def check_target_alive(url: str) -> bool:
    """
    Verifica si la URL objetivo está activa y responde a solicitudes HTTP.
    
    Args:
        url (str): La dirección web objetivo a verificar.
    
    Returns:
        bool: True si la URL responde, False en caso contrario.
    """
    
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            console.print(f"[bold green]La URL {url} está viva.[/bold green]")

        return True

    except requests.exceptions.RequestException:
        return False
