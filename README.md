# Project Annotation

## Project for Automating Smoke Testing of an Online Store

This project is designed to automate smoke testing for an online store using the **Page Object Model (POM)** and principles of **Object-Oriented Programming (OOP)**. The main goal of the project is to verify the process of selecting and purchasing products on the website, ensuring the accuracy of product names and prices. In general, to ensure that your shopping experience goes smoothly!

## Key Features of the Project

1. **Page Object Model (POM)**: The project uses POM to simplify interaction with web pages and improve code maintainability. Each page of the site is represented by a separate object, which allows for easy management of elements and actions on the pages.

2. **OOP**: Applying Object-Oriented Programming principles allows organizing code in a way that ensures its reusability and extensibility. It's like building a house from blocks: adding pieces as needed without risking the entire structure falling apart.

## Project Structure

### 1. Directory `base`

- `base_class.py`: Contains the main class for working with web pages, providing common methods for interacting with elements on the pages. This class manages driver initialization and basic functions such as checking by text, link, and scrolling pages.

### 2. Directory `pages`

- `login_page.py`: Contains methods and locators for performing operations on the login page. Includes getters for login form element locators and methods for entering data and executing login.
  
- `cart_page.py`: Contains methods for clearing cart data, and more methods can be added later.
  
- `main_page.py`: Describes methods for navigating the main page, including selecting product categories, applying filters, and choosing specific products. Implements actions such as selecting a category, applying filters, and choosing a specific product.
  
- `products_page.py`: Contains methods and locators for performing actions on the specific product page, including selecting color and size of the product and adding it to the cart. Also includes verification of the product name and price as displayed on the product page and in the cart.
  
- `checkout_page.py`: Contains methods for entering shipping information, and uses the Faker library for generating random data. This class is responsible for handling shipping information and verifying the correctness of entered data.
  
- `payment_page.py`: Implements methods for selecting the payment method and entering credit card details. This class uses the Faker library to generate random test data such as card number, security code, and cardholder name. However, during the final checkout stage, automation was not used for entering card data, as in the production version of the site, card details must be entered manually, possibly for security reasons.

### 3. Directory `tests`

- `test_buy_product_1.py`: Contains tests for selecting the first product. The folder also includes tests for selecting the second and third products.
  
- `test_login.py`: Includes checks for correct login and various error scenarios such as incorrect email, incorrect password, and empty fields. Also includes a test for logout.

### 4. Directory `screen`

- This folder contains screenshots taken at the final step of the smoke test. The method for taking screenshots is stored in the `base` folder.

## Testing Process

- **Smoke Test**: The project implements a smoke test to check the basic functionality of the site. Tests cover scenarios such as product selection, applying filters, adding products to the cart, and proceeding to payment. If something goes wrong, it’s not the end of the world, but we will definitely notice it.

- **Cart Clearing**: In each product purchase test, after login operations, the cart is cleared to ensure a clean test environment and to prevent previous tests from affecting subsequent ones.

- **Data Verification**: Tests verify that the selected product is displayed with the correct name and price according to the applied filters. It also checks the success of login, logout, and continuously verifies the current URL.

- **Using the Faker Library**: The Faker library is used in the project to generate random data such as names and addresses, making the tests more realistic.

- **Exception Handling**: Exception handling mechanisms are applied in vulnerable areas of the project to prevent test failures due to unforeseen errors such as timeouts or missing elements. This ensures that tests do not collapse like a row of dominoes due to unexpected issues.

This project demonstrates a robust approach to automating web application testing, ensuring the validation of critical online store functionalities and maintaining a high level of code quality and reliability.

