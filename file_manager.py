import os
from typing import List, Dict
import chardet
from datetime import datetime

class Logger:
    def __init__(self, log_file: str):
        self.log_file = log_file

    def log(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        with open(self.log_file, 'a', encoding='utf-8') as file:
            file.write(log_entry)

class FileManager:
    def __init__(self, directory: str, log_file: str):
        self.directory = directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.logger = Logger(log_file)
        self.file_path = None  # Nouveau: pour stocker le chemin du fichier actuel

    def set_file_path(self, filename: str):
        self.file_path = os.path.join(self.directory, filename)
        self.logger.log(f"Fichier courant défini : {self.file_path}")

    def read_file(self) -> str:
        if not self.file_path:
            self.logger.log("Erreur : Aucun fichier sélectionné")
            return "Erreur : Aucun fichier sélectionné"
        
        try:
            with open(self.file_path, 'rb') as file:
                raw_data = file.read()
                encoding = chardet.detect(raw_data)['encoding']
            with open(self.file_path, 'r', encoding=encoding) as file:
                content = file.read()
            self.logger.log(f"Fichier lu : {self.file_path}")
            print("Contenu du fichier:")
            print(content)
            return content
        except IOError as e:
            error_message = f"Erreur lors de la lecture du fichier {self.file_path}: {e}"
            print(error_message)
            self.logger.log(error_message)
            return ""

    def write_to_file(self, data: str) -> bool:
        if not self.file_path:
            self.logger.log("Erreur : Aucun fichier sélectionné")
            return False
        
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                file.write(data)
            self.logger.log(f"Données écrites dans le fichier : {self.file_path}")
            return True
        except IOError as e:
            error_message = f"Erreur lors de l'écriture dans le fichier {self.file_path}: {e}"
            print(error_message)
            self.logger.log(error_message)
            return False

    def count_lines(self) -> int:
        if not self.file_path:
            self.logger.log("Erreur : Aucun fichier sélectionné")
            return 0
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                line_count = sum(1 for _ in file)
            self.logger.log(f"Nombre de lignes comptées dans {self.file_path}: {line_count}")
            return line_count
        except IOError as e:
            error_message = f"Erreur lors du comptage des lignes dans {self.file_path}: {e}"
            print(error_message)
            self.logger.log(error_message)
            return 0

    def search_keyword(self, keyword: str) -> List[str]:
        if not self.file_path:
            self.logger.log("Erreur : Aucun fichier sélectionné")
            return []
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                matching_lines = [line.strip() for line in file if keyword in line]
            
            self.logger.log(f"Recherche du mot-clé '{keyword}' dans {self.file_path}")
            if matching_lines:
                print(f"Lignes contenant le mot-clé '{keyword}':")
                for line in matching_lines:
                    print(line)
            else:
                print(f"Aucune ligne contenant le mot-clé '{keyword}' n'a été trouvée.")
            return matching_lines
        except IOError as e:
            error_message = f"Erreur lors de la recherche dans {self.file_path}: {e}"
            print(error_message)
            self.logger.log(error_message)
            return []

    def analyze_file(self) -> Dict:
        if not self.file_path:
            self.logger.log("Erreur : Aucun fichier sélectionné")
            return {}
        
        content = self.read_file()
        analysis = {
            "filename": os.path.basename(self.file_path),
            "size": len(content),
            "line_count": self.count_lines(),
            "word_count": len(content.split()),
            "char_count": len(content)
        }
        self.logger.log(f"Fichier analysé : {self.file_path}")
        return analysis

    def list_files(self) -> List[str]:
        files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]
        self.logger.log("Liste des fichiers récupérée")
        return files
