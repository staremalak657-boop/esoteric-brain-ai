# 🧠 Offline Esoteric AI Classifier (Python to Brainfuck)

An experimental, 100% offline project that builds a local Sentiment Analysis AI in **Python** and compiles its core output logic into **Brainfuck**—one of the hardest esoteric programming languages in history.

---

## 🚀 Project Overview

This project proves the computer science theory of **Turing Completeness** by demonstrating that complex AI-driven communication can be represented through the 8 minimal symbols of Brainfuck. 

It consists of three core components working entirely local (no internet required):
1. **`offline_ai.py`**: A local NLP classifier analyzing user sentiments based on localized keyword arrays.
2. **`transpiler.py`**: A custom-built compiler that translates high-level text outputs into optimized Brainfuck cells (`+`, `-`, `.`).
3. **`run_bf.py`**: A simulated virtual memory interpreter that reads the esoteric code and executes it directly from cells.

---

## 🛠️ How It Works

### 1. Python AI Logic (`offline_ai.py`)
Processes input strings locally, calculates a sentiment score (Positive vs. Negative), and selects the corresponding AI response matrix without any API calls.

### 2. The Transpiler (`transpiler.py`)
Converts the generated output into ASCII sequences and computes the delta shift values to output raw brainfuck:
```text
AI Offline: Hello! -> ++++++++[>++++[>++>+++...