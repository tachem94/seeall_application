#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEE ALL AVKN - Automatic Fix Script for Site Buttons
Script de correction automatique pour les boutons de sites

Author: Expert Developer Assistant
Date: November 2025

Ce script corrige automatiquement le problème de visibilité des boutons
"Modifier Site" et "Supprimer Site" dans l'interface.
"""

import os
import re
import shutil
from datetime import datetime

def backup_file(filepath):
    """Create a backup of the original file"""
    if os.path.exists(filepath):
        backup_name = f"{filepath}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(filepath, backup_name)
        print(f"✅ Sauvegarde créée: {backup_name}")
        return backup_name
    return None

def fix_site_buttons_visibility(filepath="main_application.py"):
    """Fix the visibility of site action buttons"""
    
    print("🔧 Correction automatique des boutons de sites...")
    
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"❌ Fichier {filepath} non trouvé!")
        return False
    
    # Create backup
    backup_file(filepath)
    
    try:
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Define the new sites section code with guaranteed visible buttons
        new_sites_section = '''        # Sites list - FIXED VERSION with visible buttons
        columns = ('N° Site', 'Adresse Complète', 'Coordonnées', 'Description', 'Prix HT')
        
        # Tree container with proper layout
        tree_container = ttk.Frame(sites_frame)
        tree_container.pack(fill='both', expand=True)
        
        # Tree view with reduced height to ensure buttons are visible
        self.sites_tree = ttk.Treeview(tree_container, columns=columns, show='headings', height=4)
        
        for col in columns:
            self.sites_tree.heading(col, text=col)
            if col == 'N° Site':
                self.sites_tree.column(col, width=80)
            elif col == 'Adresse Complète':
                self.sites_tree.column(col, width=200)
            elif col == 'Coordonnées':
                self.sites_tree.column(col, width=150)
            elif col == 'Description':
                self.sites_tree.column(col, width=250)
            elif col == 'Prix HT':
                self.sites_tree.column(col, width=80)
        
        # Scrollbar for sites
        sites_scrollbar = ttk.Scrollbar(tree_container, orient='vertical', command=self.sites_tree.yview)
        self.sites_tree.configure(yscrollcommand=sites_scrollbar.set)
        
        # Pack tree and scrollbar
        self.sites_tree.pack(side='left', fill='both', expand=True)
        sites_scrollbar.pack(side='right', fill='y')
        
        # GUARANTEED VISIBLE: Action buttons frame at bottom of sites_frame
        site_buttons_frame = ttk.LabelFrame(sites_frame, text="Actions", padding=10)
        site_buttons_frame.pack(fill='x', pady=(10, 0))
        
        # Edit site button with icon for better visibility
        edit_site_button = ttk.Button(site_buttons_frame, text="✏️ Modifier Site", command=self.edit_site)
        edit_site_button.pack(side='left', padx=(0, 10))
        
        # Remove site button with icon for better visibility
        remove_site_button = ttk.Button(site_buttons_frame, text="🗑️ Supprimer Site", command=self.remove_site)
        remove_site_button.pack(side='left')
        
        # Help text for user guidance
        help_label = ttk.Label(site_buttons_frame, 
                              text="💡 Sélectionnez d'abord un site dans la liste, puis cliquez sur l'action souhaitée", 
                              font=('Arial', 8), foreground='#666666')
        help_label.pack(side='right', padx=(20, 0))'''
        
        # Find the pattern to replace
        # Look for the sites list section and replace it
        pattern = r'(\s+# Sites list[^\n]*\n.*?remove_site_button\.pack\(side=\'left\'[^\n]*)'
        
        if re.search(pattern, content, re.DOTALL):
            # Replace the sites section
            new_content = re.sub(pattern, new_sites_section, content, flags=re.DOTALL)
            
            # Write the fixed content back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Fichier corrigé avec succès!")
            print("✅ Les boutons 'Modifier Site' et 'Supprimer Site' sont maintenant visibles!")
            return True
        else:
            print("⚠️  Section des sites non trouvée automatiquement.")
            print("   Veuillez appliquer la correction manuelle.")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors de la correction: {e}")
        return False

def verify_fix(filepath="main_application.py"):
    """Verify that the fix was applied correctly"""
    print("\n🔍 Vérification de la correction...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for the presence of key elements
        checks = [
            ('edit_site_button', 'Bouton Modifier Site'),
            ('remove_site_button', 'Bouton Supprimer Site'), 
            ('site_buttons_frame', 'Frame des boutons'),
            ('command=self.edit_site', 'Commande de modification'),
            ('command=self.remove_site', 'Commande de suppression')
        ]
        
        all_good = True
        for element, description in checks:
            if element in content:
                print(f"  ✅ {description}")
            else:
                print(f"  ❌ {description} (manquant)")
                all_good = False
        
        if all_good:
            print("✅ Vérification réussie - Tous les éléments sont présents!")
        else:
            print("⚠️  Certains éléments sont manquants")
        
        return all_good
        
    except Exception as e:
        print(f"❌ Erreur lors de la vérification: {e}")
        return False

def main():
    """Main function to run the automatic fix"""
    print("🚀 SEE ALL AVKN - Correction Automatique des Boutons Sites")
    print("=" * 60)
    
    filepath = "main_application.py"
    
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"❌ Fichier {filepath} non trouvé dans le répertoire courant")
        print(f"📁 Répertoire courant: {os.getcwd()}")
        print("💡 Assurez-vous d'être dans le bon répertoire avec main_application.py")
        return 1
    
    # Apply the fix
    if fix_site_buttons_visibility(filepath):
        # Verify the fix
        if verify_fix(filepath):
            print("\n🎉 CORRECTION RÉUSSIE!")
            print("\n📋 Prochaines étapes:")
            print("  1. Lancez l'application: python main_application.py")
            print("  2. Ouvrez ou créez un devis")
            print("  3. Les boutons 'Modifier Site' et 'Supprimer Site' sont maintenant visibles!")
            print("  4. Testez les fonctionnalités de modification et suppression")
            return 0
        else:
            print("\n⚠️  Correction appliquée mais vérification échouée")
            return 1
    else:
        print("\n❌ CORRECTION ÉCHOUÉE")
        print("\n🔧 Solution alternative:")
        print("  Consultez le fichier quick_fix_buttons.py pour une correction manuelle")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        input("\nAppuyez sur Entrée pour fermer...")
        exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nAnnulé par l'utilisateur")
        exit(1)
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")
        exit(1)
