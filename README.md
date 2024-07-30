# Аннотация к проекту

## Проект автоматизации смоук тестирования интернет-магазина

Этот проект предназначен для автоматизации смоук тестирования интернет-магазина с использованием **Page Object Model (POM)** и принципов **объектно-ориентированного программирования (ООП)**. Основная цель проекта — проверить процесс выбора и покупки товаров на сайте, верифицируя правильность имени и цены товара. В общем, убедиться, что ваш шопинг проходит гладко! Annotation in English is located below:)

## Основные особенности проекта

1. **Page Object Model (POM)**: Проект использует POM для упрощения взаимодействия с веб-страницами и улучшения поддерживаемости кода. Каждая страница сайта представлена отдельным объектом, что позволяет легко управлять элементами и действиями на страницах.

2. **ООП**: Применение принципов объектно-ориентированного программирования позволяет организовать код таким образом, чтобы обеспечить его переиспользуемость и расширяемость. Это как строить дом из конструктора: добавляем детали по мере необходимости, без риска разрушить всю конструкцию.

## Структура проекта

### 1. Папка `base`

- `base_class.py`: Содержит основной класс для работы с веб-страницами, предоставляющий общие методы для взаимодействия с элементами на страницах. Этот класс управляет инициализацией драйвера и базовыми функциями, такими как проверка по слову, ссылке и скроллинг страниц.

### 2. Папка `pages`

- `login_page.py`: Содержит методы и локаторы для выполнения операций на странице логина. Включает в себя геттеры для локаторов элементов формы логина и методы для ввода данных и выполнения логина.
  
- `cart_page.py`: Содержит методы для очистки данных в корзине, позднее разнообразие методов можно будет дополнить.
  
- `main_page.py`: Описывает методы для навигации по главной странице, включая выбор категорий товаров, применение фильтров и выбор конкретных товаров. Реализует действия, такие как выбор категории, применение фильтров, выбор конкретного товара.
  
- `products_page.py`: Содержит методы и локаторы для выполнения действий на странице конкретного товара, содержит выбор цвета, а также размера продукта и добавление его в корзину. Здесь же производится проверка на соответствие имени и цены товара – указанных на странице товара и в корзине.
  
- `checkout_page.py`: Содержит методы для ввода данных доставки, также использует библиотеку Faker для генерации случайных данных. Этот класс отвечает за обработку информации о доставке и проверку корректности введенных данных.
  
- `payment_page.py`: Реализует методы для выбора способа оплаты и ввода данных кредитной карты. В этом классе использована библиотека Faker для генерации случайных данных для тестов, таких как номер карты, код безопасности, имя владельца карты. Однако, на последнем этапе оформления заказа автоматизация не была задействована для ввода данных карты, так как на продакшн-версии сайта данные карты должны вводиться вручную, возможно, в целях безопасности.

### 3. Папка `tests`

- `test_buy_product_1.py`: Содержит тест для выбора первого товара. Также в папке находятся тесты для выбора второго и третьего товара.
  
- `test_login.py`: Включает проверки на корректный логин и различные сценарии ошибок, такие как неправильная почта, неправильный пароль и пустые поля. Также тест на логаут.

### 4. Папка `screen`

- В данной папке содержатся скриншоты, выполненные на последнем шаге смоук теста. Метод для выполнения скриншота хранится в папке `base`.

## Процесс тестирования

- **Смоук тест**: В проекте реализован смоук тест для проверки базовой функциональности сайта. Тесты охватывают сценарии выбора товара, применения фильтров, добавления товара в корзину и перехода к оплате. Если что-то идет не так, это не конец света, но мы обязательно это заметим.

- **Очистка корзины**: В каждом тесте покупки товара после выполнения операций логина корзина очищается, чтобы гарантировать чистоту тестовой среды и избежать влияния предыдущих тестов на последующие.

- **Верификация данных**: Тесты проверяют, что выбранный товар отображается с правильным именем и ценой, соответствующими выбранным фильтрам. Также проверяется успешность логина, логаута, постоянно проверяется текущая URL.

