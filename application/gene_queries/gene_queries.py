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

    :return:
    :rtype:
    """
    try:
        query, species, limit = get_request_params(request)
        gene_suggestions = {'gene_suggest': get_gene_suggestions(query, species, limit)}
        return jsonify(gene_suggestions)
    except Exception as e:
        raise e


def get_request_params(req):
    """
    :param req:
    :type req:
    :return:
    :rtype: object
    
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

    :param query:
    :type query:
    :param species:
    :type species:
    :param limit:
    :type limit: 
    :return:
    :rtype:
    """
    try:
        query = Gene.query.filter(Gene.display_label.startswith(query)).filter_by(species=species).limit(limit).all()
    except Exception as e:
        raise DatabaseQueryError(e)

    gene_suggestions = [gene.display_label for gene in query]
    return gene_suggestions

