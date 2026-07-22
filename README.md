# Моделирование динамики ледников и формирования Грядовых Зон Налегания (GZW)

Этот проект содержит набор численных моделей на Python и Julia, посвященных исследованию динамики скольжения ледников, их термического режима и процессов аккумуляции осадков на границе заземления (Grounding Line) с формированием грядовых зон налегания (Grounding Zone Wedges, GZW).

В основе моделей лежат современные гляциологические концепции скольжения (закон скольжения Zoet & Iverson 2020) и динамика ледяных потоков (Shallow Shelf Approximation, SSA).

---

## 🔬 Ключевые физические концепции

1. **Закон скольжения Зоета-Иверсона (Zoet & Iverson 2020)**  
   Реализован в виде регуляризованного закона трения Кулона (функция `[regularized_coulomb_drag](file:///Users/esteebarin/slip_law_glaciers/zoet_parameter_sensitivity.py#L14)`). Модель учитывает:
   * Наличие включений валунов/обломков (`has_clasts` и `has_debris`).
   * Тип ложа (`bed_type`: мягкое ложе/твердые породы).
   * Зависимость базального напряжения сдвига ($\tau_b$) от скорости скольжения ($U_b$) и эффективного давления ($N$).

2. **Динамика осадконакопления на границе заземления (Exner Equation)**  
   Формирование клиновидных наносов (GZW) моделируется с помощью связки уравнения переноса осадков (функция `[compute_sediment_flux](file:///Users/esteebarin/slip_law_glaciers/zoet_parameter_sensitivity.py#L24)`) и уравнения баланса массы Экснера для обновления рельефа дна.

3. **Теплые и холодные ледники (Warm-based vs Cold-based)**  
   Различия в профилях скоростей движения и скоростей деформации сдвига:
   * **Теплый ледник**: базальное проскальзывание на ложе + проникновение сдвиговых деформаций в подледниковую мерзлоту.
   * **Холодный ледник**: адгезионный (примерзший) контакт с ложем (скорость $u=0$) с локализацией сдвига в тонком придонном слое льда.

---

## 📂 Обзор структуры файлов и скриптов

### 🖥️ Основные симуляторы и модели
* `[SSA_dynamic_gzw.py](file:///Users/esteebarin/slip_law_glaciers/SSA_dynamic_gzw.py)` — Связанная одномерная модель течения SSA (Shallow Shelf Approximation) + динамическое накопление осадков GZW. Включает два сценария:
  1. *Storfjorden* — движение по неровному ложу с задержками границы заземления и формированием наложенных клиньев.
  2. *Mackenzie Bay* — гладкое ложе с быстрым отступанием границы заземления без задержек.
* `[SSA_simple.py](file:///Users/esteebarin/slip_law_glaciers/SSA_simple.py)` — Базовая реализация одномерного SSA-симулятора течения ледника (порт модели Robel 2021).
* `[ice_stream_ocean_model.py](file:///Users/esteebarin/slip_law_glaciers/ice_stream_ocean_model.py)` — Двунаправленная связанная модель «ледяной поток — океан» с реализацией закона скольжения Зоета, динамическим ростом GZW и расчетом прыжков границы заземления.

### 📊 Анализ чувствительности и визуализация
* `[plot_cold_based_demonstration.py](file:///Users/esteebarin/slip_law_glaciers/plot_cold_based_demonstration.py)` — Демонстрационный скрипт, строящий профили скорости и деформации для теплых и холодных ледников. Результаты сохраняются в `[cold_based_shear_preservation.png](file:///Users/esteebarin/slip_law_glaciers/cold_based_shear_preservation.png)`.
* `[zoet_parameter_sensitivity.py](file:///Users/esteebarin/slip_law_glaciers/zoet_parameter_sensitivity.py)` — Исследование чувствительности параметров закона Зоета-Иверсона.
* `[zoet_stick_slip_cycles_storfjordenGWZs.py](file:///Users/esteebarin/slip_law_glaciers/zoet_stick_slip_cycles_storfjordenGWZs.py)` — Симуляция циклов подвижек (stick-slip) и роста GZW, калиброванная под сейсмический профиль R_2018 (Storfjorden).
* `[zoet_stick_slip_cycles_mackenzieGWZs.py](file:///Users/esteebarin/slip_law_glaciers/zoet_stick_slip_cycles_mackenzieGWZs.py)` — Симуляция для залива Амундсена и окраины Маккензи (профиль AG 2014).
* `[mackenzie_transect_plot.jl](file:///Users/esteebarin/slip_law_glaciers/mackenzie_transect_plot.jl)` — Скрипт на Julia для обработки и визуализации трансекта Маккензи.

---

## ⚙️ Установка и запуск

Проект использует виртуальное окружение Python 3.12 (каталог `env/`).

### Запуск скриптов моделирования

Для запуска моделей используйте интерпретатор из виртуального окружения:

```bash
# Пример запуска демонстрации теплого/холодного ложа
env/bin/python plot_cold_based_demonstration.py

# Пример запуска анализа чувствительности закона скольжения
env/bin/python zoet_parameter_sensitivity.py
```

Графики сохраняются в корневой директории проекта.