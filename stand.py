class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo, espositore_assegnato, disponibile):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo
        self.espositore_assegnato = espositore_assegnato
        self.disponibile = disponibile

    def __str__(self):
        if self.disponibile == True:
            return f"Lo stand identificato con il codice {self.codice} copre una superficie di {self.superficie} metri quadrati, si trova nel padiglione {self.padiglione} e costa {self.prezzo}€. Attualmente è disponibile."
        else:
            return f"Lo stand identificato con il codice {self.codice} copre una superficie di {self.superficie} metri quadrati, si trova nel padiglione {self.padiglione} e costa {self.prezzo}€. Attualmente risulta assegnato all'espositore {self.espositore_assegnato}."

    def __lt__(self, other):
        return self.prezzo < other.prezzo