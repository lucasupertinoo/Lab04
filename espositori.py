class Espositori():
    def __init__(self, ID, nome, cognome, stand_associato):
        self.ID = ID
        self.nome = nome
        self.cognome = cognome
        self.stand_associato = stand_associato

    def __str__(self):
        if self.stand_associato == None:
            return f"L'espositore identificato con il codice {(self.ID)} si chiama {(self.nome)} {(self.cognome)} e non è associato a nessuno stand"
        return f"L'espositore identificato con il codice {(self.ID)} si chiama {(self.nome)} {(self.cognome)} ed è associato allo stand {(self.stand_associato.codice)}"