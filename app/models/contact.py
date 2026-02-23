"""Modèle Contact"""


class Contact:
    """Classe représentant un contact"""

    def __init__(self, nom: str, prenom: str, numero_portable: str):
        """
        Initialise un contact

        Args:
            nom: Le nom du contact
            prenom: Le prénom du contact
            numero_portable: Le numéro de téléphone portable
        """
        self.nom = nom
        self.prenom = prenom
        self.numero_portable = numero_portable

    def __str__(self) -> str:
        """Retourne une représentation lisible du contact"""
        return f"{self.prenom} {self.nom} - {self.numero_portable}"

    def __repr__(self) -> str:
        """Retourne une représentation du contact"""
        return f"Contact({self.nom}, {self.prenom}, {self.numero_portable})"
