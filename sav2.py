import pygame
import numpy as np

WIDTH = 800
HEIGHT = 600
BAR_WIDTH = 5
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SAV - Sorting Algorithm Visualizer")

def generate_arr(size):
    return [np.random.randint(10, HEIGHT) for _ in range(size)]
    
def draw_arr(arr):
    screen.fill((0, 0, 0))
    for i, val in enumerate(arr):
        pygame.draw.rect(screen, (255, 0, 0), (i * BAR_WIDTH, HEIGHT - val, BAR_WIDTH, val))
    pygame.display.flip()
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_arr(arr)
                pygame.time.delay(10)
                yield
             
def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            draw_arr(arr)
            pygame.time.delay(10)
            yield
            j -= 1
        arr[j+1] = key
        draw_arr(arr)
        pygame.time.delay(10)
        yield

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_arr(arr)
        pygame.time.delay(10)
        yield
  
def main():
    running = True
    clock = pygame.time.Clock()
    size = WIDTH // BAR_WIDTH
    arr = generate_arr(size)
    alg = "selection"
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    alg = "bubble"
                    print("Sorting algorithm set to BUBBLE SORT")
                elif event.key == pygame.K_i:
                    alg = "insertion"
                    print("Sorting algorithm set to INSERTION SORT")
                elif event.key == pygame.K_s:
                    alg = "selection"
                    print("Sorting algorithm set to SELECTION SORT")
                elif event.key == pygame.K_r:
                    arr = generate_arr(size)
                    print("Array has been REGENERATED")
                
        draw_arr(arr)
        
        if alg == "bubble":
            sorter = bubble_sort(arr)
        elif alg == "insertion":
            sorter = insertion_sort(arr)
        elif alg == "selection":
            sorter = selection_sort(arr)
        for _ in sorter:
            pass
            
        clock.tick(FPS)
    
    pygame.quit()
    
if __name__ == "__main__":
    main()