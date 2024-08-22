import json
import os

def calculate_percentage_difference(value1, value2):
    """
    Berechnet den Prozentsatz der Ungleichheit zwischen zwei Werten.
    """
    value1 = float(value1)
    value2 = float(value2)
    
    max_value = max(value1, value2)
    min_value = min(value1, value2)
    
    difference = max_value - min_value
    percentage_difference = (difference / max_value) * 100
    
    return percentage_difference

def main():
    """
    Hauptfunktion des Skripts, die die Daten aus der JSON-Datei liest,
    den Prozentsatz der Ungleichheit berechnet, und die Karten nach der Differenz sortiert.
    """
    input_file = os.path.join(os.path.dirname(__file__), 'dumb',"4filtered_cards_info.json")  # Der Pfad zur JSON-Datei
    output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '5sorted_cards_by_difference.json')    
    
    # Überprüfen, ob die Eingabedatei existiert
    if not os.path.exists(input_file):
        print(f"Die Datei {input_file} wurde nicht gefunden. Bitte überprüfen.")
        return
    
    # Lade die bestehenden JSON-Daten
    with open(input_file, 'r', encoding='utf-8') as f:
        cards_data = json.load(f)
    
    # Berechne die Differenzen und speichere die Ergebnisse
    cards_with_differences = []
    
    for card in cards_data:
        comc_price = card.get('comc')
        pricecharting_price = card.get('pricecharting')
        
        # Berechne den Unterschied, wenn beide Preise vorhanden sind
        if comc_price and pricecharting_price:
            percentage_difference = calculate_percentage_difference(comc_price, pricecharting_price)
            
            # Berücksichtige nur Karten mit einer Differenz größer oder gleich 1,5%
            if percentage_difference >= 1.5:
                card['difference'] = percentage_difference
                cards_with_differences.append(card)
    
    # Sortiere die Karten nach der Differenz (höchste zuerst)
    sorted_cards = sorted(cards_with_differences, key=lambda x: x['difference'], reverse=True)
    
    # Speichere die sortierten Karten in der neuen JSON-Datei
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sorted_cards, f, indent=4, ensure_ascii=False)
    
    print(f"Sorted data saved to {output_file}")

if __name__ == "__main__":
    main()
