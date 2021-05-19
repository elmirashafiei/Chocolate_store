"""
Make the cart available globally across all templates.
P.S. -> Don't forget to specify the context processor in the settings file.
"""

from .cart import Cart


def cart(request):
    """The data returned here is the default data that gets initialized in the Cart."""
    return {'cart': Cart(request)}