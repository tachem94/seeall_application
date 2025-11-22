# -*- coding: utf-8 -*-
"""
SEE ALL AVKN - Configuration File
Fichier de configuration pour personnaliser les paramètres de l'application

Author: Claude Assistant  
Date: November 2025
"""

# =============================================================================
# INFORMATIONS SOCIÉTÉ
# =============================================================================

COMPANY_CONFIG = {
    # Nom de la société
    'name': 'SEE ALL AVKN',
    
    # Adresse complète (utilisez \\n pour les retours à la ligne)
    'address': '38 rue Dunois\n75013 PARIS',
    
    # Contact
    'email': 'michael@seeall.fr',
    'phone': '',  # Optionnel
    'website': '',  # Optionnel
    
    # Informations légales
    'siren': '951 474 709',
    'siret': '95147470900015',
    'tva': 'FR95951474709',
    'legal_form': 'SAS',
    'capital': '1 000,00 €',
    'rcs': '951 474 709 R.C.S. Paris',
    
    # Informations bancaires
    'bank_bic': 'CMCIFRPP',
    'bank_iban': 'FR76 3006 6109 4100 0210 0820 254',
    'bank_name': '',  # Optionnel
}

# =============================================================================
# PARAMÈTRES MÉTIER
# =============================================================================

BUSINESS_CONFIG = {
    # Taux de TVA par défaut (0.20 = 20%)
    'default_vat_rate': 0.20,
    
    # Devise
    'currency': '€',
    'currency_position': 'after',  # 'before' ou 'after'
    
    # Conditions de paiement
    'payment_terms': 'VIREMENT',
    'payment_delay_penalty': 'trois fois le taux d\'intérêt légal',
    'recovery_fee': '40€',
    'no_discount_text': 'Nos conditions de ventes ne prévoient pas d\'escompte en cas de paiement anticipé.',
    
    # Préfixes pour la numérotation
    'quote_prefix': 'SA',      # Préfixe pour les devis
    'invoice_prefix': 'FA',    # Préfixe pour les factures
    
    # Format de date (Python strftime format)
    'date_format': '%d/%m/%Y',
}

# =============================================================================
# PARAMÈTRES INTERFACE
# =============================================================================

UI_CONFIG = {
    # Titre de la fenêtre principale
    'window_title': 'SEE ALL AVKN - Gestion Devis & Factures',
    
    # Taille de la fenêtre principale
    'window_size': '1200x800',
    
    # Thème de l'interface ('clam', 'alt', 'default', 'classic')
    'theme': 'clam',
    
    # Colonnes à afficher dans les listes
    'client_columns': ('ID', 'Nom', 'SIRET', 'Email', 'Téléphone'),
    'quote_columns': ('Numéro', 'Client', 'Date', 'Total HT', 'Total TTC', 'Actions'),
    'invoice_columns': ('Numéro Facture', 'Bon de Commande', 'Client', 'Date', 'Total HT', 'Total TTC'),
}

# =============================================================================
# PARAMÈTRES EXPORT
# =============================================================================

EXPORT_CONFIG = {
    # Dossier par défaut pour les exports (None = demander à l'utilisateur)
    'default_export_folder': None,
    
    # Format de nom de fichier pour les exports
    'quote_filename_format': 'devis_{number}',
    'invoice_filename_format': 'facture_{number}',
    
    # Inclure la date dans le nom de fichier
    'include_date_in_filename': True,
    'filename_date_format': '%Y%m%d',
    
    # Paramètres PDF
    'pdf_pagesize': 'A4',  # A4, LETTER, etc.
    'pdf_margin': 2,       # Marges en cm
    
    # Paramètres Word
    'word_font': 'Calibri',
    'word_font_size': 11,
}

# =============================================================================
# MESSAGES ET TEXTES
# =============================================================================

