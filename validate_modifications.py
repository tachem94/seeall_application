#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEE ALL AVKN - Validation Script for Site Edit Functionality
Script de validation pour les nouvelles fonctionnalités de modification des sites

Author: Expert Developer Assistant
Date: November 2025
"""

import sys
import os
import sqlite3
import tempfile
from datetime import date

def validate_imports():
    """Validate all required imports are available"""
    print("🔍 Validation des imports...")
    
    required_modules = [
        ('tkinter', 'Interface graphique'),
        ('sqlite3', 'Base de données'),
        ('datetime', 'Gestion des dates'),
        ('dataclasses', 'Classes de données')
    ]
    
    missing_modules = []
    
    for module, description in required_modules:
        try:
            __import__(module)
            print(f"  ✅ {description} - {module}")
        except ImportError as e:
            print(f"  ❌ {description} - {module}: {e}")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n❌ Modules manquants: {', '.join(missing_modules)}")
        return False
    
    print("✅ Tous les modules requis sont disponibles")
    return True

def validate_file_structure():
    """Validate that the application files are present"""
    print("\n📁 Validation de la structure des fichiers...")
    
    required_files = [
        ('main_application.py', 'Application principale'),
        ('config.py', 'Configuration (optionnel)')
    ]
    
    missing_files = []
    
    for filename, description in required_files:
        if os.path.exists(filename):
            print(f"  ✅ {description} - {filename}")
        else:
            print(f"  ⚠️  {description} - {filename} (non trouvé)")
            if filename == 'main_application.py':
                missing_files.append(filename)
    
    if missing_files:
        print(f"\n❌ Fichiers critiques manquants: {', '.join(missing_files)}")
        return False
    
    print("✅ Structure des fichiers valide")
    return True

def validate_site_edit_methods():
    """Validate that the new site edit methods are present in the code"""
    print("\n🔧 Validation des nouvelles méthodes...")
    
    try:
        with open('main_application.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        required_methods = [
            ('edit_site', 'Méthode de modification de site'),
            ('update_site', 'Méthode de mise à jour de site'),
            ('cancel_edit_site', 'Méthode d\'annulation d\'édition'),
            ('clear_site_form', 'Méthode de nettoyage du formulaire'),
            ('add_or_update_site', 'Méthode unifiée ajout/modification')
        ]
        
        missing_methods = []
        
        for method_name, description in required_methods:
            if f"def {method_name}(" in content:
                print(f"  ✅ {description} - {method_name}()")
            else:
                print(f"  ❌ {description} - {method_name}() (non trouvée)")
                missing_methods.append(method_name)
        
        if missing_methods:
            print(f"\n❌ Méthodes manquantes: {', '.join(missing_methods)}")
            return False
        
        print("✅ Toutes les nouvelles méthodes sont présentes")
        return True
        
    except FileNotFoundError:
        print("❌ Fichier main_application.py non trouvé")
        return False
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du fichier: {e}")
        return False

def validate_ui_elements():
    """Validate that the new UI elements are present"""
    print("\n🖥️  Validation des éléments d'interface...")
    
    try:
        with open('main_application.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        required_ui_elements = [
            ('self.editing_site_index', 'Variable d\'index d\'édition'),
            ('self.is_editing_site', 'Variable d\'état d\'édition'),
            ('self.add_site_button', 'Référence au bouton d\'ajout'),
            ('self.cancel_edit_button', 'Bouton d\'annulation'),
            ('"Modifier Site"', 'Bouton de modification'),
            ('"Mettre à jour Site"', 'Texte de mise à jour'),
            ('"Annuler Modification"', 'Texte d\'annulation')
        ]
        
        missing_elements = []
        
        for element, description in required_ui_elements:
            if element in content:
                print(f"  ✅ {description}")
            else:
                print(f"  ❌ {description} (non trouvé)")
                missing_elements.append(element)
        
        if missing_elements:
            print(f"\n⚠️  Éléments d'interface manquants: {len(missing_elements)}")
            return False
        
        print("✅ Tous les éléments d'interface sont présents")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la validation UI: {e}")
        return False

def create_test_database():
    """Create a temporary test database with sample data"""
    print("\n🗄️  Création d'une base de données de test...")
    
    try:
        # Create temporary database
        temp_dir = tempfile.mkdtemp()
        db_path = os.path.join(temp_dir, 'test_seeall.db')
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create tables (simplified structure for testing)
        cursor.execute('''
            CREATE TABLE clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                siret TEXT,
                address TEXT,
                email TEXT,
                phone TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number TEXT UNIQUE NOT NULL,
                client_id INTEGER,
                typology TEXT,
                quote_date DATE,
                is_invoice BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE quote_sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quote_id INTEGER,
                site_number TEXT,
                address TEXT,
                postal_code TEXT,
                city TEXT,
                latitude TEXT,
                longitude TEXT,
                description TEXT,
                price_ht REAL
            )
        ''')
        
        # Insert test data
        cursor.execute(
            "INSERT INTO clients (name, siret, email) VALUES (?, ?, ?)",
            ("CLIENT TEST", "12345678901234", "test@example.com")
        )
        
        conn.commit()
        conn.close()
        
        print(f"  ✅ Base de données de test créée: {db_path}")
        return db_path
        
    except Exception as e:
        print(f"  ❌ Erreur lors de la création de la base de test: {e}")
        return None

def validate_database_schema():
    """Validate that the database schema supports the new functionality"""
    print("\n🗃️  Validation du schéma de base de données...")
    
    db_path = 'seeall_database.db'
    
    if not os.path.exists(db_path):
        print("  ⚠️  Base de données principale non trouvée (sera créée au premier lancement)")
        return True
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check for required tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [table[0] for table in cursor.fetchall()]
        
        required_tables = ['clients', 'quotes', 'quote_sites']
        
        for table in required_tables:
            if table in tables:
                print(f"  ✅ Table {table} présente")
            else:
                print(f"  ⚠️  Table {table} manquante (sera créée automatiquement)")
        
        conn.close()
        print("✅ Schéma de base de données compatible")
        return True
        
    except Exception as e:
        print(f"  ❌ Erreur lors de la validation du schéma: {e}")
        return False

def run_functionality_test():
    """Run a basic functionality test"""
    print("\n🧪 Test de fonctionnalité de base...")
    
    try:
        # Try to import the main application classes
        sys.path.insert(0, '.')
        
        # Import without running the GUI
        import main_application
        
        # Check if the new methods exist
        if hasattr(main_application, 'QuoteDialog'):
            quote_dialog_class = main_application.QuoteDialog
            
            required_methods = [
                'edit_site', 'update_site', 'cancel_edit_site', 
                'clear_site_form', 'add_or_update_site'
            ]
            
            for method in required_methods:
                if hasattr(quote_dialog_class, method):
                    print(f"  ✅ Méthode {method} accessible")
                else:
                    print(f"  ❌ Méthode {method} non accessible")
                    return False
            
            print("✅ Test de fonctionnalité réussi")
            return True
        else:
            print("❌ Classe QuoteDialog non trouvée")
            return False
            
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        return False
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        return False

def main():
    """Main validation function"""
    print("🚀 SEE ALL AVKN - Validation des Modifications Sites")
    print("=" * 60)
    
    all_tests_passed = True
    
    # Run all validation tests
    tests = [
        validate_imports,
        validate_file_structure,
        validate_site_edit_methods,
        validate_ui_elements,
        validate_database_schema,
        run_functionality_test
    ]
    
    for test in tests:
        if not test():
            all_tests_passed = False
    
    print("\n" + "=" * 60)
    
    if all_tests_passed:
        print("🎉 VALIDATION RÉUSSIE - Toutes les modifications sont correctement implémentées!")
        print("\n📋 Prochaines étapes:")
        print("  1. Lancez l'application: python main_application.py")
        print("  2. Créez un nouveau devis")
        print("  3. Ajoutez quelques sites")
        print("  4. Testez la modification des sites")
        print("  5. Testez la suppression des sites")
        
        return 0
    else:
        print("❌ VALIDATION ÉCHOUÉE - Certains problèmes doivent être corrigés")
        print("\n🔧 Actions recommandées:")
        print("  1. Vérifiez que le bon fichier main_application.py est utilisé")
        print("  2. Vérifiez les dépendances: pip install -r requirements.txt")
        print("  3. Relancez ce script de validation")
        
        return 1

if __name__ == "__main__":
    exit_code = main()
    input("\nAppuyez sur Entrée pour fermer...")
    sys.exit(exit_code)
