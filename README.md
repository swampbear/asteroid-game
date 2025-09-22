# 🚀 Eliastroid Destroyer

A small asteroid destroyer game developed while following a Boot.dev course.  
The project is written in **Python** using **Pygame**, and applies several **OOP concepts** for structuring the game logic.

---

## 🎮 Gameplay
- Control the ship and shoot down incoming asteroids.
- Uses Pygame’s core loop with update/draw mechanics.
- Includes recorded **sound effects** and simple **images** to enhance the experience.

---

## ⚙️ Concepts in Practice

| OOP Concept          | Example in Project                                             |
|----------------------|----------------------------------------------------------------|
| **Classes & Objects**| `Player`, `Asteroid`, `Shot`, and `AsteroidField` are modeled as classes. |
| **Encapsulation**    | Each class handles its own state and behavior (movement, drawing, collision). |
| **Inheritance**      | Common shape behavior abstracted in `CircleShape`, extended by other objects. |
| **Polymorphism**     | Different entities implement their own `update()` and `draw()` methods. |
| **Composition**      | Game objects are built with attributes like position, velocity, and sprites. |
| **Abstraction**      | Sprite groups manage complex update/draw cycles under the hood. |

---

### Installation & Run
Clone the repository and run the game with `uv`:

```bash
git clone https://github.com/swampbear/asteroid-game
cd asteroid-game

# Install dependencies
uv sync

# Run the game
uv run main.py
