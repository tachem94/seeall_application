#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEE ALL AVKN - Installation Script
Script d'installation pour l'application de gestion des devis et factures

Author: Claude Assistant
Date: November 2025
"""

import subprocess
import sys
import os
import platform

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 ou supérieur requis")
        print(f"   Version actuelle: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} détecté")
    return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installation des dépendances...")
    
    try:
        # Upgrade pip first
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("✅ pip mis à jour")
        
        # Install requirements
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dépendances installées avec succès")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'installation: {e}")
        return False

def test_imports():
    """Test if all required modules can be imported"""
    print("\n🧪 Test des imports...")
    
    modules_to_test = [
        ("tkinter", "Interface graphique"),
        ("sqlite3", "Base de données"),
        ("reportlab.pdfgen.canvas", "Génération PDF"),
        ("docx", "Génération Word")
    ]
    
    all_ok = True
    
    for module, description in modules_to_test:
        try:
            __import__(module)
            print(f"✅ {description} - {module}")
        except ImportError as e:
            print(f"❌ {description} - {module}: {e}")
            all_ok = False
    
    return all_ok

def create_desktop_shortcut():
    """Create desktop shortcut (Windows only)"""
    if platform.system() != "Windows":
        return
    
    try:
        import winshell
        from win32com.client import Dispatch
        
        desktop = winshell.desktop()
        path = os.path.join(desktop, "SEE ALL AVKN.lnk")
        target = os.path.join(os.getcwd(), "seeall_devis_factures.py")
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = f'"{target}"'
        shortcut.WorkingDirectory = os.getcwd()
        shortcut.IconLocation = sys.executable
        shortcut.save()
        
        print(f"✅ Raccourci créé sur le bureau: {path}")
        
    except ImportError:
        print("ℹ️  Raccourci bureau non créé (winshell non disponible)")
    except Exception as e:
        print(f"⚠️  Impossible de créer le raccourci: {e}")

def create_run_script():
    """Create run script for the application"""
    script_content = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
SEE ALL AVKN - Launcher Script
Script de lancement pour l'application de gestion des devis et factures
\"\"\"

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the application
try:
    from main_application import main
    main()
except ImportError as e:
    print(f"Erreur d'import: {{e}}")
    print("Assurez-vous que main_application.py est dans le même dossier")
    input("Appuyez sur Entrée pour fermer...")
except Exception as e:
    print(f"Erreur lors du lancement: {{e}}")
    input("Appuyez sur Entrée pour fermer...")
"""
    
    # Create .py launcher
    with open("lancer_application.py", "w", encoding="utf-8") as f:
        f.write(script_content)
    
    print("✅ Script de lancement créé: lancer_application.py")
    
    # Create .bat launcher for Windows
    if platform.system() == "Windows":
        bat_content = f"""@echo off
cd /d "%~dp0"
python lancer_application.py
pause
"""
        with open("lancer_application.bat", "w", encoding="utf-8") as f:
            f.write(bat_content)
        
        print("✅ Script batch créé: lancer_application.bat")

def main():
    """Main installation function"""
    print("🚀 Installation de SEE ALL AVKN - Gestion Devis & Factures")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        input("Appuyez sur Entrée pour fermer...")
        return
    
    # Install requirements
    if not install_requirements():
        print("\n❌ L'installation a échoué")
        input("Appuyez sur Entrée pour fermer...")
        return
    
    # Test imports
    if not test_imports():
        print("\n❌ Certains modules ne sont pas disponibles")
        input("Appuyez sur Entrée pour fermer...")
        return
    
    # Create run scripts
    create_run_script()
    
    # Create desktop shortcut (Windows)
    if platform.system() == "Windows":
        create_desktop_shortcut()
    
    print("\n🎉 Installation terminée avec succès!")
    print("\n📋 Pour lancer l'application:")
    print("   • Double-cliquez sur 'lancer_application.py'")
    if platform.system() == "Windows":
        print("   • Ou double-cliquez sur 'lancer_application.bat'")
    print("   • Ou exécutez: python main_application.py")
    
    print("\n📁 Fichiers créés:")
    print("   • main_application.py - Application principale")
    print("   • requirements.txt - Dépendances")
    print("   • lancer_application.py - Script de lancement")
    if platform.system() == "Windows":
        print("   • lancer_application.bat - Script batch Windows")
    print("   • seeall_database.db - Base de données (créée au premier lancement)")
    
    input("\nAppuyez sur Entrée pour fermer...")

if __name__ == "__main__":
    main()
