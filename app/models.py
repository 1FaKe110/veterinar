# app/models.py
from app import db


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description_short = db.Column(db.Text)
    description_full = db.Column(db.Text)
    image_url = db.Column(db.Text)
    enable = db.Column(db.Boolean)

    def __repr__(self):
        return f"Service('{self.title}')"


"""
INSERT INTO service
(id, title, description_short, description_full, image_url, enable)
VALUES(1, 'Полный медицинский осмотр', 'Комплексное обследование здоровья вашего питомца.', 'Комплексное обследование здоровья вашего питомца, включая осмотр, анализы и консультацию с врачом.', 'https://img.freepik.com/premium-vector/veterinarian-with-cat-in-cabinet-examining-cat-or-checking-up-cat-in-vet-clinic_1034-1270.jpg', 1);
INSERT INTO service
(id, title, description_short, description_full, image_url, enable)
VALUES(2, 'Вакцинация', 'Профилактические прививки для защиты от различных заболеваний.', 'Профилактические прививки для защиты от различных заболеваний. Рекомендуется проводить регулярно в соответствии с графиком прививок.', 'https://img.freepik.com/premium-vector/beautiful-female-vet-with-a-dogvaccinate-a-pet-sterilization-of-animals-medical-examination-of-an_348404-246.jpg', 1);
INSERT INTO service
(id, title, description_short, description_full, image_url, enable)
VALUES(3, 'Стационарное лечение', 'Уход и лечение питомца под постоянным наблюдением врачей.', 'Уход и лечение питомца под постоянным наблюдением врачей в клинике, обеспечивающий оптимальные условия для восстановления здоровья.', 'https://img.freepik.com/free-vector/veterinary-concept-illustration_114360-3226.jpg?size=626&ext=jpg&ga=GA1.1.1197247648.1706866370&semt=ais', 1);
INSERT INTO service
(id, title, description_short, description_full, image_url, enable)
VALUES(4, 'Хирургические вмешательства', 'Проведение операций по необходимости.', 'Проведение операций по необходимости, включая стерилизацию, кастрацию, удаление опухолей и другие хирургические процедуры.', 'https://img.freepik.com/free-vector/veterinary-concept-illustration_114360-3100.jpg?size=626&ext=jpg&ga=GA1.1.1197247648.1706866370&semt=ais', 1);
INSERT INTO service
(id, title, description_short, description_full, image_url, enable)
VALUES(5, 'Дентальная гигиена', 'Профилактика и лечение зубных заболеваний.', 'Профилактика и лечение зубных заболеваний, включая чистку зубов, удаление зубных отложений и лечение зубных болезней.', 'https://img.freepik.com/free-vector/pet-care-concept-illustration_114360-10913.jpg?size=626&ext=jpg&ga=GA1.1.1197247648.1706866370&semt=ais', 1);
INSERT INTO service
(id, title, description_short, description_full, image_url, enable)
VALUES(6, 'Лечение от паразитов', 'Диагностика и лечение от блох, клещей и других паразитов.', 'Диагностика и лечение от блох, клещей и других паразитов, включая применение средств для профилактики и лечения.', 'https://img.freepik.com/free-vector/beauty-salons-sanitation-abstract-concept-illustration-hair-and-nail-salons-fully-sanitize-after-each-client-visit-disposable-supplies-social-distance-wipe-surface_335657-3339.jpg?size=626&ext=jpg&ga=GA1.1.1197247648.1706866370&semt=ais', 1);
INSERT INTO service
(id, title, description_short, description_full, image_url, enable)
VALUES(7, 'Лабораторные анализы', 'Проведение различных анализов для диагностики состояния здоровья.', 'Проведение различных анализов для диагностики состояния здоровья питомца, включая общие анализы крови, биохимические анализы и другие исследования.', 'https://img.freepik.com/free-vector/breast-cancer-research-concept-illustration_114360-7138.jpg?size=626&ext=jpg&ga=GA1.1.1197247648.1706866370&semt=ais', 1);
INSERT INTO service
(id, title, description_short, description_full, image_url, enable)
VALUES(8, 'Консультации специалистов', 'Получение рекомендаций по уходу и лечению питомца от опытных ветеринаров.', 'Получение рекомендаций по уходу и лечению питомца от опытных ветеринаров, в том числе специалистов по питанию, поведению и другим областям.', 'https://img.freepik.com/premium-vector/the-beagle-dog-at-the-vets-reception_530689-727.jpg?size=626&ext=jpg&ga=GA1.1.1197247648.1706866370&semt=ais', 1);
INSERT INTO service
(id, title, description_short, description_full, image_url, enable)
VALUES(9, 'Экстренная помощь', 'Оказание скорой ветеринарной помощи в случае неотложных состояний.', 'Оказание скорой ветеринарной помощи в случае неотложных состояний, в том числе при травмах, отравлениях и других чрезвычайных ситуациях.', 'https://img.freepik.com/free-vector/hand-drawn-animal-rescue-illustration_23-2150216542.jpg?size=626&ext=jpg&ga=GA1.1.1197247648.1706866370&semt=ais', 0);
INSERT INTO service
(id, title, description_short, description_full, image_url, enable)
VALUES(10, 'Физиотерапия', 'Применение физических методов лечения для восстановления здоровья питомца.', 'Применение физических методов лечения для восстановления здоровья питомца, включая массаж, физическую терапию и другие процедуры.', 'https://img.freepik.com/free-vector/veterinary-concept-illustration_114360-3261.jpg?size=626&ext=jpg&ga=GA1.1.1197247648.1706866370&semt=ais', 1);
"""