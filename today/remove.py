from number_worth import remove_dates
import json
from datetime import datetime, timedelta
import os

if remove_dates == True:
    def filter_cards_by_today(file_path):
        # Heutiges und gestriges Datum im Format "02 Aug 2024"
        today_date = datetime.now().strftime("%d %b %Y")
        yesterday_date = (datetime.now() - timedelta(days=1)).strftime("%d %b %Y")
        print(today_date)
        print(yesterday_date)
    
        # JSON-Datei laden
        with open(file_path, 'r', encoding='utf-8') as f:
            cards_data = json.load(f)
    
        # Neue Sammlung für gefilterte Karten erstellen
        filtered_cards = {}
    
        for card_key, card_info in cards_data.items():
            pub_date = card_info.get("pubDate", "")
        
            # Extrahiere das Datum aus dem pubDate (z.B. "02 Aug 2024")
            pub_date_extracted = " ".join(pub_date.split()[1:4])
        
            # Wenn pubDate mit dem heutigen oder gestrigen Datum übereinstimmt, die Karte behalten
            if pub_date_extracted in (today_date, yesterday_date):
                filtered_cards[card_key] = card_info
    
        # Gefilterte Karten direkt in der ursprünglichen JSON-Datei speichern
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(filtered_cards, f, indent=4, ensure_ascii=False)
    
        print(f"Data in {file_path} has been filtered and saved.")

    if __name__ == "__main__":
        file_path = os.path.join(os.path.dirname(__file__), 'dumb', '2cards_data.json')
    
        filter_cards_by_today(file_path)
    print("Daten wurden entfernt")

else:
    print("Keine Daten wurden entfernt")