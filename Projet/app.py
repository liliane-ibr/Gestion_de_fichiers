from filemanager import FileManager

def main():
    
    while True:
        """crée une boucle tant que le script renvoie true"""
        file_path = None
        file_path = input("Entrer le chemin du fichier : ")
        
        if ".txt" in file_path:
            continue
        elif ".txt" not in file_path:
            file_path = file_path + ".txt"
        
        manager = FileManager(file_path)
        
        if file_path:
            print("\n--- Menu ---")
            print("1. Lire un fichier")
            print("2. Écrire dans un fichier")
            print("3. Analyser un fichier")
            print("4. Effacer le contenu du fichier")
            print("5. Quitter") 
            
        choice = input("\nChoisissez une option: ")
        
        if choice == '1':
            try:
                content = manager.read_file()
                print("\n--- Contenu du fichier ---")
                print(content)
            except FileNotFoundError as e:
                print(e)

        elif choice == '2':
            text = input("Entrez le texte à ajouter au fichier: ")
            manager.write_file(text + "\n")

        elif choice == '3':
            try:
                stats = manager.analyze_file()
                print("\n--- Statistiques du fichier ---")
                for key, value in stats.items():
                    print(f"{key}: {value}")
            except FileNotFoundError as e:
                print(e)

        elif choice == '4':
            manager.clear_file()

        elif choice == '5':
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()