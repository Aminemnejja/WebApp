import subprocess
import threading

def run_flask():
    subprocess.run(["python", "html_flask.py"])

def run_streamlit():
    subprocess.run(["streamlit", "run", "menu.py","--server.port", "8081"])
    
# Lancer Flask dans un thread séparé
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Lancer Streamlit dans le thread principal
run_streamlit() 
# Attendre que le thread Flask se termine (si nécessaire)
flask_thread.join()
