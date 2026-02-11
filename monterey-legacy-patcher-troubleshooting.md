# Устранение проблем с OpenCore Legacy Patcher и macOS Monterey

## Проблема: зависание на "Validating Installer Integrity..."

При создании установщика macOS Monterey через OpenCore Legacy Patcher (OCLP) процесс может зависать на этапе валидации целостности установщика.

## Важно: MacBook Air 2013

**MacBook Air 2013 (MacBookAir6,1 / MacBookAir6,2) официально поддерживает macOS Monterey (12.x).**
Вам НЕ нужен OpenCore Legacy Patcher для установки Monterey на эту модель. Установите систему стандартным способом:
- Через Mac App Store
- Через Recovery Mode (Cmd+R при загрузке)
- Через утилиту `createinstallmedia`

OCLP нужен только для macOS Ventura (13) и новее на этой модели.

## Если всё же используете OCLP

### 1. Обновите OCLP
Версия 2.4.1 устарела. Скачайте последнюю версию:
https://github.com/dortania/OpenCore-Legacy-Patcher/releases

### 2. Проверьте USB-накопитель
- Используйте USB 3.0 флешку (минимум 16 ГБ)
- Попробуйте другую флешку
- Подключайте напрямую в порт Mac, без хабов

### 3. Освободите место на диске
Рекомендуется иметь минимум 35-40 ГБ свободного пространства.

### 4. Переcкачайте установщик
Повреждённый образ установщика — частая причина зависания. Удалите старый и скачайте заново через OCLP.

### 5. Создание установщика вручную
```bash
sudo /Applications/Install\ macOS\ Monterey.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume
```
Затем через OCLP установите только OpenCore на флешку (пункт "Install OpenCore to USB").

### 6. Время ожидания
Этап валидации может занимать 15-45+ минут на медленных USB-накопителях. Подождите минимум 30-40 минут перед тем, как прерывать процесс.

## Полезные ссылки
- [OpenCore Legacy Patcher](https://github.com/dortania/OpenCore-Legacy-Patcher)
- [Список поддерживаемых моделей Mac](https://dortania.github.io/OpenCore-Legacy-Patcher/MODELS.html)
