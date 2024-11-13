# run.py

import pygame
from agent import Agent
from environment import Environment

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agent Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create Environment and Agent
environment = Environment(width, height)
agent = Agent(x=width//2, y=height//2, speed=5, environment=environment)

# Font for displaying agent position
font = pygame.font.Font(None, 36)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        agent.move('up')
    if keys[pygame.K_DOWN]:
        agent.move('down')
    if keys[pygame.K_LEFT]:
        agent.move('left')
    if keys[pygame.K_RIGHT]:
        agent.move('right')

    # Clear the screen
    screen.fill(WHITE)

    # Draw the agent
    pygame.draw.circle(screen, BLACK, (int(agent.x), int(agent.y)), 10)

    # Display agent's position
    pos_text = font.render(f"Position: ({int(agent.x)}, {int(agent.y)})", True, BLACK)
    screen.blit(pos_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(30)

pygame.quit()
pos_text = font.render(f"Position: ({int(agent.x)}, {int(agent.y)})", True, BLACK)
screen.blit(pos_text, (10, 10))