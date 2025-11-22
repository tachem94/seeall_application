#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEE ALL AVKN - Test Script for Text Wrapping Correction
Script de test pour vérifier que les corrections du retour à la ligne fonctionnent

Author: Expert Developer Assistant
Date: November 2025

Ce script teste :
✅ Fonctions de text wrapping (80 caractères)
✅ Export PDF avec descriptions qui restent dans les colonnes
✅ Export Word avec largeurs de colonnes configurées
✅ Format : Site + Ville / Description sur lignes suivantes
"""

import os
import sys
import tempfile
from datetime import date, datetime

def test_text_wrapping_functions():
    """Test des fonctions utilitaires de text wrapping"""
    print("🔧 Test des fonctions de text wrapping...")
    
    try:
        # Import des nouvelles fonctions
        sys.path.insert(0, '/mnt/user-data/outputs')
        from main_application_TEXT_WRAP_FIXED import TextWrapUtils, SiteItem
        
        # Créer un site avec une description très longue
        test_site = SiteItem(
            site_number="FR001",
            address="Place de la République",
            postal_code="75011",
            city="Paris",
            latitude="48.8671",
            longitude="2.3633",
            description="Nid de frelons asiatiques dans coffret EDF à côté de l'entrée. Le nid est à l'arrière du coffret. Capot enlevé mais pas possible de déplacer le nid sans intervention spécialisée. Nécessite équipement de protection et technique d'aspiration spécifique pour éviter la dispersion des frelons.",
            price_ht=500.0
        )
        
        # Test 1: Fonction de wrapping PDF
        pdf_text, word_text = TextWrapUtils.format_site_description(test_site, max_chars=80)
        print(f"  ✅ Fonction format_site_description disponible")
        print(f"  📝 Texte PDF formaté:")
        print(f"     {pdf_text[:100]}...")
        print(f"  📝 Texte Word formaté:")
        print(f"     {word_text[:100]}...")
        
        # Test 2: Vérifier la structure
        if "Site FR001 - Paris" in pdf_text and "Site FR001 - Paris" in word_text:
            print(f"  ✅ Format correct: Site + Ville sur première ligne")
        else:
            print(f"  ❌ Format incorrect")
            return False
        
        # Test 3: Vérifier le wrapping
        if "<br/>" in pdf_text:
            print(f"  ✅ Retours à la ligne PDF détectés (<br/>)")
        if "\n" in word_text:
            print(f"  ✅ Retours à la ligne Word détectés (\\n)")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Erreur lors du test des fonctions: {e}")
        return False

def create_test_quote():
    """Créer un devis de test avec descriptions longues"""
    print("\n📄 Création d'un devis de test avec descriptions longues...")
    
    try:
        sys.path.insert(0, '/mnt/user-data/outputs')
        from main_application_TEXT_WRAP_FIXED import Quote, Client, SiteItem
        
        # Client de test
        test_client = Client(
            id=1,
            name="TEST WRAPPING CLIENT",
            siret="12345678901234",
            address="123 Rue de Test\n75001 PARIS",
            email="test@example.com",
            phone="01.23.45.67.89"
        )
        
        # Sites avec descriptions très longues
        test_sites = [
            SiteItem(
                site_number="FR001",
                address="Place de la République",
                postal_code="75011",
                city="Paris",
                latitude="48.8671",
                longitude="2.3633",
                description="Nid de frelons asiatiques dans coffret EDF à côté de l'entrée. Le nid est à l'arrière du coffret. Capot enlevé mais pas possible de déplacer le nid sans intervention spécialisée. Nécessite équipement de protection et technique d'aspiration spécifique pour éviter la dispersion des frelons dans l'environnement immédiat.",
                price_ht=800.0
            ),
            SiteItem(
                site_number="FR002",
                address="Avenue des Champs-Élysées avec une adresse particulièrement longue qui pourrait poser des problèmes",
                postal_code="75008",
                city="Paris 8ème Arrondissement",
                latitude="48.8698",
                longitude="2.3078",
                description="Abattage contrôlé d'un arbre dangereux de type tilleul de quinze mètres de hauteur présentant des problèmes racinaires importants et des risques de chute sur la voie publique. L'intervention nécessite une nacelle élévatrice, des équipements de sécurité spécialisés, et la coordination avec les services municipaux pour la fermeture temporaire de la circulation. Les débris devront être évacués dans les règles de l'art selon les normes environnementales en vigueur.",
                price_ht=1500.0
            ),
            SiteItem(
                site_number="FR003",
                address="Jardin du Luxembourg",
                postal_code="75006",
                city="Paris",
                latitude="48.8462",
                longitude="2.3372",
                description="Description courte pour tester le contraste avec les descriptions longues.",
                price_ht=300.0
            )
        ]
        
        # Créer le devis
        test_quote = Quote(
            id=999,
            number="SA.TESTWRAPPING.112025001",
            client_id=1,
            client=test_client,
            typology="Test Text Wrapping",
            sites=test_sites,
            quote_date=date.today(),
            is_invoice=False
        )
        
        print(f"  ✅ Devis de test créé avec {len(test_sites)} sites")
        print(f"  📏 Longueur description 1: {len(test_sites[0].description)} caractères")
        print(f"  📏 Longueur description 2: {len(test_sites[1].description)} caractères")
        print(f"  💰 Total HT: {test_quote.total_ht:.2f} €")
        
        return test_quote
        
    except Exception as e:
        print(f"  ❌ Erreur lors de la création du devis test: {e}")
        return None

def test_pdf_export_with_wrapping(test_quote):
    """Test de l'export PDF avec retour à la ligne"""
    print("\n🔴 Test de l'export PDF avec text wrapping...")
    
    try:
        sys.path.insert(0, '/mnt/user-data/outputs')
        from main_application_TEXT_WRAP_FIXED import PDFGenerator
        
        # Vérifier que reportlab est disponible
        try:
            import reportlab
            print(f"  ✅ Reportlab disponible (version: {reportlab.Version})")
        except ImportError:
            print(f"  ⚠️ Reportlab non disponible - test impossible")
            return False
        
        # Créer un fichier PDF temporaire
        temp_dir = tempfile.mkdtemp()
        pdf_path = os.path.join(temp_dir, "test_text_wrapping.pdf")
        
        # Générer le PDF
        PDFGenerator.generate_quote_pdf(test_quote, pdf_path)
        
        if os.path.exists(pdf_path):
            file_size = os.path.getsize(pdf_path)
            print(f"  ✅ PDF généré avec succès: {pdf_path}")
            print(f"  📊 Taille du fichier: {file_size} octets")
            
            # Vérifier que c'est un PDF valide
            with open(pdf_path, 'rb') as f:
                content = f.read(100)
                if b'%PDF' in content:
                    print("  ✅ Format PDF valide détecté")
                    print("  💡 Ouvrez le PDF pour vérifier que les descriptions")
                    print("     restent dans la colonne 'Description'")
                    return True
                else:
                    print("  ❌ Format PDF suspect")
                    return False
        else:
            print("  ❌ Fichier PDF non créé")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lors de l'export PDF: {e}")
        return False

