import argparse
import requests
from rich.console import Console
from core.requester import check_target_alive
from modules.headers import analyze_headers
from modules.robots import get_robots_txt
from rich.panel import Panel
import modules.fingerprint as fingerprint

console = Console()\

def setup_cli():
    """
    Configura y maneja los argumentos de la línea de comandos de forma nativa.
    
    Returns:
        argparse.Namespace: Objeto con los argumentos ingresados por el usuario.
    """
    parser = argparse.ArgumentParser(description="Analizador de URL")
    parser.add_argument("url", type=str, help="La URL objetivo a analizar.")
    args = parser.parse_args()
    return args


def analyze_target(url: str):
    """
    Flujo principal de análisis sobre la URL objetivo
    
    Args:
        url (str): La dirección web objetivo a analizar.
    """
    console.print(f"\n[bold dark_orange][*] Iniciando análisis de {url}...[/bold dark_orange]\n")
    
    # check server status
    with console.status(f"\n[bold yellow]Pinchando el servidor {url}...\n", spinner="bouncingBar"):
        esta_vivo = check_target_alive(url)
        
    if esta_vivo:
        console.print("\n[bold green][+] ¡El objetivo está online![/bold green]\n")
        
        # print headers
        with console.status(f"[bold cyan]Extrayendo cabeceras de {url}...", spinner="dots"):
            tabla_headers = analyze_headers(url)
        console.print(tabla_headers)

        # print robots.txt
        with console.status(f"[bold magenta]Obteniendo robots.txt de {url}...", spinner="line"):
            robots_info = get_robots_txt(url)
        console.print(Panel(robots_info, title="[bold magenta]Contenido de robots.txt [/bold magenta]", border_style="magenta"))
        
        with console.status(f"[bold blue]Detectando tecnologías en {url}...", spinner="earth"):
            tecnologias = fingerprint.detect_technologies(url)
        console.print(Panel("\n".join(tecnologias), title="[bold blue]Tecnologías detectadas [/bold blue]", border_style="blue"))

        
    else:
        console.print("[bold red][!] El objetivo no responde o la URL es inválida.[/bold red]")




def main():
    
    url = setup_cli().url
    analyze_target(url)

if __name__ == "__main__":
    main()
