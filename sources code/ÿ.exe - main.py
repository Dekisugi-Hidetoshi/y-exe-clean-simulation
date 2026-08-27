
# Import Libraries
import pygame as pg
import random as rd
import os
import sys

# Path Check
def resource_path_checkandload(path):

    try:

        base_path = sys._MEIPASS

    except Exception:
        
        base_path = os.path.abspath(".")

    return os.path.join(base_path, path)

# Initialize Pygame
pg.init()
pg.font.init()
pg.mixer.init()
pg.display.set_caption("Pygame BIOS")
WIDTH, HEIGHT = 512, 320
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Position Calculator Function
def CalcPosition(x, y):
    Calc_X = WIDTH // 2 + x
    Calc_Y = HEIGHT // 2 - y
    return Calc_X, Calc_Y

# Game States setup
STATES = {
    "BIOS":"LOADING BIOS",
    "GM_LAYER_1":"BEEP SOUND",
    "GM_LAYER_2":"MESSAGE",
    "GM_LAYER_3":"KEY TO USE MSG",
    "IN_GAME":"IN GAME",
    "GAME_OVER":"GAME OVER",
    "WIN_THE_GAME":"WHILE 8 HOURS LAST, YOU DID REALLY AMAZING, YOU WILL FREE AFTER COMPLETED THIS GAME AND SAVED YOUR COMPUTER AND ALL DATA"
}

# Game Colors
COLORS = {
    "BLACK_FILL":(0, 0, 0),
    "BROWN_COLOR":(178, 86, 9),
    "ROAD_COLOR":(85, 85, 85), 
    "ROAD_LINE":(255, 237, 33),
    "WHITE_COLOR":(255, 255, 255),
    "BLUE_FILL":(0, 32, 177),
    "RED_COLOR":(212, 10, 33),
    "DARK_RED_COLOR":(174, 2, 22),
    "ORANGE_COLOR":(222, 121, 47),
    "GREEN_COLOR":(25, 145, 24),
    "LIME_COLOR":(78, 167, 39),
    "YELLOW_COLOR":(235, 246, 82),
    "DARK_GRAY":(20, 20, 20),
    "GRAY_GRAVEL":(112, 112, 109),
    "RED_GRAVEL":(234, 107, 85),
    "ORANGE_GRAVEL":(242, 127, 34),
    "LIGHT_RED_COLOR":(246, 7, 10)
}

# Game Sounds
SOUNDS = {
    "BEEP":pg.mixer.Sound(resource_path_checkandload("Beep before.wav")),
    "BACKGROUND":pg.mixer.Sound(resource_path_checkandload("DOSert music.wav")),
    "HONK":pg.mixer.Sound(resource_path_checkandload("honk.wav")),
    "TOUCH":pg.mixer.Sound(resource_path_checkandload("Touch the grass.wav")),
    "LOOSE":pg.mixer.Sound(resource_path_checkandload("Loose.wav"))
}

# Channels Sound Player
CHANNELS = {
    "BEEP":pg.mixer.Channel(1),
    "BACKGROUND":pg.mixer.Channel(7),
    "HONK":pg.mixer.Channel(6),
    "TOUCH":pg.mixer.Channel(5),
    "LOOSE":pg.mixer.Channel(4)
}

# Text Fonts
Fonts = {
    "Large_size":pg.font.Font(resource_path_checkandload("coure.ttf"), 60),
    "Medium_size":pg.font.Font(resource_path_checkandload("coure.ttf"), 20),
    "Game_font":pg.font.Font(resource_path_checkandload("vgafix.ttf"), 25),
    "ETA_Font":pg.font.Font(resource_path_checkandload("vgafix.ttf"), 25)
}

