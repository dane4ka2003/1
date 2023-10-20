from flask import Flask, render_template, request
import asyncio
from bot import send_message_to_user, send_message_to_all, run_bot


# Инициализация Flask приложения
app = Flask(__name__)

@app.route('/admin')
def admin():
    return render_template('admin.html')





@app.route('/send_message', methods=['GET', 'POST'])
def send_mes():
    if request.method == 'POST':
        chat_id = request.form.get('chat_id')
        message = request.form.get('message')
        send_to_all = request.form.get('send_to_all')
        photo = request.files.get('photo')  # Получаем загруженное фото
        if photo:
            photo.save('uploaded_photo.jpg')  # Сохраняем загруженное фото в файл

        if send_to_all == '1':
            asyncio.run(send_message_to_all(message))
            return "Сообщение отправлено всем пользователям!"
        else:
            asyncio.run(send_message_to_user(chat_id, message, photo_path='uploaded_photo.jpg'))
            return f"Сообщение отправлено пользователю с id: {chat_id}!"
    return render_template('sendMes.html')



if __name__ == '__main__':
    app.run(debug=True)

