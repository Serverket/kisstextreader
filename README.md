# KISS Text Reader &middot; ![Release Status](https://img.shields.io/badge/release-v1.0.0-green) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
A KISS way to enable natural-voiced text reading on any GNU/Linux distribution.

# **Overview**

When it comes to an offline Text Reader or Screen Reader there are options like Orca or Festival, which are Accessibility-focused but normally this type of software is pointed towards usability -and over-complicated extensibility- more than voice quality, in this case we aim to a more Natural Voice, so articles, emails or chats can be heard without a so robotic tone.

# 1. Dependency Installs

```
apt install libmp3-info-perl libmp3-tag-perl libsox-fmt-mp3 libunicode-string-perl sox xsel mpg321 python3-pip
```
_Note: this was first tested on Parrot OS, hence is proven to work flawlessly on Debian or any other distribution based on it, for the case of the ones using a different package manager just replace the 'apt install' part for yours._

# 2. gTTS Install

You'll require ```pip``` (Python Package Installer) and also ```gTTS``` (Google Text-to-Speech), library and CLI tool to interface with Google Translate’s text-to-speech API, that’s what makes most of the job.

```
pip install gTTS
```

# 3. Execution Scripts

There are two ways to do this:

“Manual” Way

CLI-ready, Select, Execute: Select a text placed anywhere on your desktop, xsel will pipeline the order on the CLI and you’ll hear the voice reading.

:us: English Voice
```
xsel | gtts-cli --nocheck - | mpg321 -
```
:es: Spanish Voice
```
xsel | gtts-cli --nocheck --lang es - | mpg321 -
```

“Manuel” Way

Just create a keyboard shortcut or keybinding: Parrot OS comes with MATE so you can just Add another one to the existing list, it’ll do the same work. Bind the command to a key combination e.g., Ctrl + Shift + R.

:us: English Voice
```
bash -c "xsel | gtts-cli --nocheck - | mpg321 -"
```
:es: Spanish Voice
```
bash -c "xsel | gtts-cli --nocheck --lang es - | mpg321 -"
```
What’s next? Well, I would say being able to control the playing, like pause and resume functions, a GUI maybe? However, if you know an existing implementation (or have made one) for such things you can email me anytime or PM over Telegram and make great things with this one.

## :scroll: Licensing
<a rel="license" href="https://mit-license.org/"></a>This work is licensed under a <a rel="license" href="https://mit-license.org/">MIT License</a>.

## :brain: Acknowledgments

*"Whoever loves discipline loves knowledge, but whoever hates correction is stupid."*