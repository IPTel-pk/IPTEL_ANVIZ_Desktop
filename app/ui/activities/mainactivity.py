from typing import Callable
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from app.ui.components.activity import Activity
from app.ui.components.activityitem import ActivityItem
from app.ui.components.statbox import StatBox
from app.settings import SECONDARY_COLOR
from data.activities import activities_data

class MainActivity(Activity):
    """
    ### Main Activity
    This widget creates the dashboard landing page with summary stat boxes and a recent activity list to give a quick overview of system activity.
    """

    def __init__(self, navigate: Callable, parent=None) -> None:
        """
        Initialize the Main Page Activity.

        This method builds the dashboard layout including summary statistics and the recent activity panel.
        """
        super().__init__(parent=parent, activity="Main", navigate=navigate)

        # 1. Main Layout
        # This defines the vertical dashboard layout containing the stats row and the recent activity panel.
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
        recent_activities_box.setStyleSheet(f"""
            QWidget#recentActivitiesBox {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)

        recent_activities_layout = QVBoxLayout(recent_activities_box)
        recent_activities_layout.setContentsMargins(0, 0, 0, 0)
        recent_activities_layout.setSpacing(0)

        header_label = QLabel("Recent Activities")
        header_label.setFixedHeight(30)
        header_label.setStyleSheet(f"""
            font-size: 16px;
            font-weight: bold;
            padding-left: 15px;
            border-bottom: 1px solid {SECONDARY_COLOR};
            background-color: transparent;
        """)
        recent_activities_layout.addWidget(header_label)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none; background-color: transparent;
            }
        """)

        scroll_content = QWidget()
        scroll_content.setStyleSheet(
            "background-color: transparent; border: none;"
        )
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(0)

        for title, subtitle, time_text, status in activities_data:
            scroll_layout.addWidget(ActivityItem(
                title, subtitle, time_text, status
            ))
        scroll_layout.addStretch()
        scroll_area.setWidget(scroll_content)
        recent_activities_layout.addWidget(scroll_area)

        main_layout.addWidget(recent_activities_box)
        main_layout.addStretch()
