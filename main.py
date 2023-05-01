import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class EquipmentDatabaseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.connection = sqlite3.connect("equipment_database.db")
        self.refresh_rooms()

        self.current_equipment = []
        self.current_equipment_index = 0

        self.rooms_list.itemClicked.connect(self.display_equipment)
        self.previous_button.clicked.connect(self.previous_computer)
        self.next_button.clicked.connect(self.next_computer)
        self.equipment_image.setScaledContents(False)

    def refresh_rooms(self):
        self.rooms_list.clear()
        query = "SELECT * FROM rooms;"
        result = self.connection.execute(query).fetchall()
        for room_id, room_name in result:
            self.rooms_list.addItem(f"{room_id}. {room_name}")

    def display_equipment_image(self, image_path):
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(
            self.equipment_image.width(),
            self.equipment_image.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.equipment_image.setPixmap(scaled_pixmap)

    def display_equipment(self, item):
        room_id = int(item.text().split('.')[0])
        query = f"SELECT * FROM equipment WHERE room_id = {room_id};"
        result = self.connection.execute(query).fetchall()

        self.current_equipment = result
        self.current_equipment_index = 0
        self.update_equipment_display()

    def update_equipment_display(self):
        if not self.current_equipment:
            self.equipment_info.clear()
            self.equipment_image.clear()
            self.computer_count_label.setText("Компьютеры: 0/0")
            return

        row_data = self.current_equipment[self.current_equipment_index]

        with open("styles.css", "r") as file:
            css = file.read()

        css = f"<style>{css}</style>"

        equipment_html = f"""
        {css}
        <h3>Имя устройства: {row_data[2]}</h3>
        <p>Полное имя устройства: {row_data[3]}</p>
        <p>Процессор: {row_data[4]}</p>
        <p>Оперативная память: {row_data[5]}</p>
        <p>Тип системы: {row_data[6]}</p>
        <h4>Характеристики Windows</h4>
        <p>Выпуск Windows: {row_data[7]}</p>
        <p>Версия Windows: {row_data[8]}</p>
        <p>Дата установки: {row_data[9]}</p>
        <p>Сборка OC: {row_data[10]}</p>
        <p>Взаимодействие Windows Feature Experience Pack: {row_data[11]}</p>
        <hr>
        """
        image_path = row_data[12]
        if image_path:
            self.display_equipment_image(image_path)

        self.equipment_info.setHtml(equipment_html)
        self.computer_count_label.setText(
            f"Компьютеры: {self.current_equipment_index + 1}/{len(self.current_equipment)}")

    def previous_computer(self):
        if self.current_equipment_index > 0:
            self.current_equipment_index -= 1
            self.update_equipment_display()

    def next_computer(self):
        if self.current_equipment_index < len(self.current_equipment) - 1:
            self.current_equipment_index += 1
            self.update_equipment_display()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentDatabaseApp()
    window.show()
    sys.exit(app.exec())
