
from application import db

TABLE_NAME = 'gene_autocomplete'

class Gene(db.Model):
    """
    Data model for a gene
    """
    __tablename__ = TABLE_NAME
    display_label = db.Column(db.String, primary_key=True)  # symbol of the gene
    species = db.Column(db.String, primary_key=True)  # name of species to which the gene belongs
