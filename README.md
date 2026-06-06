# AI System Monitor

A Python program that monitors Windows system activities related to AI tools, connections, and files. Detects and logs AI-related activities in real-time and stores them in an Excel file.

## Features

- **Network Connection Monitoring**: Detects connections to AI-related domains (OpenAI, Anthropic, HuggingFace, etc.)
- **File Access Monitoring**: Monitors AI-related files and content
- **Process Monitoring**: Tracks AI-related processes and commands
- **Real-time CMD Display**: Shows activities as they happen
- **Excel Logging**: Stores all detected activities with risk levels
- **Windows Compatible**: Specifically designed for Windows systems

## Installation

1. Install Python 3.7 or higher
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the monitor:
```bash
python ai_system_monitor.py
```

Press `Ctrl+C` to stop monitoring.

## Monitoring Capabilities

### Network Monitoring
- Detects connections to AI domains: openai.com, anthropic.com, huggingface.co, etc.
- Monitors established network connections
- Logs process names making AI connections

### File Monitoring
- Monitors Desktop, Documents, Downloads, and current directory
- Tracks AI-related file extensions: .py, .ipynb, .json, .txt, .md, .csv
- Scans file content for AI keywords
- Detects file creation and modification

### Process Monitoring
- Tracks AI-related processes: Python, Jupyter, VS Code, browsers
- Monitors command line arguments for AI keywords
- Logs new process creation

## Output

### Real-time CMD Display
- Shows detected activities with risk levels:
  - `[HIGH]` - Critical AI activities
  - `[MEDIUM]` - Moderate AI activities  
  - `[LOW]` - Basic AI activities

### Excel Log File
- Creates `ai_monitor_log.xlsx` with:
  - Timestamp
  - Event Type
  - Description
  - Process Name
  - File/URL
  - Risk Level (color-coded)

## Configuration

The monitor can be customized by modifying the `AIMonitorConfig` class in the script:

- `ai_keywords`: Keywords to detect in files and processes
- `ai_domains`: AI-related domains to monitor
- `ai_processes`: AI-related processes to track
- `monitored_extensions`: File extensions to monitor
- `monitor_interval`: Monitoring frequency in seconds

## Requirements

- Windows OS
- Python 3.7+
- Administrative privileges (recommended for full monitoring capabilities)

## Security Note

This tool monitors system activities for security and awareness purposes. Ensure you have appropriate permissions before monitoring systems you don't own.
