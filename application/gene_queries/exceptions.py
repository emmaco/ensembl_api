class GeneQueryError(Exception):
    """
    Custom exception class for errors encountered requesting gene suggestions
    """
    code = 400
    message = 'Error requesting gene suggestions'


class DatabaseQueryError(Exception):
    """
    Custom exception class for errors encountered querying the database
    """
    code = 400
    message = 'Error querying the database'




