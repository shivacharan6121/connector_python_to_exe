# 🚀 Connector Management System

## 📌 Overview
The **Connector Management System** is a Python-based GUI application built using **CustomTkinter**. It allows users to manage electronic connectors by adding, removing, and displaying data stored in a MySQL database.

This application supports **MySQL database connectivity** and is converted into an **executable (.exe) file using auto-py-to-exe**.

---

## 🖥️ System Requirements

### **Minimum Requirements**
- **OS:** Windows 7 SP1 / 8 / 10 / 11 (64-bit recommended)
- **Processor:** Intel Core i3 (2 GHz or higher)
- **RAM:** 2 GB
- **Storage:** 300 MB free space
- **Display:** 1024x768 resolution
- **MySQL Version:** MySQL 5.7 or 8.0 (via XAMPP)
- **Python (if needed):** Python 3.7+

### **Recommended Requirements**
- **OS:** Windows 10 / 11 (64-bit)
- **Processor:** Intel Core i5 / AMD Ryzen 5 or better
- **RAM:** 4 GB or more
- **Storage:** 500 MB free space
- **Display:** 1366x768 or higher resolution
- **MySQL Version:** MySQL 8.0 (latest XAMPP version)
- **Python (if needed):** Python 3.9+

---

## 🔧 Software Requirements

### **Required Software on Target System**
✅ **[Download XAMPP](https://www.apachefriends.org/download.html)**  
- Install XAMPP and **start Apache & MySQL** before running the `.exe` file.

✅ **[Visual C++ Redistributable for VS 2015-2022](https://aka.ms/vs/17/release/vc_redist.x64.exe)**  
- Install VC++ runtime to prevent missing DLL errors.

✅ **Firewall Settings (For Remote MySQL)**  
- Ensure **port 3306 is open** in Windows Firewall if connecting to a remote database.

---

## 📁 Files Needed for One Directory Mode

If converted using **One Directory Mode**, the following files are required:

| File/Folder | Purpose |
|-------------|---------|
| `your_app.exe` | The main executable file |
| `pythonXX.dll` | Python runtime DLL |
| `pymysql`, `customtkinter` dependencies | Required for MySQL and GUI functionality |
| `lib` folder | Contains additional dependencies |
| `assets` folder (if applicable) | Stores CustomTkinter themes |

⚠️ **Important:** **Always distribute the entire folder, not just the `.exe` file.**

---

## ▶️ How to Run the `.exe` on Another System
1. Copy the **entire One Directory output folder** to the target PC.
2. Install **XAMPP** and start **MySQL** (if using a local database).
3. If using a **remote MySQL server**, check **port 3306 in Windows Firewall**.
4. Run **your_app.exe** from the folder.

---

## 🛠️ Troubleshooting Common Errors

| Error Message | Cause | Solution |
|--------------|--------|---------|
| **"ModuleNotFoundError: No module named 'pymysql'"** | Missing dependency | Ensure the entire folder is copied, not just `.exe` |
| **"Can't connect to MySQL"** | XAMPP MySQL not running | Start MySQL via XAMPP |
| **"Missing DLLs"** | Missing system files | Install **Visual C++ Redistributable** |
| **"Permission Denied"** | Windows security issue | Run `.exe` as **Administrator** |

---

## 📌 Summary
- **Minimum System:** Windows 7, 2GB RAM, Intel i3, MySQL 5.7.
- **Recommended System:** Windows 10/11, 4GB RAM, Intel i5+, MySQL 8.0.
- **Required Software:** XAMPP (for MySQL), VC++ Redistributable.
- **One Directory Mode:** **Distribute the entire folder, not just `.exe`.**
---
## DEMO
1.**Main Page** After executing the **ex_main.exe** file the main page looks like the below image where you can manage the records like adding, removing
records
![Screenshot_2025-03-01_23_42_52](https://github.com/user-attachments/assets/81d08f42-e082-4c98-9010-e7ef0251f395)

2.**Performing Add Operation** First enter the **part no:** and then enter the **No. of Connectors** you want to add if **part no:** already exists it updates the **quantity section** if **part no** does not exist it will add the **part no** and **quantity** as new record in the database existing part no **Part no:10-646401-035N** new part no **DES109-WE**

**NOTE:** The values will not be updated until you click on **OK** button

**Adding connectors to the existing part no:10-646401-035N**

**Before Adding Connectors to part no:10-646401-035N**

![Screenshot_2025-03-02_00_50_37](https://github.com/user-attachments/assets/d7992c7d-a495-4fe3-be8e-3d998cc25e28)

**After Adding Connectors to part no:10-646401-035N**

![Screenshot_2025-03-02_00_50_50](https://github.com/user-attachments/assets/1e34564d-3e4c-4559-b162-479fc19858c6)

**Before Adding New part no:DES109-WE**

![Screenshot_2025-03-02_01_02_44](https://github.com/user-attachments/assets/ce2c8480-535e-4243-8de7-447c6d7ac157)

**After Adding New part no:DES109-WE**

![Screenshot_2025-03-02_01_03_04](https://github.com/user-attachments/assets/d3f41c3d-ffc2-44a7-93e2-a89e43313924)

2.**Performing Remove Operation** First enter the **part no:** and then enter the **No. of Connectors** you want to remove if **part no:** already exists it updates the **quantity section** if **part no** does not exist it will display error message in dialog box as **Invalid part no:DOFS-WING-001** and if available connectors are less than required connectors then it displays error message as **Insufficient Connectors** if available connectors and required connectors are equal then it will update quantity value as **0** existing part no **Part no:10-646401-035N**

**NOTE:** The operation will not be perforemd(or)executed until you click on **OK** button in dialog box

**Removing connectors from existing part no:10-646401-035N**

**Before Removing Connectors from part no:10-646401-035N**

![Screenshot_2025-03-02_01_28_30](https://github.com/user-attachments/assets/4f908ebc-2cdb-431f-81d2-902e35126fb6)

**After Removing Connectors from part no:10-646401-035N**

![Screenshot_2025-03-02_01_28_41](https://github.com/user-attachments/assets/aa28b152-ae54-4fdf-b21f-e8753a3803a9)

**Removing connectors from non-existing part no:DOFS-WING-001**

![Screenshot_2025-03-02_01_31_24](https://github.com/user-attachments/assets/6851e4f7-a6f5-45f7-ac58-2b99665d48a6)

**Required connectors are more than the existing connectors from part no:10-646401-035N**

![Screenshot_2025-03-02_01_36_21](https://github.com/user-attachments/assets/a70c2d80-3c11-493f-95f2-033036120f06)

**Required connectors are equal to existing connectors of part no:10-646401-035N**

![Screenshot_2025-03-02_01_38_22](https://github.com/user-attachments/assets/9378170a-e19a-42d3-86c5-ce6b88f2857d)

**After removing the required connectors**

![Screenshot_2025-03-02_01_38_30](https://github.com/user-attachments/assets/0b69c0d8-5745-4f04-a1c0-9f40fd9dea80)









⚡ **Enjoy managing your connectors efficiently