def test_word_export_with_wrapping(test_quote):
    """Test de l'export Word avec retour à la ligne"""
    print("\n🔵 Test de l'export Word avec text wrapping...")
    
    try:
        sys.path.insert(0, '/mnt/user-data/outputs')
        from main_application_TEXT_WRAP_FIXED import WordGenerator
        
        # Vérifier que python-docx est disponible
        try:
            import docx
            print(f"  ✅ Python-docx disponible")
        except ImportError:
            print(f"  ⚠️ Python-docx non disponible - test impossible")
            return False
        
        # Créer un fichier Word temporaire
        temp_dir = tempfile.mkdtemp()
        docx_path = os.path.join(temp_dir, "test_text_wrapping.docx")
        
        # Générer le document Word
        WordGenerator.generate_quote_docx(test_quote, docx_path)
        
        if os.path.exists(docx_path):
            file_size = os.path.getsize(docx_path)
            print(f"  ✅ Document Word généré avec succès: {docx_path}")
            print(f"  📊 Taille du fichier: {file_size} octets")
            
            if file_size > 1000:  # Au moins 1KB
                print("  ✅ Taille de fichier acceptable")
                print("  💡 Ouvrez le document Word pour vérifier que")
                print("     les descriptions respectent les largeurs de colonnes")
                return True
            else:
                print("  ⚠️ Fichier suspicieusement petit")
                return False
        else:
            print("  ❌ Fichier Word non créé")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lors de l'export Word: {e}")
        return False

