from espositori import Espositori
from stand import Stand
from stand_premium import StandPremium
from stand_prese_bonus import StandPreseBonus

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.stand = []
        self.espositori = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nuovoNome):
        self._nome = nuovoNome

    @property
    def espositori(self):
        return self.espositori
    @espositori.setter
    def espositori(self, nuovoEspositore):
        self.espositori.append(nuovoEspositore)

    @property
    def stand(self):
        return self.stand
    @stand.setter
    def stand(self, nuovoStand):
        self.stand.append(nuovoStand)


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            file = open(file_path, "r", encoding="utf-8")
        except Exception as e:
            print(e)

        file.readline()
        for line in file:
            while line != "":
                campo = line.strip().split(",")
                if campo[0][0] == "S":
                    if len(campo) == 4:
                        stand_normale = Stand(campo[0], campo[1], campo[2], campo[3])
                        self.stand.append(stand_normale)
                    elif len(campo) == 5 and campo[4].isnumeric():
                        stand_con_prese = StandPreseBonus(campo[0], campo[1], campo[2], campo[3], campo[4])
                        self.stand.append(stand_con_prese)
                    elif len(campo) == 5 and campo[4].isalpha():
                        stand_prem = StandPremium(campo[0], campo[1], campo[2], campo[3], campo[4])
                        self.stand.append(stand_prem)
                elif campo[0][0] == "E":
                    espositore_nuovo = Espositori(campo[0], campo[1], campo[2])
                    self.espositori.append(espositore_nuovo)

        file.close()


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
