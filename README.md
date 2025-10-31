# 🧠 Smart Service Center Management System

### 💻 Overview

**Smart Service Center Management System** is a GUI-based Python application designed to streamline the daily operations of a service center.
It efficiently manages **customer registrations, engineer assignments, service calls, OTP verification, email automation, and feedback collection** using a **MySQL database** for data storage and **Tkinter** for the GUI interface.
All entered data (customers, engineers, products, calls, and feedback) is **securely stored in SQL tables**, ensuring persistence and easy retrieval for reporting or future use.

---

## ⚙️ Features

### 🔐 Authentication

* Secure **Login System** for admin/staff
* **OTP Verification** for account security
* **Email verification** after successful signup

### 👥 Customer Management

* Add, view, update, delete customer records
* Auto email confirmation upon customer registration

### 🧑‍🔧 Engineer Management

* Add and manage engineer details
* Automatic email notification when a new engineer is added

### 📦 Product Management

* Manage products and their warranty details
* **Autofill Functionality:** Entering a product ID automatically displays product name and related info

### 📞 Service Call Management

* Modules for **Call Register**, **Call Close**, and **Call Feedback**
* Links customer, product, and engineer information dynamically
* Sends automatic emails for every status update

### ⭐ Smart Feedback System

* Customers can rate service quality (1–5 stars)
* System automatically generates feedback messages:

  ```python
  if rating >= 4:
      feedback = "Thank you for your positive response!"
  elif rating == 3:
      feedback = "We appreciate your feedback and will improve further."
  else:
      feedback = "We’re sorry for the inconvenience and will resolve the issue soon."
  ```
* Feedback is stored and accessible in the system

### 📧 Email Automation

* OTP and registration confirmation emails
* Engineer assignment notifications
* Feedback acknowledgment emails
* Auto-deletion of temporary mail data after successful send

---

## 🖼️ Screenshot Guide

| Screenshot Name                   | Description                            |
| --------------------------------- | -------------------------------------- |
| `login_page.png`                  | Login interface for admin/staff        |
| `dashboard_main.png`              | Main dashboard with all module options |
| `insert_customer_form.png`        | Add new customer                       |
| `customer_details_table.png`      | Displays all registered customers      |
| `engineer_form.png`               | Add engineer details                   |
| `engineer_details_table.png`      | Engineer record display                |
| `product_form.png`                | Add or update product                  |
| `product_details.png`             | Product list view                      |
| `callregister_form.png`           | Register a new service call            |
| `callregister_table.png`          | List of service calls                  |
| `callclose_form.png`              | Close existing service call            |
| `callclose_table.png`             | Closed service record                  |
| `feedback_form.png`               | Submit customer feedback               |
| `feedback_table.png`              | All feedback records                   |
| `otp_verification.png`            | OTP verification screen                |
| `email_verification_mail.png`     | Email sent for OTP verification        |
| `customer_email_confirmation.png` | Customer registration email            |
| `engineer_email_notification.png` | Engineer notification email            |
| `feedback_email_confirmation.png` | Feedback acknowledgment email          |

---

## 🧩 Technologies Used

* **Frontend:** Python (Tkinter GUI)
* **Backend & Database:** MySQL (all records securely stored in SQL tables)
* **Email Service:** `smtplib`
* **Verification:** OTP via Email
* **Version:** Python 3.12

---

## 🚀 Future Enhancements

* Add report generation (PDF/Excel)
* Integrate SMS-based OTP verification
* Add analytics and performance dashboard
* Include dark mode UI

---

## 🛠️ Setup & Run Instructions

### Step 1: Clone Repository

```bash
git clone https://github.com/kartikaymishra27/project-on-Service-Center.git
cd project-on-Service-Center
```

### Step 2: Setup Database

Open MySQL and run:

```sql
create database servicecenter;
use servicecenter;

create table servicecenter(officeid varchar(50), name varchar(50), address varchar(50), email varchar(50), phone varchar(50), regno varchar(50));
create table productcategory(catid varchar(50), catname varchar(50), description varchar(50));
create table products(productid varchar(50), pname varchar(50), catid varchar(50), warrantydays varchar(50));
create table servicetypes(serviceid varchar(50), catid varchar(50), productid varchar(50), sname varchar(50), charges int, estimationtime varchar(50));
create table customer(cusid varchar(50), cname varchar(50), address varchar(50), email varchar(50), phone varchar(50), catid varchar(50), productid varchar(50));
create table engineers(engid varchar(50), ename varchar(50), address varchar(50), email varchar(50), phone varchar(50), catid varchar(50));
create table staff(staffid varchar(50), sname varchar(50), address varchar(50), email varchar(50), phone varchar(50));
create table callregister(callid varchar(50), cusid varchar(50), catid varchar(50), productid varchar(50), engid varchar(50), estcharge int);
create table callclose(callid varchar(50), cusid varchar(50), engid varchar(50), dateofclose varchar(50));
create table callfeedback(callid varchar(50), feedbackrating varchar(50), remarks varchar(50));
```

### Step 3: Install Dependencies

```bash
pip install mysql-connector-python
```

### Step 4: Run Project

```bash
python login.py
```

---

## 👨‍💻 Developer

**Kartikay Mishra**
📧 [kartikaymishra7417@gmail.com](mailto:kartikaymishra7417@gmail.com)
📍 Agra, India

