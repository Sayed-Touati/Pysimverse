# 🚁 Pysimverse Drone Simulation Course

This project is a hands-on learning course for understanding **drone simulation using Python** with the `pysimverse` package.

It is designed for beginners who want to learn how drones work in a **safe, simulated environment**, starting from basic commands and gradually progressing to more advanced control techniques.

---

## 📌 Project Objectives

By following this project, you will learn how to:

* Connect to a simulated drone
* Execute basic flight commands
* Perform takeoff and landing safely
* Control movement (forward, backward, up, down)
* Rotate and adjust drone orientation
* Understand timing and delays in drone behavior
* Build small scripts for experimentation
* Prepare for real-world drone programming concepts

---

## 🧰 Requirements

Make sure you have the following installed:

* **Python 3.13+**
* `pysimverse`
* Standard Python library (`time` module is used)
* (Recommended) Virtual environment (`venv`)

---

## ⚙️ Setup Guide

Follow these steps to set up the project on your machine:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pysimverse-course.git
cd pysimverse-course
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

---

### 3. Activate the virtual environment

#### 🪟 Windows

```bash
venv\Scripts\activate
```

#### 🍎 macOS / 🐧 Linux

```bash
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install pysimverse
```

*(Optional: later you can use `pip install -r requirements.txt`)*

---

## ▶️ How to Run

The project contains multiple Python scripts for different drone exercises.

To run a script:

```bash
python script_name.py
```

### Example

```bash
python basic_flight.py
```

---

## 📚 Learning Path

This course is structured to grow step by step:

### 🟢 Beginner Level

* Create a drone object
* Connect to the simulator
* Takeoff
* Hover (using time delays)
* Land safely

### 🟡 Intermediate Level

* Move in different directions
* Rotate (yaw control)
* Adjust speed
* Combine movements

### 🔵 Advanced Level

* Automated flight routines
* Path planning basics
* Simple missions
* Experimentation with control logic

---

## 🧠 Notes

* This is a **learning project**, so expect frequent updates and changes.
* Scripts are intentionally simple to help you understand concepts step by step.
* Feel free to experiment and modify the code — that’s the best way to learn!

---

## 🚀 Future Improvements

* Add more structured lessons
* Create reusable drone control modules
* Add documentation for each script
* Include real-world drone concepts
* Possibly connect to real drone hardware in the future

---

## 🤝 Contributing

If you have ideas, improvements, or new exercises, feel free to contribute!
