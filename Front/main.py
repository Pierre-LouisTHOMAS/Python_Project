# main.py
import runpy
from Back.bdd import get_db_connection


def main():
    # Connexion à la base de données
    connection = get_db_connection()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # Exécution d'une requête simple, par exemple pour vérifier que la connexion fonctionne
                cursor.execute("SELECT * FROM Client LIMIT 1;")
                result = cursor.fetchone()
                print("Connexion à la base de données réussie. Résultat de test:", result)
        finally:
            # S'assurer que la connexion est fermée après avoir terminé
            connection.close()

    # Exécuter un autre script Python
    # Assurez-vous que le chemin est correct
    runpy.run_path(path_name='Page_Principale.py')


if __name__ == "__main__":
    main()
