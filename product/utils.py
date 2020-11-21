def calculate_amount(product, quantity: int):
    """
    This method takes product and units as arguments and calulate the amount
    based on the price of the product and required quantity of product
    :param product: Product object
    :param quantity: Request quantity
    :return: Final amount
    """
    # Additional operations can be done here for eg: applying discount
    final_amount = quantity * product.price
    return final_amount
