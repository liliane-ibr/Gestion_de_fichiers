from file_manager import FileManager
import os

def main():
    base_dir = "./files"
    log_file = os.path.join(base_dir, "file_manager.log")
    manager = FileManager(base_dir, log_file)
    
    while True:
        print("\nGestionnaire de fichiers")
        print("1. Sélectionner un fichier")
        print("2. Lire le fichier")
        print("3. Écrire dans le fichier")
        print("4. Compter les lignes")
        print("5. Rechercher un mot-clé")
        print("6. Analyser le fichier")
        print("7. Lister les fichiers")
        print("8. Voir les logs")
        print("9. Quitter")
        
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            filename = input("Nom du fichier à sélectionner : ")
            manager.set_file_path(filename)
        elif choice == "2":
            manager.read_file()
        elif choice == "3":
            content = input("Contenu à écrire : ")
            if manager.write_to_file(content):
                print("Fichier écrit avec succès.")
            else:
                print("Échec de l'écriture du fichier.")
        elif choice == "4":
            line_count = manager.count_lines()
            print(f"Nombre de lignes : {line_count}")
        elif choice == "5":
            keyword = input("Mot-clé à rechercher : ")
            manager.search_keyword(keyword)
        elif choice == "6":
            analysis = manager.analyze_file()
            for key, value in analysis.items():
                print(f"{key}: {value}")
        elif choice == "7":
            files = manager.list_files()
            print("Fichiers dans le répertoire :")
            for file in files:
                print(file)
        elif choice == "8":
            log_content = manager.read_file()
            print("Contenu du fichier de logs :")
            print(log_content)
        elif choice == "9":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()