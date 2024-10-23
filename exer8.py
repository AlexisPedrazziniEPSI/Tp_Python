import threading
import time
from functools import wraps


class TimeoutError(Exception):
    """Exception levée lorsque la limite de temps est dépassée."""
    pass


def timeout_limit(timeout, raise_exception=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Variable pour stocker l'exception
            result = [None]
            exc = [None]

            # Fonction interne exécutée dans un thread séparé
            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    exc[0] = e

            # Démarrage du thread pour exécuter la fonction
            thread = threading.Thread(target=target)
            thread.start()

            # Attente pendant la durée spécifiée
            thread.join(timeout)

            # Si le thread est toujours actif après le timeout
            if thread.is_alive():
                if raise_exception:
                    raise TimeoutError("Exécution interrompue par raise_exception.")
                else:
                    raise TimeoutError("La limite de temps a été dépassée.")

            # Si une exception a été levée dans le thread, la relancer
            if exc[0]:
                raise exc[0]

            return result[0]

        return wrapper

    return decorator


# Exemple d'utilisation :
@timeout_limit(5, raise_exception=False)
def long_task():
    print("Tâche longue démarrée")
    time.sleep(10)  # Simuler une tâche longue
    print("Tâche longue terminée")


try:
    long_task()
except TimeoutError as e:
    print(e)