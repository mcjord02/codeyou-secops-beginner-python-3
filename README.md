# 🧩 **Week 3 – Conditionals and Logic in Python**

### **Assignment Title:** *Building a Login Attempt Analyzer*

---

## 🧠 **Learning Objectives**

By the end of this assignment, you will:

* Understand and use Python conditional statements (`if`, `elif`, `else`)
* Apply logical operators (`and`, `or`, `not`) to evaluate multiple conditions
* Use conditional logic to trigger security-relevant alerts or messages
* Develop a “Login Attempt Analyzer” script that identifies suspicious behavior based on user input

---

## ⚙️ **Setup**

Before starting:

* Create a new folder called `week3_conditionals`
* Inside it, create a new Python file: `login_analyzer.py`
* You’ll reuse skills from Week 2 (input handling, variables, and formatting)

---

## 🧩 **Walkthrough Activity**

### **Part 1 – Introduction to Logic**

Conditional statements let your script “think.”
They decide what happens next based on given conditions.

Example:

```python
failed_logins = 5

if failed_logins > 3:
    print("[!] Warning: Multiple failed login attempts detected!")
else:
    print("[+] Normal login behavior.")
```

✅ Run this code and change the `failed_logins` value to see different results.

---

### **Part 2 – Taking User Input**

Let’s make it interactive so analysts can input data.

```python
username = input("Enter username: ")
failed_logins = int(input("Enter number of failed login attempts: "))

if failed_logins > 5:
    print(f"[!] ALERT: {username} has {failed_logins} failed logins!")
else:
    print(f"User {username} appears normal.")
```

💡 *Why it matters:*
Security teams often set thresholds (like “5 or more failed logins”) to detect brute-force or credential-stuffing attacks.

---

### **Part 3 – Adding More Logic**

Now, add logic that checks *both* failed logins and user criticality.

```python
critical_user = input("Is this a privileged user? (yes/no): ")

if failed_logins > 5 and critical_user.lower() == "yes":
    print("[*] CRITICAL ALERT: Privileged account under attack!")
elif failed_logins > 5:
    print("[!] ALERT: Multiple failed logins detected.")
elif failed_logins > 0:
    print("[-] Notice: Some failed attempts observed.")
else:
    print("[+] No failed logins recorded.")
```

✅ Try several combinations (e.g., 0, 3, 7 failed logins; yes/no privileged) and observe the outcomes.

---

### **Part 4 – Combining Logic with Reporting**

Add structured output for better readability.

```python
print("\n=== Login Attempt Summary ===")
print(f"Username: {username}")
print(f"Failed Attempts: {failed_logins}")
print(f"Privileged Account: {critical_user}")
```

Now you’re producing output that *feels* like an automated SOC report.

---

## 🔍 **Challenge: “Login Attempt Analyzer”**

Create a new script named `login_report.py` that:

1. Asks for the following input:

   * Analyst name
   * Username being analyzed
   * Number of failed login attempts
   * Whether the account is privileged (yes/no)
2. Uses logic to classify the event:

   * **High Risk:** privileged account with >5 failed logins
   * **Medium Risk:** standard account with >5 failed logins
   * **Low Risk:** 1–5 failed logins
   * **Informational:** 0 failed logins
3. Prints a formatted report like:

   ```
   ========================================
      Cyber Defense - Login Attempt Report
   ========================================
   Analyst: Jordan
   User: workstation-admin
   Failed Attempts: 9
   Privileged Account: Yes
   Risk Level: HIGH
   Alert: [*] Privileged account shows multiple failed logins!
   Report Generated: 2025-11-07 14:32
   ```

💡 *Hint:* Use `from datetime import datetime` to timestamp the report again.

---

## 🧩 **Optional Extension**

* Allow the script to process *multiple users* in one run using a loop.
* Add a counter that tracks how many total alerts were raised.

---

## ✅ **Submission**

Submit your `login_report.py` file in your classroom workspace or repository.
Your script should:

* Accept all required inputs
* Accurately classify risk levels
* Display a clean, readable summary

---

## 🧠 **Reflection Question**

> Why do automated systems often use thresholds and logic like this instead of requiring analysts to review every login attempt manually?

---
