import flet 
from flet import Page, FilePickerResultEvent, ElevatedButton,FilePicker,FilePickerFileType, Text, Row, icons, Checkbox, Dropdown, AlertDialog
from join_image import join_image

def main(page: Page):
    page.window_width = 800 
    page.window_height = 600

    def find_option(option_name):
        for option in d.options:
            if option_name == option.key:
                return option
        return None

    def add_clicked(e):
        a = []
        for name in selected_files.value.split("\n"):
            if name !="" and name!="\n":
                a.append(name)
        d.options = []
        print(f"{a=}")
        for i in a:
            d.options.append(flet.dropdown.Option(i))
        page.update()
        option = find_option("")
        while option != None:
            option = find_option("")
            if option != None:
                d.options.remove(option)
        
        d.value = selected_files.value.split("\n")[-1]    


    def delete_clicked(e):
        option = find_option(d.value)
        if option != None:
            print(d.options)
            d.options.remove(option)
            # d.value = None
            replace_text = selected_files.value[selected_files.value.index(option.key): len(option.key)+2]
            print([d.options])
            print(f"1{[selected_files.value]}")
            l = len(selected_files.value)
            selected_files.value = selected_files.value.replace("\n"+option.key, "", 1)
            if len(selected_files.value)==l:
                    selected_files.value = selected_files.value.replace(option.key, "", 1)
            if selected_files.value[:2]=="\n":
                selected_files.value = selected_files.value[2:]
            selected_files.update()
            print(f"2{[selected_files.value]}")
            d.value = selected_files.value.split("\n")[-1]
            page.update()

    d = Dropdown(options=[], width=500)
    add = ElevatedButton("Add", on_click=add_clicked)
    delete = ElevatedButton("Delete selected", on_click=delete_clicked)
    



    def pick_files_result(e: FilePickerResultEvent):

        if isinstance(selected_files.value, str):
            selected_files.value = (selected_files.value+"\n"+
            "\n".join(map(lambda f: f.path, e.files)) if e.files else selected_files
            )
        else:
            selected_files.value = (
                "\n".join(map(lambda f: f.path, e.files)) if e.files else selected_files
        )

        selected_files.update()
        add_clicked(1)
    def go_to_join_image(e):
        end = join_image(
        selected_files = selected_files,
        end_derictory=save_file_path.value.replace("Путь для сохранения фото: ", ""),
        gap=gap_checkbox,
        where=select_where_add.value#0-добавить справа, 1-добавить снизу
    
    )
        dlg = AlertDialog(
        title=Text(end)
    )
        page.dialog = dlg
        dlg.open = True
        page.update()
    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text(font_family="Consolas", size=20)
    page.overlay.append(pick_files_dialog)

    page.add(
        ElevatedButton(
            "Pick files",
            icon=icons.UPLOAD_FILE,
            on_click=lambda _: pick_files_dialog.pick_files(
                allow_multiple=True,
                file_type="IMAGE",
                allowed_extensions = ["jpeg", "jpg", "png"], 
            ),
        )
    )
    selected_text = Text(value="⬇Выбраные файлы⬇", font_family="Consolas",size=30)
    
    gap_checkbox = Checkbox(value=True)


    select_where_add = Dropdown(
        width=100,
        height=60,
        text_size=15,
        options=[
            flet.dropdown.Option("Справа"),
            flet.dropdown.Option("Снизу")
        ],
        value="Справа"
    )

    button = ElevatedButton(text="Объединить", on_click=go_to_join_image, style=flet.ButtonStyle(
                color={
                    flet.MaterialState.HOVERED: flet.colors.WHITE,
                    flet.MaterialState.DEFAULT: "silver",
                },
                side={
                    flet.MaterialState.DEFAULT: flet.BorderSide(1, "silver"),
                    flet.MaterialState.HOVERED: flet.BorderSide(2, flet.colors.BLACK),
                },
                shape={
                    flet.MaterialState.HOVERED: flet.RoundedRectangleBorder(radius=20),
                    flet.MaterialState.DEFAULT: flet.RoundedRectangleBorder(radius=10),
                },
            ))
    #!Добавление всех эл-ов на страницу
    page.add(selected_text)
    if selected_files.value!="":page.add(selected_files)
    page.add(Row(controls=[d, delete]))
    page.add(Text("Настройки:", size=30, font_family="Consolas"))
    page.add(Row([Text("Отступ 10px?", size=20, font_family="Consolas"), gap_checkbox]))
    page.add(Row([Text("С какой стороны добавить фото", size=20, font_family="Consolas"), select_where_add]))

    #!Создание меню выбора дериктории для конечного файла
    def save_file_result(e: FilePickerResultEvent):
        save_file_path.value = "Путь для сохранения фото: "+e.path if e.path else "Cancelled!"
        save_file_path.update()
    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text(value="Путь для сохранения фото:", font_family="Consolas", size=20)
    page.overlay.extend([save_file_dialog])

    page.add(Row(
            [save_file_path,
                ElevatedButton(
                    "Save file",
                    icon=icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(
                    file_type=FilePickerFileType.CUSTOM,
                    allowed_extensions = ["jpeg", "jpg", "png"], 
                ),
                disabled=page.web,),
            ]
        ),)



    page.add(button)






flet.app(target=main)