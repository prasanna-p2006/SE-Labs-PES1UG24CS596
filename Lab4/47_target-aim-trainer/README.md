# Target Aim Trainer

This project is a terminal-based target aim trainer using **Pygame**. It introduces students to interactive game design using object-oriented principles and real-time graphical rendering.

---

## What’s Provided

A partially working version of an aim trainer with:

- A single target that spawns at a random position and visually shrinks the longer it's on screen
- Click-to-hit scoring, with a timed-out target counting as a miss
- A countdown timer, score, and accuracy display

You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**

---

## Getting Started

### Setup

1. Clone the repo or download the project folder.
2. Make sure you have Python 3.10+ installed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python main.py
```

---


## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Refine Collision Detection

> Late clicks well outside the small, shrunken target circle can still register as a hit. Investigate and enhance click accuracy so the clickable area always matches what's actually drawn on screen.

### Task 2: Implement Game Over Condition

> Add a screen that displays the final score and accuracy once the round timer reaches zero, then gracefully waits for input instead of just printing to the console.



### Task 3: Add Replay Option

> After Game Over, allow the user to play again by choosing a difficulty (Easy, Medium, or Hard target lifespan/size), or exit.



### Task 4: Add Sound Feedback

> Add basic sound effects for a successful hit, a miss (including a timed-out target), and the round ending.



---

## Expected Behavior

- A single target appears at a random position and shrinks the longer it stays on screen
- Clicking the target scores a hit and immediately spawns a new one elsewhere
- Clicking anywhere else counts as a miss; letting a target's timer run out also counts as a miss
- A countdown timer, score, and live accuracy percentage are visible at all times
- The round ends when the timer reaches zero

---

## Folder Structure

```
target-aim-trainer-main/
├── main.py
├── requirements.txt
├── game/
│   ├── game_engine.py
│   └── target.py
└── README.md
```

---

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history