# **CSRF PoC Generator ⚠️🛠️**

### **Overview 🌐**

This tool allows you to generate a Cross-Site Request Forgery (CSRF) proof-of-concept (PoC) HTML form from raw HTTP requests, cURL commands, or text files containing HTTP requests. It simplifies the process of creating a CSRF attack vector for security testing purposes.

### **Features ✨**
- Parse raw HTTP requests interactively 📝
- Parse HTTP requests from cURL commands 🐚
- Read HTTP requests from `.txt` files 📂
- Generate an HTML form replicating the original request 🧩
- Save the CSRF PoC HTML file locally and open it in the browser 🌍💻
- Handles URL-encoded and JSON-like request bodies 🔐

### **Installation 💾**

Ensure you have Python 3.x installed. This tool uses only Python standard libraries; no external dependencies are required.
Clone this repository or download the source files:


### **Usage**

#### **1. Parsing Requests 🔍**
You can input HTTP requests in three ways:

##### **Raw HTTP request (interactive):**
    python csrf_poc_generator.py
You will be prompted to paste your HTTP request line-by-line. Type **END** on a new line to finish.

#### **cURL command input:**
    python csrf_poc_generator.py -c "curl -X POST https://example.com/api -d 'param1=value1&param2=value2'"


#### **Text file input:**
    python csrf_poc_generator.py -t /path/to/request.txt

### **2. Generating the CSRF PoC HTML**

Run the CSRF PoC generator script, which will prompt for input using the request parser, then generate and open the CSRF PoC form:

    python csrf_poc_generator.py

This will create an HTML file (default: CSRF_POC csrf_poc.html) containing a form with the specified HTTP method, action URL, and parameters pre-filled as hidden inputs.

### **Sample HTML OUTPUT**
![img.png](img.png)

#### **How It Works ⚙️**
1. The request parser extracts HTTP method, URL, and request body.
2. The generator creates an HTML form matching these details.
3. When the form is submitted, it replicates the original request — useful for testing CSRF vulnerabilities.

### **Notes 📝**

1. Currently, supports application/x-www-form-urlencoded and simple JSON-like bodies.
2. The generated form uses the HTTPS scheme by default.
3. The generated CSRF PoC HTML file is automatically opened in your default web browser upon creation.

### Disclaimer ⚠️

This tool is intended **only for educational purposes** and **authorized penetration testing**. **Do not use this tool on systems without proper permission.**

The developer of this tool **does not accept any responsibility or liability** for misuse or damage caused by this project.
**Use responsibly. Stay ethical.**

### **Author 👤**

**Pawan Kadwadi**