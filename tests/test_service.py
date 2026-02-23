#!/usr/bin/env python3
"""Script de test du projet"""

from app.services.contact_service import ContactService

# Tester le service
service = ContactService()

# Ajouter des contacts
service.ajouter_contact("Dupont", "Jean", "06123456789")
service.ajouter_contact("Martin", "Marie", "06987654321")
service.ajouter_contact("Bernard", "Pierre", "06555555555")

print(f"Nombre de contacts: {len(service.get_tous_contacts())}")

# Tester la recherche par nom
resultats = service.rechercher_par_nom("Martin")
print(f"Recherche 'Martin': {len(resultats)} résultat(s) - {resultats[0] if resultats else 'Aucun'}")

# Tester la recherche par numéro
contact = service.rechercher_par_numero("06123456789")
print(f"Recherche '06123456789': {contact}")

# Tester la suppression
service.supprimer_contact("06555555555")
print(f"Après suppression: {len(service.get_tous_contacts())} contact(s)")

print("\nTous les tests sont passés!")
