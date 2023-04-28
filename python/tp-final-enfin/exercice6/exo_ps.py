import logging
import shutil
import psutil
import sched
import time

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.RotatingFileHandler(
        filename='check_bad_programs.log',
        maxBytes=1024 * 1024,
        backupCount=3
    )]
)
logger = logging.getLogger(__name__)

process_names_to_kill = ["Teams.exe", "Discord.exe", "Spotify.exe"]

def check_processes_and_disk_space():
    killed_processes = []
    for process in psutil.process_iter():
        try:
            if process.name() in process_names_to_kill:
                process.kill()
                killed_processes.append(process.name())
                logger.warning(f"Le processus {process.name()} a été tué.")
        except:
            pass

    usage = shutil.disk_usage('/')
    if usage.percent > 80:
        logger.critical("L'espace disque disponible est inférieur à 20%.")
    elif usage.percent > 70:
        logger.warning("L'espace disque maximal est presque atteint.")
    elif not killed_processes:
        logger.info("Il n'y a rien à signaler.")

scheduler = sched.scheduler(time.time, time.sleep)
def periodic_check():
    check_processes_and_disk_space()
    scheduler.enter(5, 1, periodic_check, ())

periodic_check()
scheduler.run()
