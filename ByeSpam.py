import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pytesseract
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# ========================= APP RESOURCE HELPER =========================
def resource_path(relative_path):
    """Get absolute path to resource, works for dev & for PyInstaller .exe"""
    import sys, os
    try:
        base_path = sys._MEIPASS  # folder created by PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def train_model():
    try:
        df = pd.read_csv(resource_path("spam.csv"), encoding="latin-1")

        possible_label_cols = [c for c in df.columns if "label" in c.lower() or "category" in c.lower() or c.lower() == "v1"]
        possible_text_cols = [c for c in df.columns if "message" in c.lower() or "text" in c.lower() or c.lower() == "v2"]

        if not possible_label_cols or not possible_text_cols:
            possible_label_cols = [df.columns[0]]
            possible_text_cols = [df.columns[1]]

        label_col = possible_label_cols[0]
        text_col = possible_text_cols[0]

        df = df[[label_col, text_col]]
        df.columns = ['label', 'message']
        df['label'] = df['label'].map(lambda x: 'Spam' if 'spam' in str(x).lower() else 'Not Spam')

        tfidf = TfidfVectorizer(stop_words='english', lowercase=True, max_features=3000)
        X = tfidf.fit_transform(df['message'])

        nb = MultinomialNB(alpha=0.5)
        nb.fit(X, df['label'])
        print("✅ Model trained successfully from spam.csv")
        return tfidf, nb
    except Exception as e:
        import sys
        messagebox.showerror("Error", f"⚠️ Error loading spam.csv: {e}")
        sys.exit()



# ========================= HELPERS =========================
def predict_text(text, tfidf, nb):
    X_test = tfidf.transform([text])
    return nb.predict(X_test)[0]


