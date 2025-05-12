from tkinter import Frame, Label, Entry, Button, Listbox, END
from tkcalendar import Calendar
from utils.save_load import add_route_for_date, get_places_by_date
from map.map_controller import write_place_to_html
import webbrowser
import os

place_items = []

def create_calendar_ui(root):
    frame = Frame(root)
    frame.pack(pady=20)

    cal = Calendar(frame, selectmode='day')
    cal.grid(row=0, column=0, padx=10)

    Label(frame, text="장소:").grid(row=1, column=0, sticky="w", padx=10)
    place_entry = Entry(frame, width=40)
    place_entry.grid(row=2, column=0, padx=10)

    Label(frame, text="메모:").grid(row=3, column=0, sticky="w", padx=10)
    note_entry = Entry(frame, width=40)
    note_entry.grid(row=4, column=0, padx=10)

    listbox = Listbox(frame, width=50, height=6)
    listbox.grid(row=5, column=0, padx=10, pady=5)

    def update_listbox():
        listbox.delete(0, END)
        for item in place_items:
            listbox.insert(END, f"{item['place']} - {item['note']}")

    def on_add():
        place = place_entry.get().strip()
        note = note_entry.get().strip()
        if place:
            place_items.append({"place": place, "note": note})
            update_listbox()
            place_entry.delete(0, END)
            note_entry.delete(0, END)

    def on_delete():
        selected = listbox.curselection()
        if selected:
            idx = selected[0]
            place_items.pop(idx)
            update_listbox()

    def on_save():
        selected_date = cal.get_date()
        add_route_for_date(selected_date, place_items.copy())

    def on_load():
        selected_date = cal.get_date()
        global place_items
        place_items = get_places_by_date(selected_date)
        update_listbox()

    def on_show_map():
        selected_date = cal.get_date()
        places = get_places_by_date(selected_date)
        if places:
            write_place_to_html(places)
            map_path = os.path.abspath("map/map_view.html")
            webbrowser.open(f"file://{map_path}")
        else:
            print("[지도보기] 저장된 장소가 없습니다.")

    Button(frame, text="장소 추가", command=on_add).grid(row=6, column=0, pady=2)
    Button(frame, text="선택 삭제", command=on_delete).grid(row=7, column=0, pady=2)
    Button(frame, text="저장", command=on_save).grid(row=8, column=0, pady=2)
    Button(frame, text="불러오기", command=on_load).grid(row=9, column=0, pady=2)
    Button(frame, text="지도 보기", command=on_show_map).grid(row=10, column=0, pady=6)