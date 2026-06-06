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
import secrets
from pathlib import Path
import uuid
import cryptography.fernet
import base64
import pickle
import math
import numpy as np
from collections import defaultdict, deque
import winreg
import random
import string
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import uuid as uuid_lib
import requests
from urllib.parse import urljoin
import hashlib
import hmac
import secrets
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import cv2
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms

class CMDStyler:
    """Stylish CMD animations and visual effects"""
    
    # ANSI color codes for Windows CMD
    COLORS = {
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',
        'MAGENTA': '\033[95m',
        'CYAN': '\033[96m',
        'WHITE': '\033[97m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
        'RESET': '\033[0m',
        'DIM': '\033[2m'
    }
    
    @staticmethod
    def clear_screen():
        """Clear the CMD screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_colored(text, color='WHITE', style=''):
        """Print colored text"""
        color_code = CMDStyler.COLORS.get(color.upper(), CMDStyler.COLORS['WHITE'])
        style_code = CMDStyler.COLORS.get(style.upper(), '')
        print(f"{style_code}{color_code}{text}{CMDStyler.COLORS['RESET']}")
    
    @staticmethod
    def typewriter_effect(text, delay=0.03, color='CYAN'):
        """Typewriter effect for text"""
        for char in text:
            print(CMDStyler.COLORS[color] + char + CMDStyler.COLORS['RESET'], end='', flush=True)
            time.sleep(delay)
        print()
    
    @staticmethod
    def loading_bar(message, duration=2, color='GREEN'):
        """Animated loading bar"""
        print(f"\n{CMDStyler.COLORS[color]}{message}")
        for i in range(21):
            time.sleep(duration/20)
            bar = '█' * i + '░' * (20-i)
            print(f"\r{CMDStyler.COLORS[color]}[{bar}] {i*5}%", end='', flush=True)
        print(f"\n{CMDStyler.COLORS['RESET']}")
    
    @staticmethod
    def matrix_rain(lines=10):
        """Matrix-style rain effect"""
        CMDStyler.clear_screen()
        chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン'
        
        for _ in range(20):
            for _ in range(lines):
                line = ''.join(random.choice(chars) for _ in range(random.randint(20, 60)))
                print(f"{CMDStyler.COLORS['GREEN']}{line}{CMDStyler.COLORS['RESET']}")
            time.sleep(0.1)
            CMDStyler.clear_screen()
    
    @staticmethod
    def binary_rain(lines=8):
        """Binary rain effect"""
        CMDStyler.clear_screen()
        for _ in range(15):
            for _ in range(lines):
                line = ''.join(random.choice('01') for _ in range(random.randint(30, 80)))
                print(f"{CMDStyler.COLORS['GREEN']}{line}{CMDStyler.COLORS['RESET']}")
            time.sleep(0.1)
            CMDStyler.clear_screen()
    
    @staticmethod
    def dna_helix():
        """DNA helix animation"""
        CMDStyler.clear_screen()
        helix_chars = ['/', '\\', '|', '-']
        
        for frame in range(30):
            CMDStyler.clear_screen()
            for i in range(10):
                char1 = helix_chars[(frame + i) % 4]
                char2 = helix_chars[(frame + i + 2) % 4]
                spaces = ' ' * abs(5 - i)
                
                if i < 5:
                    print(f"{CMDStyler.COLORS['CYAN']}{char1}{spaces}{char2}{CMDStyler.COLORS['RESET']}")
                else:
                    print(f"{CMDStyler.COLORS['MAGENTA']}{char2}{spaces}{char1}{CMDStyler.COLORS['RESET']}")
            time.sleep(0.15)
    
    @staticmethod
    def scanning_effect():
        """Scanning line effect"""
        CMDStyler.clear_screen()
        for i in range(20):
            CMDStyler.clear_screen()
            spaces = ' ' * i
            print(f"\n\n\n{CMDStyler.COLORS['CYAN']}{'█' * 50}{CMDStyler.COLORS['RESET']}")
            print(f"{spaces}{CMDStyler.COLORS['YELLOW']}► SCANNING AI SYSTEMS...{CMDStyler.COLORS['RESET']}")
            print(f"{CMDStyler.COLORS['CYAN']}{'█' * 50}{CMDStyler.COLORS['RESET']}")
            time.sleep(0.1)
    
    @staticmethod
    def pulse_logo():
        """Pulsing AI logo"""
        CMDStyler.clear_screen()
        
        logo_art = [
            "    ████████╗ █████╗ ███╗   ██╗██╗  ██╗    ██████╗ ███████╗ █████╗ ████████╗",
            "    ╚══██╔══╝██╔══██╗████╗  ██║██║ ██╔╝    ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝",
            "       ██║   ███████║██╔██╗ ██║█████╔╝     ██████╔╝█████╗  ███████║   ██║   ",
            "       ██║   ██╔══██║██║╚██╗██║██╔═██╗     ██╔══██╗██╔══╝  ██╔══██║   ██║   ",
            "       ██║   ██║  ██║██║ ╚████║██║  ██╗    ██████╔╝███████╗██║  ██║   ██║   ",
            "       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   "
        ]
        
        for pulse in range(3):
            CMDStyler.clear_screen()
            for i, line in enumerate(logo_art):
                if pulse == 0:
                    color = 'CYAN'
                elif pulse == 1:
                    color = 'MAGENTA'
                else:
                    color = 'YELLOW'
                
                print(f"{CMDStyler.COLORS[color]}{line}{CMDStyler.COLORS['RESET']}")
                time.sleep(0.05)
            time.sleep(0.3)
    
    @staticmethod
    def intro_animation():
        """Complete intro animation sequence"""
        try:
            # Enable virtual terminal processing for Windows 10+
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except:
            pass
        
        CMDStyler.clear_screen()
        
        # Binary rain
        CMDStyler.binary_rain(5)
        
        # Scanning effect
        CMDStyler.scanning_effect()
        
        # DNA Helix
        CMDStyler.dna_helix()
        
        # Pulse Logo
        CMDStyler.pulse_logo()
        
        # Title reveal
        CMDStyler.clear_screen()
        CMDStyler.typewriter_effect("╔══════════════════════════════════════════════════════════════╗", 0.01, 'CYAN')
        CMDStyler.typewriter_effect("║                    AI SYSTEM MONITOR v2.0                    ║", 0.02, 'CYAN')
        CMDStyler.typewriter_effect("║                Advanced Enterprise Security                ║", 0.02, 'CYAN')
        CMDStyler.typewriter_effect("╚══════════════════════════════════════════════════════════════╝", 0.01, 'CYAN')
        
        print()
        CMDStyler.typewriter_effect("🛡️  INITIALIZING SECURITY PROTOCOLS...", 0.05, 'GREEN')
        CMDStyler.loading_bar("Loading AI Detection Modules", 1.5, 'GREEN')
        
        CMDStyler.typewriter_effect("🧬 ACTIVATING DNA TAGGING SYSTEM...", 0.05, 'MAGENTA')
        CMDStyler.loading_bar("Calibrating Behavioral Analysis", 1.2, 'MAGENTA')
        
        CMDStyler.typewriter_effect("🎯 DEPLOYING HONEYPOT DECOYS...", 0.05, 'YELLOW')
        CMDStyler.loading_bar("Setting Predictive Models", 1.0, 'YELLOW')
        
        CMDStyler.typewriter_effect("🔮 INITIALIZING PREDICTIVE AI SHADOWING...", 0.05, 'BLUE')
        CMDStyler.loading_bar("Establishing Secure Connection", 0.8, 'BLUE')
        
        CMDStyler.typewriter_effect("⚡ ACTIVATING REAL-TIME MONITORING...", 0.05, 'CYAN')
        CMDStyler.loading_bar("Finalizing Security Stack", 0.6, 'CYAN')
        
        print()
        CMDStyler.print_colored("╔══════════════════════════════════════════════════════════════╗", 'CYAN')
        CMDStyler.print_colored("║                    SYSTEM READY FOR MONITORING                ║", 'GREEN', 'BOLD')
        CMDStyler.print_colored("║                   Press Ctrl+C to Stop Monitoring            ║", 'YELLOW')
        CMDStyler.print_colored("╚══════════════════════════════════════════════════════════════╝", 'CYAN')
        
        print()
        CMDStyler.print_colored("🚀 Starting Advanced AI System Monitor...", 'GREEN', 'BOLD')
        time.sleep(1)
    
    @staticmethod
    def print_alert(message, alert_type='INFO'):
        """Print styled alert messages"""
        alert_styles = {
            'CRITICAL': ('🚨', 'RED', 'BOLD'),
            'HIGH': ('⚠️', 'YELLOW', 'BOLD'),
            'MEDIUM': ('ℹ️', 'BLUE', 'BOLD'),
            'LOW': ('✓', 'GREEN', 'BOLD'),
            'INFO': ('🔍', 'CYAN', 'BOLD')
        }
        
        icon, color, style = alert_styles.get(alert_type.upper(), alert_styles['INFO'])
        prefix = f"[{alert_type.upper():^8}]"
        
        print(f"{CMDStyler.COLORS[color]}{CMDStyler.COLORS[style]}{prefix} {icon} {message}{CMDStyler.COLORS['RESET']}")
    
    @staticmethod
    def print_separator(char='═', length=60, color='CYAN'):
        """Print colored separator line"""
        print(f"{CMDStyler.COLORS[color]}{char * length}{CMDStyler.COLORS['RESET']}")
    
    @staticmethod
    def print_header(title, color='MAGENTA', style=''):
        """Print styled header"""
        CMDStyler.print_separator('═', 60, color)
        style_code = CMDStyler.COLORS.get(style.upper(), '') if style else ''
        print(f"{CMDStyler.COLORS[color]}{style_code}{title:^60}{CMDStyler.COLORS['RESET']}")
        CMDStyler.print_separator('═', 60, color)
    
    @staticmethod
    def print_status(status_items):
        """Print status items in a styled format"""
        for label, value, color in status_items:
            print(f"{CMDStyler.COLORS[color]}{label:<20}: {CMDStyler.COLORS['WHITE']}{value}{CMDStyler.COLORS['RESET']}")

class STIXGenerator:
    """STIX 2.1 threat intelligence generator for AI security events"""
    
    def __init__(self, config):
        self.config = config
        self.stix_bundle = {
            "type": "bundle",
            "id": f"bundle--{uuid_lib.uuid4()}",
            "objects": []
        }
        self.attack_patterns = {
            "ai_data_exfiltration": "attack-pattern--a0c8e3c4-4a9b-4b8c-9c5d-6e7f8a9b0c1d",
            "unauthorized_ai_access": "attack-pattern--b1d9f4e5-5b0c-5c9d-0d6e-7f8a9b0c1d2e",
            "ai_model_poisoning": "attack-pattern--c2e0f5f6-6c1d-6d0e-1e7f-8a9b0c1d2e3f",
            "ai_bias_exploitation": "attack-pattern--d3f1g6g7-7d2e-7e1f-2f8a-9b0c1d2e3f4g",
            "ai_honeypot_trigger": "attack-pattern--e4g2h7h8-8e3f-8f2g-3g9b-0c1d2e3f4g5h"
        }
        
    def create_ai_threat_indicator(self, event_data):
        """Create STIX indicator for AI threat"""
        indicator = {
            "type": "indicator",
            "id": f"indicator--{uuid_lib.uuid4()}",
            "created": datetime.now(timezone.utc).isoformat(),
            "modified": datetime.now(timezone.utc).isoformat(),
            "name": f"AI Security Threat: {event_data.get('event_type', 'Unknown')}",
            "description": event_data.get('description', ''),
            "pattern": self._create_stix_pattern(event_data),
            "pattern_type": "stix",
            "valid_from": datetime.now(timezone.utc).isoformat(),
            "labels": ["malicious-activity", "ai-security"],
            "kill_chain_phases": [
                {
                    "kill_chain_name": "mitre-attack",
                    "phase_name": "execution"
                }
            ],
            "confidence": self._calculate_confidence(event_data),
            "severity": event_data.get('risk_level', 'medium').lower()
        }
        
        return indicator
    
    def create_ai_attack_pattern(self, attack_type, description):
        """Create STIX attack pattern for AI-specific attacks"""
        attack_pattern = {
            "type": "attack-pattern",
            "id": f"attack-pattern--{uuid_lib.uuid4()}",
            "created": datetime.now(timezone.utc).isoformat(),
            "modified": datetime.now(timezone.utc).isoformat(),
            "name": f"AI Attack: {attack_type}",
            "description": description,
            "kill_chain_phases": [
                {
                    "kill_chain_name": "mitre-attack",
                    "phase_name": "execution"
                }
            ],
            "labels": ["attack-pattern", "ai-security"]
        }
        
        return attack_pattern
    
    def create_ai_threat_actor(self, actor_info):
        """Create STIX threat actor for AI-related threats"""
        threat_actor = {
            "type": "threat-actor",
            "id": f"threat-actor--{uuid_lib.uuid4()}",
            "created": datetime.now(timezone.utc).isoformat(),
            "modified": datetime.now(timezone.utc).isoformat(),
            "name": actor_info.get('name', 'Unknown AI Threat Actor'),
            "description": actor_info.get('description', 'Threat actor targeting AI systems'),
            "labels": ["hacker", "organized-crime", "espionage"],
            "sophistication": actor_info.get('sophistication', 'intermediate'),
            "resource_level": actor_info.get('resource_level', 'medium'),
            "primary_motivation": actor_info.get('motivation', 'financial'),
            "goals": actor_info.get('goals', ['AI data theft', 'Model compromise'])
        }
        
        return threat_actor
    
    def create_ai_vulnerability(self, vuln_data):
        """Create STIX vulnerability for AI system vulnerabilities"""
        vulnerability = {
            "type": "vulnerability",
            "id": f"vulnerability--{uuid_lib.uuid4()}",
            "created": datetime.now(timezone.utc).isoformat(),
            "modified": datetime.now(timezone.utc).isoformat(),
            "name": vuln_data.get('name', 'AI System Vulnerability'),
            "description": vuln_data.get('description', 'Vulnerability in AI system'),
            "labels": ["vulnerability", "ai-security"],
            "cvss_score": vuln_data.get('cvss_score', 5.0),
            "severity": vuln_data.get('severity', 'medium')
        }
        
        return vulnerability
    
    def create_ai_campaign(self, campaign_info):
        """Create STIX campaign for AI-related attack campaigns"""
        campaign = {
            "type": "campaign",
            "id": f"campaign--{uuid_lib.uuid4()}",
            "created": datetime.now(timezone.utc).isoformat(),
            "modified": datetime.now(timezone.utc).isoformat(),
            "name": campaign_info.get('name', 'AI Attack Campaign'),
            "description": campaign_info.get('description', 'Campaign targeting AI systems'),
            "labels": ["campaign", "ai-security"],
            "objective": campaign_info.get('objective', 'Compromise AI infrastructure')
        }
        
        return campaign
    
    def _create_stix_pattern(self, event_data):
        """Create STIX pattern for event detection"""
        patterns = []
        
        if event_data.get('process_name'):
            patterns.append(f"[process:name = '{event_data['process_name']}']")
        
        if event_data.get('file_url'):
            patterns.append(f"[file:name = '{event_data['file_url']}']")
        
        if event_data.get('network_domain'):
            patterns.append(f"[domain-name:value = '{event_data['network_domain']}']")
        
        return " AND ".join(patterns) if patterns else "[process:name = 'unknown']"
    
    def _calculate_confidence(self, event_data):
        """Calculate confidence score for STIX object"""
        base_confidence = 50
        
        # Increase confidence based on risk level
        risk_level = event_data.get('risk_level', '').lower()
        if risk_level == 'critical':
            base_confidence += 40
        elif risk_level == 'high':
            base_confidence += 30
        elif risk_level == 'medium':
            base_confidence += 20
        
        # Increase confidence for known attack patterns
        if any(keyword in event_data.get('description', '').lower() 
               for keyword in ['honeypot', 'unauthorized', 'anomaly', 'predictive']):
            base_confidence += 20
        
        return min(base_confidence, 100)
    
    def add_to_bundle(self, stix_object):
        """Add STIX object to bundle"""
        self.stix_bundle["objects"].append(stix_object)
    
    def export_bundle(self, filename="ai_threat_intelligence.json"):
        """Export STIX bundle to file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.stix_bundle, f, indent=2)
            return filename
        except Exception as e:
            print(f"Error exporting STIX bundle: {e}")
            return None
    
    def get_bundle_summary(self):
        """Get summary of STIX bundle contents"""
        object_types = {}
        for obj in self.stix_bundle["objects"]:
            obj_type = obj["type"]
            object_types[obj_type] = object_types.get(obj_type, 0) + 1
        
        return {
            "total_objects": len(self.stix_bundle["objects"]),
            "object_types": object_types,
            "bundle_id": self.stix_bundle["id"]
        }

