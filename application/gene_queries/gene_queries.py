from flask import Blueprint, jsonify, request

from application.gene_queries.models import Gene

gene_query_bp = Blueprint(
    'gene_query_bp', __name__,
    template_folder='templates'
)


@gene_query_bp.route('/v1/resources/gene_suggest', methods=['GET'])
def gene_suggest_query():
    query = request.args.get('query', type=str)
    species = request.args.get('species', type=str)
    limit = request.args.get('limit', type=int)

    if query is None or len(query == 0):
        return 'error'
    if species is None or len(species==0):
        return 'error'
    # if limit is none returns all?

    try:
        gene_suggestions = {'gene_suggest': get_gene_suggestions(query, species, limit)}
        return jsonify(gene_suggestions)
    except Exception as e:
        return e


def get_gene_suggestions(query, species, limit):
    query = Gene.query.filter(Gene.display_label.startswith(query)).filter_by(species=species).limit(limit).all()
    gene_suggestions = [gene.display_label for gene in query]
    # raise for status

    return gene_suggestions
