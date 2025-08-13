import os
import sys
import time
import json
import pylast
from dotenv import load_dotenv
from rich.console import Console
from rich.style import Style


console = Console()
console.rule("[bold red]🎵 LAST.FM SCRUBBLER 🎵[/]", style="bold blue")


load_dotenv()

def load_config():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'config.json')
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def initialize_lastfm(api_key, api_secret, username, password):
    try:
        return pylast.LastFMNetwork(
            api_key=api_key,
            api_secret=api_secret,
            username=username,
            password_hash=pylast.md5(password)
        )
    except pylast.NetworkError as e:
        console.print(f"[red]Erro de conexão:[/red] Verifique sua internet\n{e}")
        sys.exit(1)
    except pylast.WSError as e:
        console.print(f"[red]Erro de credenciais:[/red] Verifique seu arquivo .env\n{e}")
        sys.exit(1)

def scrobble_tracks(network, config):
    try:
        artist = config['ARTIST']
        track = config['TRACK']
        album = config['ALBUM']
        limit = config['LIMIT']
        interval = config['INTERVAL']
        
        progress_style = Style(color="blue", bold=True)
        success_style = Style(color="green", bold=True)
        
        with console.status("[bold blue]Scrobbling...", spinner="dots"):
            for scrobbles in range(1, limit + 1):
                network.scrobble(
                    artist=artist,
                    title=track,
                    timestamp=int(time.time()),
                    album=album
                )
                console.print(
                    f"Scrobbling [bold]{track}[/] by [bold]{artist}[/] "
                    f"[{progress_style}]{scrobbles}/{limit}[/]",
                    end="\r"
                )
                time.sleep(interval)
        
        console.print(f"\n[bold {success_style}]✅ Successo![/] "
                    f"Scrobbled {limit} tracks.", style=success_style)
        
    except pylast.NetworkError as e:
        console.print(f"[red]Erro durante scrobble:[/red]\n{e}")

def main():
    config = load_config()
    
    network = initialize_lastfm(
        os.getenv('API_KEY'),
        os.getenv('API_SECRET'),
        os.getenv('LASTFM_USERNAME'),
        os.getenv('LASTFM_PASSWORD')
    )
    
    scrobble_tracks(network, config)
    
    if console.input("[bold green]Reiniciar? (y/n): [/]").lower() in ('y', 'yes'):
        console.clear()
        main()
    else:
        sys.exit()

if __name__ == '__main__':
    main()

