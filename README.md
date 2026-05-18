# Lottery Game

A small object-oriented lottery game written in Python.

This project was created as a progression-oriented software engineering exercise focused on:

* OOP design,
* state management,
* game logic separation,
* input validation,
* and maintainable architecture.

---

# Features

## Current Features

* Multiple players
* Persistent balances during runtime
* Betting system
* Random lottery system
* Input validation
* Structured game engine
* Centralized messages system
* Player switching
* Dictionary-based player storage
* Separation between UI and game logic

---

# Project Structure

```text
Lottery_game_folder/
│
├── lottery_game.py
├── README.md
├── messages.py
```


---

# Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Dictionaries
* Structured game state management

---

# Example Gameplay

```text
Welcome Jean! Starting balance: 100$

Press Enter to play, type 'q' to quit...

How much do you want to bet? 20

Choose a color: rouge
Choose a number: 12

→ Result: rouge / 12

🎉 Jackpot! You won 80$
```

---

# How to Run

## Requirements

* Python 3 installed

Check installation:

```bash
python --version
```

---

## Run the Project

```bash
python main.py
```

---

# Current Architecture

The project currently contains:

| Component       | Responsibility                        |
| --------------- | ------------------------------------- |
| `Player`        | Stores player data                    |
| `PlayerManager` | Manages player creation and retrieval |
| `GameEngine`    | Handles lottery logic and rules       |
| `UI`            | Handles interaction and display       |

---

# Engineering Goals

The project aims to progressively improve:

* maintainability,
* modularity,
* architecture quality,
* and software engineering rigor.

The objective is not only to create a working game, but also to practice:

* cleaner abstractions,
* better separation of concerns,
* and scalable design patterns.


---

# Roadmap

## Milestone 1 — Core Terminal Version ✅

* Basic gameplay
* OOP architecture
* Player management
* Validation system

---

## Milestone 2 — Architecture Improvements ✅

* Constants system
* Centralized messages
* Dictionary-based player storage
* Better responsibility separation

---

## Milestone 3 — Graphical User Interface (GUI) 🚧

Planned features:

* Tkinter interface
* Interactive buttons
* Real-time balance updates
* Improved user experience
* Better visual feedback

