import streamlit as st
from pathlib import Path
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="File Manager", page_icon="🗂️", layout="wide")

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Syne:wght@400;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

.stApp {
    background: #0d0d0d;
    color: #e8e8e8;
}

h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
}

.big-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    color: #f0f0f0;
    letter-spacing: -1px;
    margin-bottom: 0;
}

.subtitle {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: #00e5a0;
    margin-top: 4px;
    margin-bottom: 2rem;
}

.file-card {
    background: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    margin: 4px 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: #a0a0a0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.file-card:hover {
    border-color: #00e5a0;
    color: #f0f0f0;
}

.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 2px;
    color: #00e5a0;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.success-box {
    background: #0d2a1f;
    border: 1px solid #00e5a0;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    color: #00e5a0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
}

.error-box {
    background: #2a0d0d;
    border: 1px solid #ff4d4d;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    color: #ff6b6b;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
}

.stButton > button {
    background: #00e5a0 !important;
    color: #0d0d0d !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 0.5rem 1.5rem !important;
    width: 100% !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover {
    opacity: 0.85 !important;
}

.stTextInput > div > input,
.stTextArea > div > textarea {
    background: #1a1a1a !important;
    color: #f0f0f0 !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.9rem !important;
}

.stTextInput > div > input:focus,
.stTextArea > div > textarea:focus {
    border-color: #00e5a0 !important;
    box-shadow: 0 0 0 2px rgba(0,229,160,0.15) !important;
}

.stRadio > div {
    gap: 0.5rem !important;
}

[data-testid="stSidebar"] {
    background: #111111 !important;
    border-right: 1px solid #1f1f1f !important;
}

.stSelectbox > div > div {
    background: #1a1a1a !important;
    color: #f0f0f0 !important;
    border: 1px solid #2a2a2a !important;
}

div[data-testid="metric-container"] {
    background: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    padding: 0.75rem;
}
</style>
""", unsafe_allow_html=True)


# ── Helpers ───────────────────────────────────────────────────────────────────
def get_all_items():
    p = Path('.')
    return list(p.rglob('*'))

def msg_success(text):
    st.markdown(f'<div class="success-box">✓ &nbsp;{text}</div>', unsafe_allow_html=True)

def msg_error(text):
    st.markdown(f'<div class="error-box">✗ &nbsp;{text}</div>', unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="big-title">🗂️ FileSys</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">// file handling system</div>', unsafe_allow_html=True)

    operation = st.radio(
        "OPERATION",
        ["📄 Create File", "👁️ Read File", "✏️ Update File", "🗑️ Delete File",
         "✏️ Rename File", "📁 Create Folder", "🗑️ Delete Folder", "📄 File in Folder"],
        label_visibility="visible"
    )

    st.divider()
    st.markdown('<div class="section-label">Explorer</div>', unsafe_allow_html=True)
    items = get_all_items()
    files  = [i for i in items if i.is_file()]
    folders = [i for i in items if i.is_dir()]

    col1, col2 = st.columns(2)
    col1.metric("Files", len(files))
    col2.metric("Folders", len(folders))

    if st.button("🔄 Refresh", key="refresh_sidebar"):
        st.rerun()

    st.markdown('<div class="section-label" style="margin-top:1rem">All Items</div>', unsafe_allow_html=True)
    for item in items[:30]:
        icon = "📁" if item.is_dir() else "📄"
        st.markdown(f'<div class="file-card">{icon} {item}</div>', unsafe_allow_html=True)
    if len(items) > 30:
        st.caption(f"… and {len(items)-30} more")


# ── Main panel ────────────────────────────────────────────────────────────────
op = operation.split(" ", 1)[1].strip()   # strip emoji
st.markdown(f'<div class="section-label">{op}</div>', unsafe_allow_html=True)
st.markdown(f"## {operation}")

# ─── Create File ──────────────────────────────────────────────────────────────
if op == "Create File":
    file_name = st.text_input("File name", placeholder="e.g. notes.txt")
    content   = st.text_area("File content", placeholder="Type your content here…", height=180)
    if st.button("Create File"):
        if not file_name:
            msg_error("Please enter a file name.")
        else:
            p = Path(file_name)
            if p.exists():
                msg_error("File already exists!")
            else:
                try:
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(content)
                    msg_success(f"File **{file_name}** created successfully!")
                except Exception as e:
                    msg_error(str(e))

# ─── Read File ────────────────────────────────────────────────────────────────
elif op == "Read File":
    file_name = st.text_input("File name", placeholder="e.g. notes.txt")
    if st.button("Read File"):
        if not file_name:
            msg_error("Please enter a file name.")
        else:
            p = Path(file_name)
            if p.exists() and p.is_file():
                content = p.read_text()
                st.markdown('<div class="section-label">Content</div>', unsafe_allow_html=True)
                st.code(content, language="text")
            else:
                msg_error("File not found!")

# ─── Update File ──────────────────────────────────────────────────────────────
elif op == "Update File":
    file_name = st.text_input("File name", placeholder="e.g. notes.txt")
    mode      = st.radio("Update mode", ["Overwrite", "Append"], horizontal=True)
    new_content = st.text_area("New content", height=160)
    if st.button("Update File"):
        if not file_name:
            msg_error("Please enter a file name.")
        else:
            p = Path(file_name)
            if p.exists() and p.is_file():
                try:
                    write_mode = 'w' if mode == "Overwrite" else 'a'
                    with open(file_name, write_mode) as f:
                        f.write(new_content)
                    msg_success(f"File **{file_name}** updated ({mode.lower()})!")
                except Exception as e:
                    msg_error(str(e))
            else:
                msg_error("File not found!")

# ─── Delete File ──────────────────────────────────────────────────────────────
elif op == "Delete File":
    file_name = st.text_input("File name", placeholder="e.g. notes.txt")
    if st.button("🗑️ Delete File", type="primary"):
        if not file_name:
            msg_error("Please enter a file name.")
        else:
            p = Path(file_name)
            if p.exists() and p.is_file():
                try:
                    os.remove(p)
                    msg_success(f"File **{file_name}** deleted.")
                except Exception as e:
                    msg_error(str(e))
            else:
                msg_error("File not found!")

# ─── Rename File ──────────────────────────────────────────────────────────────
elif op == "Rename File":
    file_name = st.text_input("Current file name", placeholder="e.g. old.txt")
    new_name  = st.text_input("New file name",     placeholder="e.g. new.txt")
    if st.button("Rename File"):
        if not file_name or not new_name:
            msg_error("Please fill in both fields.")
        else:
            p = Path(file_name)
            if p.exists():
                try:
                    p.rename(new_name)
                    msg_success(f"Renamed **{file_name}** → **{new_name}**")
                except Exception as e:
                    msg_error(str(e))
            else:
                msg_error("File not found!")

# ─── Create Folder ────────────────────────────────────────────────────────────
elif op == "Create Folder":
    folder_name = st.text_input("Folder name", placeholder="e.g. my_folder")
    if st.button("Create Folder"):
        if not folder_name:
            msg_error("Please enter a folder name.")
        else:
            p = Path(folder_name)
            if p.exists():
                msg_error("Folder already exists!")
            else:
                try:
                    os.mkdir(folder_name)
                    msg_success(f"Folder **{folder_name}** created!")
                except Exception as e:
                    msg_error(str(e))

# ─── Delete Folder ────────────────────────────────────────────────────────────
elif op == "Delete Folder":
    folder_name = st.text_input("Folder name", placeholder="e.g. my_folder")
    if st.button("🗑️ Delete Folder", type="primary"):
        if not folder_name:
            msg_error("Please enter a folder name.")
        else:
            p = Path(folder_name)
            if p.exists() and p.is_dir():
                try:
                    p.rmdir()
                    msg_success(f"Folder **{folder_name}** deleted.")
                except Exception as e:
                    msg_error(f"Could not delete: {e} (folder may not be empty)")
            else:
                msg_error("Folder not found!")

# ─── File in Folder ───────────────────────────────────────────────────────────
elif op == "File in Folder":
    folder_name = st.text_input("Folder name", placeholder="e.g. my_folder")
    file_name   = st.text_input("File name",   placeholder="e.g. notes.txt")
    content     = st.text_area("File content", height=160)
    if st.button("Create File in Folder"):
        if not folder_name or not file_name:
            msg_error("Please fill in both folder and file name.")
        else:
            p = Path(folder_name) / file_name
            if p.exists():
                msg_error("File already exists!")
            else:
                try:
                    Path(folder_name).mkdir(parents=True, exist_ok=True)
                    p.write_text(content)
                    msg_success(f"File **{p}** created!")
                except Exception as e:
                    msg_error(str(e))