# Static Text
Text = {
    "BIOS":["PYGAME", "Loading..."],

    "BEFORE_GAME_LAYER_1":[

        "if your computer freezes here,", 
        "please reboot.", 

        "*beep*"

        ],

    "BEFORE_GAME_LAYER_2":[

        "YOU DUCKED UP!", 
        "Sadly, all your computer data and", 
        "hardware got corrupted...", 

        "But you can still salvage this.", 
        "You just have to win a round of", 
        "DOSert Bus.", 

        "WARNING:", 
        "DO NOT TURN OFF YOUR COMPUTER", 
        "OR ELSE IT WILL BE LOST FOREVER!", 

        "Press the spacebar to continue."

        ], 

    "BEFORE_GAME_LAYER_3":[

        "CONTROLS",
        "Left Shift / A:", "Steer Left",
        "Right Shift / D:", "Steer Right",
        "Spacebar:", "Honk", 
        "Arrow keys DO NOT WORK!",

        "If you lose or reboot, your computer", 
        "WILL BE GONE FOREVER!", 

        "Press enter start the game."

    ],

    "GAME_OVER":[
        "Game Over.",

        "This computer is destroyed.",
        "The last thing it will display is this",
        "message."
    ],

    "WIN_THE_GAME":[
        "You win!",

        "It is now safe to turn off your", 
        "computer."
    ]
}

# Static Text Surface
Text_Surface = {
    "BIOS":{
        "LOGO":Fonts["Large_size"].render(Text["BIOS"][0], True, COLORS["WHITE_COLOR"]),
        "LOAD_TEXT":Fonts["Medium_size"].render(Text["BIOS"][1], True, COLORS["WHITE_COLOR"])
    },

    "BEFORE_GAME_LAYER_1":{
        "LINE 1":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_1"][0], True, COLORS["RED_COLOR"]),
        "LINE 2":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_1"][1], True, COLORS["RED_COLOR"]),
        "LINE 3":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_1"][2], True, COLORS["WHITE_COLOR"])
    },

    "BEFORE_GAME_LAYER_2":{
        "LINE 1":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_2"][0], True, COLORS["RED_COLOR"]),
        "LINE 2":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_2"][1], True, COLORS["WHITE_COLOR"]),
        "LINE 3":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_2"][2], True, COLORS["WHITE_COLOR"]),
        "LINE 4":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_2"][3], True, COLORS["WHITE_COLOR"]),
        "LINE 5":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_2"][4], True, COLORS["WHITE_COLOR"]),
        "LINE 6":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_2"][5], True, COLORS["BROWN_COLOR"]),
        "LINE 7":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_2"][6], True, COLORS["DARK_RED_COLOR"]),
        "LINE 8":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_2"][7], True, COLORS["RED_COLOR"]),
        "LINE 9":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_2"][8], True, COLORS["RED_COLOR"]),
        "LINE 10":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_2"][9], True, COLORS["ORANGE_COLOR"])
    },

    "BEFORE_GAME_LAYER_3":{
        "LINE 1":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][0], True, COLORS["ORANGE_COLOR"]),
        "LINE 2.1":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][1], True, COLORS["GREEN_COLOR"]),
        "LINE 2.2":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][2], True, COLORS["LIME_COLOR"]),
        "LINE 3.1":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][3], True, COLORS["GREEN_COLOR"]),
        "LINE 3.2":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][4], True, COLORS["LIME_COLOR"]),
        "LINE 4.1":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][5], True, COLORS["GREEN_COLOR"]),
        "LINE 4.2":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][6], True, COLORS["YELLOW_COLOR"]),
        "LINE 5":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][7], True, COLORS["RED_COLOR"]),
        "LINE 6":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][8], True, COLORS["DARK_RED_COLOR"]),
        "LINE 7":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][9], True, COLORS["DARK_RED_COLOR"]),
        "LINE 8":Fonts["Game_font"].render(Text["BEFORE_GAME_LAYER_3"][10], True, COLORS["ORANGE_COLOR"])
    },

    "ETA_TEXT":Fonts["ETA_Font"].render("ETA:", True, COLORS["GREEN_COLOR"]),

    "GAME_OVER":{
        "LINE 1":Fonts["Game_font"].render(Text["GAME_OVER"][0], True, COLORS["DARK_RED_COLOR"]),
        "LINE 2":Fonts["Game_font"].render(Text["GAME_OVER"][1], True, COLORS["LIGHT_RED_COLOR"]),
        "LINE 3":Fonts["Game_font"].render(Text["GAME_OVER"][2], True, COLORS["LIGHT_RED_COLOR"]),
        "LINE 4":Fonts["Game_font"].render(Text["GAME_OVER"][3], True, COLORS["LIGHT_RED_COLOR"])
    },

    "WIN_THE_GAME":{
        "LINE 1":Fonts["Game_font"].render(Text["WIN_THE_GAME"][0], True, COLORS["LIME_COLOR"]),
        "LINE 2":Fonts["Game_font"].render(Text["WIN_THE_GAME"][1], True, COLORS["ORANGE_COLOR"]),
        "LINE 3":Fonts["Game_font"].render(Text["WIN_THE_GAME"][2], True, COLORS["ORANGE_COLOR"])
    }
}

