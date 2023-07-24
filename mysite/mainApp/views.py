from django.shortcuts import render

from moviepy.editor import *
import os.path
from PIL import Image, ImageDraw, ImageFont

from .models import Requests
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
def index(request):

    if request.method == 'POST':

        def clip_from_image(path_dir, name_clip, s_duration):
            """Создает клип из изображений"""
            try:
                dur = float(s_duration)
            except ValueError:
                print('[-] Неверное значение длительности кадра')
                return

            if os.path.exists(path_dir):
                print('[+] Создание видео из картинок')
                os.chdir(path_dir)
                images = []
                clips = []
                for i in range(img_count):
                    images.append(f'{i}.png')
                for im in images:
                    clips.append(ImageClip(im).set_duration(dur))
                video_merge = concatenate_videoclips(clips, method='compose')
                video_merge.write_videofile(f"{name_clip}.mp4", fps=24)
                print(f"[+] Видео создано и сохранено в папку: {path_dir}")
                my_path = name_clip + '.' + 'mp4'
                print(my_path)
                return my_path
            else:
                print('[-] Указанной директории не существует')
                return

        def create_image(position, num):
            """Создает изображения для клипа"""
            new_img = Image.new('RGB', (100, 100), )
            font = ImageFont.truetype("./arial.ttf", size=60)
            pencil = ImageDraw.Draw(new_img)
            pencil.text((position, 10), text, font=font, fill='blue')

            imagefilename = f'{num}.png'
            filepath = BASE_DIR + '/media/' + imagefilename
            new_img.save(filepath)

        def delete_image():
            """Удаляет изображения после создания клипа"""

            for i in range(img_count):
                if os.path.exists(f'./{i}.png'):
                    os.remove(f'{i}.png')

        # основная программа
        text = request.POST.get('text')


        img_count = 24 * 3
        count = 0
        pos = 100
        for i in range(img_count):
            create_image(pos, i)
            count += 1
            pos -= len(text) / 1.5
        videofilename = 'runString'
        video_path = clip_from_image(MEDIA_ROOT, videofilename, 0.05)
        # delete_image()
        queryset = Requests.objects.create(text=text, video=video_path)
        context = {'video_path': video_path}

        return render(request, 'mainApp/basic_success.html', context)

    else:

        return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {
        'values': Requests.objects.all().order_by("-date")[:20]})




