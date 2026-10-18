class StandPremium:
    def __init__(self, codice, superficie, padiglione, prezzo, posizione):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.posizione = posizione
        self.prezzo = prezzo * 1.3

    def __str__(self):
        return f"{super.__str__()} posizionato nella zona {self.posizione}"