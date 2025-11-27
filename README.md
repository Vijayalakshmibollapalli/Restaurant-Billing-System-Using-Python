# 🍽️ Restaurant Billing System Using Python

## Introduction
This project implements a complete Restaurant Billing and Customer Feedback System using Python. It allows users to browse menu items, place food orders, generate detailed bills with GST and discounts, and optionally provide feedback. The system is available in both a Jupyter Notebook and a standalone Python script, making it easy to run, understand, and extend.
The goal is to provide a self-contained application that demonstrates billing logic, data handling, order validation, and structured output formatting—ideal for learning, practice, or expanding into a more feature-rich system.

## 🍕 Features
* Browse restaurant menu with item names and prices
* Add multiple food items and quantities to an order
* Handle input validation (valid items, positive quantities)
* Auto-calculate:
    * Subtotal
    * GST (5%)
    * Discount (10% for eligible bills)
    * Final total
* Generate a unique Bill ID using date & time
* Display a formatted bill receipt
* Collect customer rating, feedback, and suggestions
* Save all order details to a file (orders.txt)
* View complete order history at any time
* Menu-driven, user-friendly workflow

## 🧾 Technology Stack
* Python – Core programming language
* Jupyter Notebook (.ipynb) – Interactive version for demonstration
* Python Script (.py) – Command-line version of the application
* File Handling for storing order records
* Datetime Module for bill number generation
