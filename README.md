# 🗡️ Terminal Dungeons

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Course](https://img.shields.io/badge/Symbiosis_Institute_of_Technology-CA--3_Case_Study-orange.svg)

An interactive, retro CLI text-based RPG built in Python where players explore bug-infested dungeons, battle iconic software glitches, earn gold, purchase shop upgrades, and manage items—all while demonstrating real-world open-source software engineering practices, issue tracking, and Pull Request (PR) contribution workflows.

---

## 📌 Problem Statement

Inadequate state boundary validation in CLI applications causes runtime errors like negative health metrics upon player defeat. This project resolves these state-handling vulnerabilities using open-source issue tracking, bug reproduction, and Pull Request code reviews.

---

## ✨ Features

- **🎮 Turn-Based Combat Engine:** Battle against enemies using commands for `Attack`, `Heal`, `Inventory`, and `Shop`.
- **👾 Dynamic Bug Monsters:** Battle classic software bugs with unique stats:
  - `Null Pointer Exception`
  - `Memory Leak`
  - `Segmentation Fault`
- **🛒 Dev Shop & Economy:** Defeat monsters to earn gold and purchase upgrades:
  - **Espresso Shot (+25 HP)** – Restores health during or outside combat.
  - **Mechanical Keyboard (+5 Atk)** – Permanently boosts base attack power.
- **🎒 Inventory Management:** View collected developer equipment and consumables.
- **🎨 Retro Terminal Visuals:** Styled with ANSI escape colors, typewriter text effects, and custom ASCII banners.
- **🔍 Built-in Case Study Bug:** Engineered with a state-boundary edge case (negative player HP on game over) designed specifically for open-source issue logging, reproduction, and PR patching.

---

## 🛠️ Project Architecture & Structure

```text
terminal-dungeons/
│
├── game.py              # Main RPG loop, shop logic, combat engine, and ASCII rendering
└── README.md            # Comprehensive project documentation
```

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

2. **Run the application:**
   ```bash
   python game.py
   ```

---