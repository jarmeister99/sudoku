import pygame


def get_selected_number(event):
    selected_number = None
    if event.key == pygame.K_1:
        selected_number = '1'
    elif event.key == pygame.K_2:
        selected_number = '2'
    elif event.key == pygame.K_3:
        selected_number = '3'
    elif event.key == pygame.K_4:
        selected_number = '4'
    elif event.key == pygame.K_5:
        selected_number = '5'
    elif event.key == pygame.K_6:
        selected_number = '6'
    elif event.key == pygame.K_7:
        selected_number = '7'
    elif event.key == pygame.K_8:
        selected_number = '8'
    elif event.key == pygame.K_9:
        selected_number = '9'
    elif event.key == pygame.K_ESCAPE:
        selected_number = None
    return selected_number
