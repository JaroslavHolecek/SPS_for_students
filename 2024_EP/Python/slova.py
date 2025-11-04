clanek = """Po příchodu do Palestiny

Po svém příchodu pracoval jako zemědělský dělník a politický aktivista.[3] Brzy na to vstoupil do Židovské legie, jež byla součástí britské armády, a během první světové války bojoval proti Turkům. Po válce patřil ke skupině osadníků, která v roce 1920 založila kibuc Deganja Bet.[4] V roce 1921 se stal jedním ze zakládajících členů Histadrutu a v roce 1930 byl u založení strany Mapaj. V roce 1937 sehrál důležitou roli při založení vodní společnosti Mekorot a z této pozice hrál rovněž významnou roli při přesvědčování německé vlády v umožnění židovské emigrace do Palestiny (emigrující si mohli část svého majetku vyměnit za německé zboží, které si poté mohli vzít s sebou).[4] Ve společnosti Mekorot působil jako výkonný ředitel až do roku 1951 a do té doby zavedl systém státního vodohospodářství, které umožnilo intenzivní zemědělské zavlažování. Vrcholem jeho úsilí se stalo vybudování Národního rozvaděče vody, který byl spuštěn v roce 1964, kdy již byl premiérem.[4]

V roce 1940 vstoupil do Hagany a stal se členem jejího vrchního velení, kde byl zodpovědný za nákup zbraní. Během izraelské války za nezávislost se stal vůbec prvním generálním ředitelem na ministerstvu obrany a během svého působení v tomto úřadě se aktivně podílel na budování izraelského obranného průmyslu. V tomto období si rovněž hebraizoval své příjmení na Eškol.[3] V letech 1944 až 1948 byl tajemníkem telavivského magistrátu a od roku 1948 se stal rovněž předsedou Světové sionistické organizace.[2] Byl rovněž členem vedení Židovské agentury, kde zastával dvě významné funkce, a to konkrétně funkci pokladníka (v letech 1949 až 1951) a ředitele oddělení osadnictví (v letech 1948 až 1963).[5] """

mnozina = set()
for slovo in clanek.split(" "):
    mnozina.add(slovo)

print("Počet unikátních slov:", len(mnozina))