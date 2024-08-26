import xml.etree.ElementTree as ET
import os
import json
import re
from number_worth import price_cart


def extract_card_info_from_description(description, guid):
    # Sale Price extrahieren
    sale_price_match = re.search(r'Sale Price: \$([\d.]+)', description)
    sale_price = sale_price_match.group(1) if sale_price_match else 'N/A'
    
    # Card Number extrahieren
    card_info_match = re.search(r'#(\d+)', description)
    card_number = card_info_match.group(1) if card_info_match else 'N/A'
    
    # Entferne führende Nullen aus der Card Number
    card_number = card_number.lstrip('0')
    
    # Card Name extrahieren
    card_name_match = re.search(r'#\d+\s-\s(.+?)(?:<br />|$)', description)
    card_name = card_name_match.group(1).strip() if card_name_match else 'N/A'
    
    # Entferne unerwünschte Begriffe aus dem Kartennamen
    cleaned_card_name = re.sub(
        r'^(Ultra Rare|Illustration Rare|Hyper Rare|Special Illustration Rare|Super Rare|Shiny Rare|Shiny Ultra Rare|Secret - |Full Art - |Double Rare - |Art Rare - |Special Art Rare - |Shiny Super Rare - |Alternate Art - |Single Strike |Rapid Strike |Rainbow - |-|[^\w\s])', 
        '', 
        card_name
    ).strip()
    
    # Entferne Details in Klammern und eckigen Klammern
    cleaned_card_name = re.sub(
        r'\s*\[.*?\]|\(.*?\)',  # Entfernt alle Details in Klammern oder eckigen Klammern
        '', 
        cleaned_card_name
    ).strip()
    
    # Entferne HTML-Entities
    cleaned_card_name = re.sub(
        r'\s*\&nbsp\;*\s*',  # Entfernt HTML-Entities wie &nbsp;
        ' ', 
        cleaned_card_name
    ).strip()
    
    cleaned_card_name = re.sub(
        r'\s*&#8209;\s*',  # Entfernt HTML-Entities wie &#8209;
        ' ', 
        cleaned_card_name
    ).strip()
    
    # Entferne das &-Zeichen und verbinde die Wörter ohne Leerzeichen
    cleaned_card_name = cleaned_card_name.replace('&', '').replace('  ', ' ').replace(' ', '')
    
    # Entferne führende Bindestriche oder unerwünschte Zeichen
    cleaned_card_name = re.sub(r'^\s*-+', '', cleaned_card_name).strip()
    
    # Entferne überflüssige Leerzeichen, die durch das Entfernen der Begriffe entstanden sind
    cleaned_card_name = re.sub(r'\s+', ' ', cleaned_card_name).strip()
    
    # Wenn der bereinigte Name leer ist, setze ihn auf "N/A"
    if not cleaned_card_name:
        cleaned_card_name = 'N/A'
    
    # Falls salePrice "N/A" ist, setze es auf 0.0 für die Preisprüfung
    sale_price_value = float(sale_price) if sale_price != 'N/A' else 0.0
    
    return sale_price_value, card_number, cleaned_card_name

def extract_guids_from_file(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    cards = {}
    
    for item in root.findall(".//item"):
        guid = item.find('guid').text
        description = item.find('description').text
        pub_date = item.find('pubDate').text  # Veröffentlichungsdatum extrahieren
        
        sale_price, card_number, cleaned_card_name = extract_card_info_from_description(description, guid)
        
        # Speichere die Karte nur, wenn der Kartennamen nicht "N/A" und der Sale-Preis über 2.00 USD ist
        if cleaned_card_name != "N/A" and sale_price > price_cart:
            card_info = {
                'guid': guid,
                'salePrice': sale_price,
                'cardNumber': card_number,
                'cardName': cleaned_card_name,
                'pubDate': pub_date  # Veröffentlichungsdatum speichern
            }
            
            # Vermeide Duplikate durch Verwendung von GUID als Schlüssel
            cards[guid] = card_info
    
    return cards

def extract_guids_from_folder(folder_path):
    all_cards = {}
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing file: {filename}")
            cards = extract_guids_from_file(file_path)
            for guid, card in cards.items():
                card_name = card['cardName']
                card_number = card['cardNumber']
                
                # Schlüssel für Duplikat-Prüfung
                key = (card_name, card_number)
                
                if key not in all_cards:
                    all_cards[key] = card
    
    # Konvertiere zurück in eine Liste, um das gewünschte Format zu erhalten
    all_cards_list_format = {f"{name[0]} #{name[1]}": card for name, card in all_cards.items()}
    
    return all_cards_list_format

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    folder_path =  os.path.join(os.path.dirname(__file__), 'dumb')
    output_file = os.path.join(folder_path, '2cards_data.json')
    
    all_cards = extract_guids_from_folder(folder_path)
    save_to_json(all_cards, output_file)
    print(f"Data saved to {output_file}")
