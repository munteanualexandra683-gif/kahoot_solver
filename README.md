# Kahoot  Solver

A  Python script that uses Google's Gemini Vision API to instantly read your screen and print the correct Kahoot answer to the terminal. 

This project uses image downscaling and optimized AI prompting to reduce latency and beat the game timer. It is designed for educational and entertainment purposes.

## Features
- **Ultra-Fast Processing:** Downscales screenshots to 800x800 for rapid upload.
- **Auto-Fallback Routing:** Automatically cycles through Gemini Flash models (`gemini-3.5-flash-lite`, `gemini-3.8-flash`, `gemini-3.7-flash`) if servers are busy.
- **Terminal Highlighting:** Outputs only the exact color or text of the correct answer directly in your terminal.
