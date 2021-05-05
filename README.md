# Ensembl REST API

This API provides the endpoint **gene_suggest**. Based on the arguments provided by the user, the endpoint will return a list of suggested gene names for a given query and species.  It queries the public database from ensembl.org, namely ensembl_website_102.

### GET /gene_suggest

Get a list of suggested gene names for a given query and species. Limit the number of suggestions to return.

### Parameters

|     Name       |     Type      |     Description                                |     Example value    |   |
|----------------|---------------|------------------------------------------------|----------------------|---|
|     query      |     String    |     Query typed by the user                    |     brc              |   |
|     species    |     String    |     Name of the target species                 |     homo_sapiens     |   |
|     limit      |     String    |     Maximum number of suggestions to return    |     10               |   |


## Example URI 

/gene_suggest?query=brc&species=homo_sapiens&limit=10

### Example request using curl

`curl -get 'http://127.0.0.1:5000/gene_suggest?query=brc&species=homo_sapiens&limit=10'`

### Expected response

{"Suggested gene names":["BRCA1","BRCA2","BRCC3","BRCC3P1"]}


## Run the API

### Run locally

You will need to have python3 and pip already installed. The application dependencies will be installed with pip and can be found in requirements.txt. The steps are as follows: 

Clone the repository via HTTPS or SSH

`$ git clone https://github.com/emmaco/ensembl_api.git`

or

`$ git clone git@github.com:emmaco/ensembl_api.git`

`$ cd ensembl_api`

`$ virtualenv env`

`$ source env/bin/activate`

`$ pip3 install -r requirements.txt`

`$ python3 app.py`

### Run with Docker

You will need to have docker installed on your system. Run the following command:

`$ docker run -dp 5000:5000 emcoo/gene-suggest`






