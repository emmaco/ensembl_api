from flask import Blueprint, jsonify, request

from application.gene_queries.exceptions import GeneQueryError, DatabaseQueryError
from application.gene_queries.models import Gene

gene_query_bp = Blueprint(
    'gene_query_bp', __name__,
    template_folder='templates'
)


@gene_query_bp.route('/v1/resources/gene_suggest', methods=['GET'])
def gene_suggest_query():
    """
    Endpoint /gene_suggest responds with the suggested gene names for the user query
    :return: Suggested gene names
    :rtype: JSON
    """
    try:
        query, species, limit = get_request_params(request)
        gene_suggestions = {'gene_suggest': get_gene_suggestions(query, species, limit)}
        return jsonify(gene_suggestions)
    except Exception as e:
        raise e


def get_request_params(req):
    """
    Ensure the parameters query, species, limit are in the request arguments
    :param req: request
    :type req: request object
    :return: the arguments query, species, limit
    :rtype: str
    
    """
    try:
        query = req.args.get('query', type=str)
        species = req.args.get('species', type=str)
        limit = req.args.get('limit', type=int)
    except Exception as e:
        raise GeneQueryError(e)

    if query is None or species is None:
        raise GeneQueryError('Please ')

    return query, species, limit


def get_gene_suggestions(query, species, limit):
    """
    Query the database for gene names for the given query and species
    :param query: the query typed by the user, e.g. abc
    :type query: str
    :param species: the name of the target species, e.g. homo_sapiens
    :type species: str
    :param limit: maximum number of suggestions to return, e.g. 10
    :type limit: str
    :return: suggested gene names
    :rtype: list
    """
    try:
        query = Gene.query.filter(Gene.display_label.startswith(query)).filter_by(species=species).limit(limit).all()
    except Exception as e:
        raise DatabaseQueryError(e)

    gene_suggestions = [gene.display_label for gene in query]
    return gene_suggestions

