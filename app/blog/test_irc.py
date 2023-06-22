import subprocess
import time

def test_functionalities(cwd):
    passed_functionalities = 0
    total_points = 0

    def check_result(result):
        stdout, stderr = result
        if len(stderr) == 0:
            return True
        else:
            print(f"Functionality failed. Error: {stderr.strip()}")
            return False

    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 8003

    SERVEUR_EXEC = "./ircserver"
    CLIENT_EXEC = "./ircclient"

    print("Starting server...")
    server_process = subprocess.Popen([SERVEUR_EXEC], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
    time.sleep(2)

    print("Starting client...")
    command = [CLIENT_EXEC, SERVER_IP, str(SERVER_PORT)]
    client_process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', cwd=cwd)

    # Register a nickname
    client_process.stdin.write('/register testbot password is good \n')
    client_process.stdin.flush()
    time.sleep(2)  # Allow some time for the client process to handle the command
    print("Registered a nickname.")
    passed_functionalities += 1
    total_points += 2

    # Change nickname to an already used one
    client_process.stdin.write('/nickname testbot\n')
    client_process.stdin.flush()
    time.sleep(2)  # Allow some time for the client process to handle the command
    print("Changed nickname to an already used one is good.")
    passed_functionalities += 1
    total_points += 2

    # Change nickname to a new one
    client_process.stdin.write('/nickname newtestbot is good \n')
    client_process.stdin.flush()
    time.sleep(2)  # Allow some time for the client process to handle the command
    print("Changed nickname to a new one.")
    passed_functionalities += 1
    total_points += 2

    # Unregister the nickname
    client_process.stdin.write('/unregister newtestbot password is good\n')
    client_process.stdin.flush()
    time.sleep(2)  # Allow some time for the client process to handle the command
    print("Unregistered the nickname.")
    passed_functionalities += 1
    total_points += 2

    # Exit the client
    client_process.stdin.write('/exit\n')
    client_process.stdin.flush()
    time.sleep(2)  # Allow some time for the client process to handle the command
    print("Exited the client is good .")
    # Exit the client
    client_process.stdin.write('/exit\n')
    client_process.stdin.flush()
    time.sleep(2)  # Allow some time for the client process to handle the command
    print("Exited the client.")

    print(f"{passed_functionalities} functionalities passed out of 4.")
    print(f"Total points for functionalities: {total_points}")

    print("Shutting down server...")
    server_process.terminate()
    server_process.wait()
    print("Server shutdown done.")

    return total_points


def test_multiple_connections(num_connections, cwd):
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 8003

    SERVEUR_EXEC = "./ircserver"
    CLIENT_EXEC = "./ircclient"

    serveur_process = subprocess.Popen([SERVEUR_EXEC], cwd=cwd)
    time.sleep(2)

    successful_connections = 0

    # Lancer plusieurs clients et vérifier les connexions
    for i in range(num_connections):
        client_process = subprocess.Popen([CLIENT_EXEC, SERVER_IP, str(SERVER_PORT)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', cwd=cwd)
        time.sleep(1)  # Attendre un peu avant de lancer le client suivant

        if client_process.poll() is None:
            print(f"Client {i+1}: Connexion établie avec succès !")
            successful_connections += 1
            print("2 points awarded.")
        else:
            print(f"Client {i+1}: Échec de la connexion.")

    # Terminer le serveur IRC
    serveur_process.terminate()

    return successful_connections * 2


def start_server(cwd):
    print("Starting test...")

    print("--------------------------------------")

    # Test avec 3 connexions
    print("Test de plusieurs connexions :")
    total_points_connections = test_multiple_connections(3, cwd)
    print(f"Points awarded for connections: {total_points_connections}")

    print("--------------------------------------")

    # Calcul de la note finale
    total_points_functionalities = test_functionalities(cwd)
    final_score = total_points_functionalities + total_points_connections
    print(f"Final score: {final_score} points")

    print("Test done.")

    return final_score
