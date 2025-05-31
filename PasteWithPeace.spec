# PasteWithPeace.spec

from PyInstaller.utils.hooks import collect_submodules
import os

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[('config.json', '.')],  # Optional: just copies it alongside exe
    hiddenimports=collect_submodules('paste_with_peace') 
        + collect_submodules('plyer.platforms')
        + [
        'pyperclip',
        'plyer',
        'pystray',
        'Pillow',
        'keyboard',
        'pygetwindow',
        'pywin32',
        'pyautogui',
        'customtkinter',
        'CTkMessagebox',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
)



pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PasteWithPeace',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='PasteWithPeace'
)
