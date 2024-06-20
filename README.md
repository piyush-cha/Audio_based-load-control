
# Audio-Based Load Control Setup Guide

This guide provides step-by-step instructions for setting up your Raspberry Pi to run the Audio-Based Load Control project. The setup involves configuring locale settings, updating system packages, installing necessary software, and setting up a Python virtual environment.

```bash
sudo locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8
sudo reboot
```
# After rebooting
```bash
sudo apt update
sudo apt upgrade -y
sudo apt upgrade thonny
pip install --upgrade pip
pip install --upgrade thonny
sudo apt update
sudo apt install python3-full
python3 -m venv myenv
source myenv/bin/activate
pip install --upgrade pip
pip install SpeechRecognition
python -m speech_recognition
```
#If you done with your work 
```bash
deactivate
```
## Detailed Steps

1. **Set Locale**: Configure the locale settings to ensure proper language support.
    ```bash
    sudo locale-gen en_US.UTF-8
    sudo update-locale LANG=en_US.UTF-8
    sudo reboot
    ```

2. **Update System Packages**: After rebooting, update the package lists and upgrade installed packages.
    ```bash
    sudo apt update
    sudo apt upgrade -y
    ```

3. **Upgrade Thonny**: Upgrade Thonny, the Python IDE, to the latest version.
    ```bash
    sudo apt upgrade thonny
    pip install --upgrade pip
    pip install --upgrade thonny
    ```

4. **Install Full Python 3**: Ensure that the full Python 3 package is installed.
    ```bash
    sudo apt install python3-full
    ```

5. **Set Up Python Virtual Environment**: Create and activate a Python virtual environment for your project.
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

6. **Install Required Python Packages**: Upgrade `pip` and install the necessary Python packages.
    ```bash
    pip install --upgrade pip
    pip install SpeechRecognition
    ```

7. **Test Speech Recognition Installation**: Run a simple test to ensure that the SpeechRecognition package is installed correctly.
    ```bash
    python -m speech_recognition
    ```

8. **Deactivate Virtual Environment**: Deactivate the virtual environment when you're done.
    ```bash
    deactivate
    ```

## Running Your Project

1. **Activate the virtual environment**:
    ```bash
    source myenv/bin/activate
    ```

2. **Run your `audio.py` script**:
    ```bash
    python /path/to/your/project/audio.py
    ```

3. **To stop the script**, use `Ctrl + C`. **Deactivate the virtual environment** when you're done:
    ```bash
    deactivate
    ```

## Troubleshooting

- **Locale Issues**: If you encounter issues related to locale settings, double-check the commands used to set the locale and ensure they match your system's requirements.
- **Speech Recognition Errors**: Ensure your microphone is correctly connected and working. Speak clearly and ensure there is minimal background noise.

## Contact

For any questions or support, please contact [email](mailto:pchafle903@gmail.com).

---

Thank you for setting up the Audio-Based Load Control project!
```
