from typing import List, Optional
from app.models.contact import Contact


class ContactService:
    """Service pour gérer les contacts"""

    def __init__(self):
        """Initialise le service avec une liste vide de contacts"""
        self.contacts: List[Contact] = []

    def ajouter_contact(self, nom: str, prenom: str, numero_portable: str) -> Contact:
        contact = Contact(nom, prenom, numero_portable)
        self.contacts.append(contact)
        return contact

    def existe_contact(self, nom: str, prenom: str, numero_portable: str) -> bool:
        """Retourne True si un contact identique existe deja"""
        for contact in self.contacts:
            if (
                contact.nom.lower() == nom.lower()
                and contact.prenom.lower() == prenom.lower()
                and contact.numero_portable == numero_portable
            ):
                return True
        return False

    def modifier_contact(
        self,
        numero_portable: str,
        nouveau_nom: str,
        nouveau_prenom: str,
        nouveau_numero: str,
    ) -> bool:
        """Modifie un contact a partir de son numero"""
        contact = self.rechercher_par_numero(numero_portable)
        if not contact:
            return False

        if (
            nouveau_numero != numero_portable
            and self.rechercher_par_numero(nouveau_numero)
        ):
            return False

        contact.nom = nouveau_nom
        contact.prenom = nouveau_prenom
        contact.numero_portable = nouveau_numero
        return True

    def rechercher_par_nom(self, nom: str) -> List[Contact]:

        return [
            c for c in self.contacts
            if nom.lower() in c.nom.lower()
        ]

    def rechercher_par_numero(self, numero: str) -> Optional[Contact]:

        for contact in self.contacts:
            if contact.numero_portable == numero:
                return contact
        return None

    def supprimer_contact(self, numero_portable: str) -> bool:

        for i, contact in enumerate(self.contacts):
            if contact.numero_portable == numero_portable:
                self.contacts.pop(i)
                return True
        return False

    def get_tous_contacts(self) -> List[Contact]:

        return self.contacts

    def clear_all(self):
        """Vide la liste de tous les contacts"""
        self.contacts.clear()
