class StandPreseBonus:
    def __init__(self, codice, superficie, padiglione, prezzo, numeroprese):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.numeroprese = numeroprese
        self.prezzo = prezzo * (1 + 0.07 * numeroprese)

    def __str__(self):
        return f"{super.__str__()} con {self.numeroprese} prese aggiuntive"