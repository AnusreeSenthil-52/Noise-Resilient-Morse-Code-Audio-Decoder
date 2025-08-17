# 🔊 Noise-Resilient Morse Code Audio Decoder

## 📖 Introduction
This project decodes Morse code from noisy audio signals. It uses MATLAB to extract Morse symbols from audio and Python to convert them into readable text.

## 🛠 Tools Used
- MATLAB
- Python 3.x

## ✨ Features
- Extracts dots, dashes, and spaces from Morse audio.
- Converts Morse symbols to readable text.
- Resilient to moderate background noise.
- Saves Morse symbols for further processing.

## 📃 MATLAB Script
- Reads and normalizes Morse audio (`morse.wav`).
- Computes the envelope and thresholds the signal.
- Detects dots, dashes, letter gaps, and word gaps.
- Saves extracted Morse symbols to `morse.txt`.

## 🐍 Python Script
- Reads `morse.txt`.
- Decodes Morse symbols into readable text using a dictionary.
- Handles letters and word spacing.

## 💡 Skills Gained
- Audio signal processing
- Morse Codes
- MATLAB and Python integration

## 🔮 Future Improvements
- Real-time decoding from microphone input.
- Enhanced noise filtering.
- GUI interface for easier usage.