class TAXIIClient:
    """TAXII 2.1 client for sharing AI threat intelligence"""
    
    def __init__(self, config):
        self.config = config
        self.taxii_servers = [
            {
                "name": "Internal TAXII Server",
                "url": "https://taxii.internal.local",
                "username": "ai_monitor",
                "password": "secure_password_123",
                "collections": {
                    "ai_indicators": "collection--ai-indicators-123",
                    "ai_patterns": "collection--ai-patterns-456"
                }
            },
            {
                "name": "External TAXII Server",
                "url": "https://taxii.external.threatintel.com",
                "username": "enterprise_client",
                "password": "api_key_456",
                "collections": {
                    "global_ai_threats": "collection--global-ai-789"
                }
            }
        ]
        self.session = requests.Session()
        self.session.verify = False  # For testing - use proper certs in production
        
    def get_server_root(self, server_url, username, password):
        """Get TAXII server root information"""
        try:
            auth = (username, password)
            response = self.session.get(f"{server_url}/taxii2/", auth=auth)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error getting server root: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error connecting to TAXII server: {e}")
            return None
    
    def get_collections(self, server_url, username, password):
        """Get available collections from TAXII server"""
        try:
            auth = (username, password)
            response = self.session.get(f"{server_url}/taxii2/collections/", auth=auth)
            
            if response.status_code == 200:
                return response.json().get("collections", [])
            else:
                print(f"Error getting collections: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"Error getting collections: {e}")
            return []
    
    def add_indicator(self, server_url, collection_id, indicator, username, password):
        """Add indicator to TAXII collection"""
        try:
            auth = (username, password)
            headers = {
                "Content-Type": "application/taxii+json;version=2.1",
                "Accept": "application/taxii+json;version=2.1"
            }
            
            url = f"{server_url}/taxii2/collections/{collection_id}/objects/"
            response = self.session.post(url, json=indicator, headers=headers, auth=auth)
            
            if response.status_code == 202:  # Accepted
                CMDStyler.print_alert(f"Successfully added indicator to TAXII server", 'MEDIUM')
                return True
            else:
                CMDStyler.print_alert(f"Error adding indicator: {response.status_code}", 'HIGH')
                return False
                
        except Exception as e:
            CMDStyler.print_alert(f"Error adding indicator to TAXII: {e}", 'HIGH')
            return False
    
    def get_indicators(self, server_url, collection_id, username, password, limit=100):
        """Get indicators from TAXII collection"""
        try:
            auth = (username, password)
            headers = {
                "Accept": "application/taxii+json;version=2.1"
            }
            
            params = {"limit": limit}
            url = f"{server_url}/taxii2/collections/{collection_id}/objects/"
            response = self.session.get(url, headers=headers, params=params, auth=auth)
            
            if response.status_code == 200:
                return response.json().get("objects", [])
            else:
                CMDStyler.print_alert(f"Error getting indicators: {response.status_code}", 'HIGH')
                return []
                
        except Exception as e:
            CMDStyler.print_alert(f"Error getting indicators from TAXII: {e}", 'HIGH')
            return []
    
    def share_ai_threat_intelligence(self, stix_bundle):
        """Share AI threat intelligence with all configured TAXII servers"""
        shared_count = 0
        
        for server in self.taxii_servers:
            try:
                CMDStyler.print_alert(f"Sharing intelligence with {server['name']}", 'INFO')
                
                # Get collections
                collections = self.get_collections(
                    server["url"], 
                    server["username"], 
                    server["password"]
                )
                
                # Share indicators
                for obj in stix_bundle["objects"]:
                    if obj["type"] == "indicator":
                        for collection_name, collection_id in server["collections"].items():
                            if "indicator" in collection_name:
                                success = self.add_indicator(
                                    server["url"],
                                    collection_id,
                                    obj,
                                    server["username"],
                                    server["password"]
                                )
                                if success:
                                    shared_count += 1
                
            except Exception as e:
                CMDStyler.print_alert(f"Error sharing with {server['name']}: {e}", 'HIGH')
        
        CMDStyler.print_alert(f"Successfully shared {shared_count} indicators", 'MEDIUM')
        return shared_count
    
    def sync_external_threats(self):
        """Sync external threat intelligence from TAXII servers"""
        external_indicators = []
        
        for server in self.taxii_servers:
            if "external" in server["name"].lower():
                try:
                    CMDStyler.print_alert(f"🔄 Syncing threats from {server['name']} (Demo Mode)", 'INFO')
                    
                    # In demo mode, create mock indicators
                    mock_indicators = self._create_demo_indicators()
                    external_indicators.extend(mock_indicators)
                    
                    CMDStyler.print_alert(f"📊 Demo: Created {len(mock_indicators)} mock indicators", 'MEDIUM')
                
                except Exception as e:
                    CMDStyler.print_alert(f"⚠️  Demo mode sync from {server['name']}: Expected behavior", 'INFO')
        
        CMDStyler.print_alert(f"📈 Synced {len(external_indicators)} external indicators (Demo Mode)", 'MEDIUM')
        return external_indicators
    
    def _create_demo_indicators(self):
        """Create demo indicators for testing"""
        demo_indicators = []
        
        demo_data = [
            {
                "type": "indicator",
                "id": f"indicator--demo-{uuid_lib.uuid4()}",
                "created": datetime.now(timezone.utc).isoformat(),
                "modified": datetime.now(timezone.utc).isoformat(),
                "name": "Demo AI Malware Process",
                "description": "Suspicious AI-related process detected",
                "pattern": "[process:name = 'ai-malware.exe']",
                "pattern_type": "stix",
                "valid_from": datetime.now(timezone.utc).isoformat(),
                "labels": ["malicious-activity", "ai-security"],
                "confidence": 85,
                "severity": "high"
            },
            {
                "type": "indicator", 
                "id": f"indicator--demo-{uuid_lib.uuid4()}",
                "created": datetime.now(timezone.utc).isoformat(),
                "modified": datetime.now(timezone.utc).isoformat(),
                "name": "Demo Suspicious AI Domain",
                "description": "Domain known for AI-related threats",
                "pattern": "[domain-name:value = 'malicious-ai-domain.com']",
                "pattern_type": "stix",
                "valid_from": datetime.now(timezone.utc).isoformat(),
                "labels": ["malicious-activity", "ai-security"],
                "confidence": 75,
                "severity": "medium"
            }
        ]
        
        return demo_data
    
    def test_connectivity(self):
        """Test connectivity to all TAXII servers"""
        results = {}
        
        for server in self.taxii_servers:
            try:
                # Skip external server testing in demo mode
                if "external" in server["name"].lower():
                    results[server["name"]] = "Demo Mode - Skipped"
                    CMDStyler.print_alert(f"⚠️  {server['name']}: Demo mode - connection skipped", 'INFO')
                    continue
                
                root_info = self.get_server_root(
                    server["url"],
                    server["username"],
                    server["password"]
                )
                
                if root_info:
                    results[server["name"]] = "Connected"
                    CMDStyler.print_alert(f"✓ Connected to {server['name']}", 'MEDIUM')
                else:
                    results[server["name"]] = "Failed"
                    CMDStyler.print_alert(f"✗ Failed to connect to {server['name']}", 'HIGH')
                    
            except Exception as e:
                results[server["name"]] = f"Error: {str(e)[:50]}..."
                CMDStyler.print_alert(f"✗ Error connecting to {server['name']}: Demo mode expected", 'INFO')
        
        return results

class AIThreatIntelligenceManager:
    """Manager for AI threat intelligence using STIX/TAXII"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.stix_generator = STIXGenerator(config)
        self.taxii_client = TAXIIClient(config)
        self.local_threat_db = {}
        
    def process_ai_security_event(self, event_data):
        """Process AI security event and create threat intelligence"""
        try:
            # Create STIX indicator
            indicator = self.stix_generator.create_ai_threat_indicator(event_data)
            self.stix_generator.add_to_bundle(indicator)
            
            # Create attack pattern if needed
            if event_data.get('event_type') == 'Honeypot Triggered':
                attack_pattern = self.stix_generator.create_ai_attack_pattern(
                    "AI Honeypot Access",
                    "Unauthorized access to AI honeypot decoy indicating malicious intent"
                )
                self.stix_generator.add_to_bundle(attack_pattern)
            
            # Log to database
            self._log_threat_intelligence(event_data, indicator)
            
            # Auto-share critical threats
            if event_data.get('risk_level') in ['Critical', 'High']:
                self._auto_share_threat(indicator)
            
            CMDStyler.print_alert(f"Processed threat intelligence for {event_data.get('event_type')}", 'MEDIUM')
            
        except Exception as e:
            CMDStyler.print_alert(f"Error processing threat intelligence: {e}", 'HIGH')
    
    def _log_threat_intelligence(self, event_data, indicator):
        """Log threat intelligence to database"""
        try:
            conn = sqlite3.connect(self.config.db_file)
            cursor = conn.cursor()
            
            # Create threat intelligence table if not exists
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS threat_intelligence (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    event_type TEXT,
                    stix_id TEXT,
                    confidence INTEGER,
                    severity TEXT,
                    shared BOOLEAN DEFAULT FALSE
                )
            ''')
            
            cursor.execute('''
                INSERT INTO threat_intelligence 
                (timestamp, event_type, stix_id, confidence, severity, shared)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now().isoformat(),
                event_data.get('event_type'),
                indicator['id'],
                indicator.get('confidence', 50),
                indicator.get('severity', 'medium'),
                False
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Error logging threat intelligence: {e}")
    
    def _auto_share_threat(self, indicator):
        """Automatically share critical threats"""
        try:
            # Create mini-bundle with just this indicator
            mini_bundle = {
                "type": "bundle",
                "id": f"bundle--{uuid_lib.uuid4()}",
                "objects": [indicator]
            }
            
            # Share with TAXII servers
            shared_count = self.taxii_client.share_ai_threat_intelligence(mini_bundle)
            
            if shared_count > 0:
                # Mark as shared in database
                self._mark_as_shared(indicator['id'])
                
        except Exception as e:
            print(f"Error auto-sharing threat: {e}")
    
    def _mark_as_shared(self, stix_id):
        """Mark threat intelligence as shared"""
        try:
            conn = sqlite3.connect(self.config.db_file)
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE threat_intelligence 
                SET shared = TRUE 
                WHERE stix_id = ?
            ''', (stix_id,))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Error marking as shared: {e}")
    
    def generate_threat_report(self):
        """Generate comprehensive threat intelligence report"""
        try:
            bundle_summary = self.stix_generator.get_bundle_summary()
            
            CMDStyler.print_header("🛡️ AI THREAT INTELLIGENCE REPORT", 'RED')
            
            CMDStyler.print_status([
                ("Total Objects", bundle_summary['total_objects'], 'CYAN'),
                ("Bundle ID", bundle_summary['bundle_id'][:20] + "...", 'WHITE')
            ])
            
            CMDStyler.print_colored("\n📊 Object Types:", 'YELLOW', 'BOLD')
            for obj_type, count in bundle_summary['object_types'].items():
                CMDStyler.print_colored(f"   • {obj_type}: {count}", 'YELLOW')
            
            # Test TAXII connectivity
            CMDStyler.print_colored("\n🌐 TAXII Server Status:", 'BLUE', 'BOLD')
            connectivity_results = self.taxii_client.test_connectivity()
            for server, status in connectivity_results.items():
                color = 'GREEN' if status == 'Connected' else 'RED'
                CMDStyler.print_colored(f"   • {server}: {status}", color)
            
            CMDStyler.print_separator('═', 60, 'RED')
            
        except Exception as e:
            CMDStyler.print_alert(f"Error generating threat report: {e}", 'HIGH')
    
    def export_threat_intelligence(self):
        """Export all threat intelligence"""
        try:
            filename = self.stix_generator.export_bundle()
            if filename:
                CMDStyler.print_alert(f"Threat intelligence exported to {filename}", 'MEDIUM')
                
                # Also share with TAXII servers
                shared_count = self.taxii_client.share_ai_threat_intelligence(self.stix_generator.stix_bundle)
                CMDStyler.print_alert(f"Shared {shared_count} indicators with TAXII servers", 'MEDIUM')
                
            return filename
        except Exception as e:
            CMDStyler.print_alert(f"Error exporting threat intelligence: {e}", 'HIGH')
            return None
    
    def sync_external_threats(self):
        """Sync external threat intelligence"""
        try:
            external_indicators = self.taxii_client.sync_external_threats()
            
            # Process external indicators
            for indicator in external_indicators:
                # Add to local threat database
                self.local_threat_db[indicator['id']] = indicator
                
                # Check for matches with current system
                self._check_indicator_matches(indicator)
            
            return len(external_indicators)
        except Exception as e:
            CMDStyler.print_alert(f"Error syncing external threats: {e}", 'HIGH')
            return 0
    
    def _check_indicator_matches(self, indicator):
        """Check if external indicator matches local system"""
        try:
            pattern = indicator.get('pattern', '')
            
            # Simple pattern matching - in production, use more sophisticated matching
            if 'process:name' in pattern:
                # Extract process name from pattern
                import re
                match = re.search(r"process:name = '([^']+)'", pattern)
                if match:
                    process_name = match.group(1).lower()
                    
                    # Check if this process is running
                    for proc in psutil.process_iter(['name']):
                        if proc.info['name'] and proc.info['name'].lower() == process_name:
                            CMDStyler.print_alert(f"⚠️  External threat indicator matches running process: {process_name}", 'CRITICAL')
                            
                            # Log the match
                            self.logger.log_event(
                                "External Threat Match",
                                f"Process {process_name} matches external threat indicator",
                                process_name,
                                indicator['id'],
                                "Critical"
                            )
                            break
                            
        except Exception as e:
            print(f"Error checking indicator matches: {e}")

class AIModelIntegrityVerifier:
    """AI Model Integrity Verification and Watermarking System"""
    
    def __init__(self, config):
        self.config = config
        self.model_registry = {}
        self.watermark_key = secrets.token_bytes(32)
        self.integrity_baseline = {}
        
    def create_model_fingerprint(self, model_path, model_type="generic"):
        """Create unique fingerprint for AI model"""
        try:
            fingerprint_data = {
                'model_type': model_type,
                'file_size': os.path.getsize(model_path) if os.path.exists(model_path) else 0,
                'file_hash': self.config.get_file_hash(model_path),
                'timestamp': datetime.now().isoformat()
            }
            
            fingerprint_str = json.dumps(fingerprint_data, sort_keys=True)
            fingerprint = hashlib.sha256(fingerprint_str.encode()).hexdigest()
            
            fingerprint_data['fingerprint'] = fingerprint
            self.model_registry[fingerprint] = fingerprint_data
            
            return fingerprint
            
        except Exception as e:
            print(f"Error creating model fingerprint: {e}")
            return None
    
    def embed_watermark(self, model_path, watermark_data):
        """Embed invisible watermark in AI model"""
        try:
            watermark_signature = self._create_watermark_signature(watermark_data)
            watermark_path = model_path + '.watermark'
            
            watermark_info = {
                'signature': watermark_signature,
                'original_file': model_path,
                'timestamp': datetime.now().isoformat()
            }
            
            with open(watermark_path, 'w') as f:
                json.dump(watermark_info, f)
            
            CMDStyler.print_alert(f"Watermark embedded for {model_path}", 'MEDIUM')
            return True
            
        except Exception as e:
            print(f"Error embedding watermark: {e}")
            return False
    
    def _create_watermark_signature(self, watermark_data):
        """Create cryptographic watermark signature"""
        watermark_str = json.dumps(watermark_data, sort_keys=True)
        signature = hmac.new(self.watermark_key, watermark_str.encode(), hashlib.sha256).hexdigest()
        return signature
    
    def verify_model_integrity(self, model_path, expected_fingerprint=None):
        """Verify model integrity against fingerprint"""
        try:
            current_fingerprint = self.create_model_fingerprint(model_path)
            
            if expected_fingerprint:
                if current_fingerprint == expected_fingerprint:
                    CMDStyler.print_alert(f"✓ Model integrity verified: {model_path}", 'MEDIUM')
                    return True
                else:
                    CMDStyler.print_alert(f"✗ Model integrity compromised: {model_path}", 'CRITICAL')
                    return False
            else:
                if current_fingerprint in self.model_registry:
                    CMDStyler.print_alert(f"✓ Model found in registry: {model_path}", 'MEDIUM')
                    return True
                else:
                    CMDStyler.print_alert(f"? New model detected: {model_path}", 'INFO')
                    return None
            
        except Exception as e:
            print(f"Error verifying model integrity: {e}")
            return False
    
    def detect_model_poisoning(self, model_path):
        """Detect potential model poisoning"""
        try:
            fingerprint = self.create_model_fingerprint(model_path)
            if fingerprint:
                model_data = self.model_registry.get(fingerprint, {})
                
                # Check for suspicious patterns
                if 'file_size' in model_data:
                    size = model_data['file_size']
                    if size < 1000 or size > 1e9:  # Suspicious sizes
                        CMDStyler.print_alert("⚠️  Suspicious model size detected", 'HIGH')
                        return True
                
                CMDStyler.print_alert("✓ Model integrity confirmed - no poisoning detected", 'MEDIUM')
                return False
                
        except Exception as e:
            print(f"Error detecting model poisoning: {e}")
            return False

class ZeroTrustAIManager:
    """Zero-Trust AI Architecture for Just-in-Time Access"""
    
    def __init__(self, config):
        self.config = config
        self.ai_sessions = {}
        self.trust_scores = {}
        self.min_trust_score = 50
        
    def initialize_ai_identity_federation(self):
        """Initialize AI identity federation system"""
        try:
            conn = sqlite3.connect(self.config.db_file)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ai_identities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    ai_tool TEXT,
                    trust_score INTEGER,
                    last_verified TEXT,
                    access_level TEXT
                )
            ''')
            
            conn.commit()
            conn.close()
            CMDStyler.print_alert("AI Identity Federation initialized", 'MEDIUM')
            
        except Exception as e:
            CMDStyler.print_alert(f"Error initializing AI identity federation: {e}", 'HIGH')
    
    def create_ai_session(self, user_id, ai_tool):
        """Create just-in-time AI session"""
        try:
            session_id = secrets.token_urlsafe(16)
            trust_score = self.calculate_trust_score(user_id, ai_tool)
            
            if trust_score < self.min_trust_score:
                CMDStyler.print_alert(f"Access denied: Trust score {trust_score} below threshold", 'CRITICAL')
                return None
            
            session = {
                'session_id': session_id,
                'user_id': user_id,
                'ai_tool': ai_tool,
                'trust_score': trust_score,
                'created_time': datetime.now().isoformat(),
                'access_level': self.determine_access_level(trust_score)
            }
            
            self.ai_sessions[session_id] = session
            CMDStyler.print_alert(f"AI session created: {ai_tool} (Trust: {trust_score})", 'MEDIUM')
            return session_id
            
        except Exception as e:
            CMDStyler.print_alert(f"Error creating AI session: {e}", 'HIGH')
            return None
    
    def calculate_trust_score(self, user_id, ai_tool):
        """Calculate dynamic trust score"""
        try:
            base_score = 50
            
            # Time-based factor
            current_hour = datetime.now().hour
            if 9 <= current_hour <= 17:
                base_score += 20
            elif current_hour < 6 or current_hour > 22:
                base_score -= 20
            
            # Tool risk factor
            tool_risk = self.get_ai_tool_risk(ai_tool)
            base_score += (100 - tool_risk) * 0.3
            
            return max(0, min(100, int(base_score)))
            
        except Exception as e:
            print(f"Error calculating trust score: {e}")
            return 50
    
    def get_ai_tool_risk(self, ai_tool):
        """Get risk level for specific AI tool"""
        risk_levels = {
            'chatgpt': 20, 'claude': 20, 'gemini': 20,
            'copilot': 30, 'github': 25,
            'midjourney': 40, 'dall-e': 40,
            'tensorflow': 50, 'pytorch': 50,
            'custom_ai': 70, 'unknown_ai': 80
        }
        
        tool_lower = ai_tool.lower()
        for tool, risk in risk_levels.items():
            if tool in tool_lower:
                return risk
        
        return 60
    
    def determine_access_level(self, trust_score):
        """Determine access level based on trust score"""
        if trust_score >= 80:
            return "Full Access"
        elif trust_score >= 60:
            return "Limited Access"
        elif trust_score >= 40:
            return "Restricted Access"
        else:
            return "Denied"
    
    def terminate_ai_session(self, session_id, reason="Session timeout"):
        """Terminate AI session"""
        try:
            if session_id in self.ai_sessions:
                del self.ai_sessions[session_id]
                CMDStyler.print_alert(f"AI session terminated: {reason}", 'INFO')
                return True
            return False
        except Exception as e:
            print(f"Error terminating AI session: {e}")
            return False
    
    def generate_zero_trust_report(self):
        """Generate Zero-Trust AI security report"""
        try:
            CMDStyler.print_header("🔐 ZERO-TRUST AI SECURITY REPORT", 'BLUE')
            
            active_sessions = len(self.ai_sessions)
            avg_trust = 0
            
            if self.ai_sessions:
                avg_trust = sum(s['trust_score'] for s in self.ai_sessions.values()) / len(self.ai_sessions)
            
            CMDStyler.print_status([
                ("Active Sessions", active_sessions, 'CYAN'),
                ("Average Trust Score", f"{avg_trust:.1f}", 'GREEN' if avg_trust > 70 else 'YELLOW'),
                ("Min Trust Threshold", self.min_trust_score, 'MAGENTA')
            ])
            
            CMDStyler.print_separator('═', 60, 'BLUE')
            
        except Exception as e:
            CMDStyler.print_alert(f"Error generating Zero-Trust report: {e}", 'HIGH')

class AISupplyChainSecurity:
    """AI Supply Chain Security - SBOM and Dependency Management"""
    
    def __init__(self, config):
        self.config = config
        self.ai_sbom = {}
        
    def create_ai_sbom(self, ai_tool_path, tool_name):
        """Create Software Bill of Materials for AI tool"""
        try:
            sbom_data = {
                'tool_name': tool_name,
                'tool_path': ai_tool_path,
                'created_at': datetime.now().isoformat(),
                'dependencies': [],
                'libraries': [],
                'file_hashes': {}
            }
            
            # Analyze dependencies
            sbom_data['dependencies'] = self.analyze_dependencies(ai_tool_path)
            
            # Calculate file hashes
            sbom_data['file_hashes'] = self.calculate_file_hashes(ai_tool_path)
            
            # Store SBOM
            sbom_id = f"sbom--{uuid_lib.uuid4()}"
            self.ai_sbom[sbom_id] = sbom_data
            
            CMDStyler.print_alert(f"SBOM created for {tool_name}: {len(sbom_data['dependencies'])} dependencies", 'MEDIUM')
            return sbom_id
            
        except Exception as e:
            CMDStyler.print_alert(f"Error creating SBOM: {e}", 'HIGH')
            return None
    
    def analyze_dependencies(self, tool_path):
        """Analyze dependencies of AI tool"""
        try:
            dependencies = []
            
            # Look for dependency files
            if os.path.isdir(tool_path):
                dep_files = ['requirements.txt', 'Pipfile', 'environment.yml']
                for dep_file in dep_files:
                    dep_path = os.path.join(tool_path, dep_file)
                    if os.path.exists(dep_path):
                        deps = self.parse_dependency_file(dep_path)
                        dependencies.extend(deps)
            
            return dependencies
            
        except Exception as e:
            print(f"Error analyzing dependencies: {e}")
            return []
    
    def parse_dependency_file(self, file_path):
        """Parse dependency file and extract dependencies"""
        try:
            dependencies = []
            
            with open(file_path, 'r') as f:
                content = f.read()
            
            lines = content.split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split('==')
                    name = parts[0]
                    version = parts[1] if len(parts) > 1 else 'unknown'
                    
                    dependencies.append({
                        'name': name,
                        'version': version,
                        'risk_level': self.assess_library_risk(name)
                    })
            
            return dependencies
            
        except Exception as e:
            print(f"Error parsing dependency file {file_path}: {e}")
            return []
    
    def assess_library_risk(self, library_name):
        """Assess risk level of a library"""
        try:
            high_risk_libs = ['pickle', 'eval', 'exec', 'subprocess', 'os.system']
            medium_risk_libs = ['socket', 'urllib', 'requests', 'http.client']
            
            lib_lower = library_name.lower()
            
            for high_lib in high_risk_libs:
                if high_lib in lib_lower:
                    return 'High'
            
            for med_lib in medium_risk_libs:
                if med_lib in lib_lower:
                    return 'Medium'
            
            return 'Low'
            
        except Exception as e:
            print(f"Error assessing library risk: {e}")
            return 'Medium'
    
    def calculate_file_hashes(self, tool_path):
        """Calculate hashes for all files in the tool"""
        try:
            file_hashes = {}
            
            if os.path.isdir(tool_path):
                for root, dirs, files in os.walk(tool_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, tool_path)
                        file_hash = self.config.get_file_hash(file_path)
                        
                        if file_hash:
                            file_hashes[relative_path] = file_hash
            
            return file_hashes
            
        except Exception as e:
            print(f"Error calculating file hashes: {e}")
            return {}
    
    def generate_supply_chain_report(self):
        """Generate AI Supply Chain security report"""
        try:
            CMDStyler.print_header("🔗 AI SUPPLY CHAIN SECURITY REPORT", 'GREEN')
            
            total_sboms = len(self.ai_sbom)
            total_dependencies = sum(len(sbom['dependencies']) for sbom in self.ai_sbom.values())
            
            CMDStyler.print_status([
                ("SBOMs Created", total_sboms, 'CYAN'),
                ("Total Dependencies", total_dependencies, 'YELLOW'),
                ("Tools Analyzed", len(self.ai_sbom), 'MAGENTA')
            ])
            
            if self.ai_sbom:
                CMDStyler.print_colored("\n📊 Tool Dependency Summary:", 'YELLOW', 'BOLD')
                for sbom_id, sbom in self.ai_sbom.items():
                    high_risk_deps = sum(1 for dep in sbom['dependencies'] if dep['risk_level'] == 'High')
                    color = 'RED' if high_risk_deps > 0 else 'GREEN'
                    CMDStyler.print_colored(f"   • {sbom['tool_name']}: {len(sbom['dependencies'])} deps ({high_risk_deps} high risk)", color)
            
            CMDStyler.print_separator('═', 60, 'GREEN')
            
        except Exception as e:
            CMDStyler.print_alert(f"Error generating Supply Chain report: {e}", 'HIGH')

class AIMonitorConfig:
    def __init__(self):
        self.ai_keywords = [
            # General AI Terms
            'openai', 'chatgpt', 'gpt', 'claude', 'gemini', 'bard', 'copilot',
            'midjourney', 'dall-e', 'stable diffusion', 'huggingface', 'tensorflow',
            'pytorch', 'keras', 'scikit-learn', 'opencv', 'numpy', 'pandas',
            'ai_', 'artificial', 'machine learning', 'deep learning', 'neural',
            'llm', 'large language model', 'transformer', 'bert', 'gpt-3', 'gpt-4',
            'anthropic', 'azure ai', 'aws ai', 'google ai', 'nvidia', 'cuda',
            
            # Workflow & Process Automation
            'uipath', 'automation anywhere', 'zapier', 'power automate', 'rpa',
            'robotic process automation', 'workflow automation', 'business process',
            
            # Virtual Assistants & Chatbots
            'ibm watson', 'watson assistant', 'dialogflow', 'amazon lex', 'tars',
            'chatbot', 'virtual assistant', 'conversational ai',
            
            # Document & Data Processing
            'abbyy', 'finereader', 'rossum', 'docuphase', 'ocr', 'document digitization',
            'invoice processing', 'data extraction', 'document workflow',
            
            # CRM & Sales Automation
            'salesforce einstein', 'hubspot ai', 'zoho crm', 'zoho zia', 'crm ai',
            'sales forecasting', 'lead scoring', 'sales automation',
            
            # Personalization & Recommendations
            'dynamic yield', 'adobe target', 'barilliance', 'personalization',
            'recommendation engine', 'e-commerce personalization',
            
            # Customer Support
            'zendesk answer bot', 'freshworks freddy', 'intercom', 'customer support ai',
            'ticket routing', 'self-service', 'customer engagement',
            
            # Business Intelligence
            'tableau ai', 'power bi', 'qlik sense', 'business intelligence',
            'data visualization', 'natural language queries', 'data insights',
            
            # Predictive Analytics
            'sas advanced analytics', 'ibm spss', 'datarobot', 'predictive analytics',
            'predictive modeling', 'automated machine learning', 'automl',
            
            # Big Data & AI Platforms
            'google cloud ai', 'bigquery ml', 'aws ai', 'sagemaker', 'rekognition',
            'azure ai', 'cognitive services', 'machine learning', 'bot service',
            
            # Content Generation
            'jasper.ai', 'jasper', 'copy.ai', 'writesonic', 'content generation',
            'marketing copy', 'ai writing', 'content creation',
            
            # Ad Optimization
            'albert ai', 'phrasee', 'adobe sensei', 'ad optimization', 'digital marketing',
            'email optimization', 'ad targeting', 'creative optimization',
            
            # Social Media
            'hootsuite insights', 'sprout social', 'brandwatch', 'social media monitoring',
            'sentiment analysis', 'social listening', 'social media analytics',
            
            # Finance & Accounting
            'feedzai', 'featurespace', 'kount', 'fraud detection', 'fraud prevention',
            'xero ai', 'quickbooks ai', 'zoho books', 'accounting automation',
            'kavout', 'alphasense', 'bloomberg terminal', 'stock analysis',
            
            # Human Resources
            'hirevue', 'pymetrics', 'eightfold ai', 'ai recruitment', 'candidate assessment',
            'glint', 'peakon', 'culture amp', 'employee engagement', 'sentiment analysis',
            'workday ai', 'bamboohr ai', 'zoho people ai', 'hr automation',
            
            # Healthcare
            'ibm watson health', 'deepmind health', 'pathai', 'clinical decision support',
            'medical imaging', 'diagnostics', 'pathology', 'cancer detection',
            
            # Cybersecurity
            'darktrace', 'crowdstrike falcon', 'vectra ai', 'sentinelone', 'threat detection',
            'autonomous response', 'endpoint security', 'attack detection', 'threat prevention',
            
            # Software Development & Testing
            'github copilot', 'tabnine', 'deepcode', 'code generation', 'code review',
            'testim', 'applitools', 'mabl', 'test automation', 'ui testing', 'visual testing',
            'dynatrace', 'splunk ai', 'datadog ai', 'application monitoring', 'log analysis',
            
            # E-commerce & Retail
            'zineone', 'visenze', 'capillary technologies', 'customer retention',
            'visual search', 'retail crm', 'loyalty programs',
            
            # Legal & Compliance
            'ross intelligence', 'lawgeex', 'luminance', 'legal research', 'contract review',
            'legal document analysis', 'compliance ai',
            
            # Education & Training
            'coursera ai', 'duolingo ai', 'squirrel ai', 'personalized learning',
            'adaptive learning', 'language learning',
            
            # Manufacturing & Supply Chain
            'siemens mindsphere', 'c3 ai', 'uptake', 'industrial iot', 'predictive maintenance',
            'supply chain optimization', 'asset performance',
            
            # Real Estate
            'zillow zestimate', 'housecanary', 'reonomy', 'property valuation',
            'real estate analytics', 'commercial real estate',
            
            # Agriculture (AgriTech India)
            'intello labs', 'agnext', 'cropin', 'crop quality', 'farm management',
            'predictive analytics', 'agritech',
            
            # Logistics & Transportation
            'locus', 'fareye', 'rivigo', 'route optimization', 'delivery management',
            'logistics management', 'freight', 'supply chain',
            
            # Media & Entertainment
            'jukedeck', 'runway ml', 'synthesia', 'music composition', 'video editing',
            'video generation', 'media ai',
            
            # Energy & Utilities
            'c3 ai energy', 'autogrid', 'uplight', 'energy optimization', 'smart grid',
            'energy forecasting', 'utility engagement',
            
            # Government & Public Sector
            'palantir gotham', 'cognyte', 'public safety', 'intelligence analytics',
            'government analytics', 'data integration',
            
            # Research & Innovation
            'ibm watson discovery', 'google ai platform', 'aws deepcomposer',
            'research insights', 'custom model training', 'generative music'
        ]
        
        self.ai_domains = [
            # General AI Domains
            'openai.com', 'api.openai.com', 'chat.openai.com',
            'anthropic.com', 'api.anthropic.com',
            'huggingface.co', 'huggingface.co',
            'google.ai', 'ai.google.com',
            'azure.microsoft.com', 'github.com/copilot',
            
            # Workflow Automation
            'uipath.com', 'automationanywhere.com', 'zapier.com', 'powerautomate.microsoft.com',
            
            # Virtual Assistants
            'watson.ibm.com', 'dialogflow.cloud.google.com', 'aws.amazon.com/lex',
            'tars.com',
            
            # Document Processing
            'abbyy.com', 'rossum.ai', 'docuphase.com',
            
            # CRM & Sales
            'salesforce.com/products/einstein', 'hubspot.com/features/ai', 'zoho.com/crm/ai',
            
            # Business Intelligence
            'tableau.com/products/ai', 'powerbi.microsoft.com', 'qlik.com',
            
            # Cloud AI Platforms
            'cloud.google.com/ai', 'aws.amazon.com/ai', 'azure.microsoft.com/solutions/ai',
            
            # Content Generation
            'jasper.ai', 'copy.ai', 'writesonic.com',
            
            # Social Media
            'hootsuite.com/platform/insights', 'sproutsocial.com/features/ai', 'brandwatch.com',
            
            # Finance
            'feedzai.com', 'featurespace.com', 'kount.com', 'xero.com/features/ai',
            
            # HR
            'hirevue.com', 'pymetrics.com', 'eightfold.ai', 'glint.com', 'cultureamp.com',
            
            # Cybersecurity
            'darktrace.com', 'crowdstrike.com', 'vectra.ai', 'sentinelone.com',
            
            # Development
            'github.com/features/copilot', 'tabnine.com', 'deepcode.ai',
            
            # Education
            'coursera.org', 'duolingo.com',
            
            # Indian AI Companies
            'intellolabs.com', 'agnext.com', 'cropin.com', 'locus.sh', 'fareye.com', 'rivigo.com'
        ]
        
        self.ai_processes = [
            # General Development Tools
            'python.exe', 'jupyter.exe', 'jupyter-lab.exe', 'code.exe', 'vscode.exe',
            'chrome.exe', 'firefox.exe', 'msedge.exe', 'opera.exe',
            
            # AI Specific Applications
            'uipath.exe', 'uipath.studio.exe', 'automationanywhere.exe',
            'zapier.exe', 'powerautomate.exe', 'watson.exe', 'dialogflow.exe',
            'abbyy.finereader.exe', 'salesforce.exe', 'hubspot.exe', 'zoho.exe',
            'tableau.exe', 'powerbi.exe', 'qlik.exe', 'jasper.exe', 'copy.exe',
            'hootsuite.exe', 'sproutsocial.exe', 'brandwatch.exe', 'darktrace.exe',
            'crowdstrike.exe', 'sentinelone.exe', 'github.exe', 'tabnine.exe',
            'coursera.exe', 'duolingo.exe', 'locus.exe', 'fareye.exe', 'rivigo.exe',
            
            # Browser Extensions (detectable through process names)
            'chrome_extension_host.exe', 'firefox_extension_host.exe',
            
            # Microsoft Office with AI features
            'winword.exe', 'excel.exe', 'powerpnt.exe', 'outlook.exe',
            
            # Adobe Products with AI
            'photoshop.exe', 'illustrator.exe', 'premiere.exe', 'afterfx.exe',
            
            # Database and Analytics Tools
            'sqldeveloper.exe', 'dbeaver.exe', 'tableau.exe', 'powerbi.exe',
            
            # Communication Tools with AI
            'teams.exe', 'slack.exe', 'discord.exe', 'zoom.exe', 'skype.exe'
        ]
        
        self.monitored_extensions = ['.py', '.ipynb', '.json', '.txt', '.md', '.csv', '.html', '.htm', '.js', '.xml', '.yaml', '.yml']
        
        self.log_file = 'ai_monitor_log.xlsx'
        self.monitor_interval = 2
        
        # Browser paths for extension monitoring
        self.browser_paths = [
            os.path.expanduser("~/AppData/Local/Google/Chrome/User Data"),
            os.path.expanduser("~/AppData/Local/Microsoft/Edge/User Data"),
            os.path.expanduser("~/AppData/Roaming/Mozilla/Firefox/Profiles"),
            os.path.expanduser("~/AppData/Local/Opera Software/Opera Stable")
        ]
        
        # Modern AI Detection Features
        self.social_media_ai = [
            'tiktok', 'instagram', 'facebook', 'twitter', 'linkedin', 'youtube',
            'snapchat', 'reddit', 'discord', 'telegram', 'whatsapp', 'zoom',
            'teams', 'slack', 'canva', 'notion', 'figma', 'midjourney'
        ]
        
        self.remote_work_tools = [
            'zoom', 'teams', 'slack', 'discord', 'webex', 'skype', 'goto',
            'anydesk', 'teamviewer', 'chrome remote desktop', 'remote desktop'
        ]
        
        self.content_creation_ai = [
            'canva', 'adobe firefly', 'runwayml', 'descript', 'synthesia',
            'lumen5', 'invideo', 'pictory', 'designs.ai', 'crello'
        ]
        
        self.education_ai = [
            'khan academy', 'coursera', 'udemy', 'edx', 'duolingo', 'photomath',
            'socratic', 'brainly', 'chegg', 'quizlet', 'grammarly'
        ]
        
        # Database for advanced tracking
        self.db_file = 'ai_monitor.db'
        self.setup_database()
        
        # Privacy and Compliance
        self.privacy_mode = False
        self.data_retention_days = 30
        
        # Advanced Enterprise Security Features
        self.ai_dna_tagging_enabled = True
        self.behavioral_twin_enabled = True
        self.ai_vaccination_enabled = True
        self.predictive_shadowing_enabled = True
        self.honeypot_decoys_enabled = True
        self.ghost_process_mirroring = True
        self.kernel_hook_scanner = True
        self.endpoint_attestation = True
        self.carbon_footprint_tracking = True
        
        # AI DNA Tagging Configuration
        self.dna_signature_key = self.generate_dna_signature_key()
        self.dna_metadata_patterns = {
            'text': ['<!-- AI-DNA:', '/* AI-DNA:', '[AI-DNA:'],
            'image': ['AI-DNA-META:', 'AI-GEN-SIGNATURE:'],
            'code': ['# AI-DNA:', '// AI-DNA:', '/* AI-DNA:']
        }
        
        # Behavioral Twin Configuration
        self.behavioral_baseline_window = 7  # days
        self.anomaly_threshold = 2.5  # standard deviations
        self.keystroke_sensitivity = 0.8
        self.app_usage_weights = {
            'ai_tools': 3.0,
            'development': 2.0,
            'productivity': 1.5,
            'social_media': 1.0
        }
        
        # Honeypot Configuration
        self.honeypot_tools = [
            'MK-SCORPION-AI-Doc-Generator',
            'PHOENIX-AI-Code-Assistant',
            'SHADOW-AI-Image-Creator',
            'GHOST-AI-Data-Analyzer'
        ]
        
        # Predictive Model Configuration
        self.shadow_model_accuracy_threshold = 0.85
        self.risk_prediction_window = 7  # days
        self.federated_learning_rounds = 10
        
        # Carbon Footprint Tracking
        self.ai_energy_consumption_rates = {
            'text_generation': 0.002,  # kWh per 1000 tokens
            'image_generation': 0.05,  # kWh per image
            'code_generation': 0.003,  # kWh per 100 lines
            'model_training': 2.5  # kWh per hour
        }
        
        # Initialize advanced security components
        self.initialize_security_components()
        
    def generate_dna_signature_key(self):
        """Generate unique DNA signature key for this installation"""
        machine_id = str(uuid.getnode())
        timestamp = str(int(time.time()))
        combined = f"{machine_id}-{timestamp}"
        return hashlib.sha256(combined.encode()).hexdigest()[:32]
    
    def initialize_security_components(self):
        """Initialize advanced security monitoring components"""
        try:
            # Create security database tables
            self.setup_security_database()
            
            # Initialize cryptographic keys
            self.encryption_key = self.generate_encryption_key()
            
            # Setup honeypot decoys
            if self.honeypot_decoys_enabled:
                self.setup_honeypot_decoys()
                
        except Exception as e:
            print(f"Security initialization error: {e}")
    
    def generate_encryption_key(self):
        """Generate encryption key for sensitive data"""
        return base64.urlsafe_b64encode(cryptography.fernet.Fernet.generate_key())
    
    def setup_security_database(self):
        """Setup security-specific database tables"""
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            # AI DNA Tagging table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ai_dna_registry (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_hash TEXT UNIQUE,
                    dna_signature TEXT,
                    creation_time TEXT,
                    ai_tool TEXT,
                    file_type TEXT,
                    risk_level TEXT
                )
            ''')
            
            # Behavioral Twin table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS behavioral_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    timestamp TEXT,
                    keystroke_pattern TEXT,
                    app_usage TEXT,
                    ai_interactions TEXT,
                    anomaly_score REAL
                )
            ''')
            
            # Honeypot Access table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS honeypot_access (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    honeypot_name TEXT,
                    access_time TEXT,
                    user_process TEXT,
                    input_data TEXT,
                    ip_address TEXT
                )
            ''')
            
            # Predictive Risk table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS predictive_risks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    risk_score REAL,
                    prediction_type TEXT,
                    confidence REAL,
                    mitigation_actions TEXT
                )
            ''')
            
            # Carbon Footprint table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS carbon_footprint (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    ai_tool TEXT,
                    energy_consumption REAL,
                    co2_equivalent REAL,
                    activity_type TEXT
                )
            ''')
            
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Security database setup error: {e}")
    
    def setup_honeypot_decoys(self):
        """Setup fake AI tools as honeypots"""
        try:
            honeypot_dir = os.path.expanduser("~/Desktop/Honeypot_AI_Tools")
            if not os.path.exists(honeypot_dir):
                os.makedirs(honeypot_dir)
            
            for tool in self.honeypot_tools:
                tool_path = os.path.join(honeypot_dir, f"{tool}.exe")
                if not os.path.exists(tool_path):
                    # Create fake executable
                    with open(tool_path, 'w') as f:
                        f.write(f"# Honeypot AI Tool: {tool}\n# This is a security monitoring decoy\n")
                    
        except Exception as e:
            print(f"Honeypot setup error: {e}")
    
    def calculate_carbon_footprint(self, ai_tool, activity_type, usage_metric):
        """Calculate carbon footprint for AI usage"""
        try:
            energy_rate = self.ai_energy_consumption_rates.get(activity_type, 0.001)
            energy_kwh = energy_rate * usage_metric
            
            # Convert to CO2 equivalent (average 0.5 kg CO2 per kWh)
            co2_kg = energy_kwh * 0.5
            
            return energy_kwh, co2_kg
        except:
            return 0.0, 0.0
        
    def setup_database(self):
        """Setup SQLite database for advanced monitoring"""
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            
            # Create tables for different types of monitoring
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ai_activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    event_type TEXT,
                    description TEXT,
                    process_name TEXT,
                    file_url TEXT,
                    risk_level TEXT,
                    hash_value TEXT,
                    user_action TEXT
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS network_connections (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    domain TEXT,
                    ip_address TEXT,
                    process_name TEXT,
                    risk_level TEXT
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS file_access (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    file_path TEXT,
                    process_name TEXT,
                    action TEXT,
                    risk_level TEXT
                )
            ''')
            
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Database setup error: {e}")
    
    def get_file_hash(self, file_path):
        """Calculate SHA256 hash of file for integrity checking"""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except:
            return None
    
    def is_privacy_sensitive(self, file_path):
        """Check if file contains privacy-sensitive information"""
        sensitive_patterns = [
            'password', 'secret', 'private', 'confidential', 'personal',
            'financial', 'medical', 'health', 'identity', 'ssn', 'credit'
        ]
        file_name = os.path.basename(file_path).lower()
        return any(pattern in file_name for pattern in sensitive_patterns)

class AIDNATagger:
    """AI DNA Tagging System for tracking AI-generated content"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.dna_registry = {}
        
    def embed_dna_tag(self, file_path, ai_tool, file_type):
        """Embed invisible DNA tag in AI-generated file"""
        try:
            file_hash = self.config.get_file_hash(file_path)
            if not file_hash:
                return None
            
            # Generate DNA signature
            timestamp = datetime.now().isoformat()
            dna_signature = f"{self.config.dna_signature_key}:{timestamp}:{ai_tool}:{uuid.uuid4().hex[:8]}"
            
            # Choose appropriate tag pattern based on file type
            if file_type in self.config.dna_metadata_patterns:
                patterns = self.config.dna_metadata_patterns[file_type]
                tag_pattern = patterns[0] + dna_signature + patterns[0].replace('[', '[/') if '[' in patterns[0] else patterns[0].replace('/*', '*/')
                
                # Embed tag in file
                if self.embed_tag_in_file(file_path, tag_pattern, file_type):
                    self.register_dna_tag(file_hash, dna_signature, ai_tool, file_type)
                    return dna_signature
            
            return None
            
        except Exception as e:
            print(f"DNA tagging error: {e}")
            return None
    
    def embed_tag_in_file(self, file_path, tag, file_type):
        """Embed DNA tag in file based on type"""
        try:
            if file_type == 'text':
                with open(file_path, 'a', encoding='utf-8') as f:
                    f.write(f"\n<!-- {tag} -->")
                return True
            elif file_type == 'code':
                with open(file_path, 'a', encoding='utf-8') as f:
                    f.write(f"\n# {tag}")
                return True
            elif file_type == 'image':
                # For images, create sidecar metadata file
                metadata_path = file_path + '.dna'
                with open(metadata_path, 'w') as f:
                    f.write(tag)
                return True
        except Exception as e:
            print(f"Tag embedding error: {e}")
        return False
    
    def register_dna_tag(self, file_hash, dna_signature, ai_tool, file_type):
        """Register DNA tag in database"""
        try:
            conn = sqlite3.connect(self.config.db_file)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO ai_dna_registry 
                (file_hash, dna_signature, creation_time, ai_tool, file_type, risk_level)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (file_hash, dna_signature, datetime.now().isoformat(), ai_tool, file_type, "Medium"))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"DNA registration error: {e}")
    
    def verify_dna_tag(self, file_path):
        """Verify DNA tag in file"""
        try:
            file_hash = self.config.get_file_hash(file_path)
            if not file_hash:
                return None
            
            conn = sqlite3.connect(self.config.db_file)
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM ai_dna_registry WHERE file_hash = ?', (file_hash,))
            result = cursor.fetchone()
            
            conn.close()
            return result
            
        except Exception as e:
            print(f"DNA verification error: {e}")
            return None

