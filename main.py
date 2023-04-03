import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class EquipmentDatabaseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.connection = sqlite3.connect("equipment_database.db")
        self.refresh_rooms()

        self.rooms_list.itemClicked.connect(self.display_equipment)

    def refresh_rooms(self):
        self.rooms_list.clear()
        query = "SELECT * FROM rooms;"
        result = self.connection.execute(query).fetchall()
        for room_id, room_name in result:
            self.rooms_list.addItem(f"{room_id}. {room_name}")

    def display_equipment_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.equipment_image.setPixmap(
            pixmap.scaled(self.equipment_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def display_equipment(self, item):
        room_id = int(item.text().split('.')[0])
        query = f"SELECT * FROM equipment WHERE room_id = {room_id};"
        result = self.connection.execute(query).fetchall()

        equipment_html = ""
        for row_data in result:
            equipment_html += f"""
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
        self.equipment_info.setHtml(equipment_html)
        image_path = result[0][12]
        self.display_equipment_image(image_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EquipmentDatabaseApp()
    window.show()
    sys.exit(app.exec())
