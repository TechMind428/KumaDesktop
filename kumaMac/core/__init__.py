"""
コアロジックモジュール

アプリケーションのコア機能を提供するモジュール
"""

from .detection_processor import DetectionProcessor
from .settings_manager import SettingsManager

__all__ = ['DetectionProcessor', 'SettingsManager']