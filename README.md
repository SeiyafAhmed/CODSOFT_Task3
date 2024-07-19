# PASSWORD GENERATOR
## Overview
The Password Generator is a Python application designed to create secure passwords with customizable options. Users can easily specify password length, and choose to include uppercase letters, numbers, and symbols, ensuring passwords meet their security requirements.

## Features
* **User-Friendly Interface:** Intuitive design for easy navigation.
* **Select Password Length:** Choose the desired length of the password.
* **Customizable Options:**
    * Toggle the inclusion of **uppercase letters**.
    * Toggle the inclusion of **numbers**.
    * Toggle the inclusion of **symbols**.
* **Password Complexity:** Adjust the complexity based on selected options. 

## Getting Started

**Installation**

1. Clone the repository:
    ```
    git clone https://github.com/SeiyafAhmed/Password-Generator.git
    ```

2. Install the required libraries:
    ```
    pip install ttkbootstrap
    ```
3. Customize the theme file:
     1. Navigate to the directory
        
        ```
        cd venv\Lib\site-packages\ttkbootstrap\themes
        ```
     2. Open user.py
        ```
        notepad user.py
        ```
     3. Replace the following code
        ```
        USER_THEMES = {
            "passwordgenerator": {
                "type": "light",
                "colors": {
                    "primary": "#4582ec",
                    "secondary": "#1e247e",
                    "success": "#02b875",
                    "info": "#17a2b8",
                    "warning": "#f0c330",
                    "danger": "#d9534f",
                    "light": "#F8F9FA",
                    "dark": "#343A40",
                    "bg": "#ffffff",
                    "fg": "#343a40",
                    "selectbg": "#adb5bd",
                    "selectfg": "#ffffff",
                    "border": "#1e247e",
                    "inputfg": "#343a40",
                    "inputbg": "#fff",
                    "active": "#e5e5e5"
                }
            }
        }
        ```

## Running the Application
**Run the following command to start the application:**
```
python main.py
```


## Screenshots
![image](https://github.com/user-attachments/assets/0a66859e-225f-4c23-bcd6-4a3937a213dd)
![image](https://github.com/user-attachments/assets/7061c3ba-26e3-4705-9d68-127d44630ea8)
![image](https://github.com/user-attachments/assets/7e320395-d364-4414-905a-24b7bebb8478)
![image](https://github.com/user-attachments/assets/19d714f7-e3a0-4826-b34d-2a2fcb446ba3)


License
This project is licensed under the MIT License. See the -[LICENSE](https://github.com/SeiyafAhmed/Password-Generator/blob/main/LICENSE) file for details. 

Contact
For any questions or suggestions, please [contact us](mailto:seiyafahmed.ofc@gmail.com).
