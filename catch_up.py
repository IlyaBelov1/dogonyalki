from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
backgrournd = transform.scale(image.load('d7ede7345fff006856e5e0e633df4384.png'), (800, 500))
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100)) 
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
sprite3 = transform.scale(image.load('Freddy_Fazbear_Infobox_Original (1).png'), (120, 130))
game = True
x1 = 200
y1 = 350
x2 = 400
y2 = 250
x3 = 500
y3 = 250
speed = 2
clock = time.Clock()
FPS = 60
clock.tick(FPS)
while game:
    window.blit(backgrournd, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    window.blit(sprite3, (x3, y3))
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_presed = key.get_pressed()
    if keys_presed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_presed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_presed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_presed[K_DOWN] and y1 < 395:
        y1 += speed
    if keys_presed[K_a] and x2 > 5:
        x2 -= speed
    if keys_presed[K_d] and x2 < 595:
        x2 += speed
    if keys_presed[K_w] and y2 > 5:
        y2 -= speed
    if keys_presed[K_s] and y2 < 395:
        y2 += speed
    if keys_presed[K_j] and x3 > 5:
        x3 -= speed
    if keys_presed[K_l] and x3 < 595:
        x3 += speed
    if keys_presed[K_i] and y3 > 5:
        y3 -= speed
    if keys_presed[K_k] and y3 < 395:
        y3 += speed


    display.update()

           



