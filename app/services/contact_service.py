"""Service de gestion des contacts"""

from typing import List, Optional
from app.models.contact import Contact


class ContactService:
    """Service pour gérer les contacts"""

    def __init__(self):
        """Initialise le service avec une liste vide de contacts"""
        self.contacts: List[Contact] = []

    def ajouter_contact(self, nom: str, prenom: str, numero_portable: str) -> Contact:
        """
        Ajoute un nouveau contact

        Args:
            nom: Le nom du contact
            prenom: Le prénom du contact
            numero_portable: Le numéro de téléphone portable

        Returns:
            Le contact créé
        """
        contact = Contact(nom, prenom, numero_portable)
        self.contacts.append(contact)
        return contact

    def rechercher_par_nom(self, nom: str) -> List[Contact]:
        """
        Recherche les contacts par nom (correspondance partielle)

        Args:
            nom: Le nom à chercher

        Returns:
            Liste des contacts correspondant au nom
        """
        return [
            c for c in self.contacts
            if nom.lower() in c.nom.lower()
        ]

    def rechercher_par_numero(self, numero: str) -> Optional[Contact]:
        """
        Recherche un contact par numéro de téléphone

        Args:
            numero: Le numéro à chercher

        Returns:
            Le contact correspondant ou None
        """
        for contact in self.contacts:
            if contact.numero_portable == numero:
                return contact
        return None

    def supprimer_contact(self, numero_portable: str) -> bool:
        """
        Supprime un contact par son numéro de téléphone

        Args:
            numero_portable: Le numéro du contact à supprimer

        Returns:
            True si le contact a été supprimé, False sinon
        """
        for i, contact in enumerate(self.contacts):
            if contact.numero_portable == numero_portable:
                self.contacts.pop(i)
                return True
        return False

    def get_tous_contacts(self) -> List[Contact]:
        """
        Retourne tous les contacts

        Returns:
            Liste de tous les contacts
        """
        return self.contacts

    def clear_all(self):
        """Vide la liste de tous les contacts"""
        self.contacts.clear()
