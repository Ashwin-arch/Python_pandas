import curses
import random

# Initialize the game window
def setup_window():
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)  # (height, width, start_y, start_x)
    win.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(True)  # Make the game non-blocking
    return win

# Main game function
def snake_game():
    win = setup_window()
    
    # Snake and food initial positions
    snake = [[10, 15], [10, 14], [10, 13]]
    food = [random.randint(1, 18), random.randint(1, 58)]
    win.addch(food[0], food[1], '🍎')

    key = curses.KEY_RIGHT  # Initial movement
    score = 0

    while True:
        win.addstr(0, 2, f"Score: {score} ")  # Display score
        win.timeout(100 - (len(snake) // 5 + len(snake) // 10) % 10)  # Increase speed over time
        
        new_key = win.getch()
        key = key if new_key == -1 else new_key

        # Determine new head position
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        elif key == curses.KEY_UP:
            new_head[0] -= 1
        elif key == curses.KEY_LEFT:
            new_head[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_head[1] += 1

        # Check collision with walls or itself
        if new_head in snake or new_head[0] in [0, 19] or new_head[1] in [0, 59]:
            break

        snake.insert(0, new_head)  # Move snake

        # Check if food is eaten
        if new_head == food:
            score += 1
            food = [random.randint(1, 18), random.randint(1, 58)]
            win.addch(food[0], food[1], '🍎')
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        # Update snake position
        win.addch(snake[0][0], snake[0][1], '█')

    curses.endwin()
    print(f"Game Over! Your final score: {score}")

# Run the game
if __name__ == "__main__":
    snake_game()
