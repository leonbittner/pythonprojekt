"""
Marius Meineke

Diese aufzurufende Funktion des ChatBots beinhaltet das Spiel Pong, welches aus vielen alten Spielhallen bekannt ist. Es wurde 1972 von Atari als Arcade-Spiel produziert und zum ersten weltweit beliebten Videospiel.
Es entspricht in etwa einem Solo-Pong, bei dem man mit dem Schläger den Ball so lenken soll, dass der Ball nicht am Schläger vorbei geht. 
Wenn der Schläger den Ball verliert, bekommt man einen neuen Ball, verliert man aber insgesamt drei Bälle, so gilt das Spiel als Verloren.
Die Leben werden dabei oben Links in der Ausgabe angezeigt. 
Außerdem kann der Spieler während des Spiel seine Treffer mit dem Schläger sehen. Diese Treffer werden auf der Score-Anzeige unten links ausgegeben. 
Der Score bezieht sich auf die erzielten Treffer während der ganzen drei Leben.

"""
import pygame, random, sys

#Festlegung der Fenstergrößen x=Beite, y= Höhe
x = 500
y = 500

#Spielerleben & Score
spielerLeben = 3
spielerScore = 0
spielerAnzeige = "Score: "

#Farben
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)
red = (255,40,0)

#Festlegung der Schlägergrößen
schlaegerBreite = 100
schlaegerHoehe= 15

#Randomisierte Startposition des Schlägers
schlaeger_x = 200
schlaeger_y = 450

#Variablen des Balls
#Startposition
ball_x = int(x/2)
ball_y = int(y/2)

#Radius des Balls
ball_rad = 15

#Bewegungen Schläger / Ball
schlaeger_bew = 0
ball_x_bew = 1
ball_y_bew = -2

#Initialisierung pygame
pygame.init()
pygame.display.set_caption("Pong Game")

#Erstellung des Spielfeldscreens über pygame und einer Tupelliste für die Größe
spielfeld = pygame.display.set_mode([x,y])
back_image = pygame.image.load(r"D:\UNI\Bild_arcade.jpg")
back_top = spielfeld.get_height() - back_image.get_height()
back_left = spielfeld.get_width()/2 - back_image.get_width()/2
spielfeld.blit(back_image, (back_left,back_top))

#Zeichnung des Spielballs und des Schlägers
pygame.draw.circle(spielfeld, yellow, (ball_x, ball_y), ball_rad, 0)
pygame.draw.rect(spielfeld, red, (schlaeger_x, schlaeger_y, schlaegerBreite, schlaegerHoehe),0)

#Anzeigen der beiden Zeichnungen
pygame.display.flip()
    
"""Methoden"""
#Ausgabe Leben
def lebensAnzeige():
    schriftArt = pygame.font.SysFont("arial", 40)
    yPos = 5
    xPos = 10
    leben = schriftArt.render(str(spielerLeben), 1, white)

    spielfeld.blit(leben, (xPos,yPos))

#Ausgabe Score
def scoreAnzeige():
    schriftArt = pygame.font.SysFont("arial", 25)
    ySPos = 460
    xSPos = 465
    yAPos = 460
    xApos = 405
    score = schriftArt.render(str(spielerScore), 1, white)
    anzeige = schriftArt.render(spielerAnzeige, 1, white)

    spielfeld.blit(score, (xSPos,ySPos))
    spielfeld.blit(anzeige, (xApos,yAPos))

#Reseten des Spiels
def reset():
    global ball_y_bew, ball_x_bew, spielerLeben, ball_x, ball_y, schlaeger_x, schlaeger_y, schlaeger_bew
        
    ball_x = int(x/2)
    ball_y = int(y/2)

    schlaeger_bew = 0

    #Abfrage damit der Ball sich bewegt
    ball_x_bew = random.randint(-2,2)
    if ball_x_bew == 0:
        ball_x_bew = 2
    ball_y_bew = -2    
        
    pygame.draw.circle(spielfeld, yellow, (ball_x, ball_y), ball_rad, 0)
    pygame.draw.rect(spielfeld, red, (schlaeger_x, schlaeger_y, schlaegerBreite, schlaegerHoehe),0)
    pygame.display.update()
    pygame.time.wait(1000)

#Eingrenzung der Bewegung des Schlägers nach Rechts und Links
def schlaegerBlock():
    global schlaeger_bew
    if schlaeger_x <= 0 or schlaeger_x >= x-schlaegerBreite:
        schlaeger_bew = 0

#Schläger Bewegungen
def schlaegerAktionen():
    global schlaeger_x
    schlaeger_x += schlaeger_bew

#Bewegungen des Balls
def bewBall():
    global ball_x, ball_y
    ball_x += ball_x_bew
    ball_y += ball_y_bew

#Aufprall Bewegungen des Balls
def hitBall():
    global ball_x_bew, ball_y_bew, spielerLeben, spielerScore, x, ball_rad

    #Bewegungsänderung Hit Oben
    if ball_y-ball_rad <= 0:
        ball_y_bew *= -1

    #Bewegungsänderung Hit Links
    if ball_x-ball_rad <= 0:
        ball_x_bew *= -1

    #Bewegungsänderung Hit Rechts
    if ball_x+ball_rad >= x:
        ball_x_bew *= -1

    #Bewegungsänderung Hit Schläger
    if ball_y >= 435 and ball_y <= 450:
        if ball_x >= schlaeger_x-15 and ball_x <= schlaeger_x+schlaegerBreite+15:
            spielerScore += 1
            ball_y_bew *= -1
        else:
            spielerLeben -= 1
            reset()

#Spielablauf
def gameLogik():
    spielfeld.blit(back_image, (back_left,back_top))
    lebensAnzeige()
    scoreAnzeige()
    schlaegerAktionen()
    schlaegerBlock()
    pygame.draw.rect(spielfeld, red, (schlaeger_x, schlaeger_y, schlaegerBreite, schlaegerHoehe),0)
    bewBall()
    hitBall()
    pygame.draw.circle(spielfeld, yellow, (ball_x, ball_y), ball_rad, 0)
    pygame.display.flip()
    pygame.time.wait(5)

#SpielAblauf
def spielAblauf():
    global schlaeger_bew
    while spielerLeben > 0:
        #Standard Evenrhandler
        for event in pygame.event.get():
            #Beenden des Skriptes über Kreuz rechts oben
            if event.type == pygame.QUIT:
                sys.exit()
            #Tastenüberprüfung    
            if event.type == pygame.KEYDOWN:
                #Schläger nach links
                if event.key == pygame.K_LEFT:
                    schlaeger_bew = -2
                #Schläger nach rechts
                if event.key == pygame.K_RIGHT:
                    schlaeger_bew = 2
        gameLogik()

    print("Du hast verloren!")   


#Main
if __name__ == '__main__':
    spielAblauf()


