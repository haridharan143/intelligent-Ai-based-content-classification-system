import psutil
import time
import threading
import logging
import os
import re
import json
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter
import socket
import requests
import win32file
import win32con
import win32api
import win32security
import win32event
import win32pipe
import winerror
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import sys
import win32process
import win32gui
import pywintypes
import signal
import atexit
import hashlib
import sqlite3
import urllib.parse
from pathlib import Path
import uuid
import cryptography.fernet

class CMDStyler:
    """Stylish CMD animations and visual effects"""
    
    # ANSI color codes for Windows CMD
    COLORS = {
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'class': '\033[93m',
        'BLUE': '\033[94m',
        'MAGENTA': '\033[95m',
        'CYAN': '\033[96m',
        'WHITE': '\033[97m',
        'RESET': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
        'BLINK': '\033[5m'
    }
    
    @staticmethod
    def clear_screen():
        """Clear the console screen"""
        os.system('cls')
    
    @staticmethod
    def print_colored(text, color='WHITE', style=''):
        """Print colored text to console"""
        color_code = CMDStyler.COLORS.get(color, CMDStyler.COLORS['WHITE'])
        style_code = CMDStyler.COLORS.get(style, '')
        print(f"{color_code}{style_code}{text}{CMDStyler.COLORS['RESET']}")
    
    @staticmethod
    def print_alert(message, level='INFO'):
        """Print alert with color coding"""
        level_colors = {
            'INFO': 'CYAN',
            'MEDIUM': 'YELLOW',
            'HIGH': 'RED',
            'CRITICAL': 'RED',
            'LOW': 'GREEN'
        }
        color = level_colors.get(level, 'CYAN')
        CMDStyler.print_colored(f"⚠️  {message}", color)
    
    @staticmethod
    def print_status(status_items):
        """Print status items in a formatted way"""
        for item in status_items:
            label, value, color = item
            CMDStyler.print_colored(f"   {label}: {value}", color)
    
    @staticmethod
    def print_separator(char='═', length=60, color='CYAN'):
        """Print a separator line"""
        CMDStyler.print_colored(char * length, color)
    
    @staticmethod
    def print_header(title, color='CYAN'):
        """Print a formatted header"""
        CMDStyler.print_separator('═', len(title) + 4, color)
        CMDStyler.print_colored(f"  {title} ", color, 'BOLD')
        CMDStyler.print_separator('═', len(title) + 4, color)
    
    @staticmethod
    def typewriter_effect(text, delay=0.05):
        """Create typewriter effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  # New line after typewriter effect
    
    @staticmethod
    def loading_bar(percentage, width=50, color='CYAN'):
        """Display a loading bar"""
        filled_width = int(width * percentage / 100)
        bar = '█' * filled_width + '░' * (width - filled_width)
        CMDStyler.print_colored(f"\r[{percentage}%] {bar}", color)
    
    @staticmethod
    def matrix_rain(rows=20, columns=80, color='GREEN'):
        """Create matrix rain effect"""
        import random
        chars = '01'
        for _ in range(rows):
            line = ''.join(random.choice(chars) for _ in range(columns))
            CMDStyler.print_colored(line, color)
            time.sleep(0.1)
    
    @staticmethod
    def dna_helix(length=20, color='CYAN'):
        """Create DNA helix animation"""
        import random
        import string
        dna_chars = 'ATCG'
        
        for i in range(length):
            line = []
            for j in range(length):
                if i == j:
                    line.append(random.choice(dna_chars))
                else:
                    line.append(' ')
            CMDStyler.print_colored(''.join(line), color)
            time.sleep(0.1)
    
    @staticmethod
    def pulsing_logo(text, cycles=5, color='CYAN'):
        """Create pulsing logo effect"""
        for i in range(cycles):
            CMDStyler.print_colored(f"\r{text}", color, 'BOLD')
            time.sleep(0.5)
            CMDStyler.print_colored(f"\r{' ' * len(text)}", color)
            time.sleep(0.5)
    
    @staticmethod
    def scanning_effect(duration=3, color='CYAN'):
        """Create scanning effect"""
        import random
        chars = '/-\\|/-'
        for _ in range(duration * 10):
            CMDStyler.print_colored(f"\r{random.choice(chars)}", color)
            time.sleep(0.1)
    
    @staticmethod
    def intro_animation():
        """Complete intro animation sequence"""
        CMDStyler.clear_screen()
        
        # Typewriter effect for title
        CMDStyler.typewriter("🚀 INITIALIZING AI SYSTEM MONITOR", 0.05)
        time.sleep(0.5)
        
        # Loading bars
        CMDStyler.print_colored("📡 Loading AI Detection Modules...", 'CYAN')
        CMDStyler.loading_bar(30, 50, 'CYAN')
        time.sleep(0.5)
        
        CMDStyler.print_colored("🤖 Initializing AI Intelligence...", 'MAGENTA')
        CMDStyler.loading_bar(60, 50, 'MAGENTA')
        time.sleep(0.5)
        
        CMDStyler.print_colored("🔐 Activating Security Protocols...", 'RED')
        CMDStyler.loading_bar(90, 50, 'RED')
        time.sleep(0.5)
        
        CMDStyler.print_colored("🌐 Global AI Network Monitoring...", 'BLUE')
        CMDStyler.loading_bar(100, 50, 'BLUE')
        time.sleep(0.5)
        
        # Matrix rain effect
        CMDStyler.print_colored("\n🔍 Matrix-style AI Detection Active", 'GREEN')
        CMDStyler.matrix_rain(10, 60, 'GREEN')
        time.sleep(1)
        
        # DNA helix
        CMDStyler.print_colored("\n🧬 AI DNA Sequencing Active", 'CYAN')
        CMDStyler.dna_helix(15, 'CYAN')
        time.sleep(1)
        
        # Pulsing logo
        CMDStyler.pulsing_logo("🤖 AI MONITOR", 3, 'CYAN')
        
        # Final status
        CMDStyler.print_header("🚀 AI SYSTEM MONITOR READY", 'GREEN')
        CMDStyler.print_separator('═', 60, 'GREEN')
        
        time.sleep(1)

class AIEventLogger:
    """Enhanced AI Event Logger with Excel reporting"""
    
    def __init__(self, config):
        self.config = config
        self.workbook = None
        self.sheet = None
        self.row_counter = 1
        self.lock = threading.Lock()
        self.log_file = config.log_file
        self.db_file = config.db_file
        
    def initialize_workbook(self):
        """Initialize Excel workbook"""
        try:
            self.workbook = Workbook()
            self.sheet = self.workbook.active
            self.sheet.title = "AI_Monitor_Log"
            
            # Create headers
            headers = [
                "Timestamp", "Event Type", "Description", "Process Name", "File URL", "Risk Level",
                "AI Category", "AI Tool Name", "Detection Method", "Confidence Score", "User Session ID", 
                "Geographic Location", "Action Type", "Historical Reference ID", "Compliance Flag"
            ]
            
            for col, header in enumerate(headers, 1):
                cell = self.sheet.cell(row=1, column=col, value=header)
                cell.font = Font(bold=True)
                cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
                cell.font = Font(color="FFFFFF", bold=True)
            
            # Adjust column widths
            for col in range(1, len(headers) + 1):
                self.sheet.column_dimensions[get_column_letter(col)].width = 20
            
            self.row_counter = 2
            
        except Exception as e:
            print(f"Error initializing workbook: {e}")
    
    def save_workbook(self):
        """Save Excel workbook"""
        try:
            if self.workbook:
                self.workbook.save(self.log_file)
        except Exception as e:
            print(f"Error saving workbook: {e}")
    
    def log_event(self, event_type, description, process_name="", file_url="", risk_level="Medium"):
        with self.lock:
            try:
                if not self.workbook or not self.sheet:
                    self.initialize_workbook()
                    if not self.workbook or not self.sheet:
                        return
                
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                self.sheet.cell(row=self.row_counter, column=1, value=timestamp)
                self.sheet.cell(row=self.row_counter, column=2, value=event_type)
                self.sheet.cell(row=self.row_counter, column=3, value=description)
                self.sheet.cell(row=self.row_counter, column=4, value=process_name)
                self.sheet.cell(row=self.row_counter, column=5, value=file_url)
                self.sheet.cell(row=self.row_counter, column=6, value=risk_level)
                
                # Enhanced color coding based on risk level
                if risk_level.lower() == "critical":
                    self.sheet.cell(row=self.row_counter, column=6).fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
                    self.sheet.cell(row=self.row_counter, column=6).font = Font(color="FFFFFF", bold=True)
                elif risk_level.lower() == "high":
                    self.sheet.cell(row=self.row_counter, column=6).fill = PatternFill(start_color="FF6B6B", end_color="FF6B6B", fill_type="solid")
                    self.sheet.cell(row=self.row_counter, column=6).font = Font(color="FFFFFF")
                elif risk_level.lower() == "medium":
                    self.sheet.cell(row=self.row_counter, column=6).fill = PatternFill(start_color="FFA500", end_color="FFA500", fill_type="solid")
                else:  # Low
                    self.sheet.cell(row=self.row_counter, column=6).fill = PatternFill(start_color="90EE90", end_color="90EE90", fill_type="solid")
                
                # Add additional columns for detailed AI identification tracking
                self._add_ai_identification_columns(event_type, description, file_url, risk_level)
                
                self.row_counter += 1
                
                # Auto-adjust column widths for better readability
                self._auto_adjust_column_widths()
                
                # Save every 5 events to reduce file I/O
                if self.row_counter % 5 == 0:
                    self.save_workbook()
                
                # Enhanced user action display
                self.display_user_action(event_type, description, process_name, file_url, risk_level, timestamp)
                    
            except Exception as e:
                CMDStyler.print_alert(f"Error logging event: {e}", 'HIGH')
    
    def _add_ai_identification_columns(self, event_type, description, file_url, risk_level):
        """Add detailed AI identification columns to Excel"""
        try:
            # Column 7: AI Category
            ai_category = self._extract_ai_category(event_type, description, file_url)
            self.sheet.cell(row=self.row_counter, column=7, value=ai_category)
            
            # Column 8: AI Tool/Service Name
            ai_tool_name = self._extract_ai_tool_name(event_type, description, file_url)
            self.sheet.cell(row=self.row_counter, column=8, value=ai_tool_name)
            
            # Column 9: Detection Method
            detection_method = self._extract_detection_method(event_type, description, file_url)
            self.sheet.cell(row=self.row_counter, column=9, value=detection_method)
            
            # Column 10: Confidence Score (1-100)
            confidence_score = self._calculate_confidence_score(event_type, description, file_url, risk_level)
            self.sheet.cell(row=self.row_counter, column=10, value=confidence_score)
            
            # Column 11: User Session ID
            session_id = self._get_user_session_id()
            self.sheet.cell(row=self.row_counter, column=11, value=session_id)
            
            # Column 12: Geographic Location (if detectable)
            location = self._detect_geographic_context(file_url, description)
            self.sheet.cell(row=self.row_counter, column=12, value=location)
            
            # Column 13: Action Type
            action_type = self._classify_action_type(event_type, description)
            self.sheet.cell(row=self.row_counter, column=13, value=action_type)
            
            # Column 14: Historical Reference ID
            ref_id = self._generate_historical_reference_id()
            self.sheet.cell(row=self.row_counter, column=14, value=ref_id)
            
            # Column 15: Compliance Flag
            compliance_flag = self._check_compliance_flag(event_type, description, risk_level)
            self.sheet.cell(row=self.row_counter, column=15, value=compliance_flag)
            
        except Exception as e:
            print(f"Error adding AI identification columns: {e}")
    
    def _extract_ai_category(self, event_type, description, file_url):
        """Extract AI category from event"""
        try:
            # AI Categories mapping
            categories = {
                'LLM/Chatbot': ['chatgpt', 'claude', 'gemini', 'bard', 'llm', 'chatbot', 'conversation'],
                'Image Generation': ['midjourney', 'dall', 'stable', 'diffusion', 'image', 'art', 'design'],
                'Code Assistant': ['copilot', 'github', 'code', 'programming', 'development'],
                'Data Analytics': ['kaggle', 'colab', 'jupyter', 'pandas', 'numpy', 'analytics'],
                'Voice/Audio': ['speech', 'voice', 'audio', 'tts', 'stt', 'music'],
                'Video Generation': ['video', 'runway', 'pika', 'lumalabs', 'sora'],
                'Machine Learning': ['tensorflow', 'pytorch', 'keras', 'scikit', 'model', 'training'],
                'Productivity AI': ['notion', 'grammarly', 'canva', 'productivity', 'assistant'],
                'Research AI': ['research', 'paper', 'arxiv', 'publication', 'study'],
                'Enterprise AI': ['enterprise', 'business', 'corporate', 'professional']
            }
            
            text_to_check = (description + ' ' + file_url).lower()
            
            for category, keywords in categories.items():
                if any(keyword in text_to_check for keyword in keywords):
                    return category
            
            return 'General AI'
            
        except Exception as e:
            return 'Unknown'
    
    def _extract_ai_tool_name(self, event_type, description, file_url):
        """Extract specific AI tool name"""
        try:
            # Known AI tools mapping
            ai_tools = {
                'ChatGPT': ['chatgpt', 'chat.openai.com', 'openai'],
                'Claude': ['claude', 'claude.ai', 'anthropic'],
                'Gemini': ['gemini', 'bard', 'gemini.google.com'],
                'Copilot': ['copilot', 'github copilot'],
                'Midjourney': ['midjourney', 'midjourney.com'],
                'DALL-E': ['dall', 'dall-e', 'openai image'],
                'Stable Diffusion': ['stable', 'diffusion', 'stability.ai'],
                'HuggingFace': ['huggingface', 'huggingface.co'],
                'TensorFlow': ['tensorflow', 'tf'],
                'PyTorch': ['pytorch', 'torch'],
                'Canva': ['canva', 'canva.com'],
                'Notion': ['notion', 'notion.so'],
                'Grammarly': ['grammarly', 'grammarly.com'],
                'Character.AI': ['character', 'character.ai'],
                'Perplexity': ['perplexity', 'perplexity.ai'],
                'Replit': ['replit', 'replit.ai']
            }
            
            text_to_check = (description + ' ' + file_url).lower()
            
            for tool, patterns in ai_tools.items():
                if any(pattern in text_to_check for pattern in patterns):
                    return tool
            
            return 'Unknown AI Tool'
            
        except Exception as e:
            return 'Unknown AI Tool'
    
    def _extract_detection_method(self, event_type, description, file_url):
        """Extract detection method used"""
        try:
            if 'Browser AI Usage' in event_type:
                return 'Browser Monitoring'
            elif 'File Access' in event_type:
                return 'File System Monitoring'
            elif 'Process Activity' in event_type:
                return 'Process Monitoring'
            elif 'Network Connection' in event_type:
                return 'Network Monitoring'
            elif 'Honeypot' in event_type:
                'Honeypot Detection'
            elif 'Behavioral' in event_type:
                'Behavioral Analysis'
            elif 'Predictive' in event_type:
                'Predictive Analysis'
            elif 'Model Integrity' in event_type:
                'Model Integrity Check'
            else:
                return 'General Monitoring'
                
        except Exception as e:
            return 'Unknown Method'
    
    def _calculate_confidence_score(self, event_type, description, file_url, risk_level):
        """Calculate confidence score (1-100)"""
        try:
            base_score = 50
            
            # Adjust based on risk level
            risk_scores = {'critical': 90, 'high': 75, 'medium': 50, 'low': 25}
            base_score = risk_scores.get(risk_level.lower(), 50)
            
            # Adjust based on detection method
            if 'Browser AI Usage' in event_type:
                base_score += 10  # Browser monitoring is reliable
            elif 'File Access' in event_type:
                base_score += 15  # File access is very reliable
            elif 'Honeypot' in event_type:
                base_score += 20  # Honeypot is very reliable
            
            # Adjust based on AI tool specificity
            if 'ChatGPT' in description or 'Claude' in description:
                base_score += 15  # Well-known AI tools
            elif 'openai.com' in file_url or 'anthropic.com' in file_url:
                base_score += 20  # Official AI domains
            
            # Adjust based on description detail
            if len(description) > 50:
                base_score += 5  # Detailed descriptions are more reliable
            
            return min(100, max(1, base_score))
            
        except Exception as e:
            return 50
    
    def _get_user_session_id(self):
        """Generate or retrieve user session ID"""
        try:
            if not hasattr(self, 'session_id'):
                self.session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{secrets.token_hex(4)}"
            return self.session_id
        except Exception as e:
            return f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    def _detect_geographic_context(self, file_url, description):
        """Detect geographic context if possible"""
        try:
            # Simple geographic detection based on domains
            geo_indicators = {
                'US': ['.com', '.us', 'america', 'united states'],
                'UK': ['.co.uk', '.uk', 'britain', 'england'],
                'EU': ['.de', '.fr', '.it', '.es', '.eu'],
                'Asia': ['.jp', '.cn', '.in', '.kr', '.asia'],
                'Global': ['.ai', '.tech', '.science']
            }
            
            text_to_check = (file_url + ' ' + description).lower()
            
            for geo, indicators in geo_indicators.items():
                if any(indicator in text_to_check for indicator in indicators):
                    return geo
            
            return 'Unknown'
            
        except Exception as e:
            return 'Unknown'
    
    def _classify_action_type(self, event_type, description):
        """Classify the type of AI action"""
        try:
            if 'access' in description.lower() or 'visit' in description.lower():
                return 'Access'
            elif 'create' in description.lower() or 'generate' in description.lower():
                return 'Creation'
            elif 'modify' in description.lower() or 'edit' in description.lower():
                return 'Modification'
            elif 'download' in description.lower() or 'upload' in description.lower():
                return 'Transfer'
            elif 'login' in description.lower() or 'auth' in description.lower():
                return 'Authentication'
            elif 'error' in description.lower() or 'fail' in description.lower():
                return 'Error'
            else:
                return 'General'
                
        except Exception as e:
            return 'General'
    
    def _generate_historical_reference_id(self):
        """Generate unique historical reference ID"""
        try:
            return f"AI_REF_{datetime.now().strftime('%Y%m%d%H%M%S')}_{secrets.token_hex(6)}"
        except Exception as e:
            return f"AI_REF_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def _check_compliance_flag(self, event_type, description, risk_level):
        """Check compliance flag"""
        try:
            # Simple compliance checking
            if risk_level.lower() in ['critical', 'high']:
                return 'REVIEW_REQUIRED'
            elif 'unauthorized' in description.lower() or 'suspicious' in description.lower():
                return 'POLICY_VIOLATION'
            elif 'honeypot' in event_type.lower():
                return 'SECURITY_INCIDENT'
            else:
                return 'COMPLIANT'
                
        except Exception as e:
            return 'UNKNOWN'
    
    def _auto_adjust_column_widths(self):
        """Auto-adjust column widths for better readability"""
        try:
            # Define column widths
            column_widths = {
                1: 20,  # Timestamp
                2: 20,  # Event Type
                3: 40, # Description
                4: 20, # Process Name
                5: 50, # File URL
                6: 15, # Risk Level
                7: 20, # AI Category
                8: 25, # AI Tool Name
                9: 20, # Detection Method
                10: 15, # Confidence Score
                11: 25, # Session ID
                12: 15, # Geographic Location
                13: 15, # Action Type
                14: 25, # Historical Reference ID
                15: 20  # Compliance Flag
            }
            
            for col, width in column_widths.items():
                self.sheet.column_dimensions[get_column_letter(col)].width = width
                
        except Exception as e:
            print(f"Error adjusting column widths: {e}")
    
    def create_summary_sheet(self):
        """Create a summary sheet for AI identification statistics"""
        try:
            if not self.workbook:
                return
            
            # Remove existing summary sheet if it exists
            if 'AI_Summary' in self.workbook.sheetnames:
                del self.workbook['AI_Summary']
            
            # Create new summary sheet
            summary_sheet = self.workbook.create_sheet('AI_Summary')
            
            # Add headers
            headers = [
                'Metric', 'Count', 'Percentage', 'Last Updated'
            ]
            
            for col, header in enumerate(headers, 1):
                cell = summary_sheet.cell(row=1, column=col, value=header)
                cell.font = Font(bold=True)
                cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
                cell.font = Font(color="FFFFFF", bold=True)
            
            # Calculate statistics from main sheet
            if 'AI_Monitor_Log' in self.workbook.sheetnames:
                main_sheet = self.workbook['AI_Monitor_Log']
                
                # Count total events
                total_events = 0
                ai_events = 0
                high_risk_events = 0
                critical_events = 0
                
                for row in main_sheet.iter_rows(min_row=2, values_only=True):
                    if row[0]:  # If timestamp exists
                        total_events += 1
                        if row[1] and 'AI' in str(row[1]):
                            ai_events += 1
                        if row[5] and 'High' in str(row[5]):
                            high_risk_events += 1
                        if row[5] and 'Critical' in str(row[5]):
                            critical_events += 1
                
                # Add statistics
                stats = [
                    ('Total Events', total_events, '100%', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                    ('AI Events', ai_events, f"{(ai_events/total_events*100):.1f}%" if total_events > 0 else '0%', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                    ('High Risk Events', high_risk_events, f"{(high_risk_events/total_events*100):.1f}%" if total_events > 0 else '0%', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                    ('Critical Events', critical_events, f"{(critical_events/total_events*100):.1f}%" if total_events > 0 else '0%', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                ]
                
                for row_num, (metric, count, percentage, updated) in enumerate(stats, 2):
                    summary_sheet.cell(row=row_num, column=1, value=metric)
                    summary_sheet.cell(row=row_num, column=2, value=count)
                    summary_sheet.cell(row=row_num, column=3, value=percentage)
                    summary_sheet.cell(row=row_num, column=4, value=updated)
            
            # Auto-adjust summary sheet columns
            for col in range(1, 5):
                summary_sheet.column_dimensions[get_column_letter(col)].width = 20
            
            CMDStyler.print_alert("📊 AI Summary sheet created in Excel", 'MEDIUM')
            
        except Exception as e:
            CMDStyler.print_alert(f"Error creating summary sheet: {e}", 'HIGH')
    
    def display_user_action(self, event_type, description, process_name, file_url, risk_level, timestamp):
        """Display detailed user action with enhanced formatting"""
        try:
            # Determine action icon and color based on event type
            action_icons = {
                "File Access": "📂",
                "AI Tool Usage": "🤖",
                "Network Connection": "🌐",
                "Process Activity": "⚙️",
                "Browser Extension": "🔌",
                "Social Media AI": "📱�",
                "Honeypot Triggered": "🍯",
                "Behavioral Anomaly": "🎯",
                "Predictive Risk": "🔮",
                "Model Integrity": "🔐",
                "Zero-Trust Session": "🔑",
                "Supply Chain": "🔗"
            }
            
            icon = action_icons.get(event_type, "📋")
            
            # Format the action description
            if file_url and os.path.exists(file_url):
                file_info = f"📄 {os.path.basename(file_path)}"
                file_size = os.path.getsize(file_path)
                file_size_str = self.format_file_size(file_size)
                file_details = f"{file_info} ({file_size_str})"
            else:
                file_details = file_url or "No file"
            
            # Create action message
            action_msg = f"{icon} USER ACTION DETECTED: {description}"
            
            # Display based on risk level
            if risk_level.lower() == "critical":
                CMDStyler.print_colored(f"\n{action_msg}", 'RED', 'BOLD')
                CMDStyler.print_colored(f"   ⚠️  CRITICAL: {description}", 'RED')
                CMDStyler.print_colored(f"   👤 User: {process_name}", 'RED')
                CMDStyler.print_colored(f"   📂 File: {file_details}", 'RED')
                CMDStyler.print_colored(f"   ⏰ Time: {timestamp}", 'RED')
            elif risk_level.lower() == "high":
                CMDStyler.print_colored(f"\n{action_msg}", 'YELLOW', 'BOLD')
                CMDStyler.print_colored(f"   ⚠️  HIGH: {description}", 'YELLOW')
                CMDStyler.print_colored(f"   👤 User: {process_name}", 'YELLOW')
                CMDStyler.print_colored(f"   📂 File: {file_details}", 'YELLOW')
                CMDStyler.print_colored(f"   ⏰ Time: {timestamp}\n", 'YELLOW')
            elif risk_level.lower() == "medium":
                CMDStyler.print_colored(f"{action_msg}: {description}", 'BLUE')
                CMDStyler.print_colored(f"   👤 {process_name} → 📂 {file_details}", 'CYAN')
            else:  # Low
                CMDStyler.print_colored(f"{action_msg}: {description}", 'GREEN')
                CMDStyler.print_colored(f"   👤 {process_name} → 📂 {file_details}", 'GREEN')
            
            # Add specific AI action details
            self.add_ai_action_details(event_type, description, process_name, file_url)
            
        except Exception as e:
            print(f"Error displaying user action: {e}")
    
    def format_file_size(self, size_bytes):
        """Format file size in human readable format"""
        try:
            if size_bytes == 0:
                return "0B"
            size_names = ["B", "KB", "MB", "GB", "TB"]
            i = int(math.floor(math.log(size_bytes, 1024)))
            p = math.pow(1024, i)
            s = round(size_bytes / p, 2)
            return f"{s} {size_names[i]}"
        except:
            return f"{size_bytes} B"
    
    def add_ai_action_details(self, event_type, description, process_name, file_url):
        """Add specific details for AI-related actions"""
        try:
            if event_type == "File Access":
                if any(ai_term in description.lower() for ai_term in ['chatgpt', 'claude', 'gemini', 'copilot']):
                    CMDStyler.print_colored(f"   🤖 AI Tool File Access Detected", 'MAGENTA')
                
                if file_url and file_url.endswith(('.py', '.ipynb', '.txt', '.md')):
                    CMDStyler.print_colored(f"   💻 Code/Document File Accessed", 'BLUE')
           
            
            elif event_type == "AI Tool Usage":
                if "chatgpt" in description.lower():
                    CMDStyler.print_colored(f"   💬 ChatGPT Activity Detected", 'CYAN')
                elif "copilot" in description.lower():
                    CMDStyler.print_colored(f"   👨‍💻 GitHub Copilot Usage", 'BLUE')
                elif "midjourney" in description.lower() or "dall-e" in description.lower():
                    CMDStyler.print_colored(f"   🎨 AI Image Generation", 'MAGENTA')
            
            elif event_type == "Network Connection":
                if any(domain in description.lower() for domain in ['openai.com', 'anthropic.com', 'google.com']):
                    CMDStyler.print_colored(f"   🌐 AI Service Connection", 'YELLOW')
            
            elif event_type == "Social Media AI":
                CMDStyler.print_colored(f"   📱 Social Media AI Feature Used", 'CYAN')
            
            elif event_type == "Honeypot Triggered":
                CMDStyler.print_colored(f"   🚨 SECURITY: Unauthorized AI Tool Access Attempt", 'RED', 'BOLD')
            
            elif event_type == "Behavioral Anomaly":
                CMDStyler.print_colored(f"   🧠 Unusual User Behavior Pattern Detected", 'YELLOW')
            
            elif event_type == "Predictive Risk":
                CMDStyler.print_colored(f"   🔮 AI Risk Prediction Triggered", 'MAGENTA')
            
            elif event_type == "Model Integrity":
                CMDStyler.print_colored(f"   🔐 AI Model Security Event", 'GREEN')
            
            elif event_type == "Zero-Trust Session":
                CMDStyler.print_colored(f"   🔑 AI Access Session Management", 'BLUE')
            
            elif event_type == "Supply Chain":
                CMDStyler.print_colored(f"   🔗 AI Supply Chain Security Event", 'GREEN')
                
        except Exception as e:
            print(f"Error adding AI action details: {e}")

class FileHandleMonitor:
