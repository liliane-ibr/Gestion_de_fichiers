import os
import textstat

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
        """
        Initialisation de la classe FileManager.
        Le parametre file_path = Chemin vers le fichier texte à gérer.
        """


    def read_file(self):
        """
        Lit le contenu du fichier texte.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Le fichier {self.file_path} n'existe pas.")
        """Erreur si le fichier n'existe pas"""
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        return content
    """Contenu du fichier sous forme de chaîne de caractères."""


    def write_file(self, content, mode='a'):
        """
        Ajoute du contenu au fichier texte
        Le parametre content = contenu à écrire entré par l'utilisateur 
        """
        with open(self.file_path, mode, encoding='utf-8') as file:
            file.write(content)

        print(f"Contenu ajouté au fichier {self.file_path}.")


    def analyze_file(self):
        """Analyse le fichier texte et retourne des statistiques."""
        content = self.read_file()
        
        """Incrémentation de variables pour les statistiques"""
        word_count = len(content.split()) 
        line_count = content.count('\n') + 1  
        cara_count = len(content) 
        size_count = os.path.getsize(self.file_path) 
        reading_ease_score = textstat.flesch_reading_ease(content)
        
        return {
            "Nombre de mots": word_count,
            "Nombre de lignes": line_count,
            "Nombre de caractères": cara_count,
            "Taille du fichier en octets": size_count,
            "Score de facilité de lecture": reading_ease_score
        }

    def clear_file(self):
        """
        Efface le contenu du fichier.
        """
        open(self.file_path, 'w').close()  
        """Ouvrir en mode 'w' pour écraser le fichier."""
        print(f"Le contenu du fichier {self.file_path} a été effacé.")