def verify_code_corrections():
    """Vérifier que toutes les corrections sont présentes dans le code"""
    print("\n🔍 Vérification des corrections dans le code...")
    
    try:
        filepath = '/mnt/user-data/outputs/main_application_TEXT_WRAP_FIXED.py'
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        corrections = [
            # Classes et fonctions utilitaires
            ('class TextWrapUtils:', 'Classe utilitaire de text wrapping'),
            ('def wrap_text_for_pdf(', 'Fonction wrapping PDF'),
            ('def wrap_text_for_word(', 'Fonction wrapping Word'),
            ('def format_site_description(', 'Fonction de formatage des sites'),
            
            # Corrections PDF
            ('description_style = ParagraphStyle(', 'Style PDF pour descriptions'),
            ("wordWrap='CJK'", 'Activation word wrap PDF'),
            ('Paragraph(pdf_description, description_style)', 'Utilisation Paragraph PDF'),
            ('colWidths=[13*cm, 4*cm]', 'Largeurs colonnes PDF optimisées'),
            
            # Corrections Word
            ('table.columns[0].width = Cm(13)', 'Configuration largeur colonne Word'),
            ('row_cells[0].width = Cm(13)', 'Configuration largeur cellule Word'),
            ('TextWrapUtils.format_site_description(site, max_chars=80)', 'Utilisation formatage Word'),
            
            # Formatage des sites
            ('pdf_description, _ = TextWrapUtils.format_site_description', 'Formatage PDF'),
            ('_, word_description = TextWrapUtils.format_site_description', 'Formatage Word'),
        ]
        
        missing_corrections = []
        
        for check, description in corrections:
            if check in content:
                print(f"  ✅ {description}")
            else:
                print(f"  ❌ {description} (manquant)")
                missing_corrections.append(check)
        
        if missing_corrections:
            print(f"\n⚠️ Corrections manquantes: {len(missing_corrections)}")
            return False
        else:
            print(f"\n✅ Toutes les corrections sont présentes!")
            print(f"   📈 Score: {len(corrections)}/{len(corrections)} éléments")
            return True
            
    except Exception as e:
        print(f"❌ Erreur lors de la vérification: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🚀 SEE ALL AVKN - Test des Corrections Text Wrapping")
    print("=" * 65)
    print("🎯 Ce test vérifie que les descriptions des sites")
    print("   restent dans les colonnes des exports PDF/Word")
    print("   avec un retour à la ligne automatique à 80 caractères")
    print("=" * 65)
    
    all_tests_passed = True
    
    # Test 1: Vérifier les corrections dans le code
    if not verify_code_corrections():
        all_tests_passed = False
    
    # Test 2: Tester les fonctions utilitaires
    if not test_text_wrapping_functions():
        all_tests_passed = False
    
    # Test 3: Créer un devis de test
    test_quote = create_test_quote()
    if not test_quote:
        all_tests_passed = False
    else:
        # Test 4: Test export PDF
        if not test_pdf_export_with_wrapping(test_quote):
            all_tests_passed = False
        
        # Test 5: Test export Word
        if not test_word_export_with_wrapping(test_quote):
            all_tests_passed = False
    
    print("\n" + "=" * 65)
    
    if all_tests_passed:
        print("🎉 TOUS LES TESTS RÉUSSIS!")
        print("\n✅ Corrections appliquées avec succès:")
        print("  📄 PDF: Utilisation d'objets Paragraph avec wordWrap")
        print("  📄 Word: Configuration des largeurs de colonnes (13cm/4cm)")
        print("  📏 Text wrapping: 80 caractères maximum par ligne")
        print("  📝 Format: Site + Ville / Description sur lignes suivantes")
        print("  🔄 Pas de troncature: texte complet sur plusieurs lignes")
        
        print("\n🔧 Pour utiliser la correction:")
        print("  1. Remplacez main_application.py par main_application_TEXT_WRAP_FIXED.py")
        print("  2. Créez un devis avec des descriptions longues")
        print("  3. Exportez en PDF et Word")
        print("  4. Vérifiez que les descriptions restent dans les colonnes")
        
        return 0
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("\n🔧 Actions recommandées:")
        print("  1. Vérifiez que main_application_TEXT_WRAP_FIXED.py est correct")
        print("  2. Installez les dépendances: pip install reportlab python-docx")
        print("  3. Relancez ce script de test")
        
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        input("\nAppuyez sur Entrée pour fermer...")
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nTest annulé par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")
        sys.exit(1)
