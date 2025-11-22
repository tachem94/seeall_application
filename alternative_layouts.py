#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEE ALL AVKN - Alternative Layout for Site Management Buttons
Version alternative avec boutons mieux positionnés

Author: Expert Developer Assistant
Date: November 2025

INSTRUCTIONS D'UTILISATION:
Si les boutons "Modifier Site" et "Supprimer Site" ne sont toujours pas visibles,
remplacez la section du code principal par cette version alternative.
"""

# VERSION ALTERNATIVE - BOUTONS À DROITE DE LA LISTE
def setup_sites_section_alternative(self, sites_frame):
    """Alternative layout with buttons on the right side of the tree"""
    
    # Create main horizontal layout
    main_sites_container = ttk.Frame(sites_frame)
    main_sites_container.pack(fill='both', expand=True)
    
    # Left side: Tree view and scrollbar
    tree_side = ttk.Frame(main_sites_container)
    tree_side.pack(side='left', fill='both', expand=True, padx=(0, 10))
    
    # Sites list - Updated columns for detailed address
    columns = ('N° Site', 'Adresse Complète', 'Coordonnées', 'Description', 'Prix HT')
    self.sites_tree = ttk.Treeview(tree_side, columns=columns, show='headings', height=6)
    
    for col in columns:
        self.sites_tree.heading(col, text=col)
        if col == 'N° Site':
            self.sites_tree.column(col, width=80)
        elif col == 'Adresse Complète':
            self.sites_tree.column(col, width=180)
        elif col == 'Coordonnées':
            self.sites_tree.column(col, width=130)
        elif col == 'Description':
            self.sites_tree.column(col, width=200)
        elif col == 'Prix HT':
            self.sites_tree.column(col, width=80)
    
    # Scrollbar for sites
    sites_scrollbar = ttk.Scrollbar(tree_side, orient='vertical', command=self.sites_tree.yview)
    self.sites_tree.configure(yscrollcommand=sites_scrollbar.set)
    
    self.sites_tree.pack(side='left', fill='both', expand=True)
    sites_scrollbar.pack(side='right', fill='y')
    
    # Right side: Action buttons (ALWAYS VISIBLE)
    buttons_side = ttk.Frame(main_sites_container)
    buttons_side.pack(side='right', fill='y', padx=(10, 0))
    
    # Title for buttons section
    ttk.Label(buttons_side, text="Actions:", font=('Arial', 9, 'bold')).pack(pady=(0, 10))
    
    # Edit site button
    edit_site_button = ttk.Button(buttons_side, text="Modifier Site", 
                                 command=self.edit_site, width=15)
    edit_site_button.pack(pady=(0, 5), fill='x')
    
    # Remove site button  
    remove_site_button = ttk.Button(buttons_side, text="Supprimer Site", 
                                   command=self.remove_site, width=15)
    remove_site_button.pack(pady=(0, 10), fill='x')
    
    # Help text
    help_text = ttk.Label(buttons_side, text="Sélectionnez un site\ndans la liste puis\ncliquez sur l'action\nsouhaitée.", 
                         font=('Arial', 8), foreground='gray', justify='center')
    help_text.pack(pady=(10, 0))


# VERSION ALTERNATIVE 2 - BOUTONS DANS UNE BARRE D'OUTILS
def setup_sites_section_toolbar_style(self, sites_frame):
    """Alternative layout with toolbar-style buttons above the tree"""
    
    # Toolbar frame at the top
    toolbar_frame = ttk.Frame(sites_frame)
    toolbar_frame.pack(fill='x', pady=(0, 5))
    
    # Toolbar label
    ttk.Label(toolbar_frame, text="Actions sur les sites:", font=('Arial', 9, 'bold')).pack(side='left')
    
    # Separator
    ttk.Separator(toolbar_frame, orient='vertical').pack(side='left', fill='y', padx=(10, 10))
    
    # Action buttons in toolbar
    edit_site_button = ttk.Button(toolbar_frame, text="✏️ Modifier Site", 
                                 command=self.edit_site)
    edit_site_button.pack(side='left', padx=(0, 5))
    
    remove_site_button = ttk.Button(toolbar_frame, text="🗑️ Supprimer Site", 
                                   command=self.remove_site)
    remove_site_button.pack(side='left', padx=(0, 5))
    
    # Info label
    info_label = ttk.Label(toolbar_frame, text="(Sélectionnez d'abord un site dans la liste)", 
                          font=('Arial', 8), foreground='gray')
    info_label.pack(side='right')
    
    # Tree container
    tree_container = ttk.Frame(sites_frame)
    tree_container.pack(fill='both', expand=True)
    
    # Sites list
    columns = ('N° Site', 'Adresse Complète', 'Coordonnées', 'Description', 'Prix HT')
    self.sites_tree = ttk.Treeview(tree_container, columns=columns, show='headings', height=6)
    
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
    
    # Scrollbar
    sites_scrollbar = ttk.Scrollbar(tree_container, orient='vertical', command=self.sites_tree.yview)
    self.sites_tree.configure(yscrollcommand=sites_scrollbar.set)
    
    self.sites_tree.pack(side='left', fill='both', expand=True)
    sites_scrollbar.pack(side='right', fill='y')


# INSTRUCTIONS POUR APPLIQUER L'ALTERNATIVE
"""
Pour utiliser une de ces versions alternatives, remplacez la section du code 
dans main_application.py à partir de "# Sites list - Updated columns" 
jusqu'à "remove_site_button.pack(side='left')" par l'une des fonctions ci-dessus.

VERSION 1 (Recommandée): Boutons à droite de la liste
- Remplacez par le contenu de setup_sites_section_alternative()

VERSION 2: Barre d'outils au-dessus de la liste  
- Remplacez par le contenu de setup_sites_section_toolbar_style()

Les deux versions garantissent que les boutons sont toujours visibles.
"""
