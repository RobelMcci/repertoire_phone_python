from app.services.contact_service import ContactService
import os


class GestionnaireContacts:
    """Classe pour gérer l'interface utilisateur console"""

    def __init__(self):
        self.service = ContactService()

    def nettoyer_ecran(self):
        os.system("clear" if os.name == "posix" else "cls")

    def afficher_menu_principal(self):
        """Affiche le menu principal"""
        print("\n" + "=" * 50)
        print("     GESTIONNAIRE DE CONTACTS")
        print("=" * 50)
        print("1. Ajouter un contact")
        print("2. Rechercher un contact")
        print("3. Afficher tous les contacts")
        print("4. Supprimer un contact")
        print("5. Quitter")
        print("=" * 50)

    def ajouter_contact(self):
        print("\n--- Ajouter un contact ---")
        try:
            nom = input("Nom: ").strip()
            if not nom:
                print("Le nom ne peut pas être vide!")
                return

            prenom = input("Prénom: ").strip()
            if not prenom:
                print("Le prénom ne peut pas être vide!")
                return

            numero = input("Numéro portable: ").strip()
            if not numero:
                print("Le numéro ne peut pas être vide!")
                return

            # Vérifier si le numéro existe déjà
            if self.service.rechercher_par_numero(numero):
                print(f"Un contact avec le numéro {numero} existe déjà!")
                return

            contact = self.service.ajouter_contact(nom, prenom, numero)
            print(f"Contact '{contact.prenom} {contact.nom}' ajouté avec succès!")
        except Exception as e:
            print(f"Erreur lors de l'ajout du contact: {e}")

    def rechercher_contact(self):
        print("\n--- Rechercher un contact ---")
        print("1. Rechercher par nom")
        print("2. Rechercher par numéro")
        choix = input("Votre choix: ").strip()

        if choix == "1":
            self.rechercher_par_nom()
        elif choix == "2":
            self.rechercher_par_numero()
        else:
            print("Choix invalide!")

    def rechercher_par_nom(self):
        nom = input("Nom à chercher: ").strip()
        if not nom:
            print("Le nom ne peut pas être vide!")
            return

        contacts = self.service.rechercher_par_nom(nom)
        if contacts:
            print(f"\n{len(contacts)} contact(s) trouvé(s):")
            for i, contact in enumerate(contacts, 1):
                print(f"   {i}. {contact}")
        else:
            print(f"Aucun contact trouvé avec le nom '{nom}'")

    def rechercher_par_numero(self):
        numero = input("Numéro à chercher: ").strip()
        if not numero:
            print("Le numéro ne peut pas être vide!")
            return

        contact = self.service.rechercher_par_numero(numero)
        if contact:
            print(f"\nContact trouvé:")
            print(f"   {contact}")
        else:
            print(f"Aucun contact trouvé avec le numéro '{numero}'")

    def afficher_tous_contacts(self):
        contacts = self.service.get_tous_contacts()
        
        print("\n--- Liste des contacts ---")
        if not contacts:
            print("Aucun contact dans la liste")
            return

        print(f"\nTotal: {len(contacts)} contact(s)\n")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact}")
        print()

    def supprimer_contact(self):
        print("\n--- Supprimer un contact ---")
        numero = input("Numéro du contact à supprimer: ").strip()
        
        if not numero:
            print("Le numéro ne peut pas être vide!")
            return

        # Afficher le contact avant suppression
        contact = self.service.rechercher_par_numero(numero)
        if contact:
            print(f"\nContact à supprimer: {contact}")
            confirmation = input("Confirmer la suppression? (oui/non): ").strip().lower()
            
            if confirmation in ["oui", "o", "yes", "y"]:
                if self.service.supprimer_contact(numero):
                    print("Contact supprimé avec succès!")
                else:
                    print("Erreur lors de la suppression du contact")
            else:
                print("Suppression annulée")
        else:
            print(f"Aucun contact trouvé avec le numéro '{numero}'")

    def lancer(self):
        while True:
            self.afficher_menu_principal()
            choix = input("\nVotre choix: ").strip()

            if choix == "1":
                self.ajouter_contact()
            elif choix == "2":
                self.rechercher_contact()
            elif choix == "3":
                self.afficher_tous_contacts()
            elif choix == "4":
                self.supprimer_contact()
            elif choix == "5":
                print("\n Au revoir!")
                break
            else:
                print("Choix invalide! Veuillez entrer un numéro entre 1 et 5")

            input("\nAppuyez sur Entrée pour continuer...")


def main():
    """Fonction principale"""
    gestionnaire = GestionnaireContacts()
    gestionnaire.lancer()


if __name__ == "__main__":
    main()
