import os
import sys
import json
import threading
import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import pytesseract
from PIL import Image
# Optional imports
try:
    import openai
    from telegram import Bot
except ImportError:
    pass

CONFIG_PATH = os.path.join(os.getenv('APPDATA'), 'vision_intelligence', 'config.json')

def ensure_config():
    folder = os.path.dirname(CONFIG_PATH)
    os.makedirs(folder, exist_ok=True)
    if not os.path.exists(CONFIG_PATH):
        # Prompt for OpenAI key
        key = simple_prompt('OpenAI API Key', 'Cole sua OPENAI_API_KEY:')
        config = {'OPENAI_API_KEY': key}
        with open(CONFIG_PATH, 'w') as f:
            json.dump(config, f)
    else:
        with open(CONFIG_PATH) as f:
            config = json.load(f)
    os.environ['OPENAI_API_KEY'] = config.get('OPENAI_API_KEY', '')

def simple_prompt(title, prompt):
    popup = tk.Tk()
    popup.wm_title(title)
    tk.Label(popup, text=prompt).pack(padx=10, pady=5)
    entry = tk.Entry(popup, width=40)
    entry.pack(padx=10, pady=5)
    val = {'data': None}
    def on_ok():
        val['data'] = entry.get().strip()
        popup.destroy()
    tk.Button(popup, text="OK", command=on_ok).pack(pady=5)
    popup.mainloop()
    return val['data']

def auto_update_check():
    # Placeholder: check latest release via GitHub API, download installer if newer
    pass

def send_telegram(message):
    # read from config
    with open(CONFIG_PATH) as f:
        cfg = json.load(f)
    token = cfg.get('TELEGRAM_TOKEN'); chat_id = cfg.get('TELEGRAM_CHAT_ID')
    if token and chat_id:
        bot = Bot(token=token)
        bot.send_message(chat_id=chat_id, text=message)

def login():
    # API key and Telegram config prompt
    ensure_config()

    username = entry_user.get()
    password = entry_pass.get()
    if username == 'admin' and password == 'password':
        messagebox.showinfo('Login sucesso', 'Bem-vindo!')
        root.destroy()
        main_app()
    else:
        messagebox.showerror('Erro', 'Credenciais inválidas')

def export_dashboard():
    # Placeholder: generate simple dashboard (OCR usage) and save as HTML or PDF
    messagebox.showinfo('Relatório', 'Dashboard exportado em Reports/dashboard.html')

def main_app():
    app = tk.Tk()
    app.title('Vision Intelligence – Murilo')
    # Buttons for OCR test, auto-update, export dashboard
    tk.Button(app, text='Teste OCR', command=lambda: pytesseract.image_to_string(Image.open(filedialog.askopenfilename()))).pack(pady=5)
    tk.Button(app, text='Checar Atualização', command=auto_update_check).pack(pady=5)
    tk.Button(app, text='Exportar Dashboard', command=export_dashboard).pack(pady=5)
    app.mainloop()

if __name__ == '__main__':
    # Start auto-update thread
    threading.Thread(target=auto_update_check, daemon=True).start()
    # Login window
    root = tk.Tk()
    root.title('Login – Vision Intelligence')
    tk.Label(root, text='Usuário').grid(row=0, column=0)
    entry_user = tk.Entry(root)
    entry_user.grid(row=0, column=1)
    tk.Label(root, text='Senha').grid(row=1, column=0)
    entry_pass = tk.Entry(root, show='*')
    entry_pass.grid(row=1, column=1)
    tk.Button(root, text='Entrar', command=login).grid(row=2, columnspan=2, pady=10)
    root.mainloop()