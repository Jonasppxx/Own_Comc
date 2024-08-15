import json
import requests
from bs4 import BeautifulSoup
import time
import sys
import os

def fetch_price(url):
    """Holt den aktuellen Preis von der angegebenen URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Überprüfe, ob die Anfrage erfolgreich war
        soup = BeautifulSoup(response.text, 'html.parser')
        price_span = soup.find('span', class_='price js-price')
        if price_span:
            price_text = price_span.get_text(strip=True).replace('$', '')
            return float(price_text)
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def process_json_file(json_file):
    """Verarbeitet die JSON-Datei, vergleicht die Preise und gibt die Ergebnisse aus."""
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        results = []
        error_urls = []
        errors = 0
        total_urls = len(data)
        checked_urls = 0

        for i, item in enumerate(data):
            url = item.get('url')
            guid = item.get('guid')
            comc_price = item.get('salePrice')

            if url:
                current_price = fetch_price(url)
                if current_price is not None:
                    checked_urls += 1
                    if float(comc_price) < current_price:
                        result = {
                            'guid': guid,
                            'url': url,
                            'comc': comc_price,  # Ursprünglicher Sale Price
                            'pricecharting': current_price  # Aktueller Preis
                        }
                        results.append(result)
                else:
                    errors += 1
                    error_urls.append(url)  # Speichern der URL direkt

                # Warte 2 Sekunden bevor die nächste URL überprüft wird
                time.sleep(1.5)

                # Live-Update der Statusanzeige
                sys.stdout.write(f"\rProcessed: {checked_urls}/{total_urls} URLs | Errors: {errors}")
                sys.stdout.flush()

        return results, error_urls, total_urls, checked_urls, errors

    except Exception as e:
        print(f"Error processing JSON file: {e}", file=sys.stderr)
        return [], [], 0, 0, 1

def save_to_json(data, output_file):
    """Speichert die Daten in eine neue JSON-Datei."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\nData saved to {output_file}")
    except Exception as e:
        print(f"Error saving data to file: {e}", file=sys.stderr)

def main():
    folder_path = r'C:\Users\jonas\OneDrive\Desktop\Own_comc\today\dumb'
    input_json_file = os.path.join(folder_path, '3cards_info.json')
    output_json_file = os.path.join(folder_path, '4filtered_cards_info.json')
    error_urls_file = os.path.join(folder_path, 'error_urls.json')

    filtered_data, error_urls, total_urls, checked_urls, errors = process_json_file(input_json_file)

    save_to_json(filtered_data, output_json_file)
    save_to_json(error_urls, error_urls_file)  # Fehler-URLs speichern

    # Ausgabe der finalen Ergebnisse
    print(f"\nTotal URLs: {total_urls}")
    print(f"Checked URLs: {checked_urls}")
    print(f"Errors: {errors}")

if __name__ == "__main__":
    main()
