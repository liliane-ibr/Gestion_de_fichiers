### README.md

```markdown
# File Manager Project

This project implements a simple file management system using Python, demonstrating object-oriented programming concepts and the use of external libraries.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/file-manager-project.git
   cd file-manager-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the project, execute the main script:

```bash
python main.py
```

This will demonstrate the functionality of the `FileManager` class, including:

- Reading from a file
- Writing to a file
- Searching for keywords
- Analyzing the file
- Counting lines
- Listing files in the directory

### Example Usage

1. **Select a File**: Choose option 1 from the menu and enter the name of the file to select.
2. **Read File**: Select option 2 to read the contents of the selected file.
3. **Write to File**: Choose option 3 to write data to the file.
4. **Count Lines**: Use option 4 to count the number of lines in the file.
5. **Search for a Keyword**: Use option 5 to search for a specific keyword within the file.
6. **Analyze File**: Select option 6 to get an analysis of the file, including the number of words and characters.
7. **List Files**: Option 7 will list all files in the specified directory.

## Project Structure

- `file_manager.py`: Contains the implementation of the `FileManager` class.
- `main.py`: Demonstrates the usage of the `FileManager` class.
- `log.txt`: Sample log file for testing and logging purposes.
- `requirements.txt`: Lists the project dependencies.

## The `requirements.txt` File

The `requirements.txt` file lists all the Python packages that the project depends on. By specifying the exact versions of the dependencies, we ensure that the project works consistently across different environments.

In this project, we use the following dependencies:
- `chardet`: A library used for character encoding detection.

To install the dependencies listed in `requirements.txt`, use:

```bash
pip install -r requirements.txt
```

This command will install all the specified packages and their correct versions, ensuring that your environment matches the one used for development.


### Documentation de la classe `FileManager`

```python
import os
from typing import List, Dict
import chardet
from datetime import datetime

class Logger:
    def __init__(self, log_file: str):
        """
        Initialise un logger avec un fichier de log spécifié.
        
        :param log_file: Chemin du fichier de log.
        """
        self.log_file = log_file

    def log(self, message: str):
        """
        Enregistre un message dans le fichier de log avec un timestamp.
        
        :param message: Le message à enregistrer dans le log.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        with open(self.log_file, 'a', encoding='utf-8') as file:
            file.write(log_entry)

class FileManager:
    def __init__(self, directory: str, log_file: str):
        """
        Initialise une instance de FileManager.
        
        :param directory: Répertoire dans lequel les fichiers seront gérés.
        :param log_file: Chemin du fichier de log où les actions seront enregistrées.
        """
        self.directory = directory
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.logger = Logger(log_file)
        self.file_path = None  # Nouveau: pour stocker le chemin du fichier actuel

    def set_file_path(self, filename: str):
        """
        Définit le chemin du fichier courant à partir du nom de fichier donné.
        
        :param filename: Nom du fichier à définir comme fichier courant.
        """
        self.file_path = os.path.join(self.directory, filename)
        self.logger.log(f"Fichier courant défini : {self.file_path}")

    def read_file(self) -> str:
        """
        Lit le contenu du fichier courant et retourne son contenu.
        
        :return: Contenu du fichier ou un message d'erreur si aucun fichier n'est sélectionné.
        """
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
        """
        Écrit des données dans le fichier courant.
        
        :param data: Données à écrire dans le fichier.
        :return: True si l'écriture est réussie, sinon False.
        """
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
        """
        Compte le nombre de lignes dans le fichier courant.
        
        :return: Nombre de lignes ou 0 si aucun fichier n'est sélectionné.
        """
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
        """
        Recherche un mot-clé dans le fichier courant et retourne les lignes correspondantes.
        
        :param keyword: Mot-clé à rechercher dans le fichier.
        :return: Liste des lignes contenant le mot-clé ou une liste vide si aucun fichier n'est sélectionné.
        """
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
        """
        Analyse le fichier courant et retourne des statistiques sur son contenu.
        
        :return: Dictionnaire contenant le nom du fichier, la taille, le nombre de lignes, de mots et de caractères.
        """
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
        """
        Liste tous les fichiers dans le répertoire géré.
        
        :return: Liste des fichiers présents dans le répertoire.
        """
        files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]
        self.logger.log("Liste des fichiers récupérée")
        return files
```