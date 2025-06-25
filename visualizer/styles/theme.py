from tkinter import ttk

def BaseStyles(style: ttk.Style):
    style.theme_use("clam")

    # Paleta de colores moderna
    background_color = "#f5f5f5"
    panel_color = "#ffffff"
    border_color = "#e0e0e0"
    primary_color = "#4a6fa5"
    secondary_color = "#6c757d"
    button_color = "#4a6fa5"
    button_hover = "#3a5a8c"
    danger_color = "#e74c3c"
    success_color = "#28a745"
    text_color = "#333333"
    light_text = "#6c757d"
    input_bg = "#ffffff"
    disabled_color = "#b0b0b0"

    # Configuración general
    style.configure('.', 
                   background=background_color, 
                   foreground=text_color, 
                   font=("Segoe UI", 10),
                   borderwidth=0)
    
    # Frames
    style.configure('TFrame', 
                   background=panel_color, 
                   relief="flat",
                   borderwidth=0)
    
    style.configure('Section.TFrame',
                   background=panel_color,
                   relief="flat",
                   borderwidth=0,
                   padding=10)
    
    # Labels
    style.configure('TLabel', 
                   background=panel_color, 
                   foreground=text_color, 
                   font=("Segoe UI", 10),
                   padding=2)
    
    style.configure('Title.TLabel', 
                   font=('Segoe UI', 18, 'bold'), 
                   background=background_color,
                   foreground=primary_color,
                   padding=(0, 10, 0, 5))
    
    style.configure('Subtitle.TLabel', 
                   font=('Segoe UI', 12), 
                   background=background_color,
                   foreground=secondary_color,
                   padding=(0, 5, 0, 15))
    
    style.configure('Light.TLabel',
                   foreground=light_text,
                   font=("Segoe UI", 9))

    # LabelFrames
    style.configure('TLabelframe', 
                   background=panel_color, 
                   foreground=text_color, 
                   bordercolor=border_color,
                   relief="groove",
                   borderwidth=1)
    
    style.configure('TLabelframe.Label', 
                   background=panel_color, 
                   foreground=primary_color,
                   font=('Segoe UI', 11, 'bold'))
    
    style.configure('Section.TLabelframe', 
                   background=background_color, 
                   relief="groove", 
                   borderwidth=1,
                   padding=10)
    
    style.configure('Section.TLabelframe.Label', 
                   font=('Segoe UI', 11, 'bold'),
                   foreground=primary_color)

    # Entradas de texto
    style.configure('TEntry',
                    foreground=text_color,
                    fieldbackground=input_bg,
                    background=input_bg,
                    borderwidth=1,
                    relief="solid",
                    padding=5,
                    insertcolor=text_color)
    
    style.map('TEntry',
              fieldbackground=[('disabled', disabled_color)],
              foreground=[('disabled', '#777777')],
              bordercolor=[('focus', primary_color)])

    # Combobox
    style.configure('TCombobox',
                    foreground=text_color,
                    fieldbackground=input_bg,
                    background=input_bg,
                    padding=5,
                    arrowsize=12,
                    arrowcolor=text_color)
    
    style.map('TCombobox',
              fieldbackground=[('readonly', input_bg)],
              background=[('readonly', input_bg)],
              foreground=[('readonly', text_color)],
              bordercolor=[('focus', primary_color)],
              arrowcolor=[('disabled', disabled_color)])

    # Spinbox
    style.configure('TSpinbox',
                    foreground=text_color,
                    fieldbackground=input_bg,
                    background=input_bg,
                    padding=5,
                    arrowsize=12,
                    arrowcolor=text_color)
    
    style.map('TSpinbox',
              fieldbackground=[('readonly', input_bg)],
              background=[('readonly', input_bg)],
              foreground=[('readonly', text_color)],
              bordercolor=[('focus', primary_color)],
              arrowcolor=[('disabled', disabled_color)])

    # Botones
    style.configure('TButton',
                    font=('Segoe UI', 10),
                    padding=6,
                    borderwidth=1,
                    relief="raised")
    
    style.configure('Primary.TButton',
                    font=('Segoe UI', 10, 'bold'),
                    padding=8,
                    background=button_color,
                    foreground="white",
                    borderwidth=1,
                    relief="raised",
                    focuscolor=button_color + "30")  # Color de foco con transparencia
    
    style.map('Primary.TButton',
              background=[('active', button_hover), ('pressed', button_hover)],
              relief=[('pressed', 'sunken')],
              bordercolor=[('focus', primary_color)])
    
    style.configure('Secondary.TButton',
                    font=('Segoe UI', 10),
                    padding=6,
                    background="#e0e0e0",
                    foreground=text_color,
                    borderwidth=1,
                    relief="raised")
    
    style.map('Secondary.TButton',
              background=[('active', '#d0d0d0'), ('pressed', '#d0d0d0')],
              relief=[('pressed', 'sunken')])
    
    style.configure('Danger.TButton',
                    font=('Segoe UI', 10, 'bold'),
                    padding=8,
                    background=danger_color,
                    foreground="white",
                    borderwidth=1,
                    relief="raised")
    
    style.map('Danger.TButton',
              background=[('active', '#c0392b'), ('pressed', '#c0392b')],
              relief=[('pressed', 'sunken')])
    
    style.configure('Success.TButton',
                    font=('Segoe UI', 10, 'bold'),
                    padding=8,
                    background=success_color,
                    foreground="white",
                    borderwidth=1,
                    relief="raised")
    
    style.map('Success.TButton',
              background=[('active', '#218838'), ('pressed', '#218838')],
              relief=[('pressed', 'sunken')])

    # Radio buttons y checkbuttons
    style.configure('TRadiobutton', 
                   background=panel_color, 
                   foreground=text_color,
                   indicatorcolor=input_bg,
                   indicatordiameter=15,
                   indicatorrelief="sunken",
                   padding=5)
    
    style.map('TRadiobutton',
              indicatorcolor=[('selected', primary_color), ('active', primary_color + "80")])
    
    style.configure('TCheckbutton', 
                   background=panel_color, 
                   foreground=text_color,
                   indicatorcolor=input_bg,
                   indicatordiameter=15,
                   indicatorrelief="sunken",
                   padding=5)
    
    style.map('TCheckbutton',
              indicatorcolor=[('selected', primary_color), ('active', primary_color + "80")])

    # Scrollbars
    style.configure('TScrollbar',
                   background=background_color,
                   troughcolor=background_color,
                   bordercolor=background_color,
                   arrowcolor=text_color,
                   gripcount=0)
    
    style.map('TScrollbar',
              background=[('active', secondary_color)],
              arrowcolor=[('disabled', disabled_color)])

    # Progressbar
    style.configure('TProgressbar',
                   background=primary_color,
                   troughcolor=background_color,
                   bordercolor=background_color,
                   lightcolor=primary_color,
                   darkcolor=primary_color,
                   thickness=20)

    # Notebook (tabs)
    style.configure('TNotebook',
                   background=background_color,
                   tabmargins=(2, 2, 2, 0),
                   borderwidth=0)
    
    style.configure('TNotebook.Tab',
                   background="#e0e0e0",
                   foreground=text_color,
                   padding=(12, 6),
                   borderwidth=1,
                   focuscolor=background_color)
    
    style.map('TNotebook.Tab',
              background=[('selected', panel_color), ('active', '#f0f0f0')],
              expand=[('selected', (1, 1, 1, 0))])

    # Separator
    style.configure('TSeparator',
                   background=border_color)

    # Treeview
    style.configure('Treeview',
                   background=input_bg,
                   foreground=text_color,
                   fieldbackground=input_bg,
                   borderwidth=0,
                   font=('Segoe UI', 10))
    
    style.map('Treeview',
              background=[('selected', primary_color)],
              foreground=[('selected', 'white')])
    
    style.configure('Treeview.Heading',
                   font=('Segoe UI', 10, 'bold'),
                   background=background_color,
                   foreground=text_color,
                   padding=5,
                   relief="flat")
    
    style.configure('Treeview.Item',
                   padding=2)
    
    style.configure('Treeview.Cell',
                   padding=5)