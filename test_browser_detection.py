#!/usr/bin/env python3
"""
Test script to debug browser detection
"""

import win32gui
import win32process
import psutil
import time

def test_browser_detection():
    """Test browser window detection"""
    print("🔍 Testing Browser Detection...")
    print("=" * 50)
    
    def enum_windows_callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            class_name = win32gui.GetClassName(hwnd)
            
            print(f"\nWindow Found:")
            print(f"  Title: {window_title}")
            print(f"  Class: {class_name}")
            
            # Check if it's a browser
            browser_patterns = {
                'chrome': ['chrome_widgetwin_1', 'chrome'],
                'firefox': ['mozilla', 'firefox'],
                'edge': ['msedge', 'edge', 'chromium'],
                'opera': ['opera'],
                'brave': ['brave'],
                'ie': ['ieframe']
            }
            
            detected_browser = None
            for browser, patterns in browser_patterns.items():
                if any(pattern in class_name.lower() for pattern in patterns):
                    detected_browser = browser
                    break
            
            if detected_browser:
                print(f"  🌐 Browser Type: {detected_browser}")
                
                try:
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    print(f"  PID: {pid}")
                    
                    process = psutil.Process(pid)
                    process_name = process.name()
                    print(f"  Process: {process_name}")
                    
                    # Check for AI keywords in title
                    ai_keywords = ['chatgpt', 'claude', 'gemini', 'bard', 'copilot', 'openai', 'anthropic']
                    title_lower = window_title.lower()
                    
                    for keyword in ai_keywords:
                        if keyword in title_lower:
                            print(f"  🤖 AI Keyword Found: {keyword}")
                            
                            # Try to infer URL
                            if 'chatgpt' in title_lower or 'chat.openai.com' in title_lower:
                                print(f"  🔗 Likely URL: https://chat.openai.com")
                            elif 'claude' in title_lower or 'claude.ai' in title_lower:
                                print(f"  🔗 Likely URL: https://claude.ai")
                            elif 'gemini' in title_lower or 'bard' in title_lower:
                                print(f"  🔗 Likely URL: https://gemini.google.com")
                            break
                    
                    windows.append({
                        'hwnd': hwnd,
                        'pid': pid,
                        'process_name': process_name,
                        'title': window_title,
                        'class_name': class_name,
                        'browser_type': detected_browser
                    })
                    
                except Exception as e:
                    print(f"  ❌ Error getting process info: {e}")
            else:
                print(f"  ❓ Not a recognized browser")
        
        return True
    
    print("\nScanning for browser windows...")
    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    
    print(f"\n" + "=" * 50)
    print(f"Found {len(windows)} browser windows")
    
    if windows:
        print("\n📊 Summary:")
        for window in windows:
            print(f"  • {window['browser_type']} ({window['process_name']}) - {window['title'][:50]}...")
    else:
        print("\n❌ No browser windows detected!")
        print("\n💡 Tips:")
        print("  1. Make sure a browser is open")
        print("  2. Try opening a new tab")
        print("  3. Check if browser is running as administrator")
        print("  4. Try with Chrome, Firefox, or Edge")

def test_edge_specifically():
    """Test Edge browser specifically"""
    print("\n🔍 Testing Edge Browser Specifically...")
    print("=" * 50)
    
    # Look for Edge processes
    edge_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if 'msedge' in proc.info['name'].lower():
                edge_processes.append(proc.info)
                print(f"Found Edge Process:")
                print(f"  PID: {proc.info['pid']}")
                print(f"  Name: {proc.info['name']}")
                if proc.info['cmdline']:
                    print(f"  Command: {' '.join(proc.info['cmdline'][:3])}...")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    print(f"\nFound {len(edge_processes)} Edge processes")
    
    if edge_processes:
        print("\n✅ Edge is running! The AI monitor should detect it.")
    else:
        print("\n❌ Edge is not running or not accessible.")
        print("\n💡 Try:")
        print("  1. Open Edge browser")
        print("  2. Navigate to an AI website like chat.openai.com")
        print("  3. Run this test again")

if __name__ == "__main__":
    test_browser_detection()
    test_edge_specifically()
    
    print("\n" + "=" * 50)
    print("🎯 Next Steps:")
    print("1. If browsers are detected, the AI monitor should work")
    print("2. Open Edge and go to chat.openai.com")
    print("3. Run the main AI monitor: python sm.py")
    print("4. Look for debug messages showing browser detection")
