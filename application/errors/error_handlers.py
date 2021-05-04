from flask import Blueprint, jsonify

from application.gene_queries.exceptions import GeneQueryError, DatabaseQueryError

error_handlers_bp = Blueprint('error_handlers_bp', __name__)


@error_handlers_bp.app_errorhandler(GeneQueryError)
def handle_gene_query_error(error):
    """
    Error handler for exceptions encountered when querying the gene_suggest endpoint

    :param error: Error object
    :type error: Exception
    :return: response, in JSON format
    :rtype: JSON object
    """
    return get_error_response(error)


@error_handlers_bp.app_errorhandler(DatabaseQueryError)
def handle_db_query_error(error):
    """
    Error handler for exceptions encountered when querying the database

    :param error: Error object
    :type error: Exception
    :return: response, in JSON format
    :rtype: JSON object
    """
    return get_error_response(error)


def get_error_response(error):
    """
    Return the error response object

    :param error: Error object
    :type error: Exception
    :return: response, in JSON format
    :rtype: JSON object
    """
    response = {
        'Error message': error.message,
        'Status code': error.code,
    }

    if len(error.args) > 0:
        response['More info'] = [str(arg) for arg in error.args]
    return jsonify(response)
