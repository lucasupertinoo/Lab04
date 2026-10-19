from stand import Stand   # Importo la superclasse

class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, espositore_assegnato, disponibile, posizione):
        super().__init__(codice, superficie, padiglione, prezzo, espositore_assegnato, disponibile)  #Super richiama la superclasse
        self.posizione = posizione
        self.prezzo = prezzo * 1.3   # Modifico il prezzo con l'aggiunta fissa del 30%

    def __str__(self):
        return f"{super().__str__()} posizionato nella zona {self.posizione}"   # Concateno la stampa della superclasse a cosa c'è solo qua