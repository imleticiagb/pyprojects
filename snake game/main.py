import pygame
import random

pygame.init()
pygame.display.set_caption("ssssnake game")
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

tam_quadrado = 20
vel_jogo = 15

def comida():
    comida_x = round(random.randrange(0, largura - tam_quadrado) / float(tam_quadrado)) * float(tam_quadrado)
    comida_y = round(random.randrange(0, altura - tam_quadrado) / float(tam_quadrado)) * float(tam_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho, tamanho])
    
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])
    
def escrever_pontos(pontuacao):
    fonte = pygame.font.Font("Tiny5-Regular.ttf", 22)
    texto = fonte.render(f"{pontuacao} pontos", True, verde)
    tela.blit(texto, [1,1])

def sel_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tam_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tam_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tam_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tam_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def msg(mensagem, cor):
    fonte = pygame.font.Font("Tiny5-Regular.ttf", 50)
    texto = fonte.render(mensagem, True, cor)
    rect = texto.get_rect(center=(largura / 2, altura / 2))
    tela.blit(texto, rect)
    pygame.display.update()

def jogo():
    fim = False
    sair = False
   
    x = largura / 2
    y = altura / 2
   
    velocidade_x = 0
    velocidade_y = 0
   
    tam_cobra = 1
    pixels = [[x, y]] 
   
    comida_x, comida_y = comida()
   
    while not fim:
        tela.fill(preto)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim = True 
                sair = True
                msg("até a próxima!")
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = sel_velocidade(evento.key)
                
    
        desenhar_comida(tam_quadrado, comida_x, comida_y)
        
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim = True
        
        x += velocidade_x
        y += velocidade_y
        
        pixels.append([x, y])
        if len(pixels) > tam_cobra:
            del pixels[0]
            
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim = True
                     
        desenhar_cobra(tam_quadrado, pixels)
        escrever_pontos(tam_cobra-1)
        
        pygame.display.update()
              
        if x == comida_x and y == comida_y:
            tam_cobra += 1
            comida_x, comida_y = comida() 
        
        if fim and not sair:
            msg("GAME OVER", vermelho)
            while fim and not sair:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        sair = True
                        fim = False
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_SPACE:
                            fim = False
                            jogo()
                            
        relogio.tick(vel_jogo)
        
        if sair:
            pygame.quit()
            quit()

jogo()
