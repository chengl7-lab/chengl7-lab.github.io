#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import webbrowser
from threading import Timer

PORT = 8000

class AutoReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and (event.src_path.endswith('.md') or 
                                     event.src_path.endswith('.html') or 
                                     event.src_path.endswith('.css') or 
                                     event.src_path.endswith('.js')):
            print(f"\nFile changed: {event.src_path}")
            print("Changes detected! Refresh your browser to see updates.")

def open_browser():
    webbrowser.open(f'http://localhost:{PORT}')

if __name__ == "__main__":
    try:
        # Change to the repository root directory
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # Set up the file watcher
        event_handler = AutoReloadHandler()
        observer = Observer()
        observer.schedule(event_handler, path='.', recursive=True)
        observer.start()

        # Set up the server
        Handler = http.server.SimpleHTTPRequestHandler
        Handler.extensions_map.update({
            '.md': 'text/markdown',
            '': 'application/octet-stream',
        })

        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"\n🚀 Development server started at http://localhost:{PORT}")
            print("📁 Serving files from:", os.getcwd())
            print("\n✨ Features:")
            print("   - Auto-detection of file changes")
            print("   - Proper handling of markdown files")
            print("   - Browser will open automatically")
            print("\n📝 Instructions:")
            print("   - Edit your files as normal")
            print("   - When you save changes, refresh your browser")
            print("   - Press Ctrl+C to stop the server")
            
            # Open browser after a short delay
            Timer(1.5, open_browser).start()
            
            # Start the server
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping development server...")
        observer.stop()
        observer.join()
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        observer.stop()
        observer.join()
        sys.exit(1) 