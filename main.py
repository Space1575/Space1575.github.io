"""ALL RIGHTS ARE PRESERVED BY AUTHOR RIGHTS
NO COPING!!!
ALL RIGHTS ARE BELONG TO BATYR NURMANOV"""
import time,pygame,random
from sys import exit
#importing modules
W, H = 500, 500
pygame.display.init()
pygame.font.init()
LOG = pygame.image.load('New Piskel.png')
screen = pygame.display.set_mode((W, H))
LOGO = pygame.transform.scale(LOG,(500,500))
ICON = pygame.image.load('warthunder.png')
f = pygame.font.SysFont('Botsmatic',100)
font = pygame.font.SysFont('Botsmatic',110)
FONT = pygame.font.SysFont("Helvetica",40)
highscore = 0
def setup():
  global W, H, Y, X,UP, FPS, pipe_x, pipe_y, gap, width, height, scroll, score, ground, player, gravity, screen, Stop, vel_down, clock, pipesDOWN, pipesUP
  W, H = 500, 500
  Y = 100
  pipe_y, pipe_x = 100, W
  FPS = 60
  UP = -10
  X = 0
  gap = 80
  width = 40
  height = H
  scroll = 3
  ground = pygame.Rect(0, H - 20, W, 20)
  gravity = 1
  score = 0
  vel_down = 0
  Stop = False
  player = pygame.Rect(50, Y, 20, 20)
  pygame.display.set_icon(ICON)  
  #Assets,анау-мнау вообщем
  clock = pygame.time.Clock()
  pygame.display.set_caption('Cube-Nube')
  pipesUP = []
  pipesDOWN = []  
def time_between_pipes():
  global score, wait
  if score >= 0 and score < 5:
    wait = 2000
  if score >= 5 and score < 10:
    wait = 1700
  if score >= 10 and score < 25:
    wait = 1400
  if score >= 25 and score < 35:
    wait = 1100
  if score >= 35 and score < 40:
    wait = 900
  return wait
def reset():
  main()
def game_over():
  screen.fill((0, 200, 245))
  screen.blit(LOGO,(0,0))
  Restart_shadow = FONT.render('PRESS SPACE TO RESTART', True, ('WHITE'))
  screen.blit(Restart_shadow, (28, 123))
  Restart = FONT.render('PRESS SPACE TO RESTART', True, ('BLACK'))
  screen.blit(Restart, (25, 120))
  Game_OVER = font.render(f'GAME OVER', True, (0, 0, 0))
  screen.blit(Game_OVER, (20, 6))
  Game = font.render(f'GAME OVER', True, (200, 100, 0))
  screen.blit(Game, (15, 0))
  Game_shadow = FONT.render(f'Highscore:  {highscore}', True, (0, 0, 0))
  screen.blit(Game_shadow, (3,224))
  Highscore_text = FONT.render(f'Highscore:  {highscore}', True, (255, 255, 255))
  screen.blit(Highscore_text, (0, 220))
  pygame.display.update()
  while  True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                reset()
                break
def creating_Upper_pipes():
  global pipesUP, pipeUP
  pipeUP = pygame.Rect(pipe_x, pipe_y - height, width, height)
  pipesUP.append(pipeUP)
def creating_Lower_pipes():
  global pipesDOWN, pipeDOWN
  pipeDOWN = pygame.Rect(pipe_x, pipe_y + gap, width, height)
  pipesDOWN.append(pipeDOWN)
def JumpUP():
  global vel_down, UP
  vel_down = UP
def main():
  global vel_down, Y, gravity, pipe_y, scroll, Stop, scrollbg, score, highscore
  starting_time = time.time()
  now = 0
  wait = 2000
  n = 0
  setup()
  while True:
    now = time.time() - starting_time
    screen.fill((0, 200, 245))
    n += clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if not Y < 0:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    if Stop == False:
                        JumpUP()
                    if event.key == pygame.K_RIGHT:
                      X += 2

    vel_down += gravity
    Y += vel_down
    if n > wait:
        creating_Lower_pipes()
        creating_Upper_pipes()
        n = 0
        pipe_y = random.randint(0, W - (gap + 10))

    for pipeDOWN in pipesDOWN[:]:
        pygame.draw.rect(screen, ('DARK GREEN'),pygame.Rect(pipeDOWN.x - 10, pipeDOWN.y, width + 20, 20))
        pygame.draw.rect(screen, ('DARK GREEN'), pipeDOWN)
        pipeDOWN.x -= scroll
        if pipeDOWN.x < 0 - width:
            pipesDOWN.remove(pipeDOWN)
        if pipeDOWN.colliderect(player):
            scroll = 0
    for pipeUP in pipesUP[:]:
        pygame.draw.rect(screen, ('DARK GREEN'),pygame.Rect(pipeUP.x - 10, pipeUP.y + height - 20, width + 20, 20))
        pygame.draw.rect(screen, ('DARK GREEN'), pipeUP)
        check = pygame.Rect(pipeUP.x, pipeUP.y + height, width, gap)
        pipeUP.x -= scroll
        if pipeUP.x < 0 - width:
            pipesUP.remove(pipeUP)
        if pipeUP.colliderect(player):
            Stop = True
            scroll = 0
        if check.colliderect(player) and player.x == check.x:
            score += 1
    text = f.render(f'{score}', False, ('WHITE'))
    text_shadow = font.render(f'{score}', False, ('BLACK'))
    screen.blit(text_shadow, (W // 2 - 100, 2))
    screen.blit(text, (W // 2 - 100, 10))
    player = pygame.Rect(50, Y, 20, 20)
    pygame.draw.rect(screen, (253,239,105), player)
    pygame.draw.rect(screen,(0,0,0),(pygame.Rect(player.x+12,player.y+2,4,4)))
    pygame.draw.rect(screen, (0, 200, 50), ground)
    if scroll == 0:
      Stop = True
    if player.colliderect(ground):
        screen.fill((0, 200, 245))
        gravity = 0
        vel_down = 0
        player.y = ground.y - 10
        pygame.draw.rect(screen,(0,0,0),(pygame.Rect(player.x+12,player.y+2,4,4)))
        screen.blit(text_shadow, (W // 2 - 100, 2))
        screen.blit(text, (W // 2 - 100, 10))
        for pipeUP in pipesUP:
            pygame.draw.rect(screen,("DARK GREEN"),pipeUP)
            pygame.draw.rect(screen, ('DARK GREEN'),pygame.Rect(pipeUP.x - 10, pipeUP.y + height - 20, width + 20, 20))
        for pipeDOWN in pipesDOWN:
            pygame.draw.rect(screen,("DARK GREEN"),pipeDOWN)
            pygame.draw.rect(screen, ('DARK GREEN'),pygame.Rect(pipeDOWN.x - 10, pipeDOWN.y, width + 20, 20))
        pygame.draw.rect(screen, (0, 200, 50), ground)
        pygame.draw.rect(screen, (253,239,105), player)
        pygame.draw.rect(screen,(200,0,0),(pygame.Rect(player.x+12,player.y+2,4,4)))
        screen.blit(text_shadow, (W // 2 - 100, 2))
        screen.blit(text, (W // 2 - 100, 10))
        pygame.display.update()
        pygame.time.delay(1200)
        if highscore < score:
            highscore = score
        game_over()
        break
    wait = time_between_pipes()
    pygame.display.flip()
    clock.tick(FPS)
if __name__ == "__main__":
    main()     
