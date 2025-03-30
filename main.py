#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Kumakita - AITRIOSによる物体検出と熊検出警告アプリケーション
メインエントリーポイント

作成者：AI Assistant
"""

import sys
import os

# 現在のディレクトリをパスに追加
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# デバッグ出力
print(f"Python path: {sys.path}")
print(f"Current directory: {current_dir}")

# kumaMacのUI部分をインポート
from kumaMac.ui.main_window import KumakitaApp

def main():
    """アプリケーションのエントリーポイント"""
    app = KumakitaApp()
    app.mainloop()

if __name__ == "__main__":
    main()