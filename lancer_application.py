#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEE ALL AVKN - Launcher Script
Script de lancement pour l'application de gestion des devis et factures
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the application
try:
    from main_application import main
    main()
except ImportError as e:
    print(f"Erreur d'import: {e}")
    print("Assurez-vous que main_application.py est dans le même dossier")
    input("Appuyez sur Entrée pour fermer...")
except Exception as e:
    print(f"Erreur lors du lancement: {e}")
    input("Appuyez sur Entrée pour fermer...")
