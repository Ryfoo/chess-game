import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Colors
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)

# Board and piece size
TILE_SIZE = WIDTH // 8

# Load piece images
def load_images():
    pieces = ["pawn", "rook", "knight", "bishop", "queen", "king"]
    colors = ["w", "b"]  # White, Black
    images = {}
    for color in colors:
        for piece in pieces:
            img = pygame.image.load(f"assets/{color}_{piece}.png")
            img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))  # Resize
            images[f"{color}_{piece}"] = img
    return images

piece_images = load_images()

# Initial chessboard setup
chessboard = [
    ["b_rook", "b_knight", "b_bishop", "b_queen", "b_king", "b_bishop", "b_knight", "b_rook"],
    ["b_pawn"] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    ["w_pawn"] * 8,
    ["w_rook", "w_knight", "w_bishop", "w_queen", "w_king", "w_bishop", "w_knight", "w_rook"]
]

# Variables for dragging
selected_piece = None
dragging = False
start_pos = None

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col, row = x // TILE_SIZE, y // TILE_SIZE

            # Check if there's a piece at the clicked position
            if chessboard[row][col] != "":
                selected_piece = chessboard[row][col]
                chessboard[row][col] = ""  # Remove from board temporarily
                start_pos = (row, col)
                dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                x, y = event.pos
                col, row = x // TILE_SIZE, y // TILE_SIZE

                # Place the piece in the new position
                chessboard[row][col] = selected_piece
                selected_piece = None
                dragging = False

        elif event.type == pygame.MOUSEMOTION and dragging:
            x, y = event.pos

    # Draw chessboard
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

            # Draw pieces if there's one at (row, col)
            piece = chessboard[row][col]
            if piece and not (dragging and piece == selected_piece):  # Avoid redrawing dragged piece
                screen.blit(piece_images[piece], (col * TILE_SIZE, row * TILE_SIZE))

    # Draw the dragged piece following the mouse
    if dragging and selected_piece:
        screen.blit(piece_images[selected_piece], (x - TILE_SIZE // 2, y - TILE_SIZE // 2))

    pygame.display.flip()

pygame.quit()
sys.exit()