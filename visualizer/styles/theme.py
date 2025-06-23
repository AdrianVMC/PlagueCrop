from tkinter import ttk

def BaseStyles(style: ttk.Style):
    style.theme_use("clam")

    style.configure('Primary.TButton',
                    font=('Helvetica', 12, 'bold'),
                    padding=10,
                    background="#999999",
                    foreground="white")
    style.map('Primary.TButton',
              background=[('active', "#555555")],
              foreground=[('disabled', "#999999")])


    style.configure('Secondary.TButton',
                    font=('Helvetica', 11),
                    padding=8,
                    background="#DDDDDD",
                    foreground="#000000")

    style.configure('Danger.TButton',
                    font=('Helvetica', 12, 'bold'),
                    padding=10,
                    background="red",
                    foreground="white")
    style.map('Danger.TButton',
              background=[('active', '#cc0000')])

    style.configure('Title.TLabel',
                    font=('Helvetica', 24, 'bold'),
                    foreground="#000000",
                    background="#F0F0F0")
    
    style.configure('Subtitle.TLabel',
                    font=('Helvetica', 12),
                    foreground="#000000",
                    background="#F0F0F0")

    style.configure('TLabel',
                    font=('Helvetica', 10),
                    background="#A4A4A4",
                    foreground="#000000")

    style.configure('Section.TLabelframe',
                    background="#A4A4A4",
                    foreground="#333333",
                    relief="groove",
                    borderwidth=2)

    style.configure('Section.TLabelframe.Label',
                    font=('Helvetica', 11, 'bold'),
                    background="#A4A4A4",
                    foreground="#222222")
