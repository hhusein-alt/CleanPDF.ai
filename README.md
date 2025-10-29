# CleanPDF.ai – Fast & Smart PDF Watermark Remover

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.101.1-brightgreen.svg)](https://fastapi.tiangolo.com/)

CleanPDF.ai — это современный веб-сервис для **мгновенного удаления водяных знаков из PDF**, а также будущих функций вроде **сжатия и оптимизации PDF**. Идеально подходит для учебы, работы и личных проектов, где PDF-документы нужно быстро очистить от брендинга.

---

# CleanPDF.ai – Быстрый и умный PDF Watermark Remover (English)

CleanPDF.ai is a modern web service for **instant PDF watermark removal**, with upcoming features like **PDF compression and optimization**. Perfect for students, professionals, and anyone who needs clean PDF documents quickly.

---

## 🚀 Особенности / Features

- **Удаление водяных знаков Gamma.app / Gamma.app watermark removal** — автоматически находит и удаляет логотипы и ссылки в правом нижнем углу / Automatically detects and removes logos and links in the bottom-right corner.
- **Удаление других водяных знаков / Remove other watermarks** — расширяемая система для любых PDF / Extensible system for any PDF watermark.
- **Clean + Compress (будет / upcoming)** — очистка и оптимизация PDF для меньшего размера / Clean and optimize PDF for smaller file size.
- **Поддержка FastAPI и асинхронной обработки / FastAPI + async processing** — быстрый отклик сервера / Fast server response.
- **Безопасная загрузка файлов / Secure file handling** — временные файлы очищаются после обработки / Temporary files are removed after processing.
- **Лёгкая интеграция с бесплатными AI API / Easy integration with free AI APIs** — для распознавания сложных водяных знаков / For detecting complex watermarks.

---

## 📂 Структура проекта / Project Structure

CLEANPDF.AI/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # Точка входа FastAPI 
│   │
│   ├── routes/                # Разделение эндпоинтов
│   │   ├── __init__.py
│   │   ├── pdf_routes.py      # Основные API для PDF
│   │   └── status_routes.py   # Служебные эндпоинты (healthcheck)
│   │
│   ├── services/              # Логика (анализ, очистка, компрессия)
│   │   ├── __init__.py
│   │   ├── watermark_detector.py
│   │   ├── watermark_remover.py
│   │   ├── pdf_compressor.py  # Позже добавим Clean+Compress
│   │   └── utils.py           # Общие функции, тип allowed_file и т.п.
│   │
│   ├── templates/             # HTML-шаблоны (Jinja2)
│   │   ├── index.html         # Главная страница загрузки
│   │   ├── result.html        # Страница результата
│   │   ├── error.html         # Ошибки
│   │   └── partials/          # Повторяющиеся куски (header/footer)
│   │       ├── header.html
│   │       └── footer.html
│   │
│   ├── static/                # Фронтенд: CSS, JS, картинки
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   │       └── favicon.png
│   │
│   └── config/
│       ├── __init__.py
│       └── settings.py        # пути, лимиты, домен для watermark, env
│
├── tests/
│   ├── __init__.py
│   └── test_pdf_processing.py # базовые pytest тесты
│
├── uploads/                   # Временные файлы (можно игнорировать в git)
├── outputs/                   # Очищенные PDF
│
├── .env                       # переменные окружения (например, TARGET_DOMAIN)
├── .gitignore
├── requirements.txt
├── CHANGELOG.md
├── README.md
└── run_local.sh               # скрипт для локального запуска (uvicorn)


---

## ⚡ Установка и локальный запуск / Installation & Local Run

1. Клонируйте репозиторий / Clone repository:
```bash
git clone https://github.com/yourusername/CleanPDF.ai.git
cd CleanPDF.ai


#Создайте виртуальное окружение и установите зависимости / Create virtual env & install dependencies:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install --upgrade pip
pip install -r requirements.txt


#Запуск сервера / Run server

python -m app.main

#Откройте браузер / Open browser:
http://127.0.0.1:8000

# 📝Использование / Usage

"""
Выберите PDF-файл через веб-интерфейс / Select a PDF file through the web interface.

Нажмите Remove Watermark / Click Remove Watermark.

После обработки файл автоматически скачивается / Processed file will be downloaded automatically.

"""
# 🔧 Планируемые функции / Planned Features

"""
Поддержка удаления водяных знаков в любом месте PDF / Detect watermarks anywhere in PDF.

Интеграция с бесплатными AI API для распознавания логотипов / Integration with free AI APIs for logo detection.

PDF сжатие и оптимизация / PDF compression and optimization (Clean + Compress).

Возможность массовой обработки PDF / Batch PDF processing.

"""

# ⚖️ Лицензия / License

"""
MIT License – свободное использование и модификация / MIT License – free use and modification.

"""
# 🔑 Ключевые слова / SEO Keywords

"""
PDF Watermark Remover, Gamma.app PDF, Clean PDF, PDF Compression, Free PDF Tools, Remove Logo from PDF, Fast PDF Cleaner
PDF Watermark Remover, Удаление водяных знаков PDF, Очистка PDF, Сжатие PDF, Бесплатные PDF инструменты, Удалить логотип из PDF, Быстрое удаление водяных знаков

"""