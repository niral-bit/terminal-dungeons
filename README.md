# Terminal Dungeons 🗡️🐍

An interactive, retro text-based Python RPG built for investigating open-source software development practices, issue tracking, and Pull Request (PR) workflows as part of the **Symbiosis Institute of Technology (CA-3)** curriculum.

---

## 📌 Project Overview
**Terminal Dungeons** is a lightweight command-line game where players fight turn-based monsters (like the infamous `Segmentation Fault`), manage health points, and navigate combat scenarios. 

This repository serves as a hands-on case study to explore:
* **Repository Architecture:** Clean, modular Python project structure.
* **Issue Tracking & Bug Investigation:** Identifying, documenting, and reproducing state-handling edge cases (e.g., negative HP on game over).
* **Open Source Contribution Workflows:** Using feature branching, pull requests, code reviews, and issue linking (`Closes #1`).

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.8+** installed on your system.
* **Git** installed on your system.

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone https://github.com/niral-bit/terminal-dungeons.git
   cd terminal-dungeons
   ```

2. **Run the game:**
   ```bash
   python game.py
   ```

---

## 🎮 How to Play
* Select numerical actions during combat:
  * `1`: **Attack** the monster to deal randomized physical damage.
  * `2`: **Heal** to restore player HP.
* Defeat the monster before your health drops to `0 HP`!

---

## 🛠️ Project Structure
```text
.
├── game.py             # Core game engine loop and combat arithmetic
└── README.md           # Project documentation
```
