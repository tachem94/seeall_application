# SEE ALL AVKN - Gestion Devis & Factures

Application complète de gestion des devis et factures pour la société SEE ALL AVKN.

## 📋 Fonctionnalités

### 🏢 Gestion des Clients
- Ajout de nouveaux clients avec informations complètes
- Stockage des données : nom, SIRET, adresse, email, téléphone
- Liste de tous les clients existants
- Interface intuitive de gestion

### 📄 Gestion des Devis
- Création de devis avec numérotation automatique : `SA.<CLIENT>.<SITE>.<VILLE>.MMYYYY001`
- Ajout d'articles avec description et prix HT
- Calcul automatique des totaux (HT, TVA 20%, TTC)
- Sauvegarde en base de données SQLite
- Export PDF et Word

### 🧾 Gestion des Factures
- Conversion automatique devis → facture
- Numérotation facture : `FA.<CLIENT>.MMYYYY001`
- Gestion du numéro de bon de commande
- Export PDF et Word avec informations bancaires
- Suivi des factures émises

### 📤 Export et Impression
- **Export PDF** : Documents professionnels avec logo et mise en forme
- **Export Word** : Documents modifiables (.docx)
- Respect de la charte graphique SEE ALL AVKN
- Informations légales automatiques (SIRET, TVA, RCS)

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur
- Connexion Internet pour l'installation des dépendances

### Installation Automatique
1. Téléchargez tous les fichiers dans un dossier
2. Double-cliquez sur `install.py` ou exécutez :
   ```bash
   python install.py
   ```
3. Suivez les instructions à l'écran

### Installation Manuelle
```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python seeall_devis_factures.py
```

## 🖥️ Utilisation

### Premier Lancement
1. Lancez l'application via `lancer_application.py` ou `lancer_application.bat`
2. La base de données SQLite sera créée automatiquement
3. L'interface principale s'ouvre avec 3 onglets

### Workflow Typique

#### 1. Ajouter un Client
1. Aller dans l'onglet **"Clients"**
2. Remplir le formulaire (nom obligatoire)
3. Cliquer sur **"Ajouter Client"**
4. Le client apparaît dans la liste

#### 2. Créer un Devis
1. Aller dans l'onglet **"Devis"**
2. Cliquer sur **"Nouveau Devis"**
3. Sélectionner un client dans la liste déroulante
4. Ajouter des articles :
   - Description du service/produit
   - Prix HT
   - Cliquer **"Ajouter"**
5. Vérifier les totaux automatiques
6. Cliquer **"Sauvegarder"**

#### 3. Convertir en Facture
1. Dans l'onglet **"Devis"**, faire clic-droit sur un devis
2. Sélectionner **"Convertir en Facture"**
3. Saisir le numéro de bon de commande
4. La facture apparaît dans l'onglet **"Factures"**

#### 4. Exporter des Documents
1. Clic-droit sur un devis ou une facture
2. Choisir **"Exporter PDF"** ou **"Exporter Word"**
3. Choisir l'emplacement de sauvegarde
4. Le document est généré automatiquement

## 📊 Structure des Données

### Numérotation Automatique
- **Devis** : `SA.<NOM_CLIENT>.<SITE>.<VILLE>.MMYYYY001`
- **Factures** : `FA.<NOM_CLIENT>.<SITE>.<VILLE>.MMYYYY001`
- Auto-incrémentation par client, site, ville et mois
- Exemple : `SA.STAUBINSURMER.SITE01.PARIS.112025001`

### Base de Données
- **clients** : Informations clients
- **quotes** : Devis et factures
- **quote_items** : Articles des devis/factures
- **counters** : Compteurs pour numérotation automatique

## 🎨 Personnalisation

### Informations Société
Pour modifier les informations de SEE ALL AVKN, éditer dans `seeall_devis_factures.py` :

```python
COMPANY_INFO = {
    'name': 'SEE ALL AVKN',
    'address': '38 rue Dunois\\n75013 PARIS',
    'email': 'michael@seeall.fr',
    'siren': '951 474 709',
    'siret': '95147470900015',
    'tva': 'FR95951474709',
    # ... autres informations
}
```

### Taux de TVA
Par défaut fixé à 20%. Pour modifier, chercher `0.20` dans le code et ajuster.

## 📁 Structure des Fichiers

```
seeall-devis-factures/
├── seeall_devis_factures.py    # Application principale
├── requirements.txt            # Dépendances Python
├── install.py                 # Script d'installation
├── lancer_application.py      # Lanceur principal
├── lancer_application.bat     # Lanceur Windows (créé automatiquement)
├── README.md                  # Cette documentation
├── seeall_database.db         # Base de données (créée au premier lancement)
└── exports/                   # Dossier pour les exports (optionnel)
```

## ⚠️ Dépannage

### Erreur "Module not found"
```bash
pip install -r requirements.txt
```

### Problème d'affichage GUI
Vérifiez que tkinter est installé :
```python
python -c "import tkinter; print('OK')"
```

### Export Word indisponible
Installez python-docx :
```bash
pip install python-docx
```

### Base de données corrompue
Supprimez le fichier `seeall_database.db` - il sera recréé au prochain lancement.

## 🔧 Développement

### Architecture
- **Frontend** : Tkinter (interface graphique native)
- **Backend** : SQLite (base de données locale)
- **Export PDF** : ReportLab
- **Export Word** : python-docx
- **Structure** : Classes orientées objet avec dataclasses

### Extensions Possibles
- [ ] Sauvegarde automatique cloud
- [ ] Templates de documents personnalisés
- [ ] Gestion multi-utilisateurs
- [ ] Statistiques et rapports
- [ ] Intégration comptabilité
- [ ] Envoi email automatique

## 📞 Support

Pour toute question ou suggestion :
- Email : michael@seeall.fr
- Société : SEE ALL AVKN
- Adresse : 38 rue Dunois, 75013 PARIS

## 📄 Licence

Application développée spécifiquement pour SEE ALL AVKN.
Tous droits réservés.

---

**Version** : 1.0.0  
**Date** : Novembre 2025  
**Développé par** : Claude Assistant pour SEE ALL AVKN
