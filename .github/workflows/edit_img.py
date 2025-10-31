from PIL import Image
import pytesseract

# --- Config de la grille et des cases ---
rows, cols = 3, 8
case_width = 30
case_height = 30
start_x = 380
start_y = 380


# --- Fonctions utilitaires ---

def get_grid_boxes(image, rows, cols):
    """Découpe l'image en cases pour OCR"""
    width, height = image.size
    box_width = width // cols
    box_height = height // rows
    boxes = []
    for r in range(rows):
        row_boxes = []
        for c in range(cols):
            x0 = c * box_width
            y0 = r * box_height
            x1 = x0 + box_width
            y1 = y0 + box_height
            row_boxes.append((x0, y0, x1, y1))
        boxes.append(row_boxes)
    return boxes

def coord_to_click(r, c):
    """Convertit ligne/colonne en coordonnées réelles pour clic"""
    x = start_x + c * case_width
    y = start_y + r * case_height
    return x, y

def reel_coordonnees(number_to_coord):
    """
    Transforme le dictionnaire number_to_coord en coordonnées réelles.
    Retourne un dictionnaire {number: (x, y)}
    """
    number_to_click = {}
    for number, coord in number_to_coord.items():
        r = int(coord[0])
        c = int(coord[1])
        number_to_click[number] = coord_to_click(r, c)
    return number_to_click

def get_croped_screenshot(is_headed):
    img = Image.open("full.png")
    w, h = img.size
    
    # Jai tout melanger desole top left bottom cest pas le bon ordre mais jai juste mal nomme
    # plus faut ajouter une variable headless ou pas
    
    if is_headed:
        left = 375
        top = 265
        right = 460
        bottom = 500
    else:
        left = 375
        top = 355
        right = 460
        bottom = 590
    

#------value en headed
    # left = 375
    # top = 265
    # right = 460
    # bottom = 500
    
#------value en headless
    
    # left = 375
    # top = 355
    # right = 460
    # bottom = 590

    box = (top, left, bottom, right)
    crop = img.crop(box)
    crop.save("center.png")

def extract_numbers_from_image(image_path):
    """Lit une image et retourne le dictionnaire number -> coord case"""
    image = Image.open(image_path)
    boxes = get_grid_boxes(image, rows, cols)
    number_to_coord = {}
    for r in range(rows):
        for c in range(cols):
            cropped = image.crop(boxes[r][c])
            text = pytesseract.image_to_string(cropped, config='--psm 10 -c tessedit_char_whitelist=0123456789').strip()
            if text.isdigit():
                number_to_coord[int(text)] = f"{r}{c}"
    return number_to_coord


# --- Fonction principale pour générer le code ---
def generate_grid(is_headed):
    """
    Découpe la grille, détecte les chiffres et clique sur le chiffre demandé.
    `password` = chiffre à cliquer (ex: 8)
    """
    get_croped_screenshot(is_headed)
    
    # Extraire les chiffres et leurs coordonnées
    number_to_coord = extract_numbers_from_image("center.png")
    number_to_click = reel_coordonnees(number_to_coord)
    
    # Ici tu peux appeler ta fonction Selenium/PyAutoGUI
    return number_to_click
    

# --- Exemple d'utilisation ---
# generate_code(8)
