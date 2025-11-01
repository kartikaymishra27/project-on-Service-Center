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

## 🖼️ Screenshots Guide

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

## 🖼️ Screenshot Previews

🔐 Login Page

<img width="957" height="509" alt="login_page png" src="https://github.com/user-attachments/assets/41f9448e-f125-46c6-bb35-3a00227dfee4" />

🏠 Dashboard

<img width="750" height="509" alt="main_dashboard" src="https://github.com/user-attachments/assets/e9196c0a-4575-49b3-89ae-8424a772eaff" />


👥 Add Customer

<img width="596" height="504" alt="customer_registration_form png" src="https://github.com/user-attachments/assets/6154a8cf-f3bb-46c8-be4b-1f75f1f364cf" />

🧑‍🔧 Engineer Form

<img width="602" height="508" alt="engineer_form" src="https://github.com/user-attachments/assets/cfda4ddf-6f87-4f22-9ccb-df0a1069bfef" />


🧑‍🔧 Engineer Table

<img width="598" height="509" alt="engineer_details table" src="https://github.com/user-attachments/assets/923d97e5-1092-4ed8-a9d4-c7deacb67601" />


📦 Product Form

<img width="525" height="473" alt="product_entry_form png" src="https://github.com/user-attachments/assets/132ec49c-84e0-45be-b6d5-bfbb511f1f64" />


📦 Product Details

<img width="592" height="506" alt="product_list png" src="https://github.com/user-attachments/assets/a254294e-197f-46ca-b29f-a2f1823bfb56" />


☎️ Call Register

<img width="675" height="510" alt="call_register_form png" src="https://github.com/user-attachments/assets/46b15f29-1597-48e9-987d-c2150eaedcab" />


☎️ Call Register Table

<img width="951" height="510" alt="call_register_table png" src="https://github.com/user-attachments/assets/4aef2e17-b749-4735-8fef-743ca26b0198" />


🧾 Call Close Form

<img width="529" height="475" alt="call_close_form png" src="https://github.com/user-attachments/assets/35a780a0-37bf-47e9-802e-aca78abd1b80" />


🧾 Call Close Table

<img width="744" height="503" alt="call_close_table png" src="https://github.com/user-attachments/assets/3be2174b-3ace-4116-af6d-823388ccd87f" />


⭐ Feedback Form

<img width="526" height="447" alt="call_feedback_form png" src="https://github.com/user-attachments/assets/d45abd06-7ae6-493c-976b-209a3f479adc" />

📊 Feedback Table

<img width="742" height="507" alt="call_feedback_table png" src="https://github.com/user-attachments/assets/2c1c241f-82d9-4bb7-aa5f-71b9a24a28a7" />


📧 OTP Verification

<img width="452" height="433" alt="email_verification_screen png" src="https://github.com/user-attachments/assets/e834dde7-00af-47de-bcbf-f3e7c703bd1c" />

![otp_verification_mail png](https://github.com/user-attachments/assets/61062d04-28d5-4d52-8e5d-28289fd2eda9)


📬 Email Verification Mail for Password reset

![otp_password_reset_mail png](https://github.com/user-attachments/assets/c04b4623-ec6e-4070-9137-7c3b5fe93dcf)


📬 Customer Confirmation Mail

![customer_confirmation_mail png](https://github.com/user-attachments/assets/e6de774b-7dcb-4fef-94f7-8e1b3bc9a207)


🧑‍🔧 Engineer Notification Mail

![engineer_assignment_mail png](https://github.com/user-attachments/assets/64a77cdd-d57a-4f7d-9a11-e9195772c956)


💬 Feedback Confirmation Mail

![customer_feedback_mail png](https://github.com/user-attachments/assets/763c6dc7-36aa-4c1d-a3f8-62894617fd2a)

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

