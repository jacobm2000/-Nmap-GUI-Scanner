# Nmap GUI Scanner

A lightweight Python-based GUI frontend for Nmap that allows users to perform customizable network scans easily, without needing to memorize command-line arguments.

## Features

- GUI built with `tkinter`
- Supports popular Nmap scan modes (`-sS`, `-sT`, `-O`, etc.)
- Input port range
- Choose scan speed using Nmap timing templates (`-T0` to `-T5`)
- Displays formatted scan results
- Threads scanning in the background to prevent GUI freezing
- Shows elapsed scan time

## Requirements

- Python 3.6+
- python-nmap
- Nmap (must be installed and available in system PATH)

## Installation

1. Install Python dependencies:

```bash
pip install python-nmap
