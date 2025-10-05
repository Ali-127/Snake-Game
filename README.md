# 🐍 Snake Game

A classic Snake game implementation built with Python and Pygame, demonstrating core object-oriented programming principles and game development fundamentals.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.5+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 About

This project is a recreation of the timeless Snake game, where players control a growing snake that must avoid colliding with itself or the game boundaries. Built as a demonstration of object-oriented programming concepts, the game features clean code architecture with separate classes for game logic, snake behavior, and food mechanics.

## ✨ Features

- **Classic Gameplay**: Navigate the snake to eat food and grow longer
- **Score Tracking**: Real-time score display based on food consumed
- **Collision Detection**: Game ends when snake hits walls or itself
- **Smooth Controls**: Responsive arrow key input for directional movement
- **OOP Architecture**: Clean separation of concerns using classes
- **Game Over Screen**: Display final score and option to restart

## 🎮 How to Play

- **Arrow Keys**: Control the snake's direction
  - ↑ Move Up
  - ↓ Move Down
  - ← Move Left
  - → Move Right
- **Objective**: Eat the food (red squares) to grow longer and increase your score
- **Rules**: 
  - Don't hit the walls
  - Don't collide with your own body
  - Each food item increases your score by 10 points

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Pygame 2.5+**: Game development library for graphics and input handling

## 📋 Prerequisites

Before running the game, ensure you have:

- Python 3.8 or higher installed
- pip (Python package installer)

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ali-127/Snake-Game.git
cd Snake-Game
```

### 2. Install Dependencies

```bash
pip install pygame
```

Or using requirements.txt:

```bash
pip install -r requirements.txt
```

### 3. Run the Game

```bash
python main.py
```

## 📁 Project Structure

```
Snake-Game/
├── main.py          # Main file for running game
├── snake.py          # Snake implementation
├── game.py          # Game logic file with OOP implementation
├── food.py          # Food Implementation
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
└── screenshots/          # Game screenshots (optional)
```

## 🎯 Object-Oriented Design

The game is structured using OOP principles with the following key components:

### Classes:
- **Snake Class**: Manages snake movement, growth, and collision detection
- **Food Class**: Handles food generation and positioning
- **Game Class**: Controls game loop, scoring, and game state

### Key Concepts Demonstrated:
- **Encapsulation**: Each class manages its own data and behavior
- **Separation of Concerns**: Game logic separated from rendering
- **State Management**: Clean handling of game states (playing, game over)

## 🎨 Game Mechanics

### Snake Movement
- Snake moves continuously in the current direction
- Movement is grid-based for precise collision detection
- Direction changes are queued to prevent invalid moves

### Food System
- Food appears randomly on the grid
- Eating food increases snake length by one segment
- New food spawns immediately after consumption

### Collision Detection
- Wall collision: Snake hits game boundaries
- Self-collision: Snake head intersects with body
- Food collision: Snake head reaches food position

## 🔮 Future Enhancements

Potential features for future versions:

- [ ] Difficulty levels (varying snake speed)
- [ ] High score persistence using file I/O or database
- [ ] Sound effects and background music
- [ ] Power-ups (speed boost, invincibility, etc.)
- [ ] Multiple game modes (classic, endless, timed)
- [ ] Obstacle generation for increased difficulty
- [ ] Leaderboard system
- [ ] Menu system with settings

## 🧪 Learning Outcomes

This project demonstrates proficiency in:

- Python programming fundamentals
- Object-oriented programming (OOP) design patterns
- Game loop implementation
- Event handling and user input processing
- Collision detection algorithms
- 2D graphics rendering with Pygame
- Code organization and project structure

## 🐛 Known Issues

- None currently. Please report any bugs in the [Issues](https://github.com/Ali-127/Snake-Game/issues) section.

## 🤝 Contributing

This is a portfolio project, but suggestions and feedback are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

Ali - [GitHub Profile](https://github.com/Ali-127)

Project Link: [https://github.com/Ali-127/Snake-Game](https://github.com/Ali-127/Snake-Game)

## 🙏 Acknowledgments

- Inspired by the classic Nokia Snake game
- Built with Pygame community resources
- Created as a portfolio project to demonstrate OOP principles in game development

---

⭐ If you found this project interesting, please consider giving it a star!

**Note**: This project was developed as a learning exercise to practice object-oriented programming concepts and gain experience with the Pygame library. It showcases clean code architecture and fundamental game development principles.