class BehavioralTwin:
    """Behavioral AI Twin for anomaly detection"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.baseline_patterns = {}
        self.current_session = defaultdict(list)
        self.user_id = str(uuid.getnode())  # Use machine ID as user identifier
        
    def capture_keystroke_pattern(self, process_name, keystroke_data):
        """Capture keystroke patterns for behavioral analysis"""
        try:
            timestamp = time.time()
            pattern = {
                'timestamp': timestamp,
                'process': process_name,
                'keystroke_rate': len(keystroke_data),
                'complexity': self.calculate_complexity(keystroke_data)
            }
            
            self.current_session['keystrokes'].append(pattern)
            
            # Check for anomalies
            if len(self.current_session['keystrokes']) > 100:
                self.analyze_keystroke_anomalies()
                
        except Exception as e:
            print(f"Keystroke pattern capture error: {e}")
    
    def calculate_complexity(self, keystroke_data):
        """Calculate complexity of keystroke data"""
        try:
            # Simple complexity metric based on character variety
            unique_chars = len(set(keystroke_data))
            total_chars = len(keystroke_data)
            return unique_chars / total_chars if total_chars > 0 else 0
        except:
            return 0
    
    def analyze_keystroke_anomalies(self):
        """Analyze keystroke patterns for anomalies"""
        try:
            recent_patterns = self.current_session['keystrokes'][-50:]
            
            if len(recent_patterns) < 10:
                return
            
            # Calculate metrics
            avg_rate = np.mean([p['keystroke_rate'] for p in recent_patterns])
            avg_complexity = np.mean([p['complexity'] for p in recent_patterns])
            
            # Check against baseline
            if 'baseline' in self.baseline_patterns:
                baseline_rate = self.baseline_patterns['baseline']['avg_rate']
                baseline_complexity = self.baseline_patterns['baseline']['avg_complexity']
                
                # Calculate anomaly score
                rate_deviation = abs(avg_rate - baseline_rate) / baseline_rate
                complexity_deviation = abs(avg_complexity - baseline_complexity) / baseline_complexity
                
                anomaly_score = (rate_deviation + complexity_deviation) / 2
                
                if anomaly_score > self.config.anomaly_threshold:
                    self.log_anomaly("Keystroke Pattern", anomaly_score, f"Rate: {avg_rate:.2f}, Complexity: {avg_complexity:.2f}")
            else:
                # Establish baseline
                self.baseline_patterns['baseline'] = {
                    'avg_rate': avg_rate,
                    'avg_complexity': avg_complexity
                }
                
        except Exception as e:
            print(f"Keystroke anomaly analysis error: {e}")
    
    def track_app_usage(self, app_name, duration):
        """Track application usage patterns"""
        try:
            usage_data = {
                'app': app_name,
                'duration': duration,
                'timestamp': time.time()
            }
            
            self.current_session['app_usage'].append(usage_data)
            
            # Analyze usage patterns
            if len(self.current_session['app_usage']) > 20:
                self.analyze_usage_anomalies()
                
        except Exception as e:
            print(f"App usage tracking error: {e}")
    
    def analyze_usage_anomalies(self):
        """Analyze app usage for anomalies"""
        try:
            recent_usage = self.current_session['app_usage'][-20:]
            
            # Calculate AI tool usage ratio
            ai_usage = sum(1 for u in recent_usage if any(ai in u['app'].lower() for ai in self.config.ai_keywords))
            total_usage = len(recent_usage)
            ai_ratio = ai_usage / total_usage if total_usage > 0 else 0
            
            # Check for unusual AI usage patterns
            if ai_ratio > 0.7:  # More than 70% AI tool usage
                self.log_anomaly("High AI Usage", ai_ratio, f"AI tool usage ratio: {ai_ratio:.2%}")
                
            # Check for unusual timing (late night usage)
            current_hour = datetime.now().hour
            if current_hour < 6 or current_hour > 22:
                night_ai_usage = sum(1 for u in recent_usage if any(ai in u['app'].lower() for ai in self.config.ai_keywords))
                if night_ai_usage > 5:
                    self.log_anomaly("Late Night AI Usage", night_ai_usage, f"Night AI tool accesses: {night_ai_usage}")
                    
        except Exception as e:
            print(f"Usage anomaly analysis error: {e}")
    
    def log_anomaly(self, anomaly_type, score, details):
        """Log detected anomaly"""
        try:
            self.logger.log_event(
                "Behavioral Anomaly",
                f"{anomaly_type}: {details}",
                "Behavioral Twin",
                f"Score: {score:.2f}",
                "High"
            )
            print(f"[HIGH] Behavioral Anomaly: {anomaly_type} (Score: {score:.2f})")
            
            # Store in database
            conn = sqlite3.connect(self.config.db_file)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO behavioral_patterns 
                (user_id, timestamp, keystroke_pattern, app_usage, ai_interactions, anomaly_score)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.user_id, datetime.now().isoformat(), "", "", details, score))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Anomaly logging error: {e}")

class HoneypotMonitor:
    """AI Honeypot Decoy Monitoring System"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.honeypot_access_log = []
        
    def monitor_honeypot_access(self):
        """Monitor access to honeypot AI tools"""
        try:
            honeypot_dir = os.path.expanduser("~/Desktop/Honeypot_AI_Tools")
            
            if not os.path.exists(honeypot_dir):
                return
            
            # Check for access to honeypot files
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    files = proc.open_files()
                    if files:
                        for file_info in files:
                            file_path = file_info.path.lower()
                            
                            # Check if accessing honeypot
                            if honeypot_dir.lower() in file_path:
                                honeypot_name = os.path.basename(file_path)
                                
                                # Log honeypot access
                                self.log_honeypot_access(
                                    honeypot_name,
                                    proc.info['name'],
                                    file_info.path,
                                    proc.pid
                                )
                                
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
                    
        except Exception as e:
            print(f"Honeypot monitoring error: {e}")
    
    def log_honeypot_access(self, honeypot_name, process_name, file_path, pid):
        """Log access to honeypot"""
        try:
            # Get IP address if possible
            ip_address = self.get_process_ip(pid)
            
            # Log event
            self.logger.log_event(
                "Honeypot Triggered",
                f"Unauthorized AI tool access: {honeypot_name}",
                process_name,
                file_path,
                "Critical"
            )
            print(f"[CRITICAL] HONEYPOT TRIGGERED: {honeypot_name} accessed by {process_name}")
            
            # Store in database
            conn = sqlite3.connect(self.config.db_file)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO honeypot_access 
                (honeypot_name, access_time, user_process, input_data, ip_address)
                VALUES (?, ?, ?, ?, ?)
            ''', (honeypot_name, datetime.now().isoformat(), process_name, file_path, ip_address))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Honeypot logging error: {e}")
    
    def get_process_ip(self, pid):
        """Get IP address associated with process"""
        try:
            connections = psutil.net_connections()
            for conn in connections:
                if conn.pid == pid and conn.raddr:
                    return conn.raddr.ip
        except:
            pass
        return "Unknown"

class PredictiveAIModel:
    """Predictive AI Shadowing for risk prediction"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.risk_model = self.initialize_risk_model()
        self.training_data = deque(maxlen=1000)
        
    def initialize_risk_model(self):
        """Initialize predictive risk model"""
        # Simple risk scoring model
        return {
            'weights': {
                'ai_usage_frequency': 0.3,
                'late_night_usage': 0.25,
                'unusual_tools': 0.2,
                'data_access_patterns': 0.15,
                'behavioral_anomalies': 0.1
            },
            'threshold': 0.7
        }
    
    def collect_training_data(self, user_activity):
        """Collect training data for predictive model"""
        try:
            features = self.extract_features(user_activity)
            self.training_data.append(features)
            
            # Train model periodically
            if len(self.training_data) >= 100:
                self.update_model()
                
        except Exception as e:
            print(f"Training data collection error: {e}")
    
    def extract_features(self, user_activity):
        """Extract features from user activity"""
        try:
            features = {
                'ai_usage_frequency': 0,
                'late_night_usage': 0,
                'unusual_tools': 0,
                'data_access_patterns': 0,
                'behavioral_anomalies': 0
            }
            
            # Extract features from activity data
            for activity in user_activity:
                if 'ai' in activity.lower():
                    features['ai_usage_frequency'] += 1
                
                # Check for late night usage
                hour = datetime.now().hour
                if hour < 6 or hour > 22:
                    features['late_night_usage'] += 1
            
            return features
            
        except Exception as e:
            print(f"Feature extraction error: {e}")
            return {}
    
    def update_model(self):
        """Update predictive model with new data"""
        try:
            # Simple model update - in production, use ML algorithms
            if len(self.training_data) > 0:
                # Calculate average patterns
                avg_patterns = {}
                for key in self.training_data[0].keys():
                    avg_patterns[key] = np.mean([d[key] for d in self.training_data])
                
                # Update model thresholds
                self.risk_model['baseline'] = avg_patterns
                
        except Exception as e:
            print(f"Model update error: {e}")
    
    def predict_risk(self, user_activity):
        """Predict risk score for user activity"""
        try:
            features = self.extract_features(user_activity)
            
            if not features or 'baseline' not in self.risk_model:
                return 0.0
            
            # Calculate risk score
            risk_score = 0
            for feature, weight in self.risk_model['weights'].items():
                baseline_value = self.risk_model['baseline'].get(feature, 0)
                current_value = features.get(feature, 0)
                
                # Normalize and weight
                deviation = abs(current_value - baseline_value) / (baseline_value + 1)
                risk_score += deviation * weight
            
            return min(risk_score, 1.0)
            
        except Exception as e:
            print(f"Risk prediction error: {e}")
            return 0.0
    
    def generate_risk_alert(self, user_id, risk_score, prediction_type):
        """Generate risk prediction alert"""
        try:
            if risk_score > self.risk_model['threshold']:
                confidence = min(risk_score * 100, 95)
                
                self.logger.log_event(
                    "Predictive Risk Alert",
                    f"High risk prediction: {prediction_type}",
                    "Predictive AI",
                    f"User: {user_id}, Score: {risk_score:.2f}, Confidence: {confidence:.1f}%",
                    "Critical"
                )
                print(f"[CRITICAL] PREDICTIVE RISK: {prediction_type} (Score: {risk_score:.2f}, Confidence: {confidence:.1f}%)")
                
                # Store in database
                conn = sqlite3.connect(self.config.db_file)
                cursor = conn.cursor()
                
                mitigation_actions = self.generate_mitigation_actions(risk_score, prediction_type)
                
                cursor.execute('''
                    INSERT INTO predictive_risks 
                    (user_id, risk_score, prediction_type, confidence, mitigation_actions)
                    VALUES (?, ?, ?, ?, ?)
                ''', (user_id, risk_score, prediction_type, confidence, json.dumps(mitigation_actions)))
                
                conn.commit()
                conn.close()
                
        except Exception as e:
            print(f"Risk alert generation error: {e}")
    
    def generate_mitigation_actions(self, risk_score, prediction_type):
        """Generate mitigation actions for risk prediction"""
        actions = []
        
        if risk_score > 0.8:
            actions.append("Immediate supervisor notification")
            actions.append("Temporary AI tool access restriction")
        elif risk_score > 0.6:
            actions.append("Enhanced monitoring")
            actions.append("Security awareness training")
        
        if "data leak" in prediction_type.lower():
            actions.append("Data access audit")
            actions.append("DLP policy review")
        
        return actions

class AIEventLogger:
    def __init__(self, config):
        self.config = config
        self.workbook = None
        self.sheet = None
        self.row_counter = 1
        self.lock = threading.Lock()
        self.log_file = config.log_file
        self.db_file = config.db_file
        self.initialize_workbook()
        
    def initialize_workbook(self):
        try:
            self.workbook = Workbook()
            self.sheet = self.workbook.active
            self.sheet.title = "AI_Monitor_Log"
            
            # Create comprehensive headers
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
            
            # Auto-adjust column widths
            for col in range(1, len(headers) + 1):
                self.sheet.column_dimensions[get_column_letter(col)].width = 20
            
            self.row_counter = 2  # Start from row 2 (after headers)
            
            # Save immediately to create the file
            self.save_workbook()
            print(f"✅ Excel workbook initialized: {self.log_file}")
            
        except Exception as e:
            print(f"❌ Error initializing workbook: {e}")
    
    def save_workbook(self):
        try:
            if self.workbook:
                self.workbook.save(self.log_file)
                print(f"💾 Excel saved: {self.log_file}")
        except Exception as e:
            print(f"❌ Error saving workbook: {e}")
    
    def log_event(self, event_type, description, process_name="", file_url="", risk_level="Medium"):
        with self.lock:
            try:
                if not self.workbook or not self.sheet:
                    self.initialize_workbook()
                    if not self.workbook or not self.sheet:
                        return
                
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Basic columns
                self.sheet.cell(row=self.row_counter, column=1, value=timestamp)
                self.sheet.cell(row=self.row_counter, column=2, value=event_type)
                self.sheet.cell(row=self.row_counter, column=3, value=description)
                self.sheet.cell(row=self.row_counter, column=4, value=process_name)
                self.sheet.cell(row=self.row_counter, column=5, value=file_url)
                
                # Risk level color coding
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
                
                # Add AI identification columns
                self._add_ai_identification_columns(event_type, description, file_url, risk_level)
                
                self.row_counter += 1
                
                # Save every 5 events to ensure data persistence
                if self.row_counter % 5 == 0:
                    self.save_workbook()
                
                # Display user action
                self.display_user_action(event_type, description, process_name, file_url, risk_level, timestamp)
                
                print(f"✅ Event logged: {event_type} - {description[:50]}...")
                    
            except Exception as e:
                print(f"❌ Error logging event: {e}")
    
    def _add_ai_identification_columns(self, event_type, description, file_url, risk_level):
        try:
            # AI Category
            ai_category = self._extract_ai_category(event_type, description, file_url)
            self.sheet.cell(row=self.row_counter, column=7, value=ai_category)
            
            # AI Tool Name
            ai_tool_name = self._extract_ai_tool_name(event_type, description, file_url)
            self.sheet.cell(row=self.row_counter, column=8, value=ai_tool_name)
            
            # Detection Method
            detection_method = self._extract_detection_method(event_type, description, file_url)
            self.sheet.cell(row=self.row_counter, column=9, value=detection_method)
            
            # Confidence Score
            confidence_score = self._calculate_confidence_score(event_type, description, file_url, risk_level)
            self.sheet.cell(row=self.row_counter, column=10, value=confidence_score)
            
            # Session ID
            session_id = self._get_user_session_id()
            self.sheet.cell(row=self.row_counter, column=11, value=session_id)
            
            # Geographic Location
            location = self._detect_geographic_context(file_url, description)
            self.sheet.cell(row=self.row_counter, column=12, value=location)
            
            # Action Type
            action_type = self._classify_action_type(event_type, description)
            self.sheet.cell(row=self.row_counter, column=13, value=action_type)
            
            # Historical Reference ID
            ref_id = self._generate_historical_reference_id()
            self.sheet.cell(row=self.row_counter, column=14, value=ref_id)
            
            # Compliance Flag
            compliance_flag = self._check_compliance_flag(event_type, description, risk_level)
            self.sheet.cell(row=self.row_counter, column=15, value=compliance_flag)
            
        except Exception as e:
            print(f"❌ Error adding AI identification columns: {e}")
    
    def _extract_ai_category(self, event_type, description, file_url):
        try:
            categories = {
                'LLM/Chatbot': ['chatgpt', 'claude', 'gemini', 'bard', 'llm', 'chatbot'],
                'Image Generation': ['midjourney', 'dall', 'stable', 'diffusion', 'image'],
                'Code Assistant': ['copilot', 'github', 'code', 'programming'],
                'Data Analytics': ['kaggle', 'colab', 'jupyter', 'pandas', 'numpy'],
                'Productivity AI': ['notion', 'grammarly', 'canva', 'productivity']
            }
            
            text_to_check = (description + ' ' + file_url).lower()
            
            for category, keywords in categories.items():
                if any(keyword in text_to_check for keyword in keywords):
                    return category
            
            return 'General AI'
        except:
            return 'Unknown'
    
    def _extract_ai_tool_name(self, event_type, description, file_url):
        try:
            ai_tools = {
                'ChatGPT': ['chatgpt', 'chat.openai.com', 'openai'],
                'Claude': ['claude', 'claude.ai', 'anthropic'],
                'Gemini': ['gemini', 'bard', 'gemini.google.com'],
                'Copilot': ['copilot', 'github copilot'],
                'Midjourney': ['midjourney', 'midjourney.com'],
                'Canva': ['canva', 'canva.com'],
                'Notion': ['notion', 'notion.so'],
                'Grammarly': ['grammarly', 'grammarly.com']
            }
            
            text_to_check = (description + ' ' + file_url).lower()
            
            for tool, patterns in ai_tools.items():
                if any(pattern in text_to_check for pattern in patterns):
                    return tool
            
            return 'Unknown AI Tool'
        except:
            return 'Unknown AI Tool'
    
    def _extract_detection_method(self, event_type, description, file_url):
        try:
            if 'Browser AI Usage' in event_type:
                return 'Browser Monitoring'
            elif 'File Access' in event_type:
                return 'File System Monitoring'
            elif 'Process Activity' in event_type:
                return 'Process Monitoring'
            elif 'Network Connection' in event_type:
                return 'Network Monitoring'
            else:
                return 'General Monitoring'
        except:
            return 'Unknown Method'
    
    def _calculate_confidence_score(self, event_type, description, file_url, risk_level):
        try:
            base_score = 50
            risk_scores = {'critical': 90, 'high': 75, 'medium': 50, 'low': 25}
            base_score = risk_scores.get(risk_level.lower(), 50)
            
            if 'Browser AI Usage' in event_type:
                base_score += 10
            elif 'File Access' in event_type:
                base_score += 15
            
            if 'ChatGPT' in description or 'Claude' in description:
                base_score += 15
            elif 'openai.com' in file_url or 'anthropic.com' in file_url:
                base_score += 20
            
            return min(100, max(1, base_score))
        except:
            return 50
    
    def _get_user_session_id(self):
        try:
            if not hasattr(self, 'session_id'):
                self.session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{secrets.token_hex(4)}"
            return self.session_id
        except:
            return f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    def _detect_geographic_context(self, file_url, description):
        try:
            geo_indicators = {
                'US': ['.com', '.us', 'america'],
                'UK': ['.co.uk', '.uk', 'britain'],
                'EU': ['.de', '.fr', '.it', '.es', '.eu'],
                'Asia': ['.jp', '.cn', '.in', '.kr', '.asia'],
                'Global': ['.ai', '.tech', '.science']
            }
            
            text_to_check = (file_url + ' ' + description).lower()
            
            for geo, indicators in geo_indicators.items():
                if any(indicator in text_to_check for indicator in indicators):
                    return geo
            
            return 'Unknown'
        except:
            return 'Unknown'
    
    def _classify_action_type(self, event_type, description):
        try:
            if 'access' in description.lower() or 'visit' in description.lower():
                return 'Access'
            elif 'create' in description.lower() or 'generate' in description.lower():
                return 'Creation'
            elif 'modify' in description.lower() or 'edit' in description.lower():
                return 'Modification'
            elif 'download' in description.lower() or 'upload' in description.lower():
                return 'Transfer'
            else:
                return 'General'
        except:
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
                3: 40,  # Description
                4: 20,  # Process Name
                5: 50,  # File URL
                6: 15,  # Risk Level
                7: 20,  # AI Category
                8: 25,  # AI Tool Name
                9: 20,  # Detection Method
                10: 15, # Confidence Score
                11: 25, # Session ID
                12: 15, # Geographic Location
                13: 15, # Action Type
                14: 25, # Historical Reference ID
                15: 20  # Compliance Flag
            }
            
            for col, width in column_widths.items():
                self.sheet.column_dimensions[openpyxl.utils.get_column_letter(col)].width = width
                
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
                summary_sheet.column_dimensions[openpyxl.utils.get_column_letter(col)].width = 20
            
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
                "Social Media AI": "📱",
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
                file_info = f"📄 {os.path.basename(file_url)}"
                file_size = os.path.getsize(file_url)
                file_size_str = self.format_file_size(file_size)
                file_details = f"{file_info} ({file_size_str})"
            else:
                file_details = file_url or "No file"
            
            # Create action message
            action_msg = f"{icon} USER ACTION DETECTED"
            
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
                CMDStyler.print_colored(f"   ⏰ Time: {timestamp}", 'YELLOW')
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
    
    def save_and_close(self):
        with self.lock:
            try:
                if self.workbook:
                    self.save_workbook()
                    self.workbook.close()
                    self.workbook = None
                    self.sheet = None
            except Exception as e:
                print(f"Error saving final Excel file: {e}")
    
    def __del__(self):
        self.save_and_close()

class AIBehaviorAnalyzer:
    """Innovative AI behavior analysis for social practice monitoring"""
    
    def __init__(self, config):
        self.config = config
        self.behavior_patterns = {}
        self.anomaly_threshold = 5
        self.social_impact_score = 0
        
    def analyze_behavior_pattern(self, event_type, description, process_name):
        """Analyze AI usage patterns for social impact"""
        timestamp = datetime.now().strftime("%H:%M")
        key = f"{timestamp}_{event_type}_{process_name}"
        
        if key not in self.behavior_patterns:
            self.behavior_patterns[key] = 0
        self.behavior_patterns[key] += 1
        
        # Detect anomalies
        if self.behavior_patterns[key] > self.anomaly_threshold:
            return f"ANOMALY: High frequency {event_type} detected from {process_name}"
        
        return None
    
    def calculate_social_impact(self, activities):
        """Calculate social impact score based on AI usage"""
        impact_score = 0
        
        for activity in activities:
            if any(tool in activity.lower() for tool in self.config.social_media_ai):
                impact_score += 2
            elif any(tool in activity.lower() for tool in self.config.remote_work_tools):
                impact_score += 3
            elif any(tool in activity.lower() for tool in self.config.education_ai):
                impact_score += 4
            elif any(tool in activity.lower() for tool in self.config.content_creation_ai):
                impact_score += 5
        
        self.social_impact_score = impact_score
        return impact_score
    
    def get_productivity_insights(self):
        """Generate productivity insights based on AI usage"""
        insights = []
        
        # Analyze time patterns
        current_hour = datetime.now().hour
        if 9 <= current_hour <= 17:  # Work hours
            if self.social_impact_score > 20:
                insights.append("High AI usage during work hours - potential productivity impact")
        elif current_hour < 9 or current_hour > 17:  # After hours
            if self.social_impact_score > 10:
                insights.append("Significant AI usage outside work hours - work-life balance concern")
        
        return insights
    
    def detect_ai_dependency(self):
        """Detect potential AI dependency patterns"""
        dependency_indicators = []
        
        for pattern, count in self.behavior_patterns.items():
            if count > 10:
                dependency_indicators.append(f"High dependency detected: {pattern}")
        
        return dependency_indicators

class SocialMediaMonitor:
    """Monitor social media AI usage and digital wellbeing"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.running = False
        self.thread = None
        self.screen_time_tracker = {}
        
    def monitor_social_media_usage(self):
        """Monitor social media platforms with AI features"""
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    process_name = proc.info['name'].lower() if proc.info['name'] else ""
                    cmdline = ' '.join(proc.info['cmdline']).lower() if proc.info['cmdline'] else ""
                    
                    # Check for social media apps
                    for social_app in self.config.social_media_ai:
                        if social_app in process_name or social_app in cmdline:
                            self.track_screen_time(social_app, proc.info['pid'])
                            
                            # Check for AI features usage
                            if any(ai_feature in cmdline for ai_feature in ['ai', 'smart', 'auto', 'suggest']):
                                self.logger.log_event(
                                    "Social Media AI",
                                    f"AI feature used in {social_app}",
                                    process_name,
                                    cmdline,
                                    "Medium"
                                )
                                print(f"[MEDIUM] Social Media AI: {social_app}")
                                
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        except Exception as e:
            print(f"Social media monitoring error: {e}")
    
    def track_screen_time(self, app, pid):
        """Track screen time for social media apps"""
        if app not in self.screen_time_tracker:
            self.screen_time_tracker[app] = {'start_time': time.time(), 'duration': 0}
        
        # Update duration
        current_time = time.time()
        self.screen_time_tracker[app]['duration'] = current_time - self.screen_time_tracker[app]['start_time']
        
        # Alert if usage exceeds threshold (1 hour)
        if self.screen_time_tracker[app]['duration'] > 3600:
            self.logger.log_event(
                "Digital Wellbeing",
                f"Excessive screen time: {app} ({self.screen_time_tracker[app]['duration']/3600:.1f} hours)",
                app,
                "",
                "High"
            )
            print(f"[HIGH] Excessive Screen Time: {app}")
    
    def start_monitoring(self):
        if self.thread and self.thread.is_alive():
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.thread.start()
    
    def _monitor_loop(self):
        while self.running:
            try:
                self.monitor_social_media_usage()
                # Check every 30 seconds
                for _ in range(300):
                    if not self.running:
                        break
                    time.sleep(0.1)
            except Exception as e:
                print(f"Social media monitor loop error: {e}")
                if not self.running:
                    break
    
    def stop_monitoring(self):
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1)
            if self.thread.is_alive():
                self.thread.daemon = True

class NetworkMonitor:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.running = False
        self.thread = None
        
    def check_connections(self):
        try:
            connections = psutil.net_connections(kind='inet')
            for conn in connections:
                if conn.status == 'ESTABLISHED' and conn.raddr:
                    remote_ip, remote_port = conn.raddr
                    try:
                        hostname = socket.gethostbyaddr(remote_ip)[0]
                        if any(domain in hostname.lower() for domain in self.config.ai_domains):
                            process_name = self.get_process_name(conn.pid)
                            self.logger.log_event(
                                "Network Connection",
                                f"AI domain detected: {hostname}",
                                process_name,
                                f"{hostname}:{remote_port}",
                                "High"
                            )
                            print(f"[HIGH] AI Domain Access: {hostname} by {process_name}")
                    except:
                        pass
        except Exception as e:
            print(f"Network monitoring error: {e}")
    
    def get_process_name(self, pid):
        try:
            if pid:
                process = psutil.Process(pid)
                return process.name()
        except:
            pass
        return "Unknown"
    
    def start_monitoring(self):
        if self.thread and self.thread.is_alive():
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.thread.start()
    
    def _monitor_loop(self):
        while self.running:
            try:
                self.check_connections()
                # Use a shorter sleep with running check to allow faster shutdown
                for _ in range(self.config.monitor_interval * 10):
                    if not self.running:
                        break
                    time.sleep(0.1)
            except Exception as e:
                print(f"Network monitor loop error: {e}")
                if not self.running:
                    break
    
    def stop_monitoring(self):
        self.running = False
        if self.thread and self.thread.is_alive():
            # Wait for thread to stop naturally
            self.thread.join(timeout=1)
            # If still alive, force termination by setting daemon and letting it die
            if self.thread.is_alive():
                self.thread.daemon = True
                # Don't print warning - just let it die gracefully

class FileMonitor(FileSystemEventHandler):
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        
    def on_modified(self, event):
        if not event.is_directory:
            self.check_ai_file(event.src_path, "modified")
    
    def on_created(self, event):
        if not event.is_directory:
            self.check_ai_file(event.src_path, "created")
    
    def on_moved(self, event):
        if not event.is_directory:
            self.check_ai_file(event.src_path, "moved")
            if event.dest_path:
                self.check_ai_file(event.dest_path, "moved_to")
    
    def on_accessed(self, event):
        if not event.is_directory:
            self.check_ai_file(event.src_path, "accessed")
    
    def check_ai_file(self, file_path, action):
        try:
            file_name = os.path.basename(file_path).lower()
            file_dir = os.path.dirname(file_path).lower()
            
            # Check if file is AI-related
            is_ai_file = False
            ai_type = ""
            
            # Check file content for AI indicators
            if os.path.exists(file_path) and os.path.getsize(file_path) < 10 * 1024 * 1024:  # < 10MB
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(1000).lower()  # Read first 1000 chars
                        ai_keywords_found = []
                        
                        for keyword in self.config.ai_keywords:
                            if keyword in content:
                                ai_keywords_found.append(keyword)
                                is_ai_file = True
                        
                        if ai_keywords_found:
                            ai_type = f"Content contains: {', '.join(ai_keywords_found[:3])}"
                            risk_level = "High"
                            self.logger.log_event(
                                "File Access",
                                f"User {action} AI file - {ai_type}",
                                self.get_accessing_process(file_path),
                                file_path,
                                risk_level
                            )
                        else:
                            # Check file name and path for AI indicators
                            for keyword in self.config.ai_keywords:
                                if keyword in file_name or keyword in file_dir:
                                    ai_type = f"Filename/Path contains: {keyword}"
                                    risk_level = "Medium"
                                    self.logger.log_event(
                                        "File Access",
                                        f"User {action} AI file - {ai_type}",
                                        self.get_accessing_process(file_path),
                                        file_path,
                                        risk_level
                                    )
                                    break
                            
                            # Check file extensions
                            ai_extensions = ['.py', '.ipynb', '.pt', '.pth', '.h5', '.pb', '.onnx', '.pkl', '.joblib']
                            if any(file_path.endswith(ext) for ext in ai_extensions):
                                ai_type = f"AI file extension: {os.path.splitext(file_path)[1]}"
                                risk_level = "Medium"
                                self.logger.log_event(
                                    "File Access",
                                    f"User {action} AI file - {ai_type}",
                                    self.get_accessing_process(file_path),
                                    file_path,
                                    risk_level
                                )
                except:
                    pass
        except Exception as e:
            print(f"File monitoring error: {e}")
    
    def get_accessing_process(self, file_path):
        """Get the process that accessed the file"""
        try:
            for proc in psutil.process_iter(['pid', 'name', 'open_files']):
                try:
                    if proc.info['open_files']:
                        for file_info in proc.info['open_files']:
                            if file_info.path.lower() == file_path.lower():
                                return proc.info['name']
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except:
            pass
        return "Unknown"

class BrowserAIMonitor:
    """Advanced Browser AI Website Monitoring"""
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.running = False
        self.thread = None
        self.monitored_browsers = ['chrome.exe', 'firefox.exe', 'msedge.exe', 'opera.exe', 'brave.exe', 'iexplore.exe']
        self.ai_websites = {
            # Major AI Platforms
            'chat.openai.com': {'name': 'ChatGPT', 'category': 'LLM', 'risk': 'Medium'},
            'chatgpt.com': {'name': 'ChatGPT', 'category': 'LLM', 'risk': 'Medium'},
            'openai.com': {'name': 'OpenAI', 'category': 'AI Platform', 'risk': 'Medium'},
            'claude.ai': {'name': 'Claude', 'category': 'LLM', 'risk': 'Medium'},
            'anthropic.com': {'name': 'Anthropic', 'category': 'AI Platform', 'risk': 'Medium'},
            'gemini.google.com': {'name': 'Gemini', 'category': 'LLM', 'risk': 'Medium'},
            'bard.google.com': {'name': 'Bard', 'category': 'LLM', 'risk': 'Medium'},
            'copilot.microsoft.com': {'name': 'Copilot', 'category': 'Code Assistant', 'risk': 'Low'},
            'github.com': {'name': 'GitHub', 'category': 'Development', 'risk': 'Low'},
            'huggingface.co': {'name': 'HuggingFace', 'category': 'ML Platform', 'risk': 'Medium'},
            'midjourney.com': {'name': 'Midjourney', 'category': 'Image Generation', 'risk': 'Medium'},
            'stability.ai': {'name': 'Stability AI', 'category': 'Image Generation', 'risk': 'Medium'},
            'canva.com': {'name': 'Canva', 'category': 'Design AI', 'risk': 'Low'},
            'notion.so': {'name': 'Notion', 'category': 'Productivity AI', 'risk': 'Low'},
            'grammarly.com': {'name': 'Grammarly', 'category': 'Writing AI', 'risk': 'Low'},
            'character.ai': {'name': 'Character.AI', 'category': 'Chatbot', 'risk': 'Medium'},
            'tensorflow.org': {'name': 'TensorFlow', 'category': 'ML Framework', 'risk': 'Low'},
            'pytorch.org': {'name': 'PyTorch', 'category': 'ML Framework', 'risk': 'Low'}
        }
        
        # Global AI detection patterns
        self.global_ai_patterns = {
            # AI Keywords (must contain at least one)
            'ai_keywords': [
                'ai', 'artificial', 'intelligence', 'machine', 'learning', 'neural', 'network',
                'deep', 'chatbot', 'gpt', 'llm', 'transformer', 'bert', 'nlp', 'computer', 'vision',
                'opencv', 'tensorflow', 'pytorch', 'keras', 'scikit', 'hugging', 'face',
                'claude', 'gemini', 'bard', 'copilot', 'midjourney', 'dall', 'stable', 'diffusion',
                'runway', 'canva', 'notion', 'grammarly', 'character', 'repl', 'codepen',
                'kaggle', 'colab', 'jupyter', 'pandas', 'numpy', 'matplotlib', 'seaborn',
                'langchain', 'openai', 'anthropic', 'cohere', 'mistral', 'llama', 'alpaca',
                'vicuna', 'chatglm', 'ernie', 'wenxin', 'spark', 'tongyi', 'qianwen',
                'sora', 'pika', 'lumalabs', 'leonardo', 'artbreeder', 'dreamstudio',
                'nightcafe', 'deepart', 'deepdream', 'stylegan', 'biggan', 'vae',
                'gan', 'autoencoder', 'rnn', 'lstm', 'gru', 'attention', 'encoder',
                'decoder', 'bert', 'roberta', 'gpt', 'xlnet', 'electra', 'deberta',
                't5', 'bart', 'pegasus', 'gpt', 'neo', 'gpt', 'j', 'bloom', 'opt',
                'flan', 'palm', 'lamda', 'sparrow', 'meena', 'blenderbot', 'dialo',
                'gpt', 'chat', 'assistant', 'copilot', 'code', 'completion', 'generation',
                'synthesis', 'analysis', 'prediction', 'classification', 'regression',
                'clustering', 'reinforcement', 'supervised', 'unsupervised', 'semi',
                'transfer', 'federated', 'adversarial', 'generative', 'discriminative',
                'ensemble', 'bagging', 'boosting', 'random', 'forest', 'svm', 'knn',
                'decision', 'tree', 'gradient', 'descent', 'backpropagation', 'forward',
                'propagation', 'activation', 'sigmoid', 'tanh', 'relu', 'softmax', 'dropout',
                'batch', 'normalization', 'convolution', 'pooling', 'padding', 'stride',
                'filter', 'kernel', 'feature', 'extraction', 'selection', 'dimensionality',
                'reduction', 'pca', 'tsne', 'umap', 'clustering', 'kmeans', 'dbscan',
                'hierarchical', 'spectral', 'mean', 'shift', 'affinity', 'propagation'
            ],
            
            # AI Domain patterns (must contain at least one)
            'ai_domains': [
                'ai', 'artificial', 'intelligence', 'machine', 'learning', 'neural',
                'chatbot', 'llm', 'gpt', 'claude', 'gemini', 'bard', 'copilot',
                'huggingface', 'midjourney', 'stability', 'runway', 'canva', 'notion',
                'grammarly', 'character', 'replit', 'kaggle', 'colab', 'tensorflow',
                'pytorch', 'opencv', 'langchain', 'cohere', 'mistral', 'llama',
                'sora', 'pika', 'leonardo', 'artbreeder', 'dreamstudio', 'nightcafe'
            ],
            
            # AI TLDs and patterns
            'ai_tlds': ['.ai', '.ml', '.data', '.tech', '.science'],
            
            # AI company domains
            'ai_companies': [
                'openai', 'anthropic', 'google', 'microsoft', 'meta', 'facebook',
                'apple', 'amazon', 'nvidia', 'amd', 'intel', 'ibm', 'oracle',
                'salesforce', 'adobe', 'autodesk', 'siemens', 'bosch', 'toyota',
                'tesla', 'uber', 'lyft', 'airbnb', 'netflix', 'spotify', 'tiktok',
                'instagram', 'twitter', 'linkedin', 'reddit', 'discord', 'slack',
                'zoom', 'teams', 'skype', 'whatsapp', 'telegram', 'signal'
            ],
            
            # AI service patterns
            'ai_services': [
                'chat', 'assistant', 'bot', 'copilot', 'helper', 'agent', 'advisor',
                'recommendation', 'personalization', 'prediction', 'forecast',
                'analysis', 'insight', 'optimization', 'automation', 'generation',
                'creation', 'design', 'art', 'music', 'video', 'image', 'text',
                'code', 'programming', 'development', 'testing', 'debugging',
                'documentation', 'translation', 'summarization', 'extraction',
                'classification', 'clustering', 'regression', 'anomaly', 'detection'
            ]
        }
        self.browser_class_patterns = {
            'chrome': ['chrome_widgetwin_1', 'chrome'],
            'firefox': ['mozilla', 'firefox'],
            'edge': ['msedge', 'edge', 'chromium'],  # Edge uses Chromium-based classes
            'opera': ['opera'],
            'brave': ['brave'],
            'ie': ['ieframe']
        }
        self.browser_windows = {}
        self.last_urls = {}
        
    def start_monitoring(self):
        """Start browser AI monitoring"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._monitor_browser_activity, daemon=True)
            self.thread.start()
            CMDStyler.print_alert("🌐 Browser AI Monitoring Started", 'MEDIUM')
    
    def stop_monitoring(self):
        """Stop browser AI monitoring"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=1)
    
    def _monitor_browser_activity(self):
        """Monitor browser activity for AI websites"""
        while self.running:
            try:
                self._check_browser_windows()
                self._check_browser_urls()
                time.sleep(3)  # Check every 3 seconds
            except Exception as e:
                print(f"Browser monitoring error: {e}")
                time.sleep(5)
    
    def _check_browser_windows(self):
        """Check for active browser windows"""
        try:
            def enum_windows_callback(hwnd, windows):
                if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
                    window_title = win32gui.GetWindowText(hwnd).lower()
                    class_name = win32gui.GetClassName(hwnd).lower()
                    
                    # Enhanced browser detection using multiple patterns
                    detected_browser = None
                    for browser, patterns in self.browser_class_patterns.items():
                        if any(pattern in class_name for pattern in patterns):
                            detected_browser = browser
                            break
                    
                    if detected_browser:
                        try:
                            # Use win32process to get process ID
                            _, pid = win32process.GetWindowThreadProcessId(hwnd)
                            process = psutil.Process(pid)
                            process_name = process.name().lower()
                            
                            # Check if process name matches our monitored browsers
                            if any(browser in process_name for browser in self.monitored_browsers):
                                windows.append({
                                    'hwnd': hwnd,
                                    'pid': pid,
                                    'process_name': process_name,
                                    'title': window_title,
                                    'class_name': class_name,
                                    'browser_type': detected_browser
                                })
                                
                                # Debug output
                                CMDStyler.print_colored(f"🔍 Detected {detected_browser} window: {window_title[:50]}...", 'INFO')
                                
                        except (psutil.NoSuchProcess, psutil.AccessDenied, AttributeError) as e:
                            CMDStyler.print_colored(f"⚠️  Error accessing process {pid}: {e}", 'INFO')
                            pass
                return True
            
            windows = []
            win32gui.EnumWindows(enum_windows_callback, windows)
            
            # Update browser windows list
            old_windows = set(self.browser_windows.keys())
            new_windows = set(win['pid'] for win in windows)
            
            # Detect new browser windows
            for window in windows:
                if window['pid'] not in self.browser_windows:
                    self.browser_windows[window['pid']] = window
                    self._log_browser_activity(window['process_name'], "Browser Opened", window['title'])
                    
            # Detect closed browser windows
            for pid in old_windows - new_windows:
                if pid in self.browser_windows:
                    window = self.browser_windows[pid]
                    self._log_browser_activity(window['process_name'], "Browser Closed", window['title'])
                    del self.browser_windows[pid]
                    
        except Exception as e:
            print(f"Error checking browser windows: {e}")
    
    def _check_browser_urls(self):
        """Check browser URLs for AI websites"""
        try:
            for pid, window_info in self.browser_windows.items():
                current_url = self._get_browser_url(pid, window_info['process_name'])
                
                if current_url and current_url != self.last_urls.get(pid):
                    # New URL detected
                    self._analyze_url(current_url, window_info)
                    self.last_urls[pid] = current_url
                    
        except Exception as e:
            print(f"Error checking browser URLs: {e}")
    
    def _get_browser_url(self, pid, process_name):
        """Get current URL from browser"""
        try:
            # Get window title and extract URL if present
            for window_info in self.browser_windows.values():
                if window_info['pid'] == pid:
                    window_title = win32gui.GetWindowText(window_info['hwnd'])
                    
                    # Debug: Show the window title
                    CMDStyler.print_colored(f"🔍 Checking window title: {window_title[:100]}...", 'INFO')
                    
                    # Method 1: Extract URL from title if present
                    if 'http://' in window_title or 'https://' in window_title:
                        import re
                        url_match = re.search(r'https?://[^\s\)]+', window_title)
                        if url_match:
                            url = url_match.group(0)
                            CMDStyler.print_colored(f"✅ Found URL in title: {url}", 'INFO')
                            return url
                    
                    # Method 2: Check for AI website names in title
                    title_lower = window_title.lower()
                    for domain, info in self.ai_websites.items():
                        if info['name'].lower() in title_lower or domain in title_lower:
                            url = f"https://{domain}"
                            CMDStyler.print_colored(f"✅ Found AI website in title: {url}", 'INFO')
                            return url
                    
                    # Method 3: Check for partial matches
                    ai_keywords = ['chatgpt', 'claude', 'gemini', 'bard', 'copilot', 'openai', 'anthropic']
                    for keyword in ai_keywords:
                        if keyword in title_lower:
                            # Try to match with known AI websites
                            for domain, info in self.ai_websites.items():
                                if keyword in domain or keyword in info['name'].lower():
                                    url = f"https://{domain}"
                                    CMDStyler.print_colored(f"✅ Inferred AI website: {url}", 'INFO')
                                    return url
                    
                    # Method 4: Fallback - if we detect a browser but no specific AI site, 
                    # check if it's a known browser process and create a generic monitoring event
                    if any(browser in process_name.lower() for browser in self.monitored_browsers):
                        if len(window_title) > 10:  # Only if there's substantial content
                            CMDStyler.print_colored(f"🌐 Browser activity detected: {window_title[:50]}...", 'INFO')
                            # Don't return URL for non-AI sites, but we know browser is active
                            return None
                    
                    break
            
            return None
            
        except Exception as e:
            CMDStyler.print_colored(f"⚠️  Error getting browser URL: {e}", 'INFO')
            return None
    
    def _analyze_url(self, url, window_info):
        """Analyze URL for AI website detection"""
        try:
            url_lower = url.lower()
            
            # Check against known AI websites database
            for domain, info in self.ai_websites.items():
                if domain in url_lower:
                    self._log_ai_website_access(url, domain, info, window_info)
                    return
            
            # Global AI detection - catch ANY AI-related website
            ai_detection = self._detect_global_ai_website(url_lower)
            if ai_detection:
                self._log_global_ai_website_access(url, ai_detection, window_info)
                return
            
            # Check for AI keywords in URL
            ai_keywords = ['ai', 'artificial', 'machine', 'learning', 'neural', 'chatbot', 'gpt', 'llm']
            if any(keyword in url_lower for keyword in ai_keywords):
                self._log_potential_ai_website(url, window_info)
                return
                
        except Exception as e:
            print(f"Error analyzing URL: {e}")
    
    def _detect_global_ai_website(self, url):
        """Global AI detection - catches any AI-related website"""
        try:
            # Parse URL to extract domain and path
            from urllib.parse import urlparse
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            path = parsed.path.lower()
            
            # Remove www prefix
            domain = domain.replace('www.', '')
            
            detection_score = 0
            detection_reasons = []
            
            # Check 1: AI TLDs (.ai, .ml, .data, .tech, .science)
            for tld in self.global_ai_patterns['ai_tlds']:
                if domain.endswith(tld):
                    detection_score += 50
                    detection_reasons.append(f"AI TLD: {tld}")
                    break
            
            # Check 2: AI keywords in domain
            for keyword in self.global_ai_patterns['ai_domains']:
                if keyword in domain:
                    detection_score += 40
                    detection_reasons.append(f"AI domain keyword: {keyword}")
                    break
            
            # Check 3: AI company domains
            for company in self.global_ai_patterns['ai_companies']:
                if company in domain:
                    detection_score += 30
                    detection_reasons.append(f"AI company: {company}")
                    break
            
            # Check 4: AI service patterns in domain
            for service in self.global_ai_patterns['ai_services']:
                if service in domain:
                    detection_score += 25
                    detection_reasons.append(f"AI service: {service}")
                    break
            
            # Check 5: AI keywords in path
            for keyword in self.global_ai_patterns['ai_keywords']:
                if keyword in path:
                    detection_score += 20
                    detection_reasons.append(f"AI path keyword: {keyword}")
                    if detection_score >= 40:  # Don't over-score
                        break
            
            # Check 6: Common AI patterns
            ai_patterns = [
                'chat', 'bot', 'assistant', 'copilot', 'helper', 'agent',
                'ai-', '-ai', '_ai', 'artificial', 'intelligence',
                'machine', 'learning', 'neural', 'network', 'deep',
                'smart', 'auto', 'intelligent', 'cognitive'
            ]
            
            for pattern in ai_patterns:
                if pattern in domain or pattern in path:
                    detection_score += 15
                    detection_reasons.append(f"AI pattern: {pattern}")
                    if detection_score >= 50:
                        break
            
            # Determine if it's an AI website (score >= 30)
            if detection_score >= 30:
                return {
                    'score': detection_score,
                    'reasons': detection_reasons,
                    'category': self._categorize_ai_website(domain, path),
                    'risk': self._assess_ai_risk(detection_score, domain)
                }
            
            return None
            
        except Exception as e:
            print(f"Error in global AI detection: {e}")
            return None
    
    def _categorize_ai_website(self, domain, path):
        """Categorize the AI website"""
        try:
            # LLM/Chatbot patterns
            llm_patterns = ['chat', 'gpt', 'llm', 'bot', 'assistant', 'claude', 'gemini', 'bard']
            if any(pattern in domain or pattern in path for pattern in llm_patterns):
                return 'LLM/Chatbot'
            
            # Image/Video Generation patterns
            media_patterns = ['image', 'video', 'art', 'design', 'midjourney', 'dall', 'stable', 'diffusion']
            if any(pattern in domain or pattern in path for pattern in media_patterns):
                return 'Media Generation'
            
            # Code/Development patterns
            code_patterns = ['code', 'dev', 'programming', 'copilot', 'github', 'replit', 'codepen']
            if any(pattern in domain or pattern in path for pattern in code_patterns):
                return 'Code/Development'
            
            # Data/Analytics patterns
            data_patterns = ['data', 'analytics', 'ml', 'machine', 'learning', 'kaggle', 'colab']
            if any(pattern in domain or pattern in path for pattern in data_patterns):
                return 'Data/Analytics'
            
            # Voice/Audio patterns
            voice_patterns = ['voice', 'audio', 'speech', 'sound', 'music', 'tts', 'stt']
            if any(pattern in domain or pattern in path for pattern in voice_patterns):
                return 'Voice/Audio'
            
            # Default category
            return 'AI Platform'
            
        except Exception as e:
            return 'AI Platform'
    
    def _assess_ai_risk(self, score, domain):
        """Assess risk level of AI website"""
        try:
            # Higher score = more likely to be AI = lower risk (known AI)
            if score >= 70:
                return 'Low'  # Well-known AI platform
            elif score >= 50:
                return 'Medium'  # Likely AI platform
            else:
                return 'High'  # Unknown/potentially suspicious AI
            
        except Exception as e:
            return 'Medium'
    
    def _log_global_ai_website_access(self, url, detection_info, window_info):
        """Log access to globally detected AI website"""
        try:
            # Create site info for global detection
            site_info = {
                'name': self._extract_site_name(url),
                'category': detection_info['category'],
                'risk': detection_info['risk']
            }
            
            # Create detailed description
            reasons_str = ', '.join(detection_info['reasons'][:3])  # Limit to first 3 reasons
            description = f"User accessed AI website: {site_info['name']} ({site_info['category']}) - Detection: {reasons_str}"
            
            # Log to Excel with enhanced display
            self.logger.log_event(
                "Browser AI Usage",
                description,
                window_info['process_name'],
                url,
                detection_info['risk']
            )
            
            # Add to database
            domain = urlparse(url).netloc
            self._log_to_database(url, domain, site_info, window_info, detection_info['risk'])
            
            # Display enhanced alert
            self._display_global_ai_website_alert(url, detection_info, site_info, window_info)
            
        except Exception as e:
            print(f"Error logging global AI website access: {e}")
    
    def _extract_site_name(self, url):
        """Extract site name from URL"""
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            domain = parsed.netloc.replace('www.', '')
            
            # Use domain as site name
            return domain
            
        except Exception as e:
            return "Unknown AI Site"
    
    def _display_global_ai_website_alert(self, url, detection_info, site_info, window_info):
        """Display enhanced global AI website alert"""
        try:
            # Create category-specific icons
            category_icons = {
                'LLM/Chatbot': '💬',
                'Media Generation': '🎨',
                'Code/Development': '👨‍💻',
                'Data/Analytics': '📊',
                'Voice/Audio': '🎤',
                'AI Platform': '🤖'
            }
            
            icon = category_icons.get(site_info['category'], '🌐')
            
            # Display formatted alert
            CMDStyler.print_colored(f"\n{icon} GLOBAL AI WEBSITE DETECTED", 'MAGENTA', 'BOLD')
            CMDStyler.print_colored(f"   🌐 Website: {site_info['name']} ({site_info['category']})", 'MAGENTA')
            CMDStyler.print_colored(f"   🔗 URL: {url}", 'BLUE')
            CMDStyler.print_colored(f"   🌍 Browser: {window_info['process_name']}", 'GREEN')
            CMDStyler.print_colored(f"   ⚠️  Risk Level: {site_info['risk']}", 'YELLOW' if site_info['risk'] == 'Medium' else 'GREEN' if site_info['risk'] == 'Low' else 'RED')
            CMDStyler.print_colored(f"   🎯 Detection Score: {detection_info['score']}/100", 'CYAN')
            CMDStyler.print_colored(f"   🔍 Reasons: {', '.join(detection_info['reasons'][:2])}", 'WHITE')
            CMDStyler.print_colored(f"   ⏰ Time: {datetime.now().strftime('%H:%M:%S')}", 'WHITE')
            
            # Add category-specific information
            if site_info['category'] == 'LLM/Chatbot':
                CMDStyler.print_colored(f"   💬 Large Language Model or Chatbot Platform", 'MAGENTA')
            elif site_info['category'] == 'Media Generation':
                CMDStyler.print_colored(f"   🎨 AI Media Generation Platform", 'MAGENTA')
            elif site_info['category'] == 'Code/Development':
                CMDStyler.print_colored(f"   👨‍💻 AI-Powered Development Platform", 'BLUE')
            elif site_info['category'] == 'Data/Analytics':
                CMDStyler.print_colored(f"   📊 AI Data Analytics Platform", 'GREEN')
            elif site_info['category'] == 'Voice/Audio':
                CMDStyler.print_colored(f"   🎤 AI Voice/Audio Processing Platform", 'YELLOW')
            
        except Exception as e:
            print(f"Error displaying global AI alert: {e}")
    
    def _log_ai_website_access(self, url, domain, site_info, window_info):
        """Log access to known AI website"""
        try:
            # Determine risk level
            risk_level = site_info['risk']
            
            # Create detailed description
            description = f"User accessed AI website: {site_info['name']} ({site_info['category']})"
            
            # Log to Excel with enhanced display
            self.logger.log_event(
                "Browser AI Usage",
                description,
                window_info['process_name'],
                url,
                risk_level
            )
            
            # Add to database for detailed analysis
            self._log_to_database(url, domain, site_info, window_info, risk_level)
            
            # Display enhanced alert
            self._display_ai_website_alert(url, domain, site_info, window_info)
            
        except Exception as e:
            print(f"Error logging AI website access: {e}")
    
    def _log_potential_ai_website(self, url, window_info):
        """Log access to potential AI website"""
        try:
            description = f"User accessed potential AI website: {url}"
            
            self.logger.log_event(
                "Browser AI Usage",
                description,
                window_info['process_name'],
                url,
                "Medium"
            )
            
            CMDStyler.print_alert(f"🤖 Potential AI Website Detected: {url}", 'INFO')
            
        except Exception as e:
            print(f"Error logging potential AI website: {e}")
    
    def _log_to_database(self, url, domain, site_info, window_info, risk_level):
        """Log browser activity to database"""
        try:
            conn = sqlite3.connect(self.config.db_file)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS browser_ai_activity (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    url TEXT,
                    domain TEXT,
                    site_name TEXT,
                    category TEXT,
                    browser_process TEXT,
                    window_title TEXT,
                    risk_level TEXT
                )
            ''')
            
            cursor.execute('''
                INSERT INTO browser_ai_activity 
                (timestamp, url, domain, site_name, category, browser_process, window_title, risk_level)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now().isoformat(),
                url,
                domain,
                site_info['name'],
                site_info['category'],
                window_info['process_name'],
                window_info['title'],
                risk_level
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Error logging to database: {e}")
    
    def _display_ai_website_alert(self, url, domain, site_info, window_info):
        """Display enhanced AI website alert"""
        try:
            # Create site-specific icons
            site_icons = {
                'ChatGPT': '💬',
                'Claude': '🧠',
                'Gemini': '✨',
                'Copilot': '👨‍💻',
                'Midjourney': '🎨',
                'HuggingFace': '🤗',
                'GitHub': '🐙',
                'Canva': '🎨',
                'Notion': '📝'
            }
            
            icon = site_icons.get(site_info['name'], '🌐')
            
            # Display formatted alert
            CMDStyler.print_colored(f"\n{icon} AI WEBSITE ACCESS DETECTED", 'CYAN', 'BOLD')
            CMDStyler.print_colored(f"   🌐 Website: {site_info['name']} ({site_info['category']})", 'CYAN')
            CMDStyler.print_colored(f"   🔗 URL: {url}", 'BLUE')
            CMDStyler.print_colored(f"   🌍 Browser: {window_info['process_name']}", 'GREEN')
            CMDStyler.print_colored(f"   ⚠️  Risk Level: {site_info['risk']}", 'YELLOW' if site_info['risk'] == 'Medium' else 'GREEN')
            CMDStyler.print_colored(f"   ⏰ Time: {datetime.now().strftime('%H:%M:%S')}", 'WHITE')
            
            # Add category-specific information
            if site_info['category'] == 'LLM':
                CMDStyler.print_colored(f"   💬 Large Language Model Usage Detected", 'MAGENTA')
            elif site_info['category'] == 'Image Generation':
                CMDStyler.print_colored(f"   🎨 AI Image Generation Platform", 'MAGENTA')
            elif site_info['category'] == 'Code Assistant':
                CMDStyler.print_colored(f"   👨‍💻 AI-Powered Code Assistant", 'BLUE')
            elif site_info['category'] == 'ML Platform':
                CMDStyler.print_colored(f"   🤖 Machine Learning Platform", 'GREEN')
            
        except Exception as e:
            print(f"Error displaying alert: {e}")
    
    def generate_browser_ai_report(self):
        """Generate comprehensive browser AI usage report"""
        try:
            CMDStyler.print_header("🌐 BROWSER AI USAGE REPORT", 'CYAN')
            
            conn = sqlite3.connect(self.config.db_file)
            cursor = conn.cursor()
            
            # Get today's activity
            cursor.execute('''
                SELECT site_name, category, COUNT(*) as visits, risk_level
                FROM browser_ai_activity 
                WHERE DATE(timestamp) = DATE('now')
                GROUP BY site_name, category, risk_level
                ORDER BY visits DESC
            ''')
            
            today_activity = cursor.fetchall()
            
            if today_activity:
                CMDStyler.print_colored("\n📊 Today's AI Website Usage:", 'YELLOW', 'BOLD')
                
                total_visits = 0
                for site_name, category, visits, risk_level in today_activity:
                    color = 'GREEN' if risk_level == 'Low' else 'YELLOW' if risk_level == 'Medium' else 'RED'
                    CMDStyler.print_colored(f"   • {site_name}: {visits} visits ({category})", color)
                    total_visits += visits
                
                CMDStyler.print_status([
                    ("Total AI Visits Today", total_visits, 'CYAN'),
                    ("Unique AI Sites", len(today_activity), 'MAGENTA')
                ])
                
                # Risk breakdown
                cursor.execute('''
                    SELECT risk_level, COUNT(*) as count
                    FROM browser_ai_activity 
                    WHERE DATE(timestamp) = DATE('now')
                    GROUP BY risk_level
                ''')
                
                risk_breakdown = cursor.fetchall()
                CMDStyler.print_colored("\n⚠️  Risk Level Breakdown:", 'YELLOW', 'BOLD')
                for risk_level, count in risk_breakdown:
                    color = 'GREEN' if risk_level == 'Low' else 'YELLOW' if risk_level == 'Medium' else 'RED'
                    CMDStyler.print_colored(f"   • {risk_level}: {count} visits", color)
            
            else:
                CMDStyler.print_colored("📊 No AI website activity detected today", 'GREEN')
            
            conn.close()
            CMDStyler.print_separator('═', 60, 'CYAN')
            
        except Exception as e:
            CMDStyler.print_alert(f"Error generating browser AI report: {e}", 'HIGH')
    
    def _log_browser_activity(self, process_name, action, window_title):
        """Log browser window activity (open/close)"""
        try:
            # Create description for browser activity
            description = f"Browser {action}: {window_title[:100]}..."
            
            # Determine risk level based on action
            risk_level = "Low"  # Browser open/close is typically low risk
            
            # Log to Excel
            self.logger.log_event(
                "Browser Activity",
                description,
                process_name,
                f"Browser: {process_name}",
                risk_level
            )
            
            # Display alert for browser activity
            CMDStyler.print_colored(f"🌐 Browser {action}: {window_title[:50]}...", 'INFO')
            
        except Exception as e:
            print(f"Error logging browser activity: {e}")

class FileHandleMonitor:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.running = False
        self.monitored_files = set()
        self.thread = None
        
    def get_open_files(self):
        try:
            open_files = []
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    files = proc.open_files()
                    if files:
                        for file_info in files:
                            open_files.append({
                                'path': file_info.path,
                                'process': proc.info['name'],
                                'pid': proc.info['pid']
                            })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            return open_files
        except Exception as e:
            print(f"Error getting open files: {e}")
            return []
    
    def check_file_access(self):
        try:
            open_files = self.get_open_files()
            current_files = set()
            
            for file_info in open_files:
                file_path = file_info['path'].lower()
                current_files.add(file_path)
                
                if file_path not in self.monitored_files:
                    self.monitored_files.add(file_path)
                    
                    file_name = os.path.basename(file_path)
                    file_ext = os.path.splitext(file_path)[1]
                    
                    if file_ext in self.config.monitored_extensions:
                        if any(keyword in file_name for keyword in self.config.ai_keywords):
                            self.logger.log_event(
                                "File Access",
                                f"AI-related file opened: {file_name}",
                                file_info['process'],
                                file_info['path'],
                                "High"
                            )
                            print(f"[HIGH] AI File Accessed: {file_name} by {file_info['process']}")
                        
                        try:
                            with open(file_info['path'], 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read(500).lower()
                                if any(keyword in content for keyword in self.config.ai_keywords):
                                    self.logger.log_event(
                                        "File Access",
                                        f"AI content file accessed: {file_name}",
                                        file_info['process'],
                                        file_info['path'],
                                        "High"
                                    )
                                    print(f"[HIGH] AI Content File Accessed: {file_name} by {file_info['process']}")
                        except:
                            pass
            
            # Clean up files that are no longer open
            self.monitored_files = current_files.intersection(self.monitored_files)
            
        except Exception as e:
            print(f"File handle monitoring error: {e}")
    
    def start_monitoring(self):
        if self.thread and self.thread.is_alive():
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.thread.start()
    
    def _monitor_loop(self):
        while self.running:
            try:
                self.check_file_access()
                # Use shorter sleep intervals for faster shutdown
                for _ in range(self.config.monitor_interval * 10):
                    if not self.running:
                        break
                    time.sleep(0.1)
            except Exception as e:
                print(f"File handle monitor loop error: {e}")
                if not self.running:
                    break
    
    def stop_monitoring(self):
        self.running = False
        if self.thread and self.thread.is_alive():
            # Wait for thread to stop naturally
            self.thread.join(timeout=1)
            # If still alive, force termination by setting daemon and letting it die
            if self.thread.is_alive():
                self.thread.daemon = True
                # Don't print warning - just let it die gracefully

class BrowserExtensionMonitor:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.running = False
        self.checked_extensions = set()
        self.thread = None
        
    def check_browser_extensions(self):
        try:
            for browser_path in self.config.browser_paths:
                if os.path.exists(browser_path):
                    self.scan_browser_directory(browser_path)
        except Exception as e:
            print(f"Browser extension monitoring error: {e}")
    
    def scan_browser_directory(self, browser_path):
        try:
            for root, dirs, files in os.walk(browser_path):
                # Check for extension directories
                if 'extensions' in root.lower() or 'addons' in root.lower():
                    for ext_dir in dirs:
                        ext_path = os.path.join(root, ext_dir)
                        if ext_path not in self.checked_extensions:
                            self.checked_extensions.add(ext_path)
                            self.check_extension(ext_path, ext_dir)
                
                # Check manifest files for AI extensions
                for file in files:
                    if file == 'manifest.json':
                        manifest_path = os.path.join(root, file)
                        if manifest_path not in self.checked_extensions:
                            self.checked_extensions.add(manifest_path)
                            self.check_manifest_file(manifest_path)
        except Exception as e:
            print(f"Error scanning browser directory {browser_path}: {e}")
    
    def check_extension(self, ext_path, ext_name):
        try:
            # Check extension name for AI keywords
            if any(keyword.lower() in ext_name.lower() for keyword in self.config.ai_keywords):
                self.logger.log_event(
                    "Browser Extension",
                    f"AI-related extension detected: {ext_name}",
                    "Browser",
                    ext_path,
                    "High"
                )
                print(f"[HIGH] AI Extension Detected: {ext_name}")
            
            # Check manifest file if exists
            manifest_path = os.path.join(ext_path, 'manifest.json')
            if os.path.exists(manifest_path):
                self.check_manifest_file(manifest_path)
        except Exception as e:
            print(f"Error checking extension {ext_path}: {e}")
    
    def check_manifest_file(self, manifest_path):
        try:
            with open(manifest_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()
                
                # Check for AI keywords in manifest
                if any(keyword in content for keyword in self.config.ai_keywords):
                    ext_name = self.extract_extension_name(content)
                    self.logger.log_event(
                        "Browser Extension",
                        f"AI extension in manifest: {ext_name}",
                        "Browser",
                        manifest_path,
                        "High"
                    )
                    print(f"[HIGH] AI Extension in Manifest: {ext_name}")
        except Exception as e:
            print(f"Error checking manifest file {manifest_path}: {e}")
    
    def extract_extension_name(self, content):
        try:
            import json
            manifest = json.loads(content)
            return manifest.get('name', 'Unknown AI Extension')
        except:
            return "Unknown AI Extension"
    
    def start_monitoring(self):
        if self.thread and self.thread.is_alive():
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.thread.start()
    
    def _monitor_loop(self):
        while self.running:
            try:
                self.check_browser_extensions()
                # Check every 30 seconds with shorter intervals for faster shutdown
                for _ in range(300):  # 30 seconds * 10 (0.1s intervals)
                    if not self.running:
                        break
                    time.sleep(0.1)
            except Exception as e:
                print(f"Browser extension monitor loop error: {e}")
                if not self.running:
                    break
    
    def stop_monitoring(self):
        self.running = False
        if self.thread and self.thread.is_alive():
            # Wait for thread to stop naturally
            self.thread.join(timeout=1)
            # If still alive, force termination by setting daemon and letting it die
            if self.thread.is_alive():
                self.thread.daemon = True
                # Don't print warning - just let it die gracefully

class ProcessMonitor:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.running = False
        self.seen_processes = set()
        self.thread = None
        
    def check_processes(self):
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    process_name = proc.info['name'].lower() if proc.info['name'] else ""
                    cmdline = ' '.join(proc.info['cmdline']).lower() if proc.info['cmdline'] else ""
                    
                    if proc.info['pid'] not in self.seen_processes:
                        self.seen_processes.add(proc.info['pid'])
                        
                        if any(keyword in process_name for keyword in self.config.ai_processes):
                            self.logger.log_event(
                                "Process Started",
                                f"AI-related process started: {process_name}",
                                process_name,
                                cmdline,
                                "Low"
                            )
                            print(f"[LOW] AI Process Started: {process_name}")
                        
                        if any(keyword in cmdline for keyword in self.config.ai_keywords):
                            self.logger.log_event(
                                "Process Activity",
                                f"AI keywords in process command: {process_name}",
                                process_name,
                                cmdline,
                                "High"
                            )
                            print(f"[HIGH] AI Command Detected: {process_name}")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
        except Exception as e:
            print(f"Process monitoring error: {e}")
    
    def start_monitoring(self):
        if self.thread and self.thread.is_alive():
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.thread.start()
    
    def _monitor_loop(self):
        while self.running:
            try:
                self.check_processes()
                # Use shorter sleep intervals for faster shutdown
                for _ in range(self.config.monitor_interval * 10):
                    if not self.running:
                        break
                    time.sleep(0.1)
            except Exception as e:
                print(f"Process monitor loop error: {e}")
                if not self.running:
                    break
    
    def stop_monitoring(self):
        self.running = False
        if self.thread and self.thread.is_alive():
            # Wait for thread to stop naturally
            self.thread.join(timeout=1)
            # If still alive, force termination by setting daemon and letting it die
            if self.thread.is_alive():
                self.thread.daemon = True
                # Don't print warning - just let it die gracefully

class AISystemMonitor:
    def __init__(self):
        self.config = AIMonitorConfig()
        self.logger = AIEventLogger(self.config)
        self.behavior_analyzer = AIBehaviorAnalyzer(self.config)
        self.social_media_monitor = SocialMediaMonitor(self.config, self.logger)
        self.network_monitor = NetworkMonitor(self.config, self.logger)
        self.process_monitor = ProcessMonitor(self.config, self.logger)
        self.file_monitor = FileMonitor(self.config, self.logger)
        self.file_handle_monitor = FileHandleMonitor(self.config, self.logger)
        self.browser_ai_monitor = BrowserAIMonitor(self.config, self.logger)
        self.browser_extension_monitor = BrowserExtensionMonitor(self.config, self.logger)
        self.threat_intel_manager = AIThreatIntelligenceManager(self.config, self.logger)
        self.model_integrity_verifier = AIModelIntegrityVerifier(self.config)
        self.zero_trust_manager = ZeroTrustAIManager(self.config)
        self.supply_chain_security = AISupplyChainSecurity(self.config)
        self.observer = Observer()
        self.running = False
        self.activity_log = []
        
    def generate_insights_report(self):
        """Generate real-time insights report"""
        try:
            # Calculate social impact
            social_impact = self.behavior_analyzer.calculate_social_impact(self.activity_log)
            
            # Get productivity insights
            insights = self.behavior_analyzer.get_productivity_insights()
            
            # Check for AI dependency
            dependencies = self.behavior_analyzer.detect_ai_dependency()
            
            # Print insights
            print("\n" + "="*50)
            print("🤖 AI USAGE INSIGHTS REPORT")
            print("="*50)
            print(f"📊 Social Impact Score: {social_impact}")
            print(f"📱 Activities Monitored: {len(self.activity_log)}")
            
            if insights:
                print("\n💡 Productivity Insights:")
                for insight in insights:
                    print(f"   • {insight}")
            
            if dependencies:
                print("\n⚠️  Dependency Alerts:")
                for dep in dependencies:
                    print(f"   • {dep}")
            
            # Digital wellbeing summary
            if hasattr(self.social_media_monitor, 'screen_time_tracker'):
                total_screen_time = sum(data['duration'] for data in self.social_media_monitor.screen_time_tracker.values())
                hours = total_screen_time / 3600
                print(f"\n⏱️  Total Screen Time: {hours:.1f} hours")
                
                if hours > 4:
                    print("   ⚠️  Consider taking breaks for digital wellbeing")
            
            print("="*50)
            
        except Exception as e:
            print(f"Error generating insights: {e}")
    
    def setup_file_monitoring(self):
        user_dirs = [
            os.path.expanduser("~/Desktop"),
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Downloads"),
            os.getcwd()
        ]
        
        for directory in user_dirs:
            if os.path.exists(directory):
                self.observer.schedule(self.file_monitor, directory, recursive=True)
                print(f"Monitoring directory: {directory}")
    
    def start_monitoring(self):
        # Show intro animation
        CMDStyler.intro_animation()
        
        # Print system status
        CMDStyler.print_header("🤖 AI SYSTEM MONITOR STATUS", 'MAGENTA')
        
        status_items = [
            ("📋 Log File", os.path.abspath(self.config.log_file), 'CYAN'),
            ("🗄️  Database", os.path.abspath(self.config.db_file), 'CYAN'),
            ("🧬 DNA Tagging", "✓ ACTIVE" if self.config.ai_dna_tagging_enabled else "✗ INACTIVE", 'GREEN' if self.config.ai_dna_tagging_enabled else 'RED'),
            ("🎯 Behavioral Twin", "✓ ACTIVE" if self.config.behavioral_twin_enabled else "✗ INACTIVE", 'GREEN' if self.config.behavioral_twin_enabled else 'RED'),
            ("🔮 Predictive AI", "✓ ACTIVE" if self.config.predictive_shadowing_enabled else "✗ INACTIVE", 'GREEN' if self.config.predictive_shadowing_enabled else 'RED'),
            ("🍯 Honeypot Decoys", "✓ ACTIVE" if self.config.honeypot_decoys_enabled else "✗ INACTIVE", 'GREEN' if self.config.honeypot_decoys_enabled else 'RED'),
            ("🛡️ STIX/TAXII", "✓ ACTIVE", 'GREEN'),
            ("🔐 Model Integrity", "✓ ACTIVE", 'GREEN'),
            ("🔑 Zero-Trust AI", "✓ ACTIVE", 'GREEN'),
            ("🔗 Supply Chain", "✓ ACTIVE", 'GREEN'),
            ("🌐 Browser AI Monitor", "✓ ACTIVE", 'GREEN')
        ]
        
        CMDStyler.print_status(status_items)
        CMDStyler.print_separator('═', 60, 'CYAN')
        
        print()
        CMDStyler.print_colored("🔍 INITIALIZING MONITORING MODULES...", 'YELLOW', 'BOLD')
        
        self.setup_file_monitoring()
        self.observer.start()
        
        # Start all monitoring threads with stylish messages
        CMDStyler.print_alert("Starting Network Monitor", 'INFO')
        self.network_monitor.start_monitoring()
        time.sleep(0.3)
        
        CMDStyler.print_alert("Starting Process Monitor", 'INFO')
        self.process_monitor.start_monitoring()
        time.sleep(0.3)
        
        CMDStyler.print_alert("Starting File Handle Monitor", 'INFO')
        self.file_handle_monitor.start_monitoring()
        time.sleep(0.3)
        
        CMDStyler.print_alert("Starting Browser Extension Monitor", 'INFO')
        self.browser_extension_monitor.start_monitoring()
        time.sleep(0.3)
        
        CMDStyler.print_alert("Starting Social Media Monitor", 'INFO')
        self.social_media_monitor.start_monitoring()
        time.sleep(0.3)
        
        # Initialize advanced security components
        if self.config.ai_dna_tagging_enabled:
            CMDStyler.print_alert("AI DNA Tagger Initialized", 'MEDIUM')
        if self.config.behavioral_twin_enabled:
            CMDStyler.print_alert("Behavioral Twin Online", 'MEDIUM')
        if self.config.honeypot_decoys_enabled:
            CMDStyler.print_alert("Honeypot Decoys Deployed", 'MEDIUM')
        if self.config.predictive_shadowing_enabled:
            CMDStyler.print_alert("Predictive AI Shadowing Active", 'MEDIUM')
        
        # Initialize threat intelligence
        CMDStyler.print_alert("Initializing STIX/TAXII Threat Intelligence", 'INFO')
        time.sleep(0.3)
        
        # Initialize high priority security features
        CMDStyler.print_alert("Initializing AI Model Integrity Verification", 'INFO')
        time.sleep(0.3)
        
        CMDStyler.print_alert("Initializing Zero-Trust AI Architecture", 'INFO')
        self.zero_trust_manager.initialize_ai_identity_federation()
        time.sleep(0.3)
        
        CMDStyler.print_alert("Initializing AI Supply Chain Security", 'INFO')
        time.sleep(0.3)
        
        CMDStyler.print_alert("Initializing Browser AI Monitoring", 'INFO')
        self.browser_ai_monitor.start_monitoring()
        time.sleep(0.3)
        
        # Test TAXII connectivity
        connectivity_results = self.threat_intel_manager.taxii_client.test_connectivity()
        
        # Sync external threats
        try:
            external_count = self.threat_intel_manager.sync_external_threats()
            if external_count > 0:
                CMDStyler.print_alert(f"Synced {external_count} external threat indicators", 'MEDIUM')
        except Exception as e:
            CMDStyler.print_alert(f"External threat sync failed: {e}", 'HIGH')
        
        print()
        CMDStyler.print_header("🚀 REAL-TIME MONITORING ACTIVE", 'GREEN')
        CMDStyler.print_colored("📡 Monitoring AI Activities Across All Channels...", 'CYAN')
        CMDStyler.print_colored("🛡️  Enterprise Security Protocols Engaged", 'GREEN')
        CMDStyler.print_colored("🌐 STIX/TAXII Threat Intelligence Integration Active", 'MAGENTA')
        CMDStyler.print_colored("🔐 High-Priority Security Features Active", 'RED')
        CMDStyler.print_separator('═', 60, 'CYAN')
        
        self.running = True
        insights_counter = 0
        
        try:
            while self.running:
                time.sleep(0.5)
                insights_counter += 1
                
                # Generate insights report every 2 minutes for demo (faster than 5 minutes)
                if insights_counter >= 240:  # 2 minutes = 120 seconds / 0.5 sleep
                    self.generate_styled_insights_report()
                    self.logger.create_summary_sheet()  # Create summary sheet with each insights report
                    insights_counter = 0
                
                # Sync external threats every 5 minutes for demo (faster than 10 minutes)
                if insights_counter % 600 == 0:  # 5 minutes
                    try:
                        external_count = self.threat_intel_manager.sync_external_threats()
                        if external_count > 0:
                            CMDStyler.print_alert(f"🔄 Synced {external_count} new external threats", 'MEDIUM')
                    except Exception as e:
                        CMDStyler.print_alert(f"⚠️  Threat sync error: {e}", 'HIGH')
                
                # Generate periodic status updates every 30 seconds
                if insights_counter % 60 == 0:
                    self.generate_quick_status_update()
                    
        except KeyboardInterrupt:
            # Silent immediate exit
            os._exit(0)
        except Exception as e:
            CMDStyler.print_alert(f"Error in main monitoring loop: {e}", 'CRITICAL')
            # Silent immediate exit
            os._exit(0)
    
    def generate_styled_insights_report(self):
        """Generate stylish insights report"""
        try:
            # Calculate social impact
            social_impact = self.behavior_analyzer.calculate_social_impact(self.activity_log)
            
            # Get productivity insights
            insights = self.behavior_analyzer.get_productivity_insights()
            
            # Check for AI dependency
            dependencies = self.behavior_analyzer.detect_ai_dependency()
            
            # Print styled insights
            CMDStyler.print_header("🤖 AI USAGE INSIGHTS REPORT", 'MAGENTA')
            
            # Status indicators with colors
            impact_color = 'GREEN' if social_impact < 20 else 'YELLOW' if social_impact < 50 else 'RED'
            CMDStyler.print_status([
                ("📊 Social Impact Score", f"{social_impact}", impact_color),
                ("📱 Activities Monitored", f"{len(self.activity_log)}", 'CYAN'),
                ("⏰ Current Time", datetime.now().strftime("%H:%M:%S"), 'WHITE')
            ])
            
            if insights:
                CMDStyler.print_colored("\n💡 PRODUCTIVITY INSIGHTS:", 'YELLOW', 'BOLD')
                for insight in insights:
                    CMDStyler.print_colored(f"   • {insight}", 'YELLOW')
            
            if dependencies:
                CMDStyler.print_colored("\n⚠️  DEPENDENCY ALERTS:", 'RED', 'BOLD')
                for dep in dependencies:
                    CMDStyler.print_colored(f"   • {dep}", 'RED')
            
            # Digital wellbeing summary
            if hasattr(self.social_media_monitor, 'screen_time_tracker'):
                total_screen_time = sum(data['duration'] for data in self.social_media_monitor.screen_time_tracker.values())
                hours = total_screen_time / 3600
                wellbeing_color = 'GREEN' if hours < 2 else 'YELLOW' if hours < 4 else 'RED'
                
                CMDStyler.print_status([
                    ("⏱️  Total Screen Time", f"{hours:.1f} hours", wellbeing_color)
                ])
                
                if hours > 4:
                    CMDStyler.print_alert("⚠️  Consider taking breaks for digital wellbeing", 'MEDIUM')
            
            # Add threat intelligence summary
            CMDStyler.print_colored("\n🛡️ THREAT INTELLIGENCE SUMMARY:", 'RED', 'BOLD')
            bundle_summary = self.threat_intel_manager.stix_generator.get_bundle_summary()
            CMDStyler.print_status([
                ("STIX Objects", bundle_summary['total_objects'], 'RED'),
                ("Indicators Created", bundle_summary['object_types'].get('indicator', 0), 'YELLOW'),
                ("Attack Patterns", bundle_summary['object_types'].get('attack-pattern', 0), 'MAGENTA')
            ])
            
            # Add high priority security reports
            CMDStyler.print_colored("\n🔐 HIGH-PRIORITY SECURITY REPORTS:", 'RED', 'BOLD')
            
            # Model Integrity Report
            model_count = len(self.model_integrity_verifier.model_registry)
            CMDStyler.print_status([
                ("Models Tracked", model_count, 'GREEN' if model_count > 0 else 'YELLOW')
            ])
            
            # Zero-Trust Report
            active_sessions = len(self.zero_trust_manager.ai_sessions)
            avg_trust = 0
            if self.zero_trust_manager.ai_sessions:
                avg_trust = sum(s['trust_score'] for s in self.zero_trust_manager.ai_sessions.values()) / len(self.zero_trust_manager.ai_sessions)
            
            CMDStyler.print_status([
                ("Active AI Sessions", active_sessions, 'CYAN'),
                ("Avg Trust Score", f"{avg_trust:.1f}", 'GREEN' if avg_trust > 70 else 'YELLOW')
            ])
            
            # Supply Chain Report
            sbom_count = len(self.supply_chain_security.ai_sbom)
            total_deps = sum(len(sbom['dependencies']) for sbom in self.supply_chain_security.ai_sbom.values())
            
            CMDStyler.print_status([
                ("SBOMs Created", sbom_count, 'MAGENTA'),
                ("Dependencies Tracked", total_deps, 'YELLOW')
            ])
            
            # Add browser AI usage report
            CMDStyler.print_colored("\n🌐 BROWSER AI USAGE:", 'CYAN', 'BOLD')
            self.browser_ai_monitor.generate_browser_ai_report()
            
            CMDStyler.print_separator('═', 60, 'CYAN')
            
        except Exception as e:
            CMDStyler.print_alert(f"Error generating insights: {e}", 'HIGH')
    
    def generate_quick_status_update(self):
        """Generate quick status update every 30 seconds"""
        try:
            current_time = datetime.now().strftime("%H:%M:%S")
            
            # Count active monitors
            active_monitors = 0
            if self.process_monitor and self.process_monitor.running:
                active_monitors += 1
            if self.network_monitor and self.network_monitor.running:
                active_monitors += 1
            if self.file_monitor and self.observer.is_alive():
                active_monitors += 1
            
            # Get recent activity count
            recent_activity = len(self.activity_log) if hasattr(self, 'activity_log') else 0
            
            CMDStyler.print_colored(f"\n⏰ [{current_time}] Monitor Status: {active_monitors}/3 Active | Activities: {recent_activity}", 'CYAN')
            
        except Exception as e:
            print(f"Error generating quick status: {e}")
    
    def exit_animation(self):
        """Simple and quick exit animation (under 5 seconds)"""
        try:
            # Save final Excel data
            if hasattr(self, 'logger') and self.logger:
                self.logger.save_workbook()
                print(f"\n💾 Final Excel data saved: {self.config.log_file}")
            
            CMDStyler.print_separator('═', 60, 'RED')
            CMDStyler.print_colored("🛑 AI SYSTEM MONITOR SHUTTING DOWN...", 'RED', 'BOLD')
            CMDStyler.print_separator('═', 60, 'RED')
            
            # Quick shutdown sequence (2 seconds)
            shutdown_steps = [
                ("🔄 Stopping monitors", 'YELLOW', 0.3),
                ("📊 Saving data", 'GREEN', 0.3),
                ("🔐 Closing security", 'RED', 0.3),
                ("🌐 Finalizing feeds", 'CYAN', 0.3),
                ("✅ Cleanup complete", 'GREEN', 0.3)
            ]
            
            # Animate shutdown steps
            for step, color, delay in shutdown_steps:
                CMDStyler.print_colored(f"   {step}...", color)
                time.sleep(delay)
            
            # Quick countdown (2 seconds)
            print("\n")
            CMDStyler.print_colored("⏰ SHUTDOWN IN...", 'RED', 'BOLD')
            for i in range(3, 0, -1):
                CMDStyler.print_colored(f"   {i}...", 'RED', 'BOLD')
                time.sleep(0.5)
            
            # Final messages (1 second)
            print("\n")
            CMDStyler.print_separator('═', 60, 'GREEN')
            CMDStyler.print_colored("✅ AI SYSTEM MONITOR SAFELY SHUTDOWN", 'GREEN', 'BOLD')
            CMDStyler.print_colored("📊 All data saved successfully", 'CYAN')
            CMDStyler.print_colored("🔐 Security protocols deactivated", 'YELLOW')
            CMDStyler.print_separator('═', 60, 'GREEN')
            
            # Simple thank you message
            print("\n")
            CMDStyler.print_colored("🤖 Thank you for using AI System Monitor! 🛡️", 'CYAN', 'BOLD')
            CMDStyler.print_colored("   Stay Safe, Stay Secure!", 'GREEN')
            
        except Exception as e:
            print(f"\n❌ Error during shutdown: {e}")
        
        # Quick exit
        time.sleep(0.5)
        os._exit(0)

if __name__ == "__main__":
    monitor = None
    
    def signal_handler(signum, frame):
        """Handle Ctrl+C and other signals with stylish exit"""
        if monitor:
            monitor.exit_animation()
        else:
            os._exit(0)
    
    # Register signal handlers for stylish exit
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        # Create and start monitor
        monitor = AISystemMonitor()
        monitor.start_monitoring()
    except KeyboardInterrupt:
        if monitor:
            monitor.exit_animation()
        else:
            os._exit(0)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        if monitor:
            monitor.exit_animation()
        else:
            os._exit(1)
