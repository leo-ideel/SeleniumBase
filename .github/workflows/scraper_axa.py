from seleniumbase import BaseCase
import pyautogui
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import edit_img
import os

# a retenir utiliser fonction self.cdp.anything pour etre safe de pas etre cpater bot
# car si juste utiliser self.click() on revien sur le driver en gros et faut etre en no driver 

BaseCase.main(__name__, __file__)



class MyTestClass(BaseCase):
    def test_run(self):
        
        user = "G124293"
        mdp = "09090"
        
        url = "https://inaxa.axa-courtage.fr/"
        # url = "https://chatgpt.com/"
        
        # is_headed = True
        is_headed = True
        # A changer selon si on est en headed ou headless True pour headed
        
        # self.set_window_size(1440, 900)
        

        self.activate_cdp_mode(url)
        rect = self.cdp.get_window_rect()
        print("\n\n rect : \n\n", rect)

        time.sleep(5)
        print("je crois que cest reussi")
        self.cdp.save_screenshot("full.png")
        
        time.sleep(5)
        grid = edit_img.generate_grid(is_headed)
        print(grid)

        self.cdp.save_screenshot("jeanne.png")
        

        # self.cdp.type("#input_login", user)
        # self.input_code(mdp, grid)
        return
        # self.cdp.click("#formulaire_valider")

        # time.sleep(5)
        # self.cdp.save_screenshot("elle-est-ou-jeanne.png")
        # try:
        #     self.cdp.click("#MainHomeEdito > div > div.mainHomeEdito-right > div.tools-container > div > div.tools-content > div:nth-child(1) > a > strong")
        # except:
        #     self.cdp.solve_captcha()
            
        # time.sleep(3)
        # selector = "#ptfliste > tbody > tr.even > td > a"
        # self.cdp.switch_to_newest_tab()
        # tabs = self.cdp.get_tabs()
        # self.cdp.switch_to_tab(tabs[1])

        
        # self.save_screenshot("elle-est-ou-jeanne.png")
        
        # time.sleep(5)
        # frames = self.cdp.execute_script("return Array.from(window.frames).map(f => f.name)")
        # print(frames)

        # self.switch_to_frame("main")
        # time.sleep(10)
        # input("avant le click")
        # self.cdp.click(selector)

        
        # input("wait")


        # time.sleep(2)
        # self.cdp.click("#j1 > table:nth-child(5) > tbody > tr:nth-child(1) > td:nth-child(1) > h1 > a")
        # input("here")
        # frames = self.cdp.execute_script("return Array.from(window.frames).map(f => f.name)")
        # print(frames)
        
        

        

        
        # input("fin du test")
        # self.driver.quit()

        # self.cdp.gui_click_x_y(100, 400, timeframe=0.25)


        # Liste de coordonnées
# Au lieu de coords fixes
# Boucle infinie sur les coordonnées
# 350 390 
# 450 390
# 450 340 | 461 361 | 409 329
        # while True:
            # user_input = input("Entrez les coordonnées séparées par des espaces (ex: 200 300) : ")
            # x_str, y_str = user_input.split()
            # coords = [(int(x_str), int(y_str))]

            # for x, y in coords:
            #     js = f"""
            #         // Clique simulé avant d'afficher le cercle
            #         var target = document.elementFromPoint({x}, {y});
            #         if(target) {{
            #             var ev = new MouseEvent('click', {{
            #                 clientX: {x},
            #                 clientY: {y},
            #                 bubbles: true,
            #                 cancelable: true,
            #                 view: window
            #             }});
            #             target.dispatchEvent(ev);
            #         }}

            #         // Puis affiche le cercle rouge
            #         var circle = document.createElement('div');
            #         circle.style.position = 'absolute';
            #         circle.style.left = '{x - 5}px';
            #         circle.style.top = '{y - 5}px';
            #         circle.style.width = '10px';
            #         circle.style.height = '10px';
            #         circle.style.borderRadius = '50%';
            #         circle.style.backgroundColor = 'red';
            #         circle.style.opacity = '0.5';
            #         circle.style.zIndex = 9999;
            #         document.body.appendChild(circle);
            #         """
            #     self.cdp.execute_script(js)


            # print(f"Clic effectué sur {x},{y}")



        # time.sleep(5)
        # print("Clic en 90,350")
        
        
        # # self.click_xy(100,400 )
        
        
        # input("Appuyez sur Entrée pour continuer...")
       
        
        
        
        # input("ca va prendre le screen")
        # self.save_screenshot("full.png")
        
        # input("ca va couper")
        # grid = edit_img.generate_grid()
        # print(grid)
        
        
        # self.type("#input_login", user)
        # self.input_code(mdp, grid)
        
        

        
        # input("fin du test")
        # self.driver.quit()
        
        
        
        
        
        
       
        
        
        # self.sleep(2.2)
        # self.uc_gui_click_captcha()

        # input("mettre mot de passe et appuyer sur entrée")
        
        # self.click("#MainHomeEdito > div > div.mainHomeEdito-right > div.tools-container > div > div.tools-content > div:nth-child(1) > a > strong")
        # self.click("#ptfliste > tbody > tr.odd > td > a")
        # self.click("#j1 > table:nth-child(5) > tbody > tr:nth-child(1) > td:nth-child(1) > h1 > a")
        



    
    def click_xy(self, x, y):
        time.sleep(2)
        js = f"""
            // Clique simulé avant d'afficher le cercle
            var target = document.elementFromPoint({x}, {y});
            if(target) {{
                var ev = new MouseEvent('click', {{
                    clientX: {x},
                    clientY: {y},
                    bubbles: true,
                    cancelable: true,
                    view: window
                }});
                target.dispatchEvent(ev);
            }}

            // Puis affiche le cercle rouge
            var circle = document.createElement('div');
            circle.style.position = 'absolute';
            circle.style.left = '{x - 5}px';
            circle.style.top = '{y - 5}px';
            circle.style.width = '10px';
            circle.style.height = '10px';
            circle.style.borderRadius = '50%';
            circle.style.backgroundColor = 'red';
            circle.style.opacity = '0.5';
            circle.style.pointerEvents = 'none';
            circle.style.zIndex = 9999;
            document.body.appendChild(circle);
            """
        self.cdp.execute_script(js)
        print(f"Clic effectué sur {x},{y}")
 



    def input_code(self, password, grid):
        print("Grille des chiffres détectés :")
        print(grid)
        for digit in password:
            number = int(digit)
            if number in grid:
                x, y = grid[number]
                print(f"Clic sur le chiffre {number} aux coordonnées ({x}, {y})")
                self.click_xy(x, y)
            else:
                print(f"Chiffre {number} non trouvé dans la grille.")
