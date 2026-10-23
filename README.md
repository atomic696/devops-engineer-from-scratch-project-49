# Игры разума (Python)

[![hexlet-check](https://github.com/atomic696/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/atomic696/devops-engineer-from-scratch-project-49/actions)

Учебный проект Хекслета — набор из пяти консольных игр на Python.

## Стек

* Python
* uv
* Ruff

## Установка

Клонируйте репозиторий и перейдите в директорию проекта:

```bash
git clone https://github.com/atomic696/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
```

Установите зависимости:

```bash
uv sync
```

Установите пакет Brain Games:

```bash
uv tool install .
```

## Использование

### Игра «Чётное»

Запуск игры:

```bash
brain-even
```

Демонстрация игры: [https://asciinema.org/a/tFjnZ7LTRoTVrqnF](https://asciinema.org/a/tFjnZ7LTRoTVrqnF)

---

### Игра «Калькулятор»

Запуск игры:

```bash
brain-calc
```

Демонстрация игры: [https://asciinema.org/a/jdaktMkowC6AaoFb](https://asciinema.org/a/jdaktMkowC6AaoFb)

---

### Игра «НОД»

Запуск игры:

```bash
brain-gcd
```

Демонстрация игры: [https://asciinema.org/a/r3Fgee5i6I2LDDBp](https://asciinema.org/a/r3Fgee5i6I2LDDBp)

---

### Игра «Арифметическая прогрессия»

Запуск игры:

```bash
brain-progression
```

Демонстрация игры: [https://asciinema.org/a/HBc5TAUOLsRxJh4A](https://asciinema.org/a/HBc5TAUOLsRxJh4A)

---

### Игра «Простое ли число?»

Запуск игры:

```bash
brain-prime
```

Демонстрация игры: [https://asciinema.org/a/Do5HEzuMRXgBA7xS](https://asciinema.org/a/Do5HEzuMRXgBA7xS)

---

## Проверка кода

Для проверки стиля кода выполните:

```bash
uv run ruff check brain_games
```

Статус автоматических проверок Хекслета отображается в бейдже в начале README.

## О проекте

Проект выполнен в рамках обучения на Хекслете и предназначен для практики Python, работы с пакетами, командной строкой, линтером и GitHub.