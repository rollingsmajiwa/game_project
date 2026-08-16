# NUMBER GUESSING GAME
## Project Brief
The Number Guessing Game is an interactive, command-line interface (CLI) Python application. It generates a dynamic random secret number between 1 and 100 and challenges players to guess it within a limited number of attempts, offering real-time feedback after each guess.

## Technical Rationale
A robust CLI application requires structured logic and exception-free execution. This project addresses two primary development goals:

**Interactive Control Flow:** Utilizing structured loops and dynamic condition checking to track user attempts and provide real-time game status updates.

**Randomized State Management:** Implementing Python's built-in random module ensures that every game session generates a unique winning target.

## Technologies Used
**Python :** Core programming language powering game logic, user input handling, and mathematical evaluations.

**random Module:** Python standard library used for random number generation (randint).

**Git/GitHub:** Version control and feature-based branch management.

## Game Features
**Dynamic Secret Number:** Generates a random integer between 1 and 100 for each new game session.

**Attempt Tracking:** Counts failed attempts and dynamically displays remaining tries after each guess.

**Game Over reveal:** Automatically reveals the correct answer once maximum attempts (e.g., 5) are exhausted.

**Instant Win Detection:** Exits the loop immediately upon entering the correct number using control flow statements (break).

## Git Workflow
Fork the Repository: Create your own copy of the project to work on.

Create a Feature Branch:

```Bash
git checkout -b feature/YourFeatureName
```
Commit Your Changes:

```Bash
git commit -m "feat: add attempt limiter 
logic"
```
Push to Branch:

```Bash
git push origin feature/YourFeatureName
Open a Pull Request (PR): Describe your changes clearly and link any related issues.
```

## Set Up Instructions
a. Clone this repository to your local machine:

```Bash
git clone https://github.com/rollingsmajiwa/number_guessing_game.git
cd number_guessing_game
```
b. Ensure Python 3 is installed on your system:

```Bash
python --version
```
c. Run the game in your terminal:

```Bash
python game_project.py
```
## Author
Rollings Majiwa

GitHub: [github.com/rollingsmajiwa](github.com/rollingsmajiwa)

Email: [rollingsmajiwa@gmail.com](rollingsmajiwa@gmail.com)

## Get Started
Interested in exploring or improving the code for this Number Guessing Game? Feel free to reach out via my profile or submit a pull request for collaboration!