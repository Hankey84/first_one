import os
from pytube import YouTube

# Функция для скачивания видео
def download_video(video_url, output_path):
    try:
        # Создаем объект YouTube
        yt = YouTube(video_url)

        # Выбираем наилучшее качество видео
        stream = yt.streams.get_highest_resolution()

        # Скачиваем видео в указанный путь
        stream.download(output_path)
        print("Видео успешно скачано!")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    # URL видео на YouTube
    video_url = "https://www.youtube.com/watch?v=your_video_id_here"

    # Путь к папке, в которой вы хотите сохранить видео
    output_directory = "/path/to/your/directory"

    # Проверяем, существует ли указанная папка, и создаем ее, если она не существует
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Запускаем функцию для скачивания видео
    download_video(video_url, output_directory)
    # Nothing to save
