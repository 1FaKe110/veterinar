# app.py
from loguru import logger

from app import create_app
from flask import render_template, jsonify, Blueprint
from app.models import Service

app = create_app()


@app.route('/')
def index():
    # Получаем данные о предоставляемых услугах из базы данных
    # services = Service.query.all()
    services = Service.query.filter_by(enable=True).all()
    logger.info(services[0])
    service_data = [{
        'id': service.id,
        'title': service.title,
        'description_short': service.description_short,
        'description_full': service.description_full,
        'image_url': service.image_url,
    }
        for service in services if bool(service.enable)]

    return render_template('index.html', services=service_data)


@app.route('/services', methods=['GET'])
def get_services():
    # Получить данные о предоставляемых услугах и вернуть их в виде JSON
    services = Service.query.all()
    service_data = [{
        'id': service.id,
        'title': service.title,
        'description_short': service.description_short,
        'description_full': service.description_full,
        'image_url': service.image_url,
    } for service in services]

    return jsonify(service_data)


@app.route('/about')
def about():
    return render_template('contact.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
