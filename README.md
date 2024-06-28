# KISS Text Reader &middot; ![Release Status](https://img.shields.io/badge/release-v1.0.0-green) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
A KISS way to enable natural-voiced text reading on any GNU/Linux distribution and Windows.

## **Overview**

KISS Text Reader is a text-to-speech application with a simple and intuitive graphical user interface. It uses Google's Text-to-Speech (gTTS) service to read out the text you have selected in your system. The application is designed to be easy to use while providing high-quality, natural-sounding voice output.

## **Features**

* **Package Installation Check**: The application checks if the required Python packages are installed. If not, it installs them.

* **Language Detection**: The application detects the system language and adjusts the language of the text-to-speech and the button labels accordingly.

* **Text-to-Speech**: The application reads the selected text using Google's Text-to-Speech (gTTS) service. The text is selected using the xsel command, which means it reads the text that you have currently selected in your system.

* **Play/Pause/Stop**: The application has buttons to play the audio, pause/resume the audio, and stop the audio.

* **Exit**: The application has a button to exit the application.

* **Logo Display**: The application fetches and displays a logo from a URL.

* **Threaded Commands**: The commands associated with the buttons are run in separate threads to prevent the GUI from freezing while the command is running.

* **Window Closing Handling**: The application handles window closing events, stopping the reading and exiting the program.

* **GUI**: The application has a graphical user interface created with Tkinter and customtkinter. The GUI includes a logo and buttons for each of the features.

## 1. Dependency Installs

```
apt install libmp3-info-perl libmp3-tag-perl libsox-fmt-mp3 libunicode-string-perl sox xsel mpg321 python3-pip
```
_Note: this was first tested on Parrot OS, hence is proven to work flawlessly on Debian or any other distribution based on it. For other distributions or operating systems, replace the 'apt install' part with your package manager._

## 2. gTTS Install

You'll require ```pip``` (Python Package Installer) and also ```gTTS``` (Google Text-to-Speech), library and CLI tool to interface with Google Translate’s text-to-speech API, that’s what makes most of the job.

```
pip install gTTS
```


## 3. Execution Scripts

There are two ways to do this:

**Command Line Execution**

CLI-ready, Select, Execute: Select a text placed anywhere on your desktop, xsel will pipeline the order on the CLI and you’ll hear the voice reading.

:us: English Voice
```
xsel | gtts-cli --nocheck - | mpg321 -
```
:es: Spanish Voice
```
xsel | gtts-cli --nocheck --lang es - | mpg321 -
```
**Keyboard Shortcut Execution**

Just create a keyboard shortcut or keybinding: Parrot OS comes with MATE so you can just Add another one to the existing list, it’ll do the same work. Bind the command to a key combination e.g., Ctrl + Shift + R.

:us: English Voice
```
bash -c "xsel | gtts-cli --nocheck - | mpg321 -"
```
:es: Spanish Voice
```
bash -c "xsel | gtts-cli --nocheck --lang es - | mpg321 -"
```


## 4. Running the KISS Text Reader GUI

To run the KISS Text Reader GUI, you need to execute the `kisstextreader.py` script. Here are the steps for both Linux and Windows:

### 4.1 Linux

1. **Open a Terminal**: Open a terminal window. You can typically do this by pressing `Ctrl + Alt + T`.

2. **Navigate to the Script's Directory**: Use the `cd` command to navigate to the directory where the `kisstextreader.py` script is located. For example, if the script is in a directory called `scripts` in your home directory, you would type `cd ~/scripts`.

3. **Run the Script**: Run the script by typing `python3 kisstextreader.py` and pressing `Enter`. This will start the KISS Text Reader GUI.

### 4.2 Windows

1. **Open a Command Prompt**: Press `Win + R`, type `cmd`, and press `Enter`.

2. **Navigate to the Script's Directory**: Use the `cd` command to navigate to the directory where the `kisstextreader.py` script is located. For example, if the script is in a directory called `scripts` in your `C:` drive, you would type `cd C:\scripts`.

3. **Run the Script**: Run the script by typing `python kisstextreader.py` and pressing `Enter`. This will start the KISS Text Reader GUI.

The KISS Text Reader GUI should now be running. You can use it to read selected text aloud. The GUI includes buttons to read the selected text, pause/resume the reading, stop the reading, and exit the application.

## :scroll: Licensing
This work is licensed under a [MIT License](LICENSE).

## :brain: Acknowledgments

*"Whoever loves discipline loves knowledge, but whoever hates correction is stupid."*