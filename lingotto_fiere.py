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
                        stand_normale = Stand(campo[0], campo[1], campo[2], campo[3], None, True)
                        self.stand.append(stand_normale)
                    elif len(campo) == 5 and campo[4].isnumeric():
                        stand_con_prese = StandPreseBonus(campo[0], campo[1], campo[2], campo[3], None, True, campo[4])
                        self.stand.append(stand_con_prese)
                    elif len(campo) == 5 and campo[4].isalpha():
                        stand_prem = StandPremium(campo[0], campo[1], campo[2], campo[3], None, True, campo[4])
                        self.stand.append(stand_prem)
                elif campo[0][0] == "E":
                    espositore_nuovo = Espositori(campo[0], campo[1], campo[2], None)
                    self.espositori.append(espositore_nuovo)

        file.close()


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        standtrovato = False
        espositoretrovato = False
        for st in self.stand:
            if st.codice == codice_stand:
                standtrovato = True
                disponibilita = st.disponibile
        for esp in self.espositori:
            if esp.codice == codice_espositore:
                espositoretrovato = True
                associazione = esp.stand_associato

        if not standtrovato:
            raise("Stand non trovato!")
        elif not espositoretrovato:
            raise("Espositoretro non trovato!")

        if not disponibilita:
            raise("Stand non disponibile!")

        if associazione != None:
            raise("Espositore già associato ad uno stand!")

        st.disponibilita = False
        st.espositore_associato = codice_espositore
        esp.stand_associato = codice_stand


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for elemento in self.espositori:
            return elemento

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.stand, key=lambda stand: stand.prezzo)
