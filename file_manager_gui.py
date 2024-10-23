import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import os
from file_manager import FileManager

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionnaire de fichiers")
        self.root.geometry("700x500")
        self.root.config(bg="black")  # Couleur de fond de la fenêtre principale

        self.base_dir = "./files"
        self.log_file = os.path.join(self.base_dir, "file_manager.log")
        self.manager = FileManager(self.base_dir, self.log_file)

        # Interface
        self.create_widgets()

    def create_widgets(self):
        # Frame pour la barre de titre
        title_frame = tk.Frame(self.root, bg="#34495E")
        title_frame.pack(fill=tk.X)

        # Label d'instruction
        self.label = tk.Label(title_frame, text="Gestionnaire de fichiers", font=("Arial", 18, "bold"), fg="white", bg="#34495E")
        self.label.pack(pady=20)

        # Frame pour la zone de texte et les boutons
        main_frame = tk.Frame(self.root, bg="black")  # Fond noir pour le cadre principal
        main_frame.pack(pady=10)

        # Zone de texte pour afficher les résultats (fond noir)
        self.text_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=70, height=15, font=("Arial", 12), bg="black", fg="white")
        self.text_area.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

        # Boutons avec une meilleure organisation
        self.btn_select_file = tk.Button(main_frame, text="Sélectionner un fichier", command=self.select_file, bg="#1ABC9C", fg="white", font=("Arial", 12))
        self.btn_select_file.grid(row=1, column=0, padx=10, pady=10)

        self.btn_read_file = tk.Button(main_frame, text="Lire le fichier", command=self.read_file, bg="#3498DB", fg="white", font=("Arial", 12))
        self.btn_read_file.grid(row=1, column=1, padx=10, pady=10)

        self.btn_write_file = tk.Button(main_frame, text="Écrire dans le fichier", command=self.write_file, bg="#9B59B6", fg="white", font=("Arial", 12))
        self.btn_write_file.grid(row=1, column=2, padx=10, pady=10)

        self.btn_count_lines = tk.Button(main_frame, text="Compter les lignes", command=self.count_lines, bg="#F39C12", fg="white", font=("Arial", 12))
        self.btn_count_lines.grid(row=2, column=0, padx=10, pady=10)

        self.btn_search_keyword = tk.Button(main_frame, text="Rechercher un mot-clé", command=self.search_keyword, bg="#E74C3C", fg="white", font=("Arial", 12))
        self.btn_search_keyword.grid(row=2, column=1, padx=10, pady=10)

        self.btn_analyze_file = tk.Button(main_frame, text="Analyser le fichier", command=self.analyze_file, bg="#2ECC71", fg="white", font=("Arial", 12))
        self.btn_analyze_file.grid(row=2, column=2, padx=10, pady=10)

        self.btn_view_logs = tk.Button(main_frame, text="Voir les logs", command=self.view_logs, bg="#34495E", fg="white", font=("Arial", 12))
        self.btn_view_logs.grid(row=3, column=1, padx=10, pady=10)

    # Fonctions de gestion
    def select_file(self):
        filename = filedialog.askopenfilename(initialdir=self.base_dir, title="Sélectionnez un fichier")
        if filename:
            self.manager.set_file_path(os.path.basename(filename))
            self.text_area.insert(tk.END, f"Fichier sélectionné: {filename}\n")

    def read_file(self):
        content = self.manager.read_file()
        if content:
            self.text_area.insert(tk.END, f"Contenu du fichier :\n{content}\n")

    def write_file(self):
        content = tk.simpledialog.askstring("Écrire dans le fichier", "Contenu à écrire :")
        if content and self.manager.write_to_file(content):
            self.text_area.insert(tk.END, "Fichier écrit avec succès.\n")
        else:
            self.text_area.insert(tk.END, "Erreur lors de l'écriture du fichier.\n")

    def count_lines(self):
        line_count = self.manager.count_lines()
        self.text_area.insert(tk.END, f"Nombre de lignes : {line_count}\n")

    def search_keyword(self):
        keyword = tk.simpledialog.askstring("Rechercher un mot-clé", "Mot-clé à rechercher :")
        if keyword:
            matches = self.manager.search_keyword(keyword)
            if matches:
                self.text_area.insert(tk.END, f"Lignes contenant '{keyword}':\n")
                for line in matches:
                    self.text_area.insert(tk.END, f"{line}\n")
            else:
                self.text_area.insert(tk.END, f"Aucune correspondance pour '{keyword}'.\n")

    def analyze_file(self):
        analysis = self.manager.analyze_file()
        if analysis:
            for key, value in analysis.items():
                self.text_area.insert(tk.END, f"{key}: {value}\n")

    def view_logs(self):
        try:
            with open(self.log_file, 'r', encoding='utf-8') as file:
                log_content = file.read()
            self.text_area.insert(tk.END, f"Contenu des logs :\n{log_content}\n")
        except IOError as e:
            messagebox.showerror("Erreur", f"Impossible de lire le fichier de logs : {e}")

# Programme principal
if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
