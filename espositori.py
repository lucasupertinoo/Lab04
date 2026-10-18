class Espositori():
    def __init__(self, ID, nome, cognome):
        self.ID = ID
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"L'espositore identificato con il codice {(self.ID)} si chiama {(self.nome)} {(self.cognome)}."