def recognize_text(image_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text if text.strip() else "Could not read any text."
    except Exception as e:
        return f"Could not process image: {e}"


tfidf, nb = train_model()


# ========================= FUNCTIONS =========================
def analyze_text_input():
    text = text_box.get("1.0", tk.END).strip()
    if not text or text == placeholder_text:
        messagebox.showwarning("Empty Input", "Please enter some text for analysis.")
        return
    result = predict_text(text, tfidf, nb)
    update_result_box(result, text)
    show_prediction_graph(result)


def analyze_image_input():
    file_path = filedialog.askopenfilename(
        title="Select Email Screenshot",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    if not file_path:
        return
    text = recognize_text(file_path)
    if "Could not" in text:
        messagebox.showinfo("OCR Result", "No readable text found in the image.")
        return
    result = predict_text(text, tfidf, nb)
    update_result_box(result, text)
    show_prediction_graph(result)


def update_result_box(result, text):
    result_box.config(state='normal')
    result_box.delete("1.0", tk.END)
    preview = text[:200] + "..." if len(text) > 200 else text
    result_box.insert(tk.END, f"Extracted Text (partial):\n{preview}\n\n", "normal")
    result_box.insert(tk.END, f"Result: {result}", "spam" if result == "Spam" else "safe")

    # Modern aesthetic colors
    result_box.tag_config("spam", foreground="#FF5C5C", font=("Segoe UI", 14, "bold"))
    result_box.tag_config("safe", foreground="#4AE686", font=("Segoe UI", 14, "bold"))
    result_box.tag_config("normal", foreground="white", font=("Consolas", 10))
    result_box.config(state='disabled')


class CustomScrolledText(ScrolledText):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.vbar.config(bg="#343541", troughcolor="#343541", activebackground="white", width=12, elementborderwidth=0)


# ========================= UI DESIGN =========================
root = tk.Tk()
root.title("ByeSpam — Spam Who? Never Heard of It.")
root.geometry("980x720")
root.configure(bg="#171719")

# ========================= APP ICON INIT =========================
# Works for both .py and .exe builds
try:
    icon_path = resource_path("imgs/ByeSpamIcon.ico")
    root.iconbitmap(icon_path)
except Exception as e:
    print("⚠️ Icon not found:", e)

# --- Top Bar ---
top_frame = tk.Frame(root, bg="#171719")
top_frame.pack(anchor="w", pady=(15, 10), padx=25)

try:
    # ✅ Use resource_path here so it works in the .exe
    icon_img = Image.open(resource_path("imgs/ByeSpamIcon2.jpg")).resize((40, 40))
    icon_photo = ImageTk.PhotoImage(icon_img)
    tk.Label(top_frame, image=icon_photo, bg="#171719").pack(side="left", padx=(0, 10))
except Exception as e:
    print("⚠️ Top-bar icon not found:", e)
    tk.Label(top_frame, text="⚪", bg="#171719", fg="white", font=("Segoe UI", 16)).pack(side="left", padx=(0, 10))

tk.Label(top_frame, text="ByeSpam", font=("Segoe UI", 25, "bold"), bg="#171719", fg="white").pack(side="left")


# --- Text Input Area ---
text_frame = tk.Frame(root, bg="#171719")
text_frame.pack(padx=40, pady=10, fill="x")

text_box = CustomScrolledText(
    text_frame, wrap=tk.WORD, width=80, height=10, font=("Consolas", 10),
    bg="#000000", fg="white", insertbackground="white",
    relief="solid", bd=2, highlightbackground="#888888", highlightthickness=2
)
text_box.pack(fill="x", ipady=5)

# Placeholder logic
placeholder_text = "Paste text here..."
text_box.insert("1.0", placeholder_text)
text_box.config(fg="gray")

def on_focus_in(event):
    if text_box.get("1.0", tk.END).strip() == placeholder_text:
        text_box.delete("1.0", tk.END)
        text_box.config(fg="white")

def on_focus_out(event):
    if text_box.get("1.0", tk.END).strip() == "":
        text_box.insert("1.0", placeholder_text)
        text_box.config(fg="gray")

text_box.bind("<FocusIn>", on_focus_in)
text_box.bind("<FocusOut>", on_focus_out)


# Upload Button
upload_btn = tk.Button(
    text_frame,
    text="📤",
    font=("Segoe UI Emoji", 14),
    bg="#000000",
    fg="white",
    activebackground="#000000",  # background stays dark
    activeforeground="#FCA311",  # yellow when clicked
    relief="flat",
    bd=0,
    cursor="hand2",
    command=analyze_image_input
)
upload_btn.place(relx=1.0, rely=1.0, x=-15, y=-12, anchor="se")

# --- Hover Effect (only emoji color changes) ---
def on_upload_hover(event):
    upload_btn.config(fg="#FCA311")  # yellow emoji

def on_upload_leave(event):
    upload_btn.config(fg="white")  # revert to white

upload_btn.bind("<Enter>", on_upload_hover)
upload_btn.bind("<Leave>", on_upload_leave)



# --- Result + Graph Section ---
result_frame = tk.Frame(root, bg="#171719")
result_frame.pack(padx=40, pady=10, fill="both", expand=True)

result_frame.columnconfigure(0, weight=1, uniform="equal")
result_frame.columnconfigure(1, weight=1, uniform="equal")

# LEFT SIDE (Detect + Result)
left_side = tk.Frame(result_frame, bg="#171719")
left_side.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

# Detect Spam Button
detect_btn = tk.Button(
    left_side,
    text="Detect Spam",
    font=("Segoe UI", 30, "bold"),
    bg="#FCA311",
    fg="#000000",
    activebackground="#FFD166",
    activeforeground="black",
    relief="flat",
    cursor="hand2",
    height=2,
    bd=0,
    command=analyze_text_input
)
detect_btn.pack(fill="x", pady=(0, 10), ipady=3)
detect_btn.configure(highlightthickness=0)


# Result box
result_box_frame = tk.Frame(
    left_side,
    bg="#0D0D0D",
    relief="flat",
    highlightbackground="#888888",
    highlightthickness=2,
    bd=2
)
result_box_frame.pack(fill="both", expand=True)

result_label = tk.Label(result_box_frame, text="Result", font=("Segoe UI", 18, "bold"), bg="#0D0D0D", fg="white")
result_label.pack(anchor="nw", padx=10, pady=(5, 0))

separator_line = tk.Frame(result_box_frame, bg="#888888", height=2)
separator_line.pack(fill="x", padx=10, pady=(2, 5))

result_box = tk.Text(
    result_box_frame,
    wrap=tk.WORD,
    width=40,
    height=10,
    font=("Consolas", 10),
    bg="#0D0D0D",
    fg="white",
    insertbackground="white",
    relief="flat",
    bd=0,
    state='disabled'
)
result_box.pack(padx=10, pady=(0, 10), fill="both", expand=True)


# RIGHT SIDE (Accuracy Graph)
graph_frame = tk.Frame(
    result_frame,
    bg="#0D0D0D",
    relief="solid",
    bd=2,
    highlightbackground="#888888",
    highlightthickness=2
)
graph_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

# Label same as "Result" section
accuracy_label = tk.Label(graph_frame, text="Accuracy", font=("Segoe UI", 18, "bold"), bg="#0D0D0D", fg="white")
accuracy_label.pack(anchor="nw", padx=10, pady=(5, 0))

# Matching separator line
accuracy_separator = tk.Frame(graph_frame, bg="#888888", height=2)
accuracy_separator.pack(fill="x", padx=10, pady=(2, 5))



# --- Graph Function ---
def show_prediction_graph(result):
    for widget in graph_frame.winfo_children():
        if widget != accuracy_label:
            widget.destroy()

    categories = ["Spam", "Not Spam"]
    values = [1, 0] if result == "Spam" else [0, 1]

    fig = Figure(figsize=(3, 1.8), facecolor="#000000")
    ax = fig.add_subplot(111)
    ax.bar(categories, values, color=["#FF5C5C", "#4AE686"])
    ax.tick_params(colors="white")
    ax.set_facecolor("#000000")
    for spine in ax.spines.values():
        spine.set_color("white")

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, pady=(0, 5))


root.mainloop()
