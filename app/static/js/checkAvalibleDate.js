
function loadAvailableTimes() {
    // Получаем выбранную дату
    const selectedDate = document.getElementById('appointmentDate').value;

    // Отправляем запрос на сервер, чтобы получить доступное время приема
    // В этом примере используется fetch API для отправки запроса к бэкенду
    fetch(/get-available-appointment-times?date=${selectedDate})
    .then(response => response.json())
    .then(data => {
      // Получаем данные со временем приема и обновляем выпадающий список
      const timeSelect = document.getElementById('appointmentTime');
      timeSelect.innerHTML = ''; // Очищаем список

      // Добавляем доступные часы приема в выпадающий список
      data.times.forEach(time => {
        const option = document.createElement('option');
        option.value = time;
        option.textContent = time;
        timeSelect.appendChild(option);
      });
    });
}
