#!/usr/bin/env python3
"""
Test script to verify Excel logging is working
"""

import sys
import os
from datetime import datetime

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from sm import AIEventLogger, AIMonitorConfig
    print("✅ Successfully imported AI monitoring modules")
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    sys.exit(1)

def test_excel_logging():
    """Test Excel logging functionality"""
    print("🧪 Testing Excel Logging...")
    print("=" * 50)
    
    try:
        # Create config and logger
        config = AIMonitorConfig()
        logger = AIEventLogger(config)
        
        print(f"📄 Excel file path: {os.path.abspath(config.log_file)}")
        
        # Test basic logging
        print("\n📝 Testing basic event logging...")
        logger.log_event(
            "Test Event",
            "This is a test event to verify Excel logging is working",
            "test_process.exe",
            "https://test.com",
            "Low"
        )
        
        print("✅ Basic event logged successfully")
        
        # Test AI website logging
        print("\n🤖 Testing AI website logging...")
        logger.log_event(
            "Browser AI Usage",
            "User accessed AI website: ChatGPT (LLM) - Detection: AI TLD: .ai, AI domain keyword: perplexity",
            "chrome.exe",
            "https://www.perplexity.ai",
            "Medium"
        )
        
        print("✅ AI website event logged successfully")
        
        # Test high-risk event logging
        print("\n🚨 Testing high-risk event logging...")
        logger.log_event(
            "Honeypot Triggered",
            "User accessed AI website: Unknown AI Tool (AI Platform) - Detection: AI pattern: chat",
            "powershell.exe",
            "https://suspicious-ai-tool.com",
            "High"
        )
        
        print("✅ High-risk event logged successfully")
        
        # Test critical event logging
        print("\n🔴 Testing critical event logging...")
        logger.log_event(
            "Security Incident",
            "UNAUTHORIZED AI TOOL ACCESS - Honeypot decoy triggered by suspicious process",
            "unknown_process.exe",
            "C:\\Users\\Public\\Desktop\\FAKE_AI_TOOL.exe",
            "Critical"
        )
        
        print("✅ Critical event logged successfully")
        
        # Force save the workbook
        print("\n💾 Saving Excel workbook...")
        logger.save_workbook()
        
        print("✅ Workbook saved successfully")
        
        # Check if file exists and has content
        if os.path.exists(config.log_file):
            file_size = os.path.getsize(config.log_file)
            print(f"📊 Excel file exists with size: {file_size} bytes")
            
            if file_size > 0:
                print("✅ Excel file contains data")
                
                # Try to open and verify content
                try:
                    import openpyxl
                    wb = openpyxl.load_workbook(config.log_file)
                    sheet = wb.active
                    
                    print(f"📋 Sheet name: {sheet.title}")
                    print(f"📊 Max row: {sheet.max_row}")
                    print(f"📊 Max column: {sheet.max_column}")
                    
                    if sheet.max_row > 1:  # More than just header
                        print("✅ Data found in Excel sheet")
                        
                        # Print first few rows
                        print("\n📄 First few rows of data:")
                        for row in range(1, min(sheet.max_row + 1, 6)):
                            row_data = []
                            for col in range(1, min(sheet.max_column + 1, 6)):
                                cell_value = sheet.cell(row=row, column=col).value
                                row_data.append(str(cell_value) if cell_value else "")
                            print(f"  Row {row}: {' | '.join(row_data)}")
                    else:
                        print("⚠️  No data rows found in Excel sheet")
                
                except Exception as e:
                    print(f"❌ Error reading Excel file: {e}")
            else:
                print("❌ Excel file is empty (0 bytes)")
        else:
            print(f"❌ Excel file does not exist at: {config.log_file}")
        
        print("\n" + "=" * 50)
        print("🎯 Excel Logging Test Complete!")
        print(f"📁 Check the Excel file: {config.log_file}")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

def test_manual_ai_detection():
    """Test manual AI detection simulation"""
    print("\n🔍 Testing Manual AI Detection Simulation...")
    print("=" * 50)
    
    try:
        config = AIMonitorConfig()
        logger = AIEventLogger(config)
        
        # Simulate various AI activities
        test_events = [
            {
                "type": "Browser AI Usage",
                "description": "User accessed AI website: ChatGPT (LLM) - Detection: AI domain keyword: chatgpt",
                "process": "chrome.exe",
                "url": "https://chat.openai.com",
                "risk": "Medium"
            },
            {
                "type": "File Access",
                "description": "User accessed AI file - Content contains: tensorflow, numpy",
                "process": "python.exe",
                "url": "C:\\Users\\Test\\ai_model.py",
                "risk": "Low"
            },
            {
                "type": "Browser AI Usage",
                "description": "User accessed AI website: Claude (LLM) - Detection: AI TLD: .ai",
                "process": "firefox.exe",
                "url": "https://claude.ai",
                "risk": "Medium"
            },
            {
                "type": "Browser AI Usage",
                "description": "User accessed AI website: Midjourney (Media Generation) - Detection: AI domain keyword: midjourney",
                "process": "msedge.exe",
                "url": "https://www.midjourney.com",
                "risk": "Medium"
            },
            {
                "type": "Process Activity",
                "description": "AI process detected - TensorFlow model training in progress",
                "process": "python.exe",
                "url": "",
                "risk": "Low"
            }
        ]
        
        for i, event in enumerate(test_events, 1):
            print(f"\n📝 Logging test event {i}/{len(test_events)}: {event['type']}")
            logger.log_event(
                event["type"],
                event["description"],
                event["process"],
                event["url"],
                event["risk"]
            )
        
        # Save after all events
        logger.save_workbook()
        print(f"\n✅ All {len(test_events)} test events logged and saved")
        
    except Exception as e:
        print(f"❌ Error in manual detection test: {e}")

if __name__ == "__main__":
    test_excel_logging()
    test_manual_ai_detection()
    
    print("\n" + "=" * 50)
    print("🎯 To verify Excel logging:")
    print("1. Open the Excel file: ai_monitor_log.xlsx")
    print("2. Check if data appears in the sheet")
    print("3. Look for the test events we just logged")
    print("4. Verify all 15 columns are populated")
    print("5. Check the AI_Summary sheet for statistics")
