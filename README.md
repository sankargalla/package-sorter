# 📦 Package Sorter

This project provides a simple function to **automatically sort packages** into appropriate dispatch stacks based on their **dimensions** and **mass**.

## 🛠 Functionality

The robotic arm uses the `sort()` function to determine where a package should go based on the following rules:

### 📏 Classification Rules

- A package is **bulky** if:
  - Its **volume** (Width × Height × Length) is **≥ 1,000,000 cm³**, **or**
  - Any of its **dimensions** (Width, Height, Length) is **≥ 150 cm**

- A package is **heavy** if:
  - Its **mass** is **≥ 20 kg**

### 🗂 Dispatch Stacks

- **STANDARD** – Packages that are **not bulky** and **not heavy**
- **SPECIAL** – Packages that are **bulky or heavy**, but **not both**
- **REJECTED** – Packages that are **both bulky and heavy**

---

## ⚙️ Usage

```python
from package_sorter import sort

# Example usage:
result = sort(width=100, height=120, length=80, mass=15)
print(result)  # Output: "STANDARD"
