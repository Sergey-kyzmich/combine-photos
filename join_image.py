from PIL import Image

def join_image(array_img=list, end_derictory=str, gap=bool,  where=str, selected_files = str):
    if array_img and end_derictory!="" and gap and where and len(selected_files.value.split('\n'))>=2:
        try:
            #Создание переменных
            img = []
            selected_files=selected_files.value.split('\n')
            all_width, all_height, max_width, max_height = 0,0,0,0
            now_width, now_height = 0,0
            #Расчет общего размера отступов
            gap_size = len((selected_files)-1)*10 if gap==True else 0
            #Загрузка фото
            for dir in selected_files:
                img.append(Image.open(dir))
                max_width = max(max_width, img[-1].size[0])
                all_width+=img[-1].size[0]
                max_height = max(max_height, img[-1].size[1])
                all_height += img[-1].size[1]

            if where == "Снизу":#2-й случай: Справа
                bg = Image.new("RGB", (max_width, all_height+gap_size), (0, 0, 0))
                bg.putalpha(0)
                for image in img:
                    bg.paste(image, (now_width, now_height))
                    now_height += image.size[1]
                    now_height += 10 if gap else 0



            else:
                bg = Image.new("RGB", (all_width+gap_size, max_height), (0, 0, 0))
                bg.putalpha(0)
                for image in img:
                    bg.paste(image, (now_width, now_height))
                    now_width += image.size[0]
                    now_width += 10 if gap else 0
            print(end_derictory)
            bg.save(end_derictory)

            return "Successful"
        except:
            return False
    else:
    # img0 = Image.open(input("1:"))
    # # img1 = Image.open(input("2:"))
    # img2 = Image.new("RGB", (max(img0.size[0],img1.size[0]), img0.size[1]+img1.size[1]), (0, 0, 0))
    # img2.putalpha(0)
    # img2.paste(img0, (0, 0))
    # img2.paste(img1, (0, img0.size[1]))
    # img2.show()
        return "ERROR"