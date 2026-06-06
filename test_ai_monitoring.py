#!/usr/bin/env python3
"""
Test script to trigger AI monitoring events
"""

import os
import time
import requests
import json
from datetime import datetime

def create_ai_files():
    """Create AI-related files to trigger monitoring"""
    
    # Test 1: Python file with AI imports
    ai_python_content = """
import openai
import anthropic
import tensorflow as tf
import torch
from transformers import AutoModel

# ChatGPT integration
def chat_with_gpt(prompt):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Claude integration
def chat_with_claude(prompt):
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

# TensorFlow model
def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

if __name__ == "__main__":
    print("AI Test Script Running...")
    model = create_model()
    print("Model created successfully")
"""
    
    with open("ai_integration_test.py", "w") as f:
        f.write(ai_python_content)
    
    # Test 2: Jupyter notebook content
    notebook_content = {
        "cells": [
            {
                "cell_type": "code",
                "source": [
                    "import openai\n",
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "from transformers import pipeline\n",
                    "\n",
                    "# ChatGPT API call\n",
                    "client = openai.OpenAI()\n",
                    "response = client.chat.completions.create(\n",
                    "    model=\"gpt-4\",\n",
                    "    messages=[{\"role\": \"user\", \"content\": \"Hello AI\"}]\n",
                    ")"
                ],
                "metadata": {}
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    with open("ai_analysis.ipynb", "w") as f:
        json.dump(notebook_content, f, indent=2)
    
    # Test 3: AI configuration file
    ai_config = """
{
    "openai_api_key": "sk-test-key-12345",
    "anthropic_api_key": "sk-ant-test-key-67890",
    "model_config": {
        "chatgpt_model": "gpt-4",
        "claude_model": "claude-3-sonnet-20240229",
        "temperature": 0.7
    },
    "ai_tools": ["chatgpt", "claude", "gemini", "copilot"],
    "monitoring_enabled": true
}
"""
    
    with open("ai_config.json", "w") as f:
        f.write(ai_config)
    
    print("✅ Created AI test files:")
    print("   - ai_integration_test.py")
    print("   - ai_analysis.ipynb") 
    print("   - ai_config.json")

def simulate_ai_network_activity():
    """Simulate AI service network connections"""
    
    # Test 1: Simulate OpenAI API call (will fail but trigger monitoring)
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": "Bearer sk-test-key",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4",
                "messages": [{"role": "user", "content": "Test message"}]
            },
            timeout=5
        )
    except:
        pass  # Expected to fail, but will trigger network monitoring
    
    # Test 2: Simulate Anthropic API call
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": "sk-ant-test-key",
                "Content-Type": "application/json"
            },
            json={
                "model": "claude-3-sonnet-20240229",
                "max_tokens": 100,
                "messages": [{"role": "user", "content": "Test"}]
            },
            timeout=5
        )
    except:
        pass  # Expected to fail, but will trigger network monitoring
    
    print("✅ Simulated AI network activity")

def create_honeypot_files():
    """Create honeypot files to trigger security alerts"""
    
    # Create suspicious AI tool names
    suspicious_tools = [
        "AI-Hack-Tool.exe",
        "ChatGPT-Cracker.bat", 
        "Claude-Exploit.ps1",
        "Gemini-Backdoor.py",
        "AI-Malware-Generator.exe"
    ]
    
    for tool in suspicious_tools:
        with open(tool, "w") as f:
            f.write(f"# This is a honeypot file for {tool}\n")
            f.write("# Suspicious AI tool detected\n")
            f.write("import os\n")
            f.write("import subprocess\n")
            f.write("# Malicious AI tool simulation\n")
    
    print("✅ Created honeypot files:")
    for tool in suspicious_tools:
        print(f"   - {tool}")

def test_model_integrity():
    """Test AI model integrity verification"""
    
    # Create a fake model file
    model_data = b"FAKE_AI_MODEL_DATA_" + b"X" * 1000  # 1KB fake model
    
    with open("test_model.pt", "wb") as f:
        f.write(model_data)
    
    with open("test_model.h5", "wb") as f:
        f.write(model_data)
    
    with open("test_model.onnx", "wb") as f:
        f.write(model_data)
    
    print("✅ Created test model files:")
    print("   - test_model.pt")
    print("   - test_model.h5") 
    print("   - test_model.onnx")

def create_ai_documentation():
    """Create AI documentation files"""
    
    docs = [
        ("ChatGPT_Usage_Guide.md", "# ChatGPT Usage Guide\n\nThis guide explains how to use ChatGPT API..."),
        ("AI_Model_Training.ipynb", json.dumps({
            "cells": [{"cell_type": "markdown", "source": ["# AI Model Training\n\nTraining neural networks..."]}],
            "metadata": {},
            "nbformat": 4
        })),
        ("Machine_Learning_Notes.txt", "Machine Learning Notes:\n- Supervised Learning\n- Neural Networks\n- Deep Learning"),
        ("AI_Research_Paper.pdf", b"%PDF-1.4\n%AI Research Paper\n1 0 obj\n<<\n/Type /Catalog\n>>\nendobj\n")
    ]
    
    for filename, content in docs:
        mode = "w" if isinstance(content, str) else "wb"
        with open(filename, mode) as f:
            f.write(content)
    
    print("✅ Created AI documentation files:")
    for filename, _ in docs:
        print(f"   - {filename}")

def run_all_tests():
    """Run all test scenarios"""
    print("🚀 Starting AI Monitoring Tests...")
    print("=" * 50)
    
    # Test 1: Create AI files
    print("\n📁 Test 1: Creating AI Files")
    create_ai_files()
    time.sleep(2)
    
    # Test 2: Simulate network activity
    print("\n🌐 Test 2: Simulating AI Network Activity")
    simulate_ai_network_activity()
    time.sleep(2)
    
    # Test 3: Create honeypot files
    print("\n🍯 Test 3: Creating Honeypot Files")
    create_honeypot_files()
    time.sleep(2)
    
    # Test 4: Test model integrity
    print("\n🔐 Test 4: Testing Model Integrity")
    test_model_integrity()
    time.sleep(2)
    
    # Test 5: Create documentation
    print("\n📚 Test 5: Creating AI Documentation")
    create_ai_documentation()
    time.sleep(2)
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("📊 Check the AI monitoring output for detected activities")
    print("🔍 Look for:")
    print("   - File access alerts")
    print("   - Network connection attempts")
    print("   - Honeypot triggers")
    print("   - Model integrity checks")
    print("   - STIX/TAXII threat intelligence")
    
    # Clean up some test files (leave others for monitoring)
    cleanup_files = [
        "AI-Hack-Tool.exe",
        "ChatGPT-Cracker.bat",
        "Claude-Exploit.ps1", 
        "Gemini-Backdoor.py",
        "AI-Malware-Generator.exe"
    ]
    
    print("\n🧹 Cleaning up honeypot files...")
    for file in cleanup_files:
        try:
            os.remove(file)
            print(f"   Removed: {file}")
        except:
            pass

if __name__ == "__main__":
    run_all_tests()
