import os
from typing import List, Dict
import chardet
from datetime import datetime

class Logger:
    """
    Classe gérant la journalisation des événements dans un fichier de log.
    Enregistre les messages avec horodatage.
    """
    def __init__(self, log_file: str):
        """
        Initialise le logger avec le chemin du fichier de log.
        
        Args:
            log_file (str): Chemin vers le fichier de log
        """
        self.log_file = log_file

    def log(self, message: str):
        """
        Enregistre un message dans le fichier de log avec horodatage.
        
        Args:
            message (str): Message à journaliser
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        with open(self.log_file, 'a', encoding='utf-8') as file:
            file.write(log_entry)

class FileManager:
    """
    Classe principale gérant les opérations sur les fichiers.
    Permet la lecture, l'écriture, l'analyse et la recherche dans les fichiers.
    """
    def __init__(self, directory: str, log_file: str):
        """
        Initialise le gestionnaire de fichiers.
        
        Args:
            directory (str): Répertoire de travail
            log_file (str): Chemin vers le fichier de log
        """
        # Crée le répertoire s'il n'existe pas
        self.directory = directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        # Initialise le logger et le chemin de fichier courant
        self.logger = Logger(log_file)
        self.file_path = None

    def set_file_path(self, filename: str):
        """
        Définit le fichier courant sur lequel travailler.
        
        Args:
            filename (str): Nom du fichier à utiliser
        """
        self.file_path = os.path.join(self.directory, filename)
        self.logger.log(f"Fichier courant défini : {self.file_path}")

    def read_file(self) -> str:
        """
        Lit le contenu du fichier courant en détectant automatiquement l'encodage.
        
        Returns:
            str: Contenu du fichier ou chaîne vide en cas d'erreur
        """
        if not self.file_path:
            self.logger.log("Erreur : Aucun fichier sélectionné")
            return "Erreur : Aucun fichier sélectionné"
        
        try:
            # Détecte l'encodage du fichier
            with open(self.file_path, 'rb') as file:
                raw_data = file.read()
                encoding = chardet.detect(raw_data)['encoding']
            # Lit le fichier avec l'encodage détecté
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
        """
        Écrit des données dans le fichier courant.
        
        Args:
            data (str): Données à écrire dans le fichier
            
        Returns:
            bool: True si l'écriture a réussi, False sinon
        """
        if not self.file_path:
            self.logger.log("Erreur : Aucun fichier sélectionné")
            return False
        
        try:
            # Écrit les données en UTF-8
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
        """
        Compte le nombre de lignes dans le fichier courant.
        
        Returns:
            int: Nombre de lignes ou 0 en cas d'erreur
        """
        if not self.file_path:
            self.logger.log("Erreur : Aucun fichier sélectionné")
            return 0
        
        try:
            # Utilise un générateur pour compter efficacement les lignes
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
        """
        Recherche un mot-clé dans le fichier et retourne les lignes correspondantes.
        
        Args:
            keyword (str): Mot-clé à rechercher
            
        Returns:
            List[str]: Liste des lignes contenant le mot-clé
        """
        if not self.file_path:
            self.logger.log("Erreur : Aucun fichier sélectionné")
            return []
        
        try:
            # Lit le fichier et collecte les lignes contenant le mot-clé
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
        """
        Analyse le fichier courant et retourne des statistiques.
        
        Returns:
            Dict: Dictionnaire contenant les statistiques du fichier
                (nom, taille, nombre de lignes, mots et caractères)
        """
        if not self.file_path:
            self.logger.log("Erreur : Aucun fichier sélectionné")
            return {}
        
        # Collecte diverses statistiques sur le fichier
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
        """
        Liste tous les fichiers dans le répertoire de travail.
        
        Returns:
            List[str]: Liste des noms de fichiers dans le répertoire
        """
        # Liste uniquement les fichiers (pas les dossiers)
        files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]
        self.logger.log("Liste des fichiers récupérée")
        return files