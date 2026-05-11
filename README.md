# SEE ALL AVKN - Gestion Devis & Factures

Application complète de gestion des devis et factures pour la société SEE ALL AVKN.

## 📋 Fonctionnalités

### 🏢 Gestion des Clients
- Ajout de nouveaux clients avec informations complètes
- Stockage des données : nom, SIRET, adresse, email, téléphone
- Liste de tous les clients existants
- Interface intuitive de gestion

### 📄 Gestion des Devis
- Création de devis avec numérotation automatique : `SA.<NOM_CLIENT>[.<SITE>][.<VILLE>].MMYYYY<SEQ>`
- Ajout de **sites d'intervention** (adresse, coordonnées GPS, description, prix HT)
- Calcul automatique des totaux (HT, TVA 20%, TTC)
- Sauvegarde en base de données SQLite
- Export PDF, Word et Excel

### 🧾 Gestion des Factures
- Conversion automatique devis → facture
- Numérotation facture : `FA.<NOM_CLIENT>[.<SITE>][.<VILLE>].MMYYYY<SEQ>`
- Gestion du numéro de bon de commande
- **Statut payé / non payé** avec surlignage vert des lignes payées
- Filtre par État (toutes / payées / non payées) et **totaux ventilés** payé / restant à encaisser
- Export PDF, Word et Excel avec informations bancaires

### 📤 Export et Impression
- **Export PDF** (ReportLab) : Documents professionnels avec logo et mise en forme
- **Export Word** (python-docx) : Documents modifiables (.docx)
- **Export Excel** (openpyxl) : Export de la liste des devis ou factures (.xlsx)
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
python lancer_application.py
# ou directement
python main_application.py
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
4. Ajouter un ou plusieurs **sites d'intervention** :
   - Adresse / coordonnées GPS
   - Description de la prestation
   - Prix HT
5. Vérifier les totaux automatiques (HT, TVA, TTC)
6. Cliquer **"Sauvegarder"**

#### 3. Convertir en Facture
1. Dans l'onglet **"Devis"**, faire clic-droit sur un devis
2. Sélectionner **"Convertir en Facture"**
3. Saisir le numéro de bon de commande
4. La facture apparaît dans l'onglet **"Factures"** (le devis source est marqué comme facturé)

#### 4. Marquer une Facture comme Payée
1. Dans l'onglet **"Factures"**, clic-droit sur une facture
2. Sélectionner **"Marquer comme payée"** (la ligne devient verte)
3. Le filtre **État** et les totaux *Payé / Restant à encaisser* sont mis à jour automatiquement

#### 5. Exporter des Documents
1. Clic-droit sur un devis ou une facture → **"Exporter PDF"** ou **"Exporter Word"** pour le document individuel
2. Bouton **"Exporter Excel"** au-dessus de la liste → export de l'ensemble des devis ou factures filtrés (.xlsx)
3. Choisir l'emplacement de sauvegarde — le document est généré automatiquement

## 📊 Structure des Données

### Numérotation Automatique
- **Devis** : `SA.<NOM_CLIENT>[.<SITE>][.<VILLE>].MMYYYY<SEQ>`
- **Factures** : `FA.<NOM_CLIENT>[.<SITE>][.<VILLE>].MMYYYY<SEQ>`
- Les segments `SITE` et `VILLE` sont optionnels : inclus uniquement s'ils sont renseignés dans le formulaire
- Auto-incrémentation par client et par mois

Exemples selon les données saisies :

| SITE | VILLE | Numéro généré |
|------|-------|---------------|
| ✅ | ✅ | `SA.STAUBINSURMER.SITE42.Paris.042026001` |
| ❌ | ✅ | `SA.STAUBINSURMER.Paris.042026001` |
| ✅ | ❌ | `SA.STAUBINSURMER.SITE42.042026001` |
| ❌ | ❌ | `SA.STAUBINSURMER.042026001` |

### Base de Données
- **clients** : Informations clients
- **quotes** : Devis et factures (table partagée, distinguée par `is_invoice` ; les factures portent aussi `is_paid` et `linked_invoice_id`)
- **quote_sites** : Sites d'intervention (modèle actuel — un site par ligne)
- **quote_items** : Anciens articles — conservé pour compatibilité, non utilisé par les nouvelles fonctionnalités
- **counters** : Compteurs pour numérotation automatique (par client + mois)

## 🎨 Personnalisation

Toute la personnalisation se fait dans **`config.py`** — aucune modification du code applicatif n'est nécessaire.

### Informations Société (`COMPANY_CONFIG`)
```python
COMPANY_CONFIG = {
    'name': 'SEE ALL AVKN',
    'address': '38 rue Dunois\n75013 PARIS',
    'email': 'michael@seeall.fr',
    'siren': '951 474 709',
    'siret': '95147470900015',
    'tva': 'FR95951474709',
    'legal_form': 'SAS',
    'capital': '1 000,00 €',
    'rcs': '951 474 709 R.C.S. Paris',
    'bank_bic': 'CMCIFRPP',
    'bank_iban': 'FR76 3006 6109 4100 0210 0820 254',
    # ...
}
```

