import os
import requests
from datetime import datetime
import random

# Aktualisierte Liste der URLs, die XML-Daten liefern
urls = [
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Base+Set+-korean+-anime+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Jungle+-korean+-anime+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Wizards+of+the+Coast+Promos+-korean+-anime+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Fossil+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Base+Set+2+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Team+Rocket+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Gym+Heroes+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Neo+Genesis+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Legendary+Collection+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",

    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Best+of+Game+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Aquapolis+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Expedition+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=EX+Ruby+and+Sapphire+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Diamond+and+Pearl+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Platinum+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",

    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=HeartGold+SOulSilver+-japanese+-anime+-korean+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Call+of+Legends+-japanese+-anime+-korean+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Black+and+White+-anime+-korean+Promo&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Emerging+Powers+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Noble+Victories+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Next+Destinies+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Dark+Explorers+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Dragons+Exalted+-japanese+-anime+-korean+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Dragon+Vault+-japanese+-anime+-korean+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Boundaries+Crossed+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Plasma+Blast+-japanese+-anime+-korean+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Legendary+Treasures+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Radiant+Collection+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=XY+Promo+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Flashfire+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Furious+Fists+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Silver+Tempest+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Rebel+Clash+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Cosmic+Eclipse+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Hidden+Fates+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Unified+Minds+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Unbroken+Bonds+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Team+Up+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Lost+Thunder+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Dragon+Majesty+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Forbidden+Light+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Ultra+Prism+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Shining+Legends+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Phantom+Forces+-anime+-korean+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Double+Crisis+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Roaring+Skies+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Ancient+Origins+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Generations+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=BREAKPoint+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Fates+Collide+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Steam+Siege+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Evolutions+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Lost+Origin+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Astral+Radiance+-japanese+-italian+-anime+-korean+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Brilliant+stars+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Fusion+Strike+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Evolving+skies+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Chilling+Reign+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Battle+Styles+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Shining+Fates+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Vivid+Voltage+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Darkness+ablaze+-japanese+-italian+-meiji+-anime+-korean+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Sword+and+shield+-japanese+-italian+-meiji+-anime+-korean+-&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=-japanese+Paldean+Fates&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Paradox+rift+-japanese+-italian+-meiji+-anime+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Scarlet+and+violet+151+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Obsidian+Flames+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Paldea+Evolved+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Twilight+Masquerade+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Scarlet+and+violet+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=Crown+Zenith+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&SubSearch=-thai+-russian+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Path=Cards%2fPokemon&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&Team=408021&TeamPath=Pokemon%2fPokemon_V%2fc408021&SubSearch=-thai+-russian+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&Team=407834&TeamPath=Pokemon%2fPokemon_GX%2fc407834&SubSearch=-thai+-russian+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&Team=408023&TeamPath=Pokemon%2fPokemon_VMAX%2fc408023&SubSearch=-thai+-russian+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Sort%3dr",
    "https://www.comc.com/SearchFeed?SportID=-13&Team=407940&TeamPath=Pokemon%2fMega_Pokemon%2fc407940&SubSearch=-thai+-russian+-japanese+-italian+-meiji+-topps&ListingFormat=b&GradeAction=Ungraded&Sort%3dr"
]

def fetch_xml(url):
    """Lädt die XML-Daten von der URL herunter und gibt sie zurück."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Überprüft, ob der Request erfolgreich war
        return response.content
    except requests.RequestException as e:
        print(f"Fehler beim Abrufen der URL {url}: {e}")
        return None

def save_to_file(filename, data):
    """Speichert die Daten in einer Datei."""
    try:
        with open(filename, 'wb') as file:
            file.write(data)
        print(f"Gespeichert: {filename}")
    except IOError as e:
        print(f"Fehler beim Speichern der Datei {filename}: {e}")

def generate_unique_filename():
    """Generiert einen Dateinamen basierend auf Datum, Zeit und einer Zufallszahl."""
    # Erhalte die aktuelle Zeit
    now = datetime.now()
    date_str = now.strftime("%d-%m-%y")  # z.B. 02-08-24
    time_str = now.strftime("%H-%M-%S")  # z.B. 17-36-45
    # Generiere eine zufällige Zahl
    random_number = random.randint(1000, 9999)
    # Setze den Dateinamen zusammen
    return f"{date_str}_{time_str}_{random_number}.xml"

def main():
    # Erstelle das Verzeichnis, wenn es nicht existiert
    if not os.path.exists('rss_files'):
        os.makedirs('rss_files')

    for url in urls:
        # Generiere einen einzigartigen Dateinamen
        file_name = generate_unique_filename()
        file_path = os.path.join('rss_files', file_name)
        
        # Lade die XML-Daten herunter
        xml_data = fetch_xml(url)
        if xml_data:
            # Speichere die XML-Daten in einer Datei
            save_to_file(file_path, xml_data)

if __name__ == "__main__":
    main()
