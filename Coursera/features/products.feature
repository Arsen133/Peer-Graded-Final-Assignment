Feature: Product Management

  Scenario: Read a product
    Given a product with ID 1 exists
    When I request the product with ID 1
    Then I should receive a JSON response with status code 200
    And the response should contain the product details

  Scenario: Update a product
    Given a product with ID 1 exists
    When I update the product with ID 1
      | name         | Updated Product |
      | price        | 150             |
      | description  | An updated product |
    Then I should receive a JSON response with status code 200
    And the response should contain the updated product details

  Scenario: Delete a product
    Given a product with ID 1 exists
    When I delete the product with ID 1
    Then I should receive a JSON response with status code 200
    And the response should contain a success message

  Scenario: List all products
    When I request to list all products
    Then I should receive a JSON response with status code 200
    And the response should contain a list of all products

  Scenario: Search products by name
    Given a product with name "Test Product" exists
    When I search for products with name "Test Product"
    Then I should receive a JSON response with status code 200
    And the response should contain a list of products with matching names

  Scenario: Search products by category
    Given a product with category "Electronics" exists
    When I search for products with category "Electronics"
    Then I should receive a JSON response with status code 200
    And the response should contain a list of products with matching categories

  Scenario: Search products by availability
    Given a product with availability "true" exists
    When I search for products with availability "true"
    Then I should receive a JSON response with status code 200
    And the response should contain a list of available products