# Static Objects Position
Objects_Position = {
    "BIOS":{
        "LOGO":Text_Surface["BIOS"]["LOGO"].get_rect(center=CalcPosition(0, 30)),
        "LOAD_TEXT":Text_Surface["BIOS"]["LOAD_TEXT"].get_rect(center=CalcPosition(0, -30))
    },

    "BEFORE_GAME_LAYER_1":{
        "LINE 1":Text_Surface["BEFORE_GAME_LAYER_1"]["LINE 1"].get_rect(midleft=CalcPosition(-252, 145)),
        "LINE 2":Text_Surface["BEFORE_GAME_LAYER_1"]["LINE 2"].get_rect(midleft=CalcPosition(-252, 120)),
        "LINE 3":Text_Surface["BEFORE_GAME_LAYER_1"]["LINE 3"].get_rect(midleft=CalcPosition(-252, 70))
    },

    "BEFORE_GAME_LAYER_2":{
        "LINE 1":Text_Surface["BEFORE_GAME_LAYER_2"]["LINE 1"].get_rect(midleft=CalcPosition(-252, 145)),
        "LINE 2":Text_Surface["BEFORE_GAME_LAYER_2"]["LINE 2"].get_rect(midleft=CalcPosition(-252, 110)),
        "LINE 3":Text_Surface["BEFORE_GAME_LAYER_2"]["LINE 3"].get_rect(midleft=CalcPosition(-252, 85)),
        "LINE 4":Text_Surface["BEFORE_GAME_LAYER_2"]["LINE 4"].get_rect(midleft=CalcPosition(-252, 50)),
        "LINE 5":Text_Surface["BEFORE_GAME_LAYER_2"]["LINE 5"].get_rect(midleft=CalcPosition(-252, 25)),
        "LINE 6":Text_Surface["BEFORE_GAME_LAYER_2"]["LINE 6"].get_rect(midleft=CalcPosition(-252, 5)),
        "LINE 7":Text_Surface["BEFORE_GAME_LAYER_2"]["LINE 7"].get_rect(midleft=CalcPosition(-252, -35)),
        "LINE 8":Text_Surface["BEFORE_GAME_LAYER_2"]["LINE 8"].get_rect(midleft=CalcPosition(-252, -60)),
        "LINE 9":Text_Surface["BEFORE_GAME_LAYER_2"]["LINE 9"].get_rect(midleft=CalcPosition(-252, -80)),
        "LINE 10":Text_Surface["BEFORE_GAME_LAYER_2"]["LINE 10"].get_rect(midleft=CalcPosition(-252, -120)),
    },

    "BEFORE_GAME_LAYER_3":{
        "LINE 1":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 1"].get_rect(center=CalcPosition(0, 145)),
        "LINE 2.1":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 2.1"].get_rect(midright=CalcPosition(0, 110)),
        "LINE 2.2":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 2.2"].get_rect(midleft=CalcPosition(20, 110)),
        "LINE 3.1":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 3.1"].get_rect(midright=CalcPosition(0, 85)),
        "LINE 3.2":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 3.2"].get_rect(midleft=CalcPosition(20, 85)),
        "LINE 4.1":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 4.1"].get_rect(midright=CalcPosition(0, 50)),
        "LINE 4.2":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 4.2"].get_rect(midleft=CalcPosition(20, 50)),
        "LINE 5":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 5"].get_rect(center=CalcPosition(25, 15)),
        "LINE 6":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 6"].get_rect(midleft=CalcPosition(-252, -40)),
        "LINE 7":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 7"].get_rect(midleft=CalcPosition(-252, -65)),
        "LINE 8":Text_Surface["BEFORE_GAME_LAYER_3"]["LINE 8"].get_rect(midleft=CalcPosition(-252, -130)),
    },

    "ETA_TEXT":Text_Surface["ETA_TEXT"].get_rect(midleft=CalcPosition(-240, -135)),

    "GAME_OVER":{
        "LINE 1":Text_Surface["GAME_OVER"]["LINE 1"].get_rect(midleft=CalcPosition(-250, 140)),
        "LINE 2":Text_Surface["GAME_OVER"]["LINE 2"].get_rect(midleft=CalcPosition(-250, 95)),
        "LINE 3":Text_Surface["GAME_OVER"]["LINE 3"].get_rect(midleft=CalcPosition(-250, 70)),
        "LINE 4":Text_Surface["GAME_OVER"]["LINE 4"].get_rect(midleft=CalcPosition(-250, 45))
    },

    "WIN_THE_GAME":{
        "LINE 1":Text_Surface["WIN_THE_GAME"]["LINE 1"].get_rect(midleft=CalcPosition(-250, 140)),
        "LINE 2":Text_Surface["WIN_THE_GAME"]["LINE 2"].get_rect(midleft=CalcPosition(-250, 95)),
        "LINE 3":Text_Surface["WIN_THE_GAME"]["LINE 3"].get_rect(midleft=CalcPosition(-250, 70))
    }
}

