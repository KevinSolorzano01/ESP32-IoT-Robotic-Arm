# M.R.A - Messenger Robotic Arm 🤖

## Overview
The Messenger Robotic Arm (M.R.A) is an IoT-controlled mobile robot designed to navigate spaces and transport objects autonomously or via remote control. Built with an **ESP32** microcontroller and programmed in **MicroPython**, this project integrates mobile robotics, embedded systems, and Internet of Things (IoT) technologies.

## Features
* **IoT Remote Control:** Fully operable via smartphone using the **Blynk** platform.
* **Automated Object Grasping:** Utilizes an IR sensor on the robotic claw to detect objects, automatically triggering the gripping and lifting mechanism.
* **Omnidirectional Movement:** Powered by DC gear motors and controlled via an L298N H-Bridge for precise navigation.
* **4-DOF Robotic Arm:** Constructed with SG90 servo motors, allowing for dynamic positioning (Base, Shoulder, Wrist, Claw).

## Hardware Components
* ESP32 Microcontroller
* 2x DC Gear Motors
* L298N Motor Driver (H-Bridge)
* 4x Servo Motors (SG90)
* IR Obstacle Avoidance Sensor
* 12V Power Supply

## Technologies Used
* **Language:** MicroPython
* **Libraries:** `network`, `BlynkLib`, `machine` (Pin, PWM)
* **IoT Platform:** Blynk

## Future Improvements
* Transition from blocking delays (`sleep()`) to asynchronous operations (`uasyncio`) or hardware timers to optimize the main control loop.
* Implement PID control for smoother robotic arm movements.

## Demo
*(Insertar aquí un enlace a un video corto de YouTube o un GIF del robot funcionando)*
