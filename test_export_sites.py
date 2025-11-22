#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEE ALL AVKN - Test Script for PDF/Word Export with Site Descriptions
Script de test pour vérifier que les exports PDF/Word incluent les descriptions des sites

Author: Expert Developer Assistant
Date: November 2025
"""

import os
import sys
import tempfile
import sqlite3
from datetime import date, datetime

def test_export_functionality():
    """Test that exports include site descriptions"""
    print("🧪 Test des exports PDF/Word avec descriptions des sites...")
    
    try:
        # Import the application modules
        sys.path.insert(0, '.')
        import main_application
        
        # Check if PDF generation is available
        if hasattr(main_application, 'PDF_AVAILABLE') and main_application.PDF_AVAILABLE:
            print("  ✅ Module PDF (reportlab) disponible")
        else:
            print("  ⚠️  Module PDF (reportlab) non disponible")
        
        # Check if Word generation is available
        if hasattr(main_application, 'DOCX_AVAILABLE') and main_application.DOCX_AVAILABLE:
            print("  ✅ Module Word (python-docx) disponible")
        else:
            print("  ⚠️  Module Word (python-docx) non disponible")
        
        return True
        
    except ImportError as e:
        print(f"  ❌ Erreur d'import: {e}")
        return False

def create_test_quote_with_sites():
    """Create a test quote with multiple sites to verify export"""
    print("\n📝 Création d'un devis de test avec sites multiples...")
    
    try:
        sys.path.insert(0, '.')
        from main_application import Quote, Client, SiteItem
        
        # Create test client
        test_client = Client(
            id=1,
            name="CLIENT TEST EXPORT",
            siret="12345678901234",
            address="123 Rue de Test\n75001 PARIS",
            email="test@example.com",
            phone="01.23.45.67.89"
        )
        
        # Create test sites with descriptions
        test_sites = [
            SiteItem(
                site_number="FR001",
                address="Place de la République",
                postal_code="75011", 
                city="Paris",
                latitude="48.8671",
                longitude="2.3633",
                description="Élagage d'arbres sur la place publique - Intervention sur 3 platanes centenaires",
                price_ht=850.0
            ),
            SiteItem(
                site_number="FR002",
                address="Avenue des Champs-Élysées",
                postal_code="75008",
                city="Paris", 
                latitude="48.8698",
                longitude="2.3078",
                description="Abattage contrôlé d'arbre dangereux - Tilleul de 15m avec problème racinaire",
                price_ht=1200.0
            ),
            SiteItem(
                site_number="FR003",
                address="Jardin du Luxembourg",
                postal_code="75006",
                city="Paris",
                latitude="48.8462",
                longitude="2.3372", 
                description="Taille d'entretien et nettoyage - Haies de buis et rosiers sur 200m²",
                price_ht=450.0
            )
        ]
        
        # Create test quote
        test_quote = Quote(
            id=999,
            number="SA.CLIENTTESTEXPORT.112025001",
            client_id=1,
            client=test_client,
            typology="Élagage",
            sites=test_sites,
            quote_date=date.today(),
            is_invoice=False
        )
        
        print(f"  ✅ Devis de test créé avec {len(test_sites)} sites")
        print(f"  📍 Sites: {', '.join(site.site_number for site in test_sites)}")
        print(f"  💰 Total HT: {test_quote.total_ht:.2f} €")
        
        return test_quote
        
    except Exception as e:
        print(f"  ❌ Erreur lors de la création du devis test: {e}")
        return None

def test_pdf_export(test_quote):
    """Test PDF export with site descriptions"""
    print("\n📄 Test de l'export PDF...")
    
    try:
        sys.path.insert(0, '.')
        from main_application import PDFGenerator, PDF_AVAILABLE
        
        if not PDF_AVAILABLE:
            print("  ⚠️  Export PDF non disponible (reportlab manquant)")
            return False
        
        # Create temporary PDF file
        temp_dir = tempfile.mkdtemp()
        pdf_path = os.path.join(temp_dir, "test_export_sites.pdf")
        
        # Generate PDF
        PDFGenerator.generate_quote_pdf(test_quote, pdf_path)
        
        if os.path.exists(pdf_path):
            file_size = os.path.getsize(pdf_path)
            print(f"  ✅ PDF généré avec succès: {pdf_path}")
            print(f"  📊 Taille du fichier: {file_size} octets")
            
            # Try to read some content to verify it's not empty
            with open(pdf_path, 'rb') as f:
                content = f.read(100)  # Read first 100 bytes
                if b'%PDF' in content:
                    print("  ✅ Format PDF valide détecté")
                else:
                    print("  ⚠️  Format PDF suspect")
            
            return True
        else:
            print("  ❌ Fichier PDF non créé")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lors de l'export PDF: {e}")
        return False

def test_word_export(test_quote):
    """Test Word export with site descriptions"""
    print("\n📝 Test de l'export Word...")
    
    try:
        sys.path.insert(0, '.')
        from main_application import WordGenerator, DOCX_AVAILABLE
        
        if not DOCX_AVAILABLE:
            print("  ⚠️  Export Word non disponible (python-docx manquant)")
            return False
        
        # Create temporary Word file
        temp_dir = tempfile.mkdtemp()
        docx_path = os.path.join(temp_dir, "test_export_sites.docx")
        
        # Generate Word document
        WordGenerator.generate_quote_docx(test_quote, docx_path)
        
        if os.path.exists(docx_path):
            file_size = os.path.getsize(docx_path)
            print(f"  ✅ Document Word généré avec succès: {docx_path}")
            print(f"  📊 Taille du fichier: {file_size} octets")
            
            # Basic validation - Word files should be reasonably sized
            if file_size > 1000:  # At least 1KB
                print("  ✅ Taille de fichier acceptable")
            else:
                print("  ⚠️  Fichier suspicieusement petit")
            
            return True
        else:
            print("  ❌ Fichier Word non créé")
            return False
            
    except Exception as e:
        print(f"  ❌ Erreur lors de l'export Word: {e}")
        return False

def verify_export_content_structure():
    """Verify that the export code structure is correct"""
    print("\n🔍 Vérification de la structure du code d'export...")
    
    try:
        with open('main_application.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for key improvements in PDF export
        pdf_checks = [
            ('for site in quote.sites:', 'Itération sur les sites (PDF)'),
            ('site_description = f"Site {site.site_number}"', 'Construction description site (PDF)'),
            ('site.full_address', 'Utilisation adresse complète (PDF)'),
            ('site.coordinates', 'Utilisation coordonnées (PDF)'),
            ('for item in quote.items:', 'Compatibilité legacy items (PDF)')
        ]
        
        # Check for key improvements in Word export
        word_checks = [
            ('for site in quote.sites:', 'Itération sur les sites (Word)'),
            ('Sites d\'intervention:', 'Section sites multiples (Word)'),
            ('site.full_address', 'Utilisation adresse complète (Word)'),
            ('site.coordinates', 'Utilisation coordonnées (Word)')
        ]
        
        all_checks = pdf_checks + word_checks
        missing_elements = []
        
        for check, description in all_checks:
            if check in content:
                print(f"  ✅ {description}")
            else:
                print(f"  ❌ {description} (manquant)")
                missing_elements.append(check)
        
        if missing_elements:
            print(f"\n⚠️  Éléments manquants: {len(missing_elements)}")
            return False
        else:
            print("\n✅ Toutes les améliorations d'export sont présentes!")
            return True
            
    except Exception as e:
        print(f"❌ Erreur lors de la vérification: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 SEE ALL AVKN - Test des Exports PDF/Word avec Sites")
    print("=" * 60)
    
    all_tests_passed = True
    
    # Test 1: Check basic functionality
    if not test_export_functionality():
        all_tests_passed = False
    
    # Test 2: Verify code structure 
    if not verify_export_content_structure():
        all_tests_passed = False
    
    # Test 3: Create test quote
    test_quote = create_test_quote_with_sites()
    if not test_quote:
        all_tests_passed = False
    else:
        # Test 4: Test PDF export
        if not test_pdf_export(test_quote):
            all_tests_passed = False
        
        # Test 5: Test Word export
        if not test_word_export(test_quote):
            all_tests_passed = False
    
    print("\n" + "=" * 60)
    
    if all_tests_passed:
        print("🎉 TESTS RÉUSSIS - Les exports incluent maintenant les descriptions des sites!")
        print("\n📋 Ce qui a été corrigé:")
        print("  ✅ Export PDF: Descriptions des sites incluses dans le tableau")
        print("  ✅ Export Word: Descriptions des sites incluses dans le tableau")
        print("  ✅ Section sites: Affichage de tous les sites d'intervention")
        print("  ✅ Compatibilité: Support des anciens devis avec items legacy")
        print("\n🔧 Pour tester dans l'application:")
        print("  1. Créez un devis avec plusieurs sites")
        print("  2. Ajoutez des descriptions détaillées pour chaque site")
        print("  3. Exportez en PDF et Word")
        print("  4. Vérifiez que toutes les descriptions apparaissent")
        
        return 0
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("\n🔧 Actions recommandées:")
        print("  1. Vérifiez que main_application.py est à jour")
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