MESSAGES_CONFIG = {
    # Messages de succès
    'client_added': 'Client ajouté avec succès',
    'quote_saved': 'Devis sauvegardé avec le numéro: {number}',
    'invoice_created': 'Devis converti en facture: {number}',
    'export_success': 'Document exporté: {filepath}',
    
    # Messages d'erreur
    'client_name_required': 'Le nom du client est obligatoire',
    'invalid_price': 'Prix invalide',
    'no_selection': 'Veuillez sélectionner un élément',
    'no_items': 'Veuillez ajouter au moins un article',
    'export_error': 'Erreur lors de l\'export: {error}',
    
    # Textes des documents
    'quote_title': 'DEVIS',
    'invoice_title': 'FACTURE',
    'client_label': 'Client:',
    'date_label': 'Date:',
    'number_label': 'Numéro:',
    'order_number_label': 'Bon de commande:',
    'description_label': 'Description',
    'price_ht_label': 'Prix HT',
    'total_ht_label': 'Montant total HT:',
    'total_vat_label': 'Montant total TVA:',
    'total_ttc_label': 'Montant total TTC:',
    'net_to_pay_label': 'NET A PAYER:',
    'payment_method_label': 'Mode de règlement par',
}

# =============================================================================
# PARAMÈTRES BASE DE DONNÉES
# =============================================================================

DATABASE_CONFIG = {
    # Nom du fichier de base de données
    'database_filename': 'seeall_database.db',
    
    # Sauvegarde automatique (en minutes, 0 = désactivée)
    'auto_backup_interval': 0,
    
    # Dossier de sauvegarde
    'backup_folder': 'backups',
    
    # Nombre maximum de sauvegardes à conserver
    'max_backups': 10,
}

# =============================================================================
# PARAMÈTRES AVANCÉS
# =============================================================================

ADVANCED_CONFIG = {
    # Debug mode (affiche plus d'informations en cas d'erreur)
    'debug_mode': False,
    
    # Logging (fichier de log)
    'enable_logging': False,
    'log_filename': 'seeall_app.log',
    'log_level': 'INFO',  # DEBUG, INFO, WARNING, ERROR
    
    # Validation automatique des données
    'validate_siret': False,
    'validate_email': True,
    'validate_phone': False,
    
    # Limites
    'max_items_per_quote': 50,
    'max_description_length': 500,
}

# =============================================================================
# FONCTIONS D'AIDE
# =============================================================================

def get_formatted_company_address():
    """Retourne l'adresse de l'entreprise formatée pour l'affichage"""
    return COMPANY_CONFIG['address'].replace('\\n', '\n')

def get_legal_text():
    """Retourne le texte légal complet pour les documents"""
    return (f"La Société dénommée {COMPANY_CONFIG['name']}, {COMPANY_CONFIG['legal_form']}, "
            f"au capital social de {COMPANY_CONFIG['capital']}, inscrit sous le numéro "
            f"de Siren {COMPANY_CONFIG['siren']}/ Siret n°{COMPANY_CONFIG['siret']} "
            f"au RCS de PARIS")

def get_payment_conditions():
    """Retourne les conditions de paiement complètes"""
    return (f"(En cas de retard de paiement, une pénalité égale à {BUSINESS_CONFIG['payment_delay_penalty']} "
            f"sera exigible et une indemnité pour frais de recouvrement de {BUSINESS_CONFIG['recovery_fee']} "
            f"sera appliquée article L.441-6). {BUSINESS_CONFIG['no_discount_text']}")

def format_currency(amount):
    """Formate un montant selon la configuration de devise"""
    if BUSINESS_CONFIG['currency_position'] == 'before':
        return f"{BUSINESS_CONFIG['currency']}{amount:.2f}"
    else:
        return f"{amount:.2f} {BUSINESS_CONFIG['currency']}"

# =============================================================================
# VALIDATION DE LA CONFIGURATION
# =============================================================================

def validate_config():
    """Valide la configuration et retourne les erreurs éventuelles"""
    errors = []
    
    # Vérifications obligatoires
    required_fields = ['name', 'siren', 'siret', 'tva']
    for field in required_fields:
        if not COMPANY_CONFIG.get(field):
            errors.append(f"Champ obligatoire manquant: COMPANY_CONFIG['{field}']")
    
    # Vérification du taux de TVA
    vat_rate = BUSINESS_CONFIG.get('default_vat_rate', 0)
    if not isinstance(vat_rate, (int, float)) or vat_rate < 0 or vat_rate > 1:
        errors.append("Le taux de TVA doit être un nombre entre 0 et 1")
    
    return errors

# Test de la configuration au chargement du module
if __name__ == "__main__":
    errors = validate_config()
    if errors:
        print("Erreurs de configuration détectées:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("Configuration valide ✅")
        print(f"Société: {COMPANY_CONFIG['name']}")
        print(f"TVA: {BUSINESS_CONFIG['default_vat_rate']*100}%")
        print(f"Devise: {BUSINESS_CONFIG['currency']}")
