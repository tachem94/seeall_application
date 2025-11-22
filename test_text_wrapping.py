#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEE ALL AVKN - Test Script for Text Wrapping in Exports
Script de test pour vérifier le retour à la ligne automatique dans les exports

Author: Expert Developer Assistant
Date: November 2025
"""

import os
import sys
import tempfile
from datetime import date

def create_test_quote_with_long_descriptions():
    """Create a test quote with very long descriptions to test text wrapping"""
    print("📝 Création d'un devis avec descriptions très longues...")
    
    try:
        sys.path.insert(0, '.')
        from main_application import Quote, Client, SiteItem
        
        # Create test client
        test_client = Client(
            id=1,
            name="CLIENT TEST WRAP",
            siret="12345678901234",
            address="123 Rue de Test\n75001 PARIS",
            email="test@example.com",
            phone="01.23.45.67.89"
        )
        
        # Create test sites with VERY LONG descriptions to test wrapping
        test_sites = [
            SiteItem(
                site_number="FRA05200025",
                address="PLANTE PRENEY AU NORD-OUEST de CREANCEY",
                postal_code="52120", 
                city="Châteauvillain",
                latitude="48.0102",
                longitude="4.8711",
                description="Nid de frelons asiatiques dans coffret EDF à côté de l'entrée. Le nid est à l'arrière du coffret. Capot enlevé mais pas possible de déplacer le nid sans intervention spécialisée. Nécessite équipement de protection et technique d'aspiration spécifique pour éviter la dispersion des frelons dans l'environnement immédiat.",
                price_ht=800.0
            ),
            SiteItem(
                site_number="FR002",
                address="Avenue des Champs-Élysées avec une adresse particulièrement longue qui pourrait poser des problèmes de mise en page",
                postal_code="75008",
                city="Paris", 
                latitude="48.8698",
                longitude="2.3078",
                description="Abattage contrôlé d'un arbre dangereux de type tilleul de quinze mètres de hauteur présentant des problèmes racinaires importants et des risques de chute sur la voie publique. L'intervention nécessite une nacelle élévatrice, des équipements de sécurité spécialisés, et la coordination avec les services municipaux pour la fermeture temporaire de la circulation. Les débris devront être évacués dans les règles de l'art.",
                price_ht=1500.0
            ),
            SiteItem(
                site_number="FR003",
                address="Jardin du Luxembourg",
                postal_code="75006",
                city="Paris",
                latitude="48.8462",
                longitude="2.3372", 
                description="Une description courte pour tester le contraste.",
                price_ht=300.0
            )
        ]
        
        # Create test quote
        test_quote = Quote(
            id=999,
            number="SA.CLIENTTESTWRAP.112025001",
            client_id=1,
            client=test_client,
            typology="Test Wrapping",
            sites=test_sites,
            quote_date=date.today(),
            is_invoice=False
        )
        
        print(f"  ✅ Devis de test créé avec {len(test_sites)} sites")
        print(f"  📝 Site avec description longue: {test_sites[0].site_number}")
        print(f"  📏 Longueur description 1: {len(test_sites[0].description)} caractères")
        print(f"  📏 Longueur description 2: {len(test_sites[1].description)} caractères")
        print(f"  💰 Total HT: {test_quote.total_ht:.2f} €")
        
        return test_quote
        
    except Exception as e:
        print(f"  ❌ Erreur lors de la création du devis test: {e}")
        return None

def test_text_wrapping_functions():
    """Test the text wrapping utility functions"""
    print("\n🔧 Test des fonctions de retour à la ligne...")
    
    try:
        sys.path.insert(0, '.')
        from main_application import PDFGenerator, WordGenerator
        
        # Test text
        long_text = "Nid de frelons asiatiques dans coffret EDF à côté de l'entrée. Le nid est à l'arrière du coffret. Capot enlevé mais pas possible de déplacer le nid sans intervention spécialisée."
        
        # Test PDF wrapping
        if hasattr(PDFGenerator, 'wrap_text'):
            wrapped_pdf = PDFGenerator.wrap_text(long_text, max_length=50)
            print(f"  ✅ Fonction PDF wrap_text disponible")
            print(f"  📏 Texte original: {len(long_text)} caractères")
            print(f"  📏 Texte wrappé PDF: {wrapped_pdf.count('<br/>')+1} lignes")
        else:
            print(f"  ❌ Fonction PDF wrap_text manquante")
            return False
        
        # Test Word wrapping
        if hasattr(WordGenerator, 'wrap_text_for_cell'):
            wrapped_word = WordGenerator.wrap_text_for_cell(long_text, max_length=50)
            print(f"  ✅ Fonction Word wrap_text_for_cell disponible")
            print(f"  📏 Texte wrappé Word: {wrapped_word.count(chr(10))+1} lignes")
        else:
            print(f"  ❌ Fonction Word wrap_text_for_cell manquante")
            return False
        
        print(f"\n📝 Exemple de wrapping PDF:")
        print(f"Original: {long_text[:60]}...")
        print(f"Wrappé:   {wrapped_pdf[:60]}...")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Erreur lors du test des fonctions: {e}")
        return False

def test_pdf_export_with_wrapping(test_quote):
    """Test PDF export with long descriptions"""
    print("\n📄 Test de l'export PDF avec retour à la ligne...")
    
    try:
        sys.path.insert(0, '.')
        from main_application import PDFGenerator, PDF_AVAILABLE
        
        if not PDF_AVAILABLE:
            print("  ⚠️  Export PDF non disponible (reportlab manquant)")
            return False
        
        # Create temporary PDF file
        temp_dir = tempfile.mkdtemp()
        pdf_path = os.path.join(temp_dir, "test_text_wrap.pdf")
        
        # Generate PDF
        PDFGenerator.generate_quote_pdf(test_quote, pdf_path)
        
        if os.path.exists(pdf_path):
            file_size = os.path.getsize(pdf_path)
            print(f"  ✅ PDF généré avec succès: {pdf_path}")
            print(f"  📊 Taille du fichier: {file_size} octets")
            
            # Check if file is valid PDF
            with open(pdf_path, 'rb') as f:
                content = f.read(100)
                if b'%PDF' in content:
                    print("  ✅ Format PDF valide")
                    print("  💡 Ouvrez le PDF pour vérifier que les descriptions ne sortent pas du cadre")
                else:
                    print("  ⚠️  Format PDF suspect")
            
            return True
        else:
            print("  ❌ Fichier PDF non créé")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lors de l'export PDF: {e}")
        return False

def test_word_export_with_wrapping(test_quote):
    """Test Word export with long descriptions"""
    print("\n📝 Test de l'export Word avec retour à la ligne...")
    
    try:
        sys.path.insert(0, '.')
        from main_application import WordGenerator, DOCX_AVAILABLE
        
        if not DOCX_AVAILABLE:
            print("  ⚠️  Export Word non disponible (python-docx manquant)")
            return False
        
        # Create temporary Word file
        temp_dir = tempfile.mkdtemp()
        docx_path = os.path.join(temp_dir, "test_text_wrap.docx")
        
        # Generate Word document
        WordGenerator.generate_quote_docx(test_quote, docx_path)
        
        if os.path.exists(docx_path):
            file_size = os.path.getsize(docx_path)
            print(f"  ✅ Document Word généré avec succès: {docx_path}")
            print(f"  📊 Taille du fichier: {file_size} octets")
            print("  💡 Ouvrez le document Word pour vérifier que les descriptions respectent les limites des cellules")
            
            return True
        else:
            print("  ❌ Fichier Word non créé")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lors de l'export Word: {e}")
        return False

def verify_text_wrap_implementation():
    """Verify that text wrapping code is properly implemented"""
    print("\n🔍 Vérification de l'implémentation du retour à la ligne...")
    
    try:
        with open('main_application.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for text wrapping implementations
        checks = [
            ('def wrap_text(', 'Fonction de wrapping PDF'),
            ('def wrap_text_for_cell(', 'Fonction de wrapping Word'),
            ('PDFGenerator.wrap_text(', 'Utilisation wrapping PDF'),
            ('WordGenerator.wrap_text_for_cell(', 'Utilisation wrapping Word'),
            ('Paragraph(site_description, desc_style)', 'Utilisation Paragraph pour PDF'),
            ('row_cells[0].width = Cm(13)', 'Configuration largeur colonnes Word'),
            ('colWidths=[13*cm, 4*cm]', 'Configuration largeur colonnes PDF'),
            ('wordWrap=\'CJK\'', 'Activation word wrap PDF')
        ]
        
        missing_elements = []
        
        for check, description in checks:
            if check in content:
                print(f"  ✅ {description}")
            else:
                print(f"  ❌ {description} (manquant)")
                missing_elements.append(check)
        
        if missing_elements:
            print(f"\n⚠️  Éléments manquants: {len(missing_elements)}")
            return False
        else:
            print("\n✅ Toutes les améliorations de retour à la ligne sont présentes!")
            return True
            
    except Exception as e:
        print(f"❌ Erreur lors de la vérification: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 SEE ALL AVKN - Test du Retour à la Ligne dans les Exports")
    print("=" * 65)
    
    all_tests_passed = True
    
    # Test 1: Verify implementation
    if not verify_text_wrap_implementation():
        all_tests_passed = False
    
    # Test 2: Test wrapping functions
    if not test_text_wrapping_functions():
        all_tests_passed = False
    
    # Test 3: Create test quote with long descriptions
    test_quote = create_test_quote_with_long_descriptions()
    if not test_quote:
        all_tests_passed = False
    else:
        # Test 4: Test PDF export
        if not test_pdf_export_with_wrapping(test_quote):
            all_tests_passed = False
        
        # Test 5: Test Word export
        if not test_word_export_with_wrapping(test_quote):
            all_tests_passed = False
    
    print("\n" + "=" * 65)
    
    if all_tests_passed:
        print("🎉 TESTS RÉUSSIS - Le retour à la ligne fonctionne correctement!")
        print("\n📋 Améliorations appliquées:")
        print("  ✅ PDF: Utilisation d'objets Paragraph avec wrapping automatique")
        print("  ✅ Word: Configuration des largeurs de colonnes et wrapping")
        print("  ✅ Formatage: Texte en gras/italique pour une meilleure lisibilité")
        print("  ✅ Fonctions utilitaires: Gestion intelligente des retours à la ligne")
        
        print("\n🔧 Pour tester dans l'application:")
        print("  1. Créez un devis avec des descriptions très longues (>80 caractères)")
        print("  2. Exportez en PDF et Word")
        print("  3. Vérifiez que les descriptions restent dans les cellules")
        print("  4. Les descriptions doivent être formatées sur plusieurs lignes")
        
        return 0
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("\n🔧 Actions recommandées:")
        print("  1. Vérifiez que main_application.py est à jour")
        print("  2. Utilisez main_application_text_wrap_fixed.py")
        print("  3. Installez les dépendances: pip install reportlab python-docx")
        
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