- **Использование библиотеки Faker**: В проекте применяется библиотека Faker для генерации случайных данных, таких как имя и адрес, что позволяет делать тесты более реалистичными.

- **Обработка исключений**: В уязвимых местах проекта применены механизмы обработки исключений для предотвращения падения тестов из-за непредвиденных ошибок, таких как таймауты или отсутствие элементов. Так что тесты не упадут, как домино, из-за неожиданных проблем.

Этот проект демонстрирует надежный подход к автоматизации тестирования веб-приложений, обеспечивая проверку критически важных функций интернет-магазина и поддерживая высокий уровень качества и надежности кода.



# Project Annotation

## Project for Automating Smoke Testing of an Online Store

This project is designed to automate smoke testing for an online store using the **Page Object Model (POM)** and principles of **Object-Oriented Programming (OOP)**. The main goal of the project is to verify the process of selecting and purchasing products on the website, ensuring the accuracy of product names and prices. In general, to ensure that your shopping experience goes smoothly!

## Key Features of the Project

1. **Page Object Model (POM)**: The project uses POM to simplify interaction with web pages and improve code maintainability. Each page of the site is represented by a separate object, which allows for easy management of elements and actions on the pages.

2. **OOP**: Applying Object-Oriented Programming principles allows organizing code in a way that ensures its reusability and extensibility. It's like building a house from blocks: adding pieces as needed without risking the entire structure falling apart.

## Project Structure

### 1. Folder `base`

- `base_class.py`: Contains the main class for working with web pages, providing common methods for interacting with elements on the pages. This class manages driver initialization and basic functions such as checking by text, link, and scrolling pages.

### 2. Folder `pages`

- `login_page.py`: Contains methods and locators for performing operations on the login page. Includes getters for login form element locators and methods for entering data and executing login.
  
- `cart_page.py`: Contains methods for clearing cart data, and more methods can be added later.
  
- `main_page.py`: Describes methods for navigating the main page, including selecting product categories, applying filters, and choosing specific products. Implements actions such as selecting a category, applying filters, and choosing a specific product.
  
- `products_page.py`: Contains methods and locators for performing actions on the specific product page, including selecting color and size of the product and adding it to the cart. Also includes verification of the product name and price as displayed on the product page and in the cart.
  
- `checkout_page.py`: Contains methods for entering shipping information, and uses the Faker library for generating random data. This class is responsible for handling shipping information and verifying the correctness of entered data.
  
- `payment_page.py`: Implements methods for selecting the payment method and entering credit card details. This class uses the Faker library to generate random test data such as card number, security code, and cardholder name. However, during the final checkout stage, automation was not used for entering card data, as in the production version of the site, card details must be entered manually, possibly for security reasons.

### 3. Folder `tests`

- `test_buy_product_1.py`: Contains tests for selecting the first product. The folder also includes tests for selecting the second and third products.
  
- `test_login.py`: Includes checks for correct login and various error scenarios such as incorrect email, incorrect password, and empty fields. Also includes a test for logout.

### 4. Folder `screen`

- This folder contains screenshots taken at the final step of the smoke test. The method for taking screenshots is stored in the `base` folder.

## Testing Process

- **Smoke Test**: The project implements a smoke test to check the basic functionality of the site. Tests cover scenarios such as product selection, applying filters, adding products to the cart, and proceeding to payment. If something goes wrong, it’s not the end of the world, but we will definitely notice it.

- **Cart Clearing**: In each product purchase test, after login operations, the cart is cleared to ensure a clean test environment and to prevent previous tests from affecting subsequent ones.

- **Data Verification**: Tests verify that the selected product is displayed with the correct name and price according to the applied filters. It also checks the success of login, logout, and continuously verifies the current URL.

- **Using the Faker Library**: The Faker library is used in the project to generate random data such as names and addresses, making the tests more realistic.

- **Exception Handling**: Exception handling mechanisms are applied in vulnerable areas of the project to prevent test failures due to unforeseen errors such as timeouts or missing elements. This ensures that tests do not collapse like a row of dominoes due to unexpected issues.

This project demonstrates a robust approach to automating web application testing, ensuring the validation of critical online store functionalities and maintaining a high level of code quality and reliability.

