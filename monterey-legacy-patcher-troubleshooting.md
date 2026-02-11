# Устранение проблем с OpenCore Legacy Patcher и macOS Monterey

## Проблема: зависание на "Validating Installer Integrity..."

При создании установщика macOS Monterey через OpenCore Legacy Patcher (OCLP) процесс может зависать на этапе валидации целостности установщика. Если ожидание длится более 40-60 минут — установщик скорее всего повреждён.

## Определение модели Mac

Проверьте модель: Apple Menu → About This Mac.
- **MacBook Air 2013+ (MacBookAir6,x)** — Monterey поддерживается официально, OCLP не нужен.
- **MacBook Air 2012 (MacBookAir5,x)** — Monterey НЕ поддерживается, нужен OCLP.

Если в "Обновлении ПО" предлагается только Big Sur, а Monterey не появляется — ваш Mac не поддерживается официально и OCLP необходим.

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

### 5. Создание установщика вручную (если OCLP зависает)

Шаг 1: Удалите старый установщик
```bash
sudo rm -rf "/Applications/Install macOS Monterey.app"
```

Шаг 2: Скачайте заново через OCLP → "Download macOS Installer"

Шаг 3: Проверьте размер (должен быть ~12-13 ГБ)
```bash
du -sh "/Applications/Install macOS Monterey.app"
```

Шаг 4: Узнайте номер диска USB-флешки
```bash
diskutil list
```

Шаг 5: Отформатируйте флешку (замените diskN на номер флешки)
```bash
sudo diskutil eraseDisk JHFS+ "MyVolume" GPT /dev/diskN
```

Шаг 6: Создайте загрузочный установщик вручную
```bash
sudo "/Applications/Install macOS Monterey.app/Contents/Resources/createinstallmedia" --volume /Volumes/MyVolume --nointeraction
```

Шаг 7: Через OCLP выполните только "Install OpenCore to disk" на эту флешку.

### 6. Время ожидания
Этап валидации может занимать 15-45+ минут на медленных USB-накопителях. Подождите минимум 30-40 минут перед тем, как прерывать процесс.

## Диагностика: запуск OCLP из терминала

Чтобы увидеть подробный лог и понять, зависло ли приложение:
```bash
/path/to/OpenCore-Patcher.app/Contents/MacOS/OpenCore-Patcher
```
Это выведет лог в терминал в реальном времени и покажет, на каком именно этапе застрял процесс.

## Установка Monterey без OCLP (только для MacBook Air 2013+)

Если ваш Mac **официально поддерживает** Monterey (модель 2013 года и новее):
```bash
softwareupdate --fetch-full-installer --full-installer-version 12.7
```
Или через Системные настройки → Обновление ПО.

## Полезные ссылки
- [OpenCore Legacy Patcher](https://github.com/dortania/OpenCore-Legacy-Patcher)
- [Список поддерживаемых моделей Mac](https://dortania.github.io/OpenCore-Legacy-Patcher/MODELS.html)
