class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo

    def __str__(self):
        return f"Lo stand identificato con il codice {self.codice} copre una superficie di {self.superficie} metri quadrati, si trova nel padiglione {self.padiglione} e costa {self.prezzo}€. "