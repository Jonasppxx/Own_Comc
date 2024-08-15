import json
import re

def verarbeite_urls(input_dateipfad, output_dateipfad):
    # Lese die JSON-Datei ein
    with open(input_dateipfad, 'r', encoding='utf-8') as file:
        daten = json.load(file)

    neue_daten = []

    for key, item in daten.items():  # Durchlaufe die Items im Dictionary
        url = item['guid']  # Extrahiere die URL aus dem aktuellen Item
        url = url.lower()  # Klein machen 
        url = url.strip()  # Entferne eventuelle Leerzeichen und Zeilenumbrüche
        url = url.replace("https://www.comc.com/cards/pokemon/", "https://www.pricecharting.com/game/")
 

        parts = url.split("/") #in die verschiedenen unterteilen
        positions_to_remove = [4,8,9,10,11]  #die die gelöscht werden müssen 

        positions_to_remove.sort(reverse=True)#KA

        for position in positions_to_remove: #KA
            if 0 <= position < len(parts): #KA
                parts.pop(position)  #KA

        url = '/'.join(parts) #wieder zusammen machen 

        part_to_move = parts.pop(5) # um die zahl nach hinten zu verschiene(herausnehmen)
        
        if parts:
            parts[-1] += '-' + part_to_move #das letzte entfernen"/" und mit einem - austauschen
        else:
            parts.append(part_to_move)

        url = '/'.join(parts) # wieder zusammenführen

        url = url.replace("_","-")
        url = url.replace("---","-")
        url = url.replace("--","-")
        url = url.replace("pokemon-base-set-base","pokemon-base-set")
        url = url.replace("holo-","")
        url = url.replace("pokemon-wizards-of-the-coast-exclusive-black-star-promos","pokemon-promo")
        url = url.replace("-german","")
        url = url.replace("-french","")
        url = url.replace("-spanish","")
        url = url.replace("-korean","")
        url = url.replace("-russian","")
        url = url.replace("-spanish-unlimited","")
        url = url.replace("impostor","imposter")


        
        url = re.sub(r'\(.*?\)|\[.*?\]|\{.*?\}', '', url)

        url = url.replace("--","-")


        
        
        

        if '1st-edition' in url:
            # Verwende einen regulären Ausdruck, um "1st-edition" zwischen den letzten zwei Segmenten einzufügen
            url = re.sub(r'([^/]+)-([^/]+)$', r'\1-1st-edition-\2', url)
            url = url.replace("pokemon-base-set-1st-edition","pokemon-base-set")
            url = url.replace("pokemon-base-set-shadowless","pokemon-base-set")

        if 'shadowless' in url:
            url = re.sub(r'([^/]+)-([^/]+)$', r'\1-shadowless-\2', url)
            url = url.replace("pokemon-base-set-shadowless","pokemon-base-set")
            url = url.replace("pokemon-base-set-1st-edition","pokemon-base-set")
        
        if 'missing-set' in url:

            url = re.sub(r'([^/]+)-([^/]+)$', r'\1-missing-set-\2', url)
            url = url.replace("pokemon-jungle-missing-set-symbol","pokemon-jungle")
            url = url.replace("missing-set","no-symbol")
        
        if 'reverse-foil' in url:

            url = re.sub(r'([^/]+)-([^/]+)$', r'\1-reverse-foil-\2', url)
            url = url.replace("reverse-foil","reverse-holo")
            
            

   


        url = url.replace("pokemon-fossil-base","pokemon-fossil")
        url = url.replace("pokemon-fossil-1st-edition","pokemon-fossil")
        url = url.replace("pokemon-jungle-base","pokemon-jungle")
        url = url.replace("pokemon-gym-heroes-base-1st-edition","pokemon-gym-heroes")
        url = url.replace("pokemon-gym-heroes-base-unlimited","pokemon-gym-heroes")
        url = url.replace("mistys-tentacruel-10","misty%27s-tentacruel-10")
        url = url.replace("the-rockets-training-gym-104","rocket%27s-training-gym-104")
        url = url.replace("the-rockets-trap-19","the-rocket%27s-trap-19")
        url = url.replace("brocks-sandslash-23","brock%27s-sandslash-23")
        url = url.replace("erikas-victreebel-26","erika%27s-victreebel-26")
        url = url.replace("mistys-cloyster-29","misty%27s-cloyster-29")
        url = url.replace("mistys-poliwrath-31","misty%27s-poliwrath-31")
        url = url.replace("rockets-snorlax-33","rocket%27s-snorlax-33")
        url = url.replace("sabrinas-venomoth-34","sabrina%27s-venomoth-34")
        url = url.replace("blaines-kangaskhan-36","blaine%27s-kangaskhan-36")
        url = url.replace("brocks-graveler-40","brock%27s-graveler-40")
        url = url.replace("erikas-weepinbell-48","erika%27s-weepinbell-48")
        url = url.replace("sabrinas-haunter-58","sabrina%27s-haunter-58")
        url = url.replace("lt-surges-fearow-7","lt-surge%27s-fearow-7")
        url = url.replace("lt-surges-pikachu-81","lt-surge%27s-pikachu-81")
        url = url.replace("pokemon-base-set-2-base","pokemon-base-set-2")
        url = url.replace("pokemon-neo-genesis-base-1st-edition","pokemon-neo-genesis-base")
        url = url.replace("pokemon-neo-genesis-base","pokemon-neo-genesis")
        url = url.replace("pokemon-neo-genesis-unlimited","pokemon-neo-genesis")
        url = url.replace("pokemon-team-rocket-base","pokemon-team-rocket")
        url = url.replace("rockets-sneak-attack-16","rocket%27s-sneak-attack-16")
        url = url.replace("pokemon-team-rocket-1st-edition","pokemon-team-rocket")
        url = url.replace("pokemon-legendary-collection-base","pokemon-legendary-collection")
        url = url.replace("pokemon-legendary-collection-reverse-holo","pokemon-legendary-collection")
        url = url.replace("nidoran-f-reverse-holo-82","nidoran-reverse-holo-82")
        url = url.replace("pokemon-legendary-collection-theme-deck-exclusive-non-holo","pokemon-legendary-collection")
        url = url.replace("pokemon-e-card-series-aquapolis-base","pokemon-aquapolis")
        url = url.replace("pokemon-aquapolis-reverse-holo","pokemon-aquapolis")
        url = url.replace("pokemon-e-card-series-expedition-base","pokemon-expedition")
        url = url.replace("pokemon-expedition-reverse-holo","pokemon-expedition")
        url = url.replace("pokemon-ex-ruby-sapphire-base","pokemon-ruby-&-sapphire")
        url = url.replace("pokemon-ruby-&-sapphire-reverse-holo","pokemon-ruby-&-sapphire")
        url = url.replace("pok�mon","pokemon")
        url = url.replace("é","e")
        url = url.replace("pokemon-ex-team-rocket-returns-base","pokemon-team-rocket-returns")
        url = url.replace("pokemon-team-rocket-returns-reverse-holo","pokemon-team-rocket-returns")
        url = url.replace("pokemon-ex-dragon-frontiers-expansion-set-base","pokemon-dragon-frontiers")
        url = url.replace("pokemon-dragon-frontiers-reverse-holo","pokemon-dragon-frontiers")
        url = url.replace("pokemon-diamond-pearl-base-set","pokemon-diamond-&-pearl")
        url = url.replace("pokemon-diamond-pearl-reverse-holo","pokemon-diamond-&-pearl")

        url = url.replace("pokemon-diamond-pearl-mysterious-treasures-base","pokemon-mysterious-treasures")
        url = url.replace("pokemon-diamond-pearl-great-encounters-base","pokemon-great-encounters")

        url = url.replace("pokemon-diamond-pearl-legends-awakened-base","pokemon-legends-awakened")
        url = url.replace("pokemon-legends-awakened-reverse-holo","pokemon-legends-awakened")
        url = url.replace("castform-51","castform-sunny-form-51")
        url = url.replace("pokemon-diamond-pearl-majestic-dawn-base","pokemon-majestic-dawn")
        url = url.replace("cyruss-conspiracy-105","cyrus%27s-conspiracy-105")
        url = url.replace("pokemon-platinum-base","pokemon-platinum")
        url = url.replace("palkia-12","palkia-g-12")
        url = url.replace("-1999-2000","")
        
        

        url= url.replace("darkrai-ex-044","darkrai-ex-44")
        url = url.replace("g-lvx","g-lv-x")
        url = url.replace("secret-electabuzz-128","electabuzz-128")
        url = url.replace("gyarados-30","gyarados-g-30")
        url = url.replace("pokemon-platinum-arceus-base","pokemon-arceus")
        url = url.replace("pokemon-arceus/zapdos-12","pokemon-arceus/zapdos-g-12")
        url = url.replace("pokemon-platinum-rising-rivals-base","pokemon-rising-rivals")
        url = url.replace("pokemon-rising-rivals-reverse-holo","pokemon-rising-rivals")
        url = url.replace("pokemon-platinum-supreme-victors-base","pokemon-supreme-victors")
        url = url.replace("pokemon-platinum-supreme-reverse-holo","pokemon-supreme-victors")
        url = url.replace("pokemon-heartgold-soulsilver-base","pokemon-heartgold-&-soulsilver")
        url = url.replace("pokemon-heartgold-&-soulsilver-reverse-holo","pokemon-heartgold-&-soulsilver")
        url = url.replace("pokemon-heartgold-soulsilver-triumphant-base","pokemon-triumphant")
        url = url.replace("pokemon-triumphant-reverse-holo","pokemon-triumphant")
        url = url.replace("pokemon-heartgold-soulsilver-undaunted-base","pokemon-undaunted")
        url = url.replace("pokemon-heartgold-soulsilver-unleashed-base","pokemon-unleashed")
        url = url.replace("crobat-prime-84","crobat-84?q=crobat+84")
        url = url.replace("pokemon-unleashed-reverse-holo","pokemon-unleashed")
        url = url.replace("pokemon-black-white-noble-victories-base","pokemon-noble-victories")
        url = url.replace("pokemon-heartgold-soulsilver-call-of-legends-base","pokemon-call-of-legends")
        url = url.replace("pokemon-call-of-legends-reverse-holo","pokemon-call-of-legends")
        url = url.replace("water-energy-reverse-holo-90","water-energy-90")
        url = url.replace("pokemon-black-white-emerging-powers-base","pokemon-emerging-powers")
        url = url.replace("pokemon-black-white-emerging-powers-reverse-holo","pokemon-emerging-powers")
        url = url.replace("full-art-thundurus-97","thundurus-97")
        url = url.replace("full-art-tornadus-98","tornadus-98")
        url = url.replace("pokemon-emerging-powers-reverse-holo","pokemon-emerging-powers")
        url = url.replace("pokemon-black-white","pokemon-black-&-white")
        url = url.replace("pokemon-black-&-white-pokemon-league-promo/snivy-1","pokemon-black-&-white/snivy-crosshatch-reverse-holo-1")
        url = url.replace("pokemon-black-&-white-pokemon-league-promo/watchog-79","pokemon-black-&-white/watchog-league-promo-79")
        url = url.replace("pokemon-black-&-white-boundaries-crossed-base","pokemon-boundaries-crossed")
        url = url.replace("pokemon-black-&-white-boundaries-crossed-reverse-holo","pokemon-boundaries-crossed")
        url = url.replace("full-art-celebi-ex-141","celebi-ex-141")
        url = url.replace("full-art-","")
        url = url.replace("pokemon-boundaries-crossed-reverse-holo","pokemon-boundaries-crossed")
        url = url.replace("pokemon-black-&-white-city-championships-staff-promo/eevee-84","pokemon-dark-explorers/eevee-city-championship-staff-84")
        url = url.replace("pokemon-black-&-white-winter-regional-championships-promo/flareon-12","pokemon-dark-explorers/flareon-regional-championships-12")
        url = url.replace("pokemon-dragon-vault-mini-set","pokemon-dragon-vault")
        url = url.replace("pokemon-black-&-white-dark-explorers-expansion-set-base","pokemon-dark-explorers")
        url = url.replace("pokemon-dark-explorers-reverse-holo","pokemon-dark-explorers")
        url = url.replace("hooligans-jim-cass-reverse-holo-95","hooligans-jim-&-cas-reverse-holo-95")
        url = url.replace("pokemon-black-&-white-dragons-exalted-base","pokemon-dragons-exalted")
        url = url.replace("blend-energy-wlfm-118","blend-energy-117")
        url = url.replace("pokemon-dragons-exalted-reverse-holo","pokemon-dragons-exalted")
        url = url.replace("pokemon-black-&-white-next-destinies-base","pokemon-next-destinies")
        url = url.replace("pokemon-next-destinies-reverse-holo","pokemon-next-destinies")
        url = url.replace("pokemon-black-&-white-legendary-treasures-base","pokemon-legendary-treasures")
        url = url.replace("pokemon-black-&-white-spring-regional-championships-promo/umbreon-60","pokemon-promo/umbreon-regional-champion-60")
        url = url.replace("pokemon-black-&-white-plasma-blast-base","pokemon-plasma-blast")
        url = url.replace("pokemon-xy-flashfire-base","pokemon-flashfire")
        url = url.replace("pokemon-flashfire-reverse-holo","pokemon-flashfire")
        url = url.replace("pokemon-xy-furious-fists-base-reverse-holo","pokemon-furious-fists")
        url = url.replace("pokemon-xy-furious-fists-base-base","pokemon-furious-fists")
        url = url.replace("pokemon-xy-phantom-forces-base","pokemon-phantom-forces")
        url = url.replace("pokemon-phantom-forces-reverse-holo","pokemon-phantom-forces")
        url = url.replace("battle-compressor-team-flare-gear-reverse-holo-92","battle-compressor-reverse-holo-92")
        url = url.replace("pokemon-xy-ancient-origins-reverse-holo","pokemon-ancient-origins")
        url = url.replace("pokemon-xy-ancient-origins-base","pokemon-ancient-origins")
        url = url.replace("pokemon-xy-roaring-skies-base","pokemon-roaring-skies")
        url = url.replace("shiny-ultra-rare-","")
        url = url.replace("ultra-rare-","")
        url = url.replace("secret-","")
        url = url.replace("team-magmas-groudon-ex-15","team-magma%27s-groudon-ex-15")
        url = url.replace("pokemon-xy-double-crisis-base","pokemon-double-crisis")
        url = url.replace("team-aquas-sharpedo-21","team-aqua%27s-sharpedo-21")
        url = url.replace("team-magmas-great-ball-31","team-magma%27s-great-ball-31")
        url = url.replace("team-aquas-kyogre-ex-6","team-aqua%27s-kyogre-ex-6")
        url = url.replace("pokemon-double-crisis-reverse-holo","pokemon-double-crisis")
        url = url.replace("pokemon-xy-fates-collide-base","pokemon-fates-collide")
        url = url.replace("pokemon-fates-collide-reverse-holo","pokemon-fates-collide-reverse-holo")
        url = url.replace("pokemon-xy-steam-siege-base-set","pokemon-steam-siege")
        url = url.replace("pokemon-xy-steam-siege-reverse-holo","pokemon-steam-siege")
        url = url.replace("pokemon-fates-collide-reverse-holo","pokemon-fates-collide")
        url = url.replace("pokemon-fates-collide-base-set","pokemon-fates-collide")
        url = url.replace("pokemon-xy-breakpoint-base","pokemon-breakpoint")
        url = url.replace("pokemon-breakpoint-reverse-holo","pokemon-breakpoint")
        url = url.replace("pokemon-xy-generations-base","pokemon-generations")
        url = url.replace("pokemon-generations-reverse-holo","pokemon-generations")
        url = url.replace("pokemon-xy-steam-siege-base","pokemon-steam-siege")
        url = url.replace("pokemon-steam-siege-reverse-holo","pokemon-steam-siege")
        url = url.replace("pokemon-xy-evolutions-20th-anniversary-base","pokemon-evolutions")
        url = url.replace("pokemon-evolutions-reverse-holo","pokemon-evolutions")
        url = url.replace("pokemon-sun-moon-shining-legends-base","pokemon-shining-legends")
        url = url.replace("rainbow-","")
        url = url.replace("pokemon-shining-legends-reverse-holo","pokemon-shining-legends")
        url = url.replace("pokemon-sun-moon-lost-thunder-base","pokemon-lost-thunder")
        url = url.replace("pokemon-lost-thunder-reverse-holo","pokemon-lost-thunder")
        url = url.replace("pokemon-sun-moon-dragon-majesty-base","pokemon-dragon-majesty")
        url = url.replace("pokemon-dragon-majesty-reverse-holo","pokemon-dragon-majesty")
        url = url.replace("pokemon-sun-moon-forbidden-light-base","pokemon-forbidden-light")
        url = url.replace("pokemon-forbidden-light-reverse-holo","pokemon-forbidden-light")
        url = url.replace("pokemon-sun-moon-team-up-base-set","pokemon-team-up")
        url = url.replace("pokemon-sun-moon-team-up-reverse-holo","pokemon-team-up")
        url = url.replace("pokemon-sun-moon-ultra-prism-base","pokemon-ultra-prism")
        url = url.replace("pokemon-ultra-prism-reverse-holo","pokemon-ultra-prism")
        url = url.replace("pokemon-sun-moon-team-up-base","pokemon-team-up")
        url = url.replace("pokemon-team-up-reverse-holo","pokemon-team-up")
        url = url.replace("pokemon-sun-moon-unified-minds-base","pokemon-unified-minds")
        url = url.replace("pokemon-unified-minds-reverse-holo","pokemon-unified-minds")
        url = url.replace("rowlet-alolan","rowlet-&-alolan")
        url = url.replace("alternate-art-","")
        url = url.replace("pokemon-sun-moon-cosmic-eclipse-base","pokemon-cosmic-eclipse")
        url = url.replace("pokemon-cosmic-eclipse-reverse-holo","pokemon-cosmic-eclipse")
        url = url.replace("venusaur-snivy","venusaur-&-snivy")
        url = url.replace("pokemon-sun-moon-hidden-fates-base","pokemon-hidden-fates")
        url = url.replace("pokemon-hidden-fates-reverse-holo","pokemon-hidden-fates")
        url = url.replace("pokemon-sun-moon-unbroken-bonds-base","pokemon-unbroken-bonds")
        url = url.replace("pokemon-unbroken-bonds-reverse-holo","pokemon-unbroken-bonds")
        url = url.replace("pheromosa-buzzwole","pheromosa-&-buzzwole")
        url = url.replace("lucario-melmetal","lucario-&-melmetal")
        url = url.replace("pokemon-sword-shield-rebel-clash-base","pokemon-rebel-clash")
        url = url.replace("pokemon-rebel-clash-reverse-holo","pokemon-rebel-clash")
        url = url.replace("pokemon-battle-academy-charizard-deck-base","pokemon-2020-battle-academy")
        url = url.replace("pokemon-sword-shield-darkness-ablaze-base","pokemon-darkness-ablaze")
        url = url.replace("pokemon-darkness-ablaze-reverse-holo","pokemon-darkness-ablaze")
        url = url.replace("charizard-vmax-020","charizard-vmax-20")
        url = url.replace("pokemon-sword-shield-vivid-voltage-base","pokemon-vivid-voltage")
        url = url.replace("pokemon-vivid-voltage-reverse-holo","pokemon-vivid-voltage")
        url = url.replace("charizard-reverse-holo-025","charizard-reverse-holo-25")
        url = url.replace("pokemon-sword-shield-chilling-reign-base","pokemon-chilling-reign")
        url = url.replace("pokemon-chilling-reign-reverse-holo","pokemon-chilling-reign")
        url = url.replace("pokemon-sword-shield-fusion-strike-base","pokemon-fusion-strike")
        url = url.replace("pokemon-fusion-strike-reverse-holo","pokemon-fusion-strike")
        url = url.replace("rotom-reverse-holo-094","rotom-reverse-holo-94")
        url = url.replace("pokemon-sword-shield-battle-styles-base","pokemon-battle-styles")
        url = url.replace("pokemon-battle-styles-reverse-holo","pokemon-battle-styles")
        url = url.replace("pokemon-sword-shield-evolving-skies-base","pokemon-evolving-skies")
        url = url.replace("pokemon-evolving-skies-reverse-holo","pokemon-evolving-skies")
        url = url.replace("flareon-vmax-018","flareon-vmax-18")
        url = url.replace("glaceon-vmax-041","glaceon-vmax-41")
        url = url.replace("pokemon-sword-shield-astral-radiance-base","pokemon-astral-radiance")
        url = url.replace("pokemon-astral-radiance-reverse-holo","pokemon-astral-radiance")
        url = url.replace("heatran-vmax-026","heatran-vmax-26")
        url = url.replace("origin-forme-palkia-vstar-040","origin-forme-palkia-vstar-40")
        url = url.replace("radiant-greninja-046","radiant-greninja-46")
        url = url.replace("pokemon-sword-shield-brilliant-stars-base","pokemon-brilliant-stars")
        url = url.replace("pokemon-brilliant-stars-reverse-holo","pokemon-brilliant-stars")
        url = url.replace("charizard-v-017","charizard-v-17")
        url = url.replace("flygon-reverse-holo-076","flygon-reverse-holo-76")
        url = url.replace("pokemon-sword-shield-lost-origin-base","pokemon-lost-origin")
        url = url.replace("pokemon-lost-origin-reverse-holo","pokemon-lost-origin")
        url = url.replace("oddish-reverse-holo-001","oddish-reverse-holo-1")
        url = url.replace("machop-reverse-holo-086","machop-reverse-holo-86")
        url = url.replace("rhyperior-reverse-holo-091","rhyperior-reverse-holo-91")
        url = url.replace("makuhita-reverse-holo-097","makuhita-reverse-holo-97")
        url = url.replace("pokemon-sword-shield-silver-tempest-base","pokemon-silver-tempest")
        url = url.replace("pokemon-silver-tempest-reverse-holo","pokemon-silver-tempest")
        url = url.replace("pokemon-scarlet-violet-paldean-fates-base","pokemon-paldean-fates")
        url = url.replace("shiny-rare-","")
        url = url.replace("oddish-092","oddish-92")
        url = url.replace("skiploom-097","skiploom-97")
        url = url.replace("shiny-forretress-ex-212","forretress-ex-212")
        url = url.replace("pokemon-scarlet-violet-svp-black-star-promos","pokemon-promo")
        url = url.replace("illustration-rare-","")
        url = url.replace("pokemon-scarlet-violet-base","pokemon-scarlet-violet")
        url = url.replace("pokemon-scarlet-violet-151-base","pokemon-scarlet-&-violet-151")
        url = url.replace("charizard-ex-006","charizard-ex-6")
        url = url.replace("special-","")
        url = url.replace("hyper-rare-","")
        url = url.replace("pokemon-scarlet-violet-paldea-evolved-base","pokemon-paldea-evolved")
        url = url.replace("chien-pao-ex-061","chien-pao-ex-61")
        url = url.replace("tadbulb-reverse-holo-077","tadbulb-reverse-holo-77")
        url = url.replace("pokemon-paldea-evolved-reverse-holo","pokemon-paldea-evolved")
        url = url.replace("pokemon-scarlet-violet-paradox-rift-base","pokemon-paradox-rift")
        url = url.replace("pokemon-paradox-rift-reverse-holo","pokemon-paradox-rift")
        url = url.replace("pokemon-scarlet-violet-obsidian-flames-base","pokemon-obsidian-flames")
        url = url.replace("pokemon-obsidian-flames-reverse-holo","pokemon-obsidian-flames")
        url = url.replace("pokemon-sword-shield-crown-zenith-base","pokemon-crown-zenith")
        url = url.replace("pokemon-crown-zenith-reverse-holo","pokemon-crown-zenith")
        url = url.replace("charizard-v-018","charizard-v-18")
        url = url.replace("charizard-vstar-019","charizard-vstar-19")
        url = url.replace("radiant-charizard-020","radiant-charizard-20")
        url = url.replace("zeraora-vstar-055","zeraora-vstar-55")
        url = url.replace("mew-v-060","mew-v-60")
        url = url.replace("pokemon-scarlet-violet-twilight-masquerade-base","pokemon-twilight-masquerade")
        url = url.replace("pokemon-twilight-masquerade-reverse-holo","pokemon-twilight-masquerades")
        url = url.replace("teal-mask-ogerpon-ex-025","teal-mask-ogerpon-ex-25")
        url = url.replace("magcargo-ex-029","magcargo-ex-29")
        url = url.replace("hearthflame-mask-ogerpon-ex-040","hearthflame-mask-ogerpon-ex-40")
        url = url.replace("pokemon-jungle-1st-edition","pokemon-jungle")
        url = url.replace("pokemon-base-set-printing","pokemon-base-set")
        url = url.replace("rare-","")
        url = url.replace("pokemon-sun-moon-lets-play-pikachu-theme-deck","pokemon-shining-legends")
        url = url.replace("-thai","")
        url = url.replace("shining-jirachi-073","shining-jirachi-73")
        url = url.replace("sr-pokemon-ranger-058","ranger-58")
        url = url.replace("gardevoir-ex-038","gardevoir-ex-38")
        url = url.replace("magearna-ex-035","magearna-ex-35")
        url = url.replace("volcanion-ex-012","volcanion-ex-12")
        url = url.replace("pikachu-vmax-044","pikachu-vmax-44")
        url = url.replace("charizard-v-019","charizard-v-19")
        url = url.replace("charizard-reverse-holo-010","charizard-reverse-holo-10")
        url = url.replace("radiant-blastoise-018","radiant-blastoise-18")
        url = url.replace("pokemon-sword-shield-pokemon-go-base","pokemon-go")
        url = url.replace("leafeon-vstar-014","leafeon-vstar-14")
        url = url.replace("dragonite-vstar-050","dragonite-vstar-50")
        url = url.replace("super-rare-","")
        url = url.replace("charizard-017","charizard-17")
        url = url.replace("charizard-010","charizard-10")
        url = url.replace("pikachu-reverse-holo-018","pikachu-reverse-holo-18")
        url = url.replace("pokemon-paldean-fates-reverse-holo","pokemon-paldean-fates")
        url = url.replace("blastoise-ex-009","blastoise-ex-9")
        url = url.replace("mew-ex-053","mew-ex-53")
        url = url.replace("double-rare-","")
        url = url.replace("leafeon-reverse-holo-011","leafeon-reverse-holo-11")
        url = url.replace("pikachu-088","pikachu-88")
        url = url.replace("pokemon-scarlet-violet-temporal-forces-base","pokemon-temporal-forces")
        url = url.replace("sylveon-vmax-075","sylveon-vmax-75")
        url = url.replace("pokemon-gym-challenge-base-unlimited","pokemon-gym-challenge")
        url = re.sub(r'\d+', lambda x: str(int(x.group()) * 1), url)

        parts = url.split('/')

# Überprüft, ob der zweitletzte Teil 'reverse-holo' enthält und entfernt es, falls nötig
        if '-reverse-holo' in parts[-2]:
            parts[-2] = parts[-2].replace('-reverse-holo', '')


        url = '/'.join(parts)


        


        
        
        

        


        # Füge das bearbeitete Item zu den neuen Daten hinzu
        neue_daten.append({
            "guid": item['guid'],
            "url": url,
            "salePrice": item['salePrice']
        })

    # Schreibe die neuen Daten in eine JSON-Datei
    with open(output_dateipfad, 'w', encoding='utf-8') as file:
        json.dump(neue_daten, file, ensure_ascii=False, indent=4)

# Beispielaufruf der Funktion mit dem angegebenen Pfad
verarbeite_urls('C:\\Users\\jonas\\OneDrive\\Desktop\\Own_comc\\today\\dumb\\2cards_data.json', 'C:\\Users\\jonas\\OneDrive\\Desktop\\Own_comc\\today\\dumb\\3cards_info.json')