# Print Text Function
def Print_Text(Surface_group, Position_group):
    dict_keys = list(Surface_group.keys())
    for key in dict_keys:
        screen.blit(Surface_group[key], Position_group[key])

# Random Particles (except brown particles)
def particles_generator(num):

    particles = []

    for _ in range(num):

        rand = rd.random() ** 2

        if rd.randint(0, 1) == 1:

            x = 180 - (184 * rand)

        else:

            x = 320 + (182 * rand)

        particles.append({"x":round(x), "y":rd.randint(0, HEIGHT)})

    return particles

# Random Brown Particles
def brown_particles_generator(num):

    particles = []

    for _ in range(num):

        rand = rd.randint(1, 15)

        if rd.randint(0, 1) == 1:

            x = 183 - rand

        else:

            x = 317 + rand

        particles.append({"x":round(x), "y":rd.randint(0, HEIGHT)})

    return particles

# Gravel Particles
gravel = [
    [particles_generator(900), COLORS["GRAY_GRAVEL"]],
    [particles_generator(800), COLORS["RED_GRAVEL"]],
    [particles_generator(800), COLORS["ORANGE_GRAVEL"]],
    [brown_particles_generator(500), COLORS["BROWN_COLOR"]]
]

# Respawn Particles
def respawn(condiction_color):

    if condiction_color == gravel[3][1]:

        rand = rd.randint(1, 15)
        
        if rd.randint(0, 1) == 1:
        
            x = 183 - rand
        
        else:
        
            x = 317 + rand

    else:

        rand = rd.random() ** 2
        
        if rd.randint(0, 1) == 1:
        
            x = 180 - (184 * rand)
        
        else:
        
            x = 320 + (182 * rand)

    return x

# Initalize variables before Main loop
images = [pg.image.load(resource_path_checkandload("mini bus.png")), pg.image.load(resource_path_checkandload("Bus.png"))]
bus_rect = images[1].get_rect()
bus_x = WIDTH // 2 - (bus_rect.width // 2)
step = 0
backgroundmusic_isplaying = False
remaining_seconds = 28800
TIMER = pg.event.custom_type()
start_timer = False
drift = rd.randint(0, 1)
BUSCONTROL = pg.event.custom_type()
start_buscontrol = False
line_y = [0, 81, 162, 243]
running = True
current_state = STATES["BIOS"]
state_timer = pg.time.get_ticks()
fps = pg.time.Clock()

