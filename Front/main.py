import subprocess
import platform


def main():
    script_name = 'Page_Principale.py'  # Assurez-vous que ce chemin est correct.

    python_executable = 'python3' if platform.system() != 'Windows' else 'python'

    try:
        # Exécutez le script dans un nouveau processus.
        subprocess.run([python_executable, script_name])
    except Exception as e:
        print(f"Une erreur est survenue lors du lancement du script {script_name}: {e}")


if __name__ == "__main__":
    main()
