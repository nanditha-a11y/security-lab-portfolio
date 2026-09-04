import xml.etree.ElementTree as ET
from collections import Counter
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def parse_events_detailed(file_path):
    """Parses XML event logs into structured record dictionaries."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read log file: {e}")
        return []

    parsed_records = []
    for event in root.findall('Event'):
        event_id_elem = event.find('.//EventID')
        if event_id_elem is None:
            continue
            
        event_id = event_id_elem.text
        data_fields = {}
        for data in event.findall('.//Data'):
            name = data.get('Name')
            if name:
                data_fields[name] = data.text
                
        record = {
            'event_id': event_id,
            'user': data_fields.get('TargetUserName') or data_fields.get('SubjectUserName') or 'N/A',
            'ip': data_fields.get('IpAddress', 'N/A'),
            'process': data_fields.get('NewProcessName', 'N/A'),
            'parent_process': data_fields.get('ParentProcessName', 'N/A')
        }
        parsed_records.append(record)
        
    return parsed_records

def detect_brute_force(records, threshold=5):
    """Detects repeated failed logins from an IP and checks for eventual success."""
    failed_counts = Counter()
    successful_ips = set()
    user_map = {}

    for r in records:
        ip = r['ip']
        if ip == 'N/A':
            continue
            
        if r['event_id'] == '4625':
            failed_counts[ip] += 1
            user_map[ip] = r['user']
        elif r['event_id'] == '4624':
            successful_ips.add(ip)

    alerts = []
    for ip, count in failed_counts.items():
        if count >= threshold:
            alerts.append({
                'type': 'Possible Brute Force',
                'user': user_map.get(ip, 'Unknown'),
                'ip': ip,
                'failed_attempts': count,
                'successful_login': 'YES' if ip in successful_ips else 'NO'
            })
    return alerts

def detect_suspicious_processes(records):
    """Flags PowerShell executions requiring investigation."""
    alerts = []
    for r in records:
        if r['event_id'] == '4688':
            process_path = r['process'].lower()
            if 'powershell.exe' in process_path:
                alerts.append({
                    'type': 'Suspicious Process',
                    'user': r['user'],
                    'process': r['process'].split('\\')[-1],
                    'parent': r['parent_process'].split('\\')[-1]
                })
    return alerts

class LogAnalyzerGUI:
    def __init__(self, root, file_path):
        self.root = root
        self.root.title("Windows Log Analyzer Dashboard")
        self.root.geometry("680x670")
        self.root.configure(bg="#f4f6f9")
        self.current_file = file_path
        
        self.build_ui()
        self.analyze_and_display(file_path)

    def build_ui(self):
        # Header Banner
        header = tk.Frame(self.root, bg="#1e293b", padx=15, pady=15)
        header.pack(fill="x")
        
        title_label = tk.Label(
            header, 
            text="WINDOWS LOG ANALYZER", 
            font=("Segoe UI", 16, "bold"), 
            fg="white", 
            bg="#1e293b"
        )
        title_label.pack()

        # Top Button Toolbar
        toolbar = tk.Frame(self.root, bg="#f4f6f9", padx=20, pady=10)
        toolbar.pack(fill="x")

        open_btn = tk.Button(
            toolbar, 
            text="Open XML Log File", 
            font=("Segoe UI", 9, "bold"), 
            bg="#2563eb", 
            fg="white", 
            padx=10, 
            pady=4, 
            command=self.open_file
        )
        open_btn.pack(side="left")

        export_btn = tk.Button(
            toolbar, 
            text="Export Report (.txt)", 
            font=("Segoe UI", 9, "bold"), 
            bg="#059669", 
            fg="white", 
            padx=10, 
            pady=4, 
            command=self.export_report
        )
        export_btn.pack(side="right")

        # Main Workspace Container
        self.main_frame = tk.Frame(self.root, bg="#f4f6f9", padx=20, pady=5)
        self.main_frame.pack(fill="both", expand=True)

    def analyze_and_display(self, file_path):
        # Clear workspace for refresh
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.records = parse_events_detailed(file_path)
        self.brute_alerts = detect_brute_force(self.records, threshold=5)
        self.proc_alerts = detect_suspicious_processes(self.records)

        # 1. Summary Block
        counts = Counter([r['event_id'] for r in self.records])
        
        summary_frame = tk.LabelFrame(
            self.main_frame, 
            text=" Event Summary ", 
            font=("Segoe UI", 10, "bold"), 
            bg="#f4f6f9", 
            padx=10, 
            pady=10
        )
        summary_frame.pack(fill="x", pady=(0, 15))

        stats_text = (
            f"Total Events: {len(self.records)}   |   "
            f"Successful Logons (4624): {counts.get('4624', 0)}   |   "
            f"Failed Logons (4625): {counts.get('4625', 0)}   |   "
            f"Process Creations (4688): {counts.get('4688', 0)}"
        )
        tk.Label(
            summary_frame, 
            text=stats_text, 
            font=("Segoe UI", 9), 
            bg="#f4f6f9"
        ).pack(anchor="w")

        # 2. Suspicious Activity Scroll Box
        alert_frame = tk.LabelFrame(
            self.main_frame, 
            text=" Suspicious Activity ", 
            font=("Segoe UI", 10, "bold"), 
            fg="#b91c1c", 
            bg="#f4f6f9", 
            padx=10, 
            pady=10
        )
        alert_frame.pack(fill="x", pady=(0, 15))

        text_scroll = ttk.Scrollbar(alert_frame)
        text_scroll.pack(side="right", fill="y")

        alert_box = tk.Text(
            alert_frame, 
            wrap="word", 
            font=("Consolas", 10), 
            bg="#ffffff", 
            relief="solid", 
            bd=1,
            height=11,
            yscrollcommand=text_scroll.set
        )
        alert_box.pack(fill="both", expand=True)
        text_scroll.config(command=alert_box.yview)

        if not self.brute_alerts and not self.proc_alerts:
            alert_box.insert("end", "No suspicious activity detected.\n")
        else:
            for alert in self.brute_alerts:
                alert_box.insert("end", f"[!] {alert['type']}\n", "warning")
                alert_box.insert("end", f"    User            : {alert['user']}\n")
                alert_box.insert("end", f"    Source IP       : {alert['ip']}\n")
                alert_box.insert("end", f"    Failed Attempts : {alert['failed_attempts']}\n")
                alert_box.insert("end", f"    Successful Login: {alert['successful_login']}\n\n")

            for alert in self.proc_alerts:
                alert_box.insert("end", f"[!] {alert['type']}\n", "warning")
                alert_box.insert("end", f"    User   : {alert['user']}\n")
                alert_box.insert("end", f"    Process: {alert['process']}\n")
                alert_box.insert("end", f"    Parent : {alert['parent']}\n\n")

        alert_box.tag_config("warning", foreground="#b91c1c", font=("Consolas", 10, "bold"))
        alert_box.config(state="disabled")

        # 3. Recommendation Box
        rec_frame = tk.LabelFrame(
            self.main_frame, 
            text=" Recommendation ", 
            font=("Segoe UI", 10, "bold"), 
            bg="#f4f6f9", 
            padx=10, 
            pady=10
        )
        rec_frame.pack(fill="x")

        rec_text = "Investigate the source IP and PowerShell execution." if (self.brute_alerts or self.proc_alerts) else "No immediate action required."
        tk.Label(
            rec_frame, 
            text=rec_text, 
            font=("Segoe UI", 9, "bold"), 
            fg="#1d4ed8" if (self.brute_alerts or self.proc_alerts) else "#15803d", 
            bg="#f4f6f9"
        ).pack(anchor="w")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Windows Event Log XML",
            filetypes=[("XML files", "*.xml"), ("All files", "*.*")]
        )
        if file_path:
            self.current_file = file_path
            self.analyze_and_display(file_path)

    def export_report(self):
        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save Analysis Report"
        )
        if save_path:
            counts = Counter([r['event_id'] for r in self.records])
            with open(save_path, "w", encoding="utf-8") as f:
                f.write("================================\n")
                f.write("   WINDOWS LOG ANALYZER REPORT  \n")
                f.write("================================\n\n")
                f.write(f"Total Events: {len(self.records)}\n\n")
                f.write("Event Summary:\n")
                f.write(f"4624  Successful Logons : {counts.get('4624', 0)}\n")
                f.write(f"4625  Failed Logons     : {counts.get('4625', 0)}\n")
                f.write(f"4688  Process Creation  : {counts.get('4688', 0)}\n\n")
                f.write("--------------------------------\n")
                f.write("SUSPICIOUS ACTIVITY\n")
                f.write("--------------------------------\n")
                for alert in self.brute_alerts:
                    f.write(f"\n[!] {alert['type']}\n")
                    f.write(f"User: {alert['user']}\n")
                    f.write(f"Source IP: {alert['ip']}\n")
                    f.write(f"Failed Attempts: {alert['failed_attempts']}\n")
                    f.write(f"Successful Login: {alert['successful_login']}\n")
                for alert in self.proc_alerts:
                    f.write(f"\n[!] {alert['type']}\n")
                    f.write(f"User: {alert['user']}\n")
                    f.write(f"Process: {alert['process']}\n")
                    f.write(f"Parent: {alert['parent']}\n")
                f.write("\n--------------------------------\n")
                f.write("RECOMMENDATION\n")
                f.write("--------------------------------\n")
                f.write("Investigate the source IP and PowerShell execution.\n" if (self.brute_alerts or self.proc_alerts) else "No immediate action required.\n")
            
            messagebox.showinfo("Success", f"Report saved successfully:\n{save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LogAnalyzerGUI(root, "sample_logs.xml")
    root.mainloop()