# Main loop
while running:

    # Stop updating current timer condiction
    if current_state != "IN GAME":
        current_timer = pg.time.get_ticks()

    # Even Process
    for event in pg.event.get():

        if event.type == pg.QUIT:   # Exit the pygame window
            running = False

        if event.type == pg.KEYDOWN:     # Key(s) is Pressing

            if event.key == pg.K_SPACE and current_state == "MESSAGE":       # Space to next message
                current_state = STATES["GM_LAYER_3"]

            if event.key == pg.K_RETURN and current_state == "KEY TO USE MSG":         # Start the game
                current_state = STATES["IN_GAME"]

        if event.type == TIMER:      # Timer
            remaining_seconds -= 1
            drift = rd.randint(0, 1)        # Random Drift Direction after 1 seconds
                
        if event.type == BUSCONTROL:         # Drift control by game

            if drift == 0:         # Auto drift to right
                bus_x += 1

            else:                # Auto drift to left
                bus_x -= 1
            
    keys = pg.key.get_pressed()           # Key(s) is pressing

    if current_state == "IN GAME":         # In Game

        if keys[pg.K_a] or keys[pg.K_LEFT]:      # Steer Left
            bus_x -= 5

        if keys[pg.K_d] or keys[pg.K_RIGHT]:      # Steer Right
            bus_x += 5

        if keys[pg.K_SPACE]:       # Honk

            CHANNELS["HONK"].play(SOUNDS["HONK"])

        if keys[pg.K_LSHIFT] and keys[pg.K_LALT] and remaining_seconds > 20:         # Mystery Key to win game soon

            remaining_seconds = 15
        
    if current_state == "LOADING BIOS":         # BIOS Display

        screen.fill(COLORS["BLACK_FILL"])
        screen.blit(Text_Surface["BIOS"]["LOGO"], Objects_Position["BIOS"]["LOGO"])

        if current_timer - state_timer >= 1000:        # Next line

            screen.blit(Text_Surface["BIOS"]["LOAD_TEXT"], Objects_Position["BIOS"]["LOAD_TEXT"])

        if current_timer - state_timer >= 5000:           # Next Display

            state_timer = current_timer
            current_state = STATES["GM_LAYER_1"]

    elif current_state == "BEEP SOUND":            # BEEP Display

        screen.fill(COLORS["BLUE_FILL"])
        screen.blit(Text_Surface["BEFORE_GAME_LAYER_1"]["LINE 1"], Objects_Position["BEFORE_GAME_LAYER_1"]["LINE 1"])
        screen.blit(Text_Surface["BEFORE_GAME_LAYER_1"]["LINE 2"], Objects_Position["BEFORE_GAME_LAYER_1"]["LINE 2"])

        if current_timer - state_timer >= 1000:         # Next Line

            screen.blit(Text_Surface["BEFORE_GAME_LAYER_1"]["LINE 3"], Objects_Position["BEFORE_GAME_LAYER_1"]["LINE 3"])

            if step == 0:       # *beep*

                CHANNELS["BEEP"].play(SOUNDS["BEEP"])
                step = 1
                
            if current_timer - state_timer >= 1500:         # Next Display
                current_state = STATES["GM_LAYER_2"]
                state_timer = current_timer
        
    elif current_state == "MESSAGE":            # First Message

        screen.fill(COLORS["BLACK_FILL"])
        Print_Text(Text_Surface["BEFORE_GAME_LAYER_2"], Objects_Position["BEFORE_GAME_LAYER_2"])

    elif current_state == "KEY TO USE MSG":         # Final Message

        screen.fill(COLORS["BLACK_FILL"])
        Print_Text(Text_Surface["BEFORE_GAME_LAYER_3"], Objects_Position["BEFORE_GAME_LAYER_3"])

    elif current_state == "IN GAME":            # In Game

        if not start_timer:             # Start timer ETA
            pg.time.set_timer(TIMER, 1000)
            start_timer = True

        if not start_buscontrol:        # Bus control by game
            pg.time.set_timer(BUSCONTROL, 50)
            start_buscontrol = True

        if remaining_seconds <= 0:      # Win the game
            pg.time.set_timer(TIMER, 0)
            pg.time.set_timer(BUSCONTROL, 0)
            CHANNELS["BACKGROUND"].stop()
            CHANNELS["BACKGROUND"].set_volume(0)
            CHANNELS["TOUCH"].stop()
            CHANNELS["TOUCH"].set_volume(0)
            step = 5
            current_state = STATES["WIN_THE_GAME"]

        screen.fill(COLORS["BROWN_COLOR"])
        pg.draw.rect(screen, COLORS["ROAD_COLOR"], (170, 0, 160, HEIGHT))       # Road

        for i in range(len(line_y)):        # Road line
            line_y[i] += 3
            if line_y[i] >= HEIGHT - 35:
                line_y[i] = -40
            pg.draw.rect(screen, COLORS["ROAD_LINE"], (250, line_y[i], 5, 40))

        for value in gravel:        # Draw particles

            positions = value[0]
            color = value[1]

            for pos in positions:

                pos["y"] += 3

                if pos["y"] > HEIGHT:

                    pos["y"] = -2

                    pos["x"] = respawn(color)
        
                pg.draw.rect(screen, color, (pos["x"], pos["y"], 2, 2))

        screen.blit(images[1], (bus_x, 110))

        bus_rect.x = bus_x

        if (bus_rect.left < 165 or bus_rect.right > 335) and step == 1:         # Warning by sound
            CHANNELS["BACKGROUND"].pause()
            CHANNELS["TOUCH"].unpause()
            step = 2

        if not (bus_rect.left < 170 or bus_rect.right > 330):           # Warning is off
            CHANNELS["BACKGROUND"].unpause()
            CHANNELS["TOUCH"].pause()
            step = 1

        if (bus_rect.left < 140 or bus_rect.right > 360):       # Game over
            pg.time.set_timer(TIMER, 0)
            pg.time.set_timer(BUSCONTROL, 0)
            CHANNELS["BACKGROUND"].stop()
            CHANNELS["BACKGROUND"].set_volume(0)
            CHANNELS["TOUCH"].stop()
            CHANNELS["TOUCH"].set_volume(0)
            CHANNELS["LOOSE"].play(SOUNDS["LOOSE"])
            step = 5
            current_state = STATES["GAME_OVER"]

        pg.draw.polygon(screen, COLORS["DARK_GRAY"], [(0, 320), (512, 320), (512, 0), (480, 0), (480, 273), (0, 273)])      # GUI
        pg.draw.polygon(screen, COLORS["RED_COLOR"], [(512, 320), (512, 310), (480, 310), (480, 320)])
        pg.draw.polygon(screen, COLORS["LIME_COLOR"], [(512, 0), (512, 10), (480, 10), (480, 0)])
        screen.blit(images[0], (490, round(288 - 288 * ((28800 - remaining_seconds) / 28800))))
        screen.blit(Text_Surface["ETA_TEXT"], Objects_Position["ETA_TEXT"])

        hours, min_sec = divmod(remaining_seconds, 3600)
        minutes, seconds = divmod(min_sec, 60)
        ETA_Suface = Fonts["ETA_Font"].render(f"{hours}:{minutes:02d}:{seconds:02d}", True, COLORS["LIME_COLOR"])           # This 5 lines is generating ETA clock
        ETA_Position = ETA_Suface.get_rect(midleft=CalcPosition(-180, -135))
        screen.blit(ETA_Suface, ETA_Position)

    elif current_state == "GAME OVER":          # Game Over Display
        screen.fill(COLORS["BLACK_FILL"])
        Print_Text(Text_Surface["GAME_OVER"], Objects_Position["GAME_OVER"])

    elif current_state == "WHILE 8 HOURS LAST, YOU DID REALLY AMAZING, YOU WILL FREE AFTER COMPLETED THIS GAME AND SAVED YOUR COMPUTER AND ALL DATA":           # Win the game
        screen.fill(COLORS["BLACK_FILL"])
        Print_Text(Text_Surface["WIN_THE_GAME"], Objects_Position["WIN_THE_GAME"])

    if current_state != "LOADING BIOS" and current_state != "BEEP SOUND" and not backgroundmusic_isplaying:             # Start the background music
        CHANNELS["BACKGROUND"].play(SOUNDS["BACKGROUND"], loops=-1)
        CHANNELS["TOUCH"].play(SOUNDS["TOUCH"], loops=-1)
        CHANNELS["TOUCH"].pause()
        backgroundmusic_isplaying = True   

    pg.display.flip()       # Update display

    fps.tick(15)            # FPS is 15

pg.quit()           # Quit

