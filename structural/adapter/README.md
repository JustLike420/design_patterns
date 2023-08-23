# Адаптер (Adapter)
**Также известен как:** Wrapper, Обёртка

**Адаптер** — это структурный паттерн проектирования, который позволяет объектам с несовместимыми интерфейсами работать вместе.

![img.png](img.png)

## Проблема

Предствим, что приложение скачивает данные в виде XML и рисуети графики.
Затем, решили сменить библиотеку для графиков, но она использует JSON.

![img_1.png](img_1.png)

## Решение
Вы можете создать адаптер. Это объект-переводчик, который трансформирует интерфейс или данные одного объекта в такой вид, чтобы он стал понятен другому объекту.
![img_2.png](img_2.png)
