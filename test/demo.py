from scibib import data_query
sample_entry = data_query.AuthorData("0000-0003-1062-4397")
for article in sample_entry.articles:
    print(article.title)
    print(sample_entry.work_summary_from_arxiv(article))
    print('--------------------------')
