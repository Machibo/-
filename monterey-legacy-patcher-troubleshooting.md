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
Этап валидации может занимать 15-45+ минут на медленных USB-накопителях. Если ожидание превышает 60 минут — процесс завис.

### 7. Проверка размера установщика
Если установщик весит ~12-13 ГБ — он не повреждён и перекачивать его не нужно:
```bash
du -sh "/Applications/Install macOS Monterey.app"
```
В этом случае просто создайте загрузочную флешку вручную через Терминал (шаги в разделе 5), обходя зависающий этап OCLP.

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

## Пошаговая инструкция: установка macOS Monterey через Терминал + OCLP

### Шаг 1. Откройте Терминал
Finder → Программы → Утилиты → Терминал

### Шаг 2. Узнайте номер диска флешки
```bash
diskutil list
```
Найдите флешку (128 ГБ) — запомните номер (например disk2). НЕ disk0 и НЕ disk1.

### Шаг 3. Отформатируйте флешку
```bash
sudo diskutil eraseDisk JHFS+ "Installer" GPT /dev/disk2
```
(замените disk2 на ваш номер)

### Шаг 4. Создайте загрузочный установщик (20-40 минут)
```bash
sudo "/Applications/Install macOS Monterey.app/Contents/Resources/createinstallmedia" --volume /Volumes/Installer --nointeraction
```

### Шаг 5. Установите OpenCore на флешку через OCLP
- "Build and Install OpenCore" → "Build OpenCore" → "Install OpenCore to disk"
- Выберите USB-флешку → раздел EFI

### Шаг 6. Загрузитесь с флешки
- Выключите Mac, зажмите Option (Alt) + кнопка включения
- Выберите "EFI Boot" или "Install macOS Monterey"

### Шаг 7. Установите macOS Monterey
- Выберите "Установить macOS Monterey" → диск Macintosh HD
- Дождитесь завершения (несколько перезагрузок)

### Шаг 8. Патч системы после установки
- Откройте OCLP → "Post-Install Root Patch" → "Start Root Patching"
- Это восстановит Wi-Fi, графику и другие компоненты

## Полезные ссылки
- [OpenCore Legacy Patcher](https://github.com/dortania/OpenCore-Legacy-Patcher)
- [Список поддерживаемых моделей Mac](https://dortania.github.io/OpenCore-Legacy-Patcher/MODELS.html)