### Paramètres métier (`BUSINESS_CONFIG`)
- **`default_vat_rate`** : taux de TVA (0.20 = 20 %)
- **`currency`** / **`currency_position`** : devise et position (`before` / `after`)
- **`quote_prefix`** / **`invoice_prefix`** : préfixes de numérotation (`SA` / `FA` par défaut)
- **`payment_terms`**, **`payment_delay_penalty`**, **`recovery_fee`** : conditions de paiement et pénalités

### Autres sections de `config.py`
- **`UI_CONFIG`** : titre, taille de fenêtre, thème, colonnes affichées
- **`EXPORT_CONFIG`** : dossier d'export, format de nom de fichier, police Word, format PDF
- **`DATABASE_CONFIG`** : fichier DB, sauvegarde au démarrage, dossier et nombre de sauvegardes (voir §Sauvegarde)
- **`MESSAGES_CONFIG`** : libellés visibles dans l'app et dans les documents générés
- **`ADVANCED_CONFIG`** : debug, logging, validations optionnelles

Lancer `python config.py` exécute la fonction `validate_config()` qui contrôle les champs obligatoires.

## 📁 Structure des Fichiers

```
seeall_application/
├── main_application.py        # Application principale (UI, DB, exports)
├── config.py                  # Configuration (société, TVA, UI, exports, backups)
├── lancer_application.py      # Lanceur principal
├── lancer_application.bat     # Lanceur Windows
├── install.py                 # Script d'installation des dépendances
├── requirements.txt           # Dépendances Python (reportlab, python-docx, openpyxl)
├── test_quote_number.py       # Tests unitaires de la numérotation
├── README.md                  # Cette documentation
├── CLAUDE.md                  # Guide pour Claude Code
├── seeall_database.db         # Base de données SQLite (créée au premier lancement, non versionnée)
└── backups/                   # Sauvegardes automatiques (chemin configurable)
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

### Export indisponible
Les bibliothèques d'export sont optionnelles — l'application reste utilisable si l'une manque, mais l'export correspondant est désactivé. Réinstaller au besoin :
```bash
pip install reportlab     # Export PDF
pip install python-docx   # Export Word
pip install openpyxl      # Export Excel
```

### Base de données corrompue
1. Fermez l'application.
2. Renommez/déplacez `seeall_database.db` (par sécurité).
3. **Restaurez la dernière sauvegarde** : voir la section *Sauvegarde et restauration*.
4. Si aucune sauvegarde n'est disponible, supprimer `seeall_database.db` recrée une base vide au prochain lancement (vous perdez les données).

## 💾 Sauvegarde et restauration

La base de données SQLite n'est **pas** suivie par git (elle contient des données et non du code). Un système de sauvegarde automatique est intégré à l'application.

### Sauvegarde automatique
À chaque démarrage de l'application, la base est copiée dans le dossier configuré sous `DATABASE_CONFIG['backup_folder']` (`config.py`). Le nom du fichier inclut la date et l'heure : `seeall_database_YYYYMMDD_HHMMSS.db`.

Une **rotation FIFO** garde uniquement les `max_backups` plus récentes (10 par défaut) ; les plus anciennes sont supprimées automatiquement.

### Sauvegarde manuelle
Une barre d'état en bas de la fenêtre affiche la date de la dernière sauvegarde. Le bouton **« Sauvegarder maintenant »** force une sauvegarde immédiate (utile avant une opération risquée comme une suppression en masse).

### Configuration (`config.py` → `DATABASE_CONFIG`)
```python
DATABASE_CONFIG = {
    'database_filename': 'seeall_database.db',
    'backup_on_startup': True,     # False = désactive la sauvegarde au démarrage
    'backup_folder': r'G:\My Drive\seeall\seeall_backups_db',  # cloud-synced
    'max_backups': 10,             # nombre de sauvegardes conservées
}
```
**Recommandation** : pointer `backup_folder` vers un dossier synchronisé cloud (Google Drive, OneDrive, Dropbox) pour bénéficier d'une copie hors-machine sans effort.

### Restaurer une sauvegarde
1. Fermez l'application.
2. Ouvrez votre dossier de sauvegardes.
3. Identifiez le fichier à restaurer (ils sont triés chronologiquement par leur nom).
4. Copiez ce fichier dans le dossier de l'application en le renommant `seeall_database.db` (écraser l'éventuel fichier existant — faites une copie de sécurité avant).
5. Relancez l'application.

## 🔧 Développement

### Architecture
- **Frontend** : Tkinter (interface graphique native)
- **Backend** : SQLite (base de données locale, fichier unique `seeall_database.db`)
- **Export PDF** : ReportLab — classe `PDFGenerator`
- **Export Word** : python-docx — classe `WordGenerator`
- **Export Excel** : openpyxl — fonction `export_quotes_to_excel`
- **Sauvegardes** : classe `BackupManager` (rotation FIFO au démarrage)
- **Structure** : classes orientées objet, dataclasses (`Client`, `Quote`, `SiteItem`, `QuoteItem`)
- **Migrations DB** : appliquées en ligne dans `DatabaseManager.init_database()` via `ALTER TABLE … ADD COLUMN`

### Tests
```bash
python -m pytest test_quote_number.py -v
# ou sans pytest
python test_quote_number.py
```

### Extensions Possibles
- [ ] Templates de documents personnalisés
- [ ] Gestion multi-utilisateurs
- [ ] Statistiques et rapports
- [ ] Intégration comptabilité
- [ ] Envoi email automatique
- [ ] Relances automatiques sur factures non payées

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
