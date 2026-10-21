from typing import Callable
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from app.ui.components.activity import Activity


class StatBox(QWidget):
    def __init__(self, value: str, label: str, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        container = QWidget()
        container.setObjectName("statBoxContainer")
        container.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        # Removed border-radius for sharp edges
        container.setStyleSheet("""
            QWidget#statBoxContainer {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 10, 16, 10)
        layout.setSpacing(2)

        value_label = QLabel(value)
        value_label.setStyleSheet("font-size: 28px; font-weight: 600; color: #000000; border: none; background: transparent;")
        layout.addWidget(value_label)

        title_label = QLabel(label)
        title_label.setStyleSheet("font-size: 12px; color: #878787; border: none; background: transparent;")
        layout.addWidget(title_label)

        main_layout.addWidget(container)


class ActivityItem(QWidget):
    def __init__(self, title: str, subtitle: str, time_text: str, parent=None):
        super().__init__(parent)
        self.setFixedHeight(54)
        self.setStyleSheet("QWidget { background-color: transparent; border: none; }")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 6, 15, 6)
        layout.setSpacing(12)

        indicator = QLabel()
        indicator.setFixedSize(30, 30)
        # Removed border-radius so the indicator is a sharp square
        indicator.setStyleSheet("background-color: #2d8cff; border: none;")
        layout.addWidget(indicator, alignment=Qt.AlignmentFlag.AlignVCenter)

        text_col = QWidget()
        text_col.setStyleSheet("background: transparent; border: none;")
        text_col.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        text_col_layout = QVBoxLayout(text_col)
        text_col_layout.setContentsMargins(0, 0, 0, 0)
        text_col_layout.setSpacing(0)

        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 16px; color: #000000; border: none; background: transparent;")
        text_col_layout.addWidget(title_label)

        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet("font-size: 12px; color: #878787; border: none; background: transparent;")
        text_col_layout.addWidget(subtitle_label)

        layout.addWidget(text_col, 1)

        time_label = QLabel(time_text)
        time_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        time_label.setStyleSheet("font-size: 12px; color: #878787; border: none; background: transparent;")
        layout.addWidget(time_label)


class MainActivity(Activity):
    """**Main Page**"""

    def __init__(self, navigate: Callable, parent=None) -> None:
        """Initialize the Main Page Activity"""
        super().__init__(parent=parent, activity="Main", navigate=navigate)

        main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(30)

        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(20)
        stats_layout.addWidget(StatBox("156", "Users"))
        stats_layout.addWidget(StatBox("3", "Devices"))
        stats_layout.addWidget(StatBox("1.3K", "Logs"))
        stats_layout.addWidget(StatBox("4", "Department"))
        main_layout.addLayout(stats_layout)

        recent_activities_box = QWidget()
        recent_activities_box.setObjectName("recentActivitiesBox")
        # Removed border-radius for sharp edges
        recent_activities_box.setStyleSheet("""
            QWidget#recentActivitiesBox {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)

        recent_activities_layout = QVBoxLayout(recent_activities_box)
        recent_activities_layout.setContentsMargins(0, 0, 0, 0)
        recent_activities_layout.setSpacing(0)

        header_label = QLabel("Recent Activities")
        header_label.setFixedHeight(30)
        header_label.setStyleSheet(
            """
            font-size: 16px;
            font-weight: bold;
            padding-left: 15px;
            border-bottom: 1px solid #d9d9d9;
            background-color: transparent;
            """
        )
        recent_activities_layout.addWidget(header_label)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        scroll_content = QWidget()
        scroll_content.setStyleSheet("background-color: transparent; border: none;")
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(0)

        activities_data = [
            ("John Doe checked in", "Operational Department", "9:00 AM · Today"),
            ("Sarah Smith checked out", "HR Department", "5:30 PM · Today"),
            ("Device Office-1 synced logs", "System", "10:00 AM · Today"),
        ]

        for title, subtitle, time_text in activities_data:
            scroll_layout.addWidget(ActivityItem(title, subtitle, time_text))

        scroll_layout.addStretch()

        scroll_area.setWidget(scroll_content)
        recent_activities_layout.addWidget(scroll_area)

        main_layout.addWidget(recent_activities_box)
        main_layout.addStretch()