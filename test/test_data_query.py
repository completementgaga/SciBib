import json
from scibib import data_query

sample_entry = data_query.AuthorData("0000-0003-1062-4397")


def test_articles():
    assert any(sample_entry.articles)


def test_title():
    assert "Toward Effective Liouvillian Integration" in [
        article.title for article in sample_entry.articles
    ]


def test_doi():
    assert "10.24033/asens.2494" in [article.doi for article in sample_entry.articles]

def test_url_in_journal():
    for article in sample_entry.articles:
        if article.doi=='10.24033/asens.2494':
            assert 'https://doi.org/10.24033/asens.2494'==article.url_in_journal


def test_bibtex():
    assert (
        " @article{Cousin_2014, title={Un exemple de feuilletage modulaire déduit d’une solution algébrique de l’équation de Painlevé VI}, volume={64}, ISSN={1777-5310}, url={http://dx.doi.org/10.5802/aif.2863}, DOI={10.5802/aif.2863}, number={2}, journal={Annales de l’institut Fourier}, publisher={Cellule MathDoc/CEDRAM}, author={Cousin, Gaël}, year={2014}, pages={699–737} }\n"
        in [
            article.bibtex
            for article in sample_entry.articles
            if article.title
            == "Un exemple de feuilletage modulaire déduit d’une solution algébrique de l’équation de Painlevé VI"
        ]
    )


# arxiv_test_file = "test/0000-0003-1062-4397_arxiv.json"


# def test_arxiv_record():
#     assert sample_entry.arxiv_record == json.load(arxiv_test_file)

def test_summary_from_arxiv():
    with open('test/sample_abstract_en.txt') as f:
        abstract=f.read()
    for article in sample_entry.articles:
        if article.path=="/0000-0003-1062-4397/work/71678464":
            assert sample_entry.work_summary_from_arxiv(article)==abstract.replace('\n','')
        if article.path=="/0000-0003-1062-4397/work/62472156":
            assert sample_entry.work_summary_from_arxiv(article) is not ''