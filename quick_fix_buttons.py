#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEE ALL AVKN - Quick Fix for Site Buttons Visibility
Correction rapide pour rendre les boutons visibles

INSTRUCTIONS RAPIDES:
1. Trouvez la ligne dans votre main_application.py qui contient:
   "# Sites list - Updated columns for detailed address"
   
2. Remplacez TOUT le code depuis cette ligne jusqu'à la ligne:
   "remove_site_button.pack(side='left')"
   
3. Par le code ci-dessous marqué "NOUVEAU CODE À COPIER"
"""

# NOUVEAU CODE À COPIER - DÉBUT
        # Sites list with VISIBLE buttons
        columns = ('N° Site', 'Adresse Complète', 'Coordonnées', 'Description', 'Prix HT')
        
        # Tree view with reduced height to make room for buttons
        self.sites_tree = ttk.Treeview(sites_frame, columns=columns, show='headings', height=5)
        
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
        
        # Pack tree first
        self.sites_tree.pack(fill='both', expand=False, pady=(0, 10))
        
        # Scrollbar for sites
        sites_scrollbar = ttk.Scrollbar(sites_frame, orient='vertical', command=self.sites_tree.yview)
        self.sites_tree.configure(yscrollcommand=sites_scrollbar.set)
        sites_scrollbar.pack(side='right', fill='y')
        
        # IMPORTANT: Action buttons frame - ALWAYS VISIBLE at bottom
        site_buttons_frame = ttk.LabelFrame(sites_frame, text="Actions sur les sites", padding=5)
        site_buttons_frame.pack(fill='x', pady=(10, 0))
        
        # Edit site button
        edit_site_button = ttk.Button(site_buttons_frame, text="✏️ Modifier Site", command=self.edit_site)
        edit_site_button.pack(side='left', padx=(0, 10))
        
        # Remove site button
        remove_site_button = ttk.Button(site_buttons_frame, text="🗑️ Supprimer Site", command=self.remove_site)
        remove_site_button.pack(side='left', padx=(0, 10))
        
        # Help text
        help_label = ttk.Label(site_buttons_frame, text="Sélectionnez un site dans la liste ci-dessus, puis cliquez sur l'action souhaitée", 
                              font=('Arial', 8), foreground='gray')
        help_label.pack(side='right')
# NOUVEAU CODE À COPIER - FIN

"""
ALTERNATIVE ENCORE PLUS SIMPLE:
Si le code ci-dessus ne fonctionne toujours pas, utilisez cette version ultra-simple:

        # ULTRA SIMPLE VERSION - Sites list
        columns = ('N° Site', 'Adresse Complète', 'Coordonnées', 'Description', 'Prix HT')
        self.sites_tree = ttk.Treeview(sites_frame, columns=columns, show='headings', height=4)
        
        for col in columns:
            self.sites_tree.heading(col, text=col)
        
        self.sites_tree.pack(fill='x', pady=(0, 10))
        
        # Buttons in a simple frame
        buttons_frame = ttk.Frame(sites_frame)
        buttons_frame.pack(fill='x')
        
        ttk.Button(buttons_frame, text="Modifier Site", command=self.edit_site).pack(side='left', padx=5)
        ttk.Button(buttons_frame, text="Supprimer Site", command=self.remove_site).pack(side='left', padx=5)
        ttk.Label(buttons_frame, text="← Sélectionnez d'abord un site").pack(side='left', padx=20)
"""
