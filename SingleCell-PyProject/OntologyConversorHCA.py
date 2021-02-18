from OntologyConversorAbstract import OntologyConversorAbstract
from Project import Project
from Specimen import Specimen


download_links = {
    '1.3 Million Brain Cells from E18 Mice': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/0103cc41-0b30-52fc-8108-f267296458c7.tsv?response-content-disposition=attachment%3Bfilename%3D%221M%20Neurons%202021-01-29%2017.44.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHFOXUXLVM&Signature=bLZmcTlxmnajj%2BbQfDL3%2BwUG4AE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjECAaCXVzLWVhc3QtMSJHMEUCIQDdySdVGzPafrsoZoXE4%2FLg%2F0f7aFyT8AIXJ2D0XajZUgIgAsH2U%2F7DlgdDRZJuw%2BH9ujNMFEUAXGQ6v1dFSxgN%2FhYq0AEIGRABGgw1NDI3NTQ1ODkzMjYiDDt4lGXNLnv1CTx6SiqtASp%2FlVYXsizfoR9oOS4JWEyWGswKz6njXpgq9Yz2RdqpcoZd2i69YBfBNsdUTKGdgXdSgklBscqO8UP%2Fd%2FeabscC5hiVplP3DFIDumi1fLWyy4XW6W1f4GfgDmWdLQ7hRYZxYrCF9rEqqDg7huMublR6UQN2NB2GTPGA4OzwG6MY2hSOu97nXG%2FguHvDsNcwBwTEIbmVpmnu6zaC3WyBVGttnslYL6EsvZa5U4IRMPKo8IAGOuABLe2wGe%2FYhU3xMLOPtqmDXOejd%2BXSRXPPtCXMZaErTWIntcIOJyz8dbcZTg6s9If9hDdVY6AnBJRUZtH7FjC4g%2BjPz8OvSrmd0QIg6tLU%2FgYk6l7P4%2BGOj6s7HanKzCqgK0z%2FEbxw8YO1Iq610HTmKxF1e%2FB7emdJvAkDvZ5RHVETgexFNgns5frp9ppFh850lzjVB%2F6sw9Lra1iKMXwkZTK0m6k6wRiMr8TI%2BeFkUcg484dCvV%2BZIy%2BYSwXe%2B6NFbXgc2C5FD9ByLphQBqGj6MJSlWXE3Rr4mG5JzMIhKz4%3D&Expires=1612463572',
        'matrix': None,
    },
    'A Single-Cell Transcriptomic Map of the Human and Mouse Pancreas Reveals Inter- and Intra-cell Population Structure': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/fc48a395-f853-5d15-9c28-2d68cbf97344.tsv?response-content-disposition=attachment%3Bfilename%3D%22HumanMousePancreas%202021-01-29%2000.47.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHBOMECKLI&Signature=GfnouHhEpwmmbpc%2FfuZ2XUTYncE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjECIaCXVzLWVhc3QtMSJIMEYCIQDZOaOXcvvGOVw6iAGOfaiju3Evnw67C4aC5PsEbV7hDgIhAKT9pVkupKcEVLSIVCElUdaTsZs88D6Nk3QAc%2Bj9UIsgKtABCBoQARoMNTQyNzU0NTg5MzI2Igxil9pSuUuKRZmso%2BEqrQEwxkrF1JsVI2hkbsb%2FR%2BFcCYGa5nE%2BBTsqo%2BystLPqOh3S4P6PbOkO7oJhwjJDT4AaQ%2FjHnOBQc3Q%2BeYuJZv2WvElMBMvpVtK6pN4VzTRS4hKdHM3v8VWuW7ZTLRUfcrkygDTGIARzg1JDR3MPOpZMxw15bMaPb4GWVDcGQ%2FpnYKiwpgXuUvkZv7%2FpVe9YJUQpPkSPaWQQ5uBzKnxIdAe7z0%2Bp39IPNVF32DJUqjCq1fCABjrfAR5OibQfjgsWHC5iLq84y2p6VvLkW18LV0d%2Fy70LLrDpfsF6sbm9UfuKHfSn4%2Btuat0IMYsK4n4fK94Ha%2BFXfeG%2B3n20Db%2Ffd2ETY%2F5XNbHpZuzXda%2BhdTCqjt7JP9NB0TkDyEHhHq%2FJEPchpqZyXXuPBld1Uu1l3WazJP3dbhh47%2B52b%2Fz0dw6IXYjJjrZ7MRkOmMsUN82wkQ%2BgOrEl6TFBRqyVVkw%2Fjx1gs014bmU2nR41S6%2F606%2BKwAuK59izd2lGfS6ZhwpZHXa8TH1BFBITSKOxfaPp7ehtk%2FbyAlg%3D&Expires=1612464321',
        'matrix': None,
    },
    'A single-cell molecular map of mouse gastrulation and early organogenesis': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/cc9db872-1ae4-5ad7-b13f-373a19b7c135.tsv?response-content-disposition=attachment%3Bfilename%3D%22MouseGastrulationAtlas%202021-02-04%2018.19.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHME4PMXOB&Signature=T%2B1SmCBCeZ8NxpQlVHXvkwvsEcg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjECMaCXVzLWVhc3QtMSJIMEYCIQC%2FjoDctpnkNiTBvZobkPMgEZVAJTPjFn9L%2BHdN6r0leAIhALn8tCLCiBG4bxOkIPJU3Zh5MTq23vpmzdUDU%2BQuGR%2FFKtkBCBsQARoMNTQyNzU0NTg5MzI2IgyNHtVJKU18QMoqsm0qtgFWwAq3k0Ut1XKDEEKRNggzOG%2FnHBacAp9SVgd3gqGfk3hhhqcgb8Qh9rqP%2FByIo22OU%2F%2BGANl%2FYTDx446mVMQxBhA77q4%2BYnAwACcdVyWTLSxzOMWzBuq1931wzS8D09iAT6MUBpys6imUEmoNd6UsOKOlqnqysFZnAIz8OLU66qExR78ebZsarwZMoHXCjer335qjFu0r%2FJiMB%2B0hm3Rq1xmQaJmIwD7avkhpPqLUorSRpns92TCO9fCABjrfASSGkKbUd%2BJGQosnNXJ%2FBtRs3RwDfUAeCYx1p9SHWDT5ecdC3p1bP9vx1KXsu2kKZQbah2uUd2odErKmCn3R2zqf3rgGBmJ17Nyxtn%2BB%2F7wC3cfg3MiQkb2EeD4%2B0PJTKk%2FBoRolN4z%2BYWJm4QjYwRn1Nmagg%2Fo1ZX84E6zyINqTXsECuj1S4srzieqGMeX0mmWecMt1RD3m0KHtQTQv0vP0FZnQia6krgyOh2ts9NXZN9OhlDac1uL6uN%2F2mhAAZKmqRw6osTZrwVEVgY%2BAKazsJC%2FPHaMzsba1i8Lp0wg%3D&Expires=1612466348',
        'matrix': None,
    },
    'A single-cell reference map of transcriptional states for human blood and tissue T cell activation': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/692b7b8b-74a3-5d3c-99c7-bd96ca63b6c9.tsv?response-content-disposition=attachment%3Bfilename%3D%22HumanTissueTcellActivation%202021-01-29%2000.50.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHHHG66S7G&Signature=XYVwH0Zm5u4sw1F1icno2HuK53o%3D&x-amz-security-token=IQoJb3JpZ2luX2VjECIaCXVzLWVhc3QtMSJGMEQCIDGxntj7rErFMyMhNeasQkR7%2F613qisgaZSUXZGHcywFAiBFxDznEOTrI1UerYXBaoXz2VrXonhGUdOo%2F5eXUQ%2F%2FOirQAQgbEAEaDDU0Mjc1NDU4OTMyNiIMyA%2FN%2B2HNnR8vctt0Kq0BR1rnQ2eYvu5l7dFaJ54mJw%2Blftz%2FVQOr%2FEhmgEbwQqt2%2FDCZRM3viGWGmOnQeycXvvFXWo8KW9jGKWOGQH5yEXMEHT8SZh2DbHHsYpXumkN0dnakvUrb2dpAFvZGZ%2FI2Wf8kmc30e1we%2Fg1W1Uye5CKqEoY%2B24o7PocRCPuHVjU%2BVcTZT72ksm3T5O8WtModwDJRSmOtYJx9toi920I2axbWedO7KC8hMk7xVBEwseLwgAY64QGgyv%2FSozUymVWcyC7Ct3YizMpj5ylg%2BX%2BmW8ijhw%2FXOZZSy5AWhHjBK1m2MSans%2B8NiovA3OtRkJqCurDgThj8RkJpblytDbtQz9zc0npx8fmDdYqwmIYHws8F18k7lzLsZ475x2nbc9%2FU38g2XUUpNA6%2FerHQtrbDG6CnOEypFlRTgAPkGUff%2BsrFleeARZo0%2B6IpEy8grtLcEcslO9hocpMwThVyWE063TKWC9KcbHoQ8ARcvRRVB8dEqLRIK0N3rr6hkKv2ACAX9e%2FQ0yNFnwTABIY%2FgSnfmu5xS7xTIAI%3D&Expires=1612466429',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/4ff03b1f-0162-4e34-bd00-6619535e5d98/4a95101c-9ffc-4f30-a809-f04518a23803.homo_sapiens.mtx.zip?Expires=1612525611&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=K%2BHiTIi7qf9BPnsLFrHeCa0HrY%2BVII%2B0HSKxwVdg6ZSA6am6EvtjrmTG7eeWrxwYZjxN8TciY46rF2opORrVaaW%2BS0mOdNSNvRocc7VHxmI8fPptgxq0pcso2NmK0dUCWCezUvmvwuNod1zo3ndSU8pcPq8KplwuYEfmXTjEA1WnAUE2YUOy%2B2UFUF8XGG97uxrsxnNJ5xY0Pp3UHomlGlL2kc88YA2LMaQEBrlwCAmNACdMtQUCsTOUaZirTa%2Bc8BUsgo1iaLvC404XsYfVuCgomDkSOkSuS98QaY1vVXDdwdQ3%2F8Y8p9bwVM03%2BqD98Kt1Slp4MgBP%2FziLqA7v4g%3D%3D&response-content-disposition=attachment%3B+filename%3D4a95101c-9ffc-4f30-a809-f04518a23803.homo_sapiens.mtx.zip',
    },
    'A single-cell transcriptome atlas of the adult human retina': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/81dfe082-3ffb-53fa-a8ae-cbdeed4c909b.tsv?response-content-disposition=attachment%3Bfilename%3D%22WongAdultRetina%202021-01-29%2000.52.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHPDQZ2253&Signature=%2FVZzvc5KDcPO1nekSIciXUZilYg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjECIaCXVzLWVhc3QtMSJIMEYCIQCho7blSbP7GoMn9TXtOJnGZ8Mp%2FZlrsLhfn6sdK%2B2ImwIhAPNzk8mddBeBAYgz9xFt3H2GHeO6AzSJ2175VklXrzmZKtABCBsQARoMNTQyNzU0NTg5MzI2Igx4R8VeI6bGn79sM9YqrQGmKi4vkLzXdB0qxhSoJ%2F45QAhnT3CKOKJUMIXHoUoAQ5ul8XzBEBhs0YIlpuwZ6ZHhF0mYN6mOBaCFcsQf%2Fd9P0BTu%2Bz50JVTi8iyScy3hyp%2F73cAVDLbpvHcECpEfZMUNN9opZemhyqAVtLjdZAqfDI4dHXOkjIx1gRo83ATSlteRjMLxux089gpeR3FF5Lw3dAcedmm2AYjKVFoVFHeU8BrV07uGKzqT2ir4hzC%2B3vCABjrfAZdccxkyupBnJehZiHANa4jc3uZdKMCoAr8T%2B5PTSG5hJTwgnlpvFkn32gmc86UqNL0LiRvZPV96JXpZpvzqK9vpMmBUjrOa2mDs7suS6Ng4GzqTzg6qT%2B3PHGCYrM9KYjxIQLaXDEq%2BTts1Nl6cmeEY5xtv68%2FXQtVkNALs0hWIU9WAltUUt5ZGxwcuLjkNLUMQF7JBA3Z33E9YyrsS4ZFdfx6bmLpPqtjTjBdRgkmbZfWCgFCtKjjGQc9sGoP5KB9cDwGKz4oQT3Vt8tUK%2FKInV1xPApWBqPDHqPT3hmM%3D&Expires=1612466539',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/df2476d4-ed12-4891-92cc-7384c32be978/8185730f-4113-40d3-9cc3-929271784c2b.homo_sapiens.mtx.zip?Expires=1612525654&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=HS1rp4nnTFFQK7cjiWDpSflJecSuzekRB6U4nc0mf6GmVYJzfwiF%2FT6IuwGijWT8z3fw8fbKhmY7MKgk%2FeqsJ1KwDX5%2Bv4Jnav%2BeKklQq7%2BuKFKQPwmqFx3ulFrYbjZNAIqC6jaDFLVNDVzor%2Fw59EDohI6Lh%2Bla6RaBTPHpAE9a%2FKGvgxrYU1OT8C7k1LuG5YlYociVzyU8ZoukANJv0%2FrsKFQDZBPkXvDqLqhC%2B7Bpf97%2BjKJN5gRo3LqC3eRqwT2K9hZclXjLug90wKP3GWqZGU484ZDzEgxXsl2wxsy2%2B6d0HlC%2BZew4xGmSG1ioM9Q5OWLUv2YAfLJbEh6KUQ%3D%3D&response-content-disposition=attachment%3B+filename%3D8185730f-4113-40d3-9cc3-929271784c2b.homo_sapiens.mtx.zip',
    },
    'Assessing the relevance of organoids to model inter-individual variation': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/b5661f04-b67e-504d-80a2-2a7f36ba16ac.tsv?response-content-disposition=attachment%3Bfilename%3D%22HPSI%20human%20cerebral%20organoids%202021-02-03%2007.31.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHKAZOIG5B&Signature=OItFFyq8USEfd1PfgQU04rFx%2FhA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDIaCXVzLWVhc3QtMSJHMEUCICj2PJ58QgUQMOnwq9BODhXpReoUJWe9d4O7QimNKTFBAiEAnJyyfgh4x19mNKY3NrBfUzPYUhB2zGO1G5qT2kqOGaQq0AEIKhABGgw1NDI3NTQ1ODkzMjYiDNl9GWghl%2FS6U4YBkiqtAfdlxcOplyah5Hsvlei3fqqSS5P4jQ2AZt4aOAYmFglf2Vi%2F2nIRckkdluMVxopk3lIltLprkZkZt3DdbFDYv8z0b%2FJWkb%2FbnBUshkm9hcV97F3eIBlvI0Kyt5VpMSLpiQHWMQ6BP9fYte7SJMDP%2FpCQGN7uTuoHh7%2FUjzaJe0cMGsmT2M94Ez%2BBxU121%2FoICP8eevpEgpB9rJfoNbevWX7USPykosbHC5dfaCHwMKOb9IAGOuABVa6WwZFOXZw8rUkeQjYiMkihI9af6tfnykImFuVHoqal1hgYCgjA1bsbM9Uiv5lmcNdiIyIuuyz4mL49zN0UOqjJlL%2FxTKzljs6e52i1a%2BT9lKnntZHACI%2FFQcIG9b53VYaw336sNHY4NgOjzP63mJ62bfxTk2ch3cOtNX8OFqzO1WEFnMRgoR%2B1LJQe8wqKA3kTxEkKQ%2BsCf8wK1v6pMTa680QwYp26xe78e9d5x45a09gZgJj4Sm%2FRrOzfSS4mTG7AbqRCOuywDrQrmnXOJQv9YwiAjFWcYfVlOEanMnk%3D&Expires=1612525687',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/c32442c7-756f-4a96-a019-b5ebea175413/005d611a-14d5-4fbf-846e-571a1f874f70.homo_sapiens.mtx.zip?Expires=1612525710&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=wK1TZLF6SeDEpLsEPh61fUtTwtFDHWLmGXp6PAshGzFmGdmuBy7sylgwqn0WWI4PD9NEgHs8ZaNmg6%2FVu9x6dC%2Fj9ngv4uqBxFbjx9t8bj3C2XOBnHkrWg78%2Fphj%2F6lAvaM5UInM7ve%2BRAgDPrnTUZ2X9QicU1E3yUW6rWWkIc8QNgdmU%2FlfhmahJi6NsZWS%2F5a84BNvPtWtdaGUZlO8tCMU58wCnKeiXXgjnKZlm%2FOPwTvw5IlkbqDJ7jWYLPSJTvLwYx0kwZf%2FLmlid0VLEWYUorIaHHSwQp5XPN3OdJo5%2FFEYnCD6XbLZUXG1ZXIfpyEdmNih6ts4MjlY%2B9JxaQ%3D%3D&response-content-disposition=attachment%3B+filename%3D005d611a-14d5-4fbf-846e-571a1f874f70.homo_sapiens.mtx.zip',
    },
    'Bone marrow plasma cells from hip replacement surgeries': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/98f2d860-7caf-5beb-ad3d-2a62a301e1a9.tsv?response-content-disposition=attachment%3Bfilename%3D%22BM_PC%202021-02-01%2006.49.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHJDFQLAY4&Signature=aLlh1FCYu423HhwmGxTYg6QnxAA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDIaCXVzLWVhc3QtMSJHMEUCIHWxs6RBLEqnRHEA5VCay7yMYkuB5TszPoBPqT0e6AvpAiEA6H8xWOzgGRBrO9qZG0IcMdp0pjR9%2FJVyqA10rvqnGTcq0AEIKhABGgw1NDI3NTQ1ODkzMjYiDNlFHia3YWHKYm8ioyqtAZEA6BeBlENUg5rX3nrZxT7M9W%2FVIW1NRmLwm6tpq1OHru5boX23MyL%2FtLelz5qxc6%2B17d6IDdtFDxShVuMw6ATx0CFS3p8zGIGlQcED3IZV1Kfcu8tkVMBUTm%2BI56BhPace7lysmofB4ebedwhStJlWL7snZ55bIBl9tAR4ADLoWqO%2F1viMP%2FKXAHANjtIURgfXJuYJWHN4yFqLfMUjPHsFHJvdKuJh9nSPP7zuMMOb9IAGOuABS11yy43SD3t5LgUg20vzaMKeUI4pU4IE%2BzBkjSIkp0NvG%2BiSX6%2B7u5feOVNpi7LPZ81MybOsib7D9tQ69%2BglRN%2BdfWVWxmAXxooEL%2BHnFeZKQhphk8JzFRXHZDCGVi%2FjJza2j%2BNgqZiD5WCJH5jpk%2FbQPr4Mo49N3wbh1i1amJF%2FNxaSPjJ%2Bx2M0pCGFgogxVN6oct%2F8ufYym59ELJenHAq9kCQ7Q9xdR1R6dKloV%2BVlsvM8vG4QfrLMyYDSHKqw6OOQGzKbeqCwa9i7fDNTZwe18g2Bez7bUJEsVhjBSgw%3D&Expires=1612525738',
        'matrix': None,
    },
    'Cell hashing with barcoded antibodies enables multiplexing and doublet detection for single cell genomics': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/460af53a-103a-5d5e-9651-70e54ba3eb36.tsv?response-content-disposition=attachment%3Bfilename%3D%22Multiplexed%20scRNA-seq%20with%20barcoded%20antibodies%202021-02-05%2010.49.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHLWQB5S4B&Signature=IEw%2BfuFE8oziVOflp51yx56viWI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJHMEUCIQCPAsi1tOhDiyfdlf1cDTrsAJVW1qF0%2FCGvNKBrR9x%2FLQIgKe4ySsRF7pKqnjpXwEhsdCc6I%2BJa%2Fx5t9wpeaTps%2Begq2QEILBABGgw1NDI3NTQ1ODkzMjYiDOJeA3C3HZ%2B3aQlVxyq2AVgwmVUG0S3v5N7PVV0K%2FSLzA3C%2FnP%2BB9JXRvpsUPIkkDVP427Wk9KWVH%2BL2WnEEiC5whiqcmHR%2Frv7KeA6UU8CD8jF%2FgAyIGknVWbMVcVqcrfqAZ7WTDDTFtqDmAUO1CLtLg8%2FRNwqiM7336Ajw8oTz5zEhsiXkrDkrD%2B0odNyo%2FvXNhuIJMrFGReTN%2BmnfONN8LOZmdWJy0kS7LIhblpY1ft0A3YzrqAusDao7MZsJTbIt3M2MMLXF9IAGOuABcVdLdd4eAnFA%2B6YtE0Y4iGkK91lxcEm3mayttSfFLgdeYjS8afCaumJisGTjt2fUWSx6xRK3%2Fx9k6ieg%2BOIcCxu1quWN3GgnHTTiIHHvWT7XyhoJbzyopQz1JIgwMnmH9ATQg34ncIOZYrzKKVeox08ko9En8PEPGiTM5bPYrdVRrcSkSY1R1T6cvh%2FOAFfeY99fvS1Y6fyt0mAlACHTvvjqOT0KchDIWZF7UlQlYueBd02GTcEX34Qni8dKSHpofGGZPmGQ6x%2FD7K5ZWWKPQhKyM8WMgYIB3ix%2B2%2BzvI%2Fs%3D&Expires=1612525767',
        'matrix': None,
    },
    'Census of Immune Cells': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/2046346d-2a66-5e79-af50-5642106c0f81.tsv?response-content-disposition=attachment%3Bfilename%3D%221M%20Immune%20Cells%202021-01-30%2014.17.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHLLGW7BO4&Signature=ezSE0QyOm8HT4LjfyhfGeSpf91k%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDIaCXVzLWVhc3QtMSJIMEYCIQCySvlCq1L5o7vittt6TXTh1BizZ%2FxsVHQtma9B2TB0NwIhAIUPpKHxNX1MS4a3pzjXzio2GEoGP4SHQbH7GwYIOp3wKtABCCsQARoMNTQyNzU0NTg5MzI2Igxo%2FzZ6gDrD4DjNmC8qrQGyFL37ypsvzSjfsDz9uRwDwKRtypkEuByvV2JyvprMGV4Ngih%2FAhMNPqnC8p8eoqckLBSLFB18SyhkXjdOxEPKAO9iEc8MYoksIw7mTuctl10PDEeY%2FtgSceZoPCRWi8fRDOW0cnhFzSN%2BYbubxm1jnADOEgaPhUyGvC4xyGVi7a211iIrr%2FRXb7gXBNn%2BIpSUWYeVn3plHC1XvEKF8QH1vMEVIPrP8tgjBO3W%2FzDBofSABjrfAc1Sbt0FjOBktA2R1PpOBuUXVobZUzUPrBUh5I%2BNNPYiJz63GQo6%2F8yT1bVBdm51T%2BnjvAO5%2BrSj6xfDREqChaJ5cWAi7VjrH5o9Jj3xeWwnNV%2FdGjUl43N00%2BUb8kS4Q31PjgV84KEA4PDykuTMtJ%2F8Mjhky%2F%2F8OG%2FRYMXnkFMXYAdcRiy5L%2BkUOrNtmbWy6huHzuzML0SJnhi7nY4G8IGQDcqJYo2J7L74RTvoPUDXDaEuXrYD9K1C64iNpm4ZV%2BMxYfoYmTL%2B3FAQDOE9RGtqk6%2BHYIdbtYDEkkemuOU%3D&Expires=1612525787',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/3263bdb4-38dc-43ab-a4c6-fb281f37b26a/cc95ff89-2e68-4a08-a234-480eca21ce79.homo_sapiens.mtx.zip?Expires=1612525852&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=DniMRER5FTDiOZQKaXIliLqb5tJCUAK4QD4nDjklIIKHsIxoGz1wzrz4J1eOPiQf5d0YDfXxwCfIpKmTsEg7k65AfJh08kcuSamXgQ27DoWx8DLQ%2Fck553TFUjGbTz%2Bibz7fSB2JIajMf%2FxQXSiWNUy9Pk43D6AEhrlGhS1APpqMpNStWFyshmTx%2BSk0pQkmA%2BV%2BW2%2F8r3JlfbDCslPFXWQC82DeSnEqeXZ3iKLv%2Bsz1nec5KssiTlDy9DdL2zcyxdseZ%2BG6aXA4IyWF6PHspgB9aQefaMzEYpoyQ8dnmGX7wGSEVOWUFUEjgXbkfaDLZud4KBei0EDJC5OJo0A%2Brw%3D%3D&response-content-disposition=attachment%3B+filename%3Dcc95ff89-2e68-4a08-a234-480eca21ce79.homo_sapiens.mtx.zip',
    },
    'Comparison, calibration, and benchmarking of high-throughput single cell RNA-Seq techniques for unbiased cell-type classification': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/3657cc8b-2860-58f9-8090-75a8fdb61d5c.tsv?AWSAccessKeyId=ASIAX4XVRZKHLLGW7BO4&Signature=MxWGWusx7ueGK5FSqel4B6pM45M%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDIaCXVzLWVhc3QtMSJIMEYCIQCySvlCq1L5o7vittt6TXTh1BizZ%2FxsVHQtma9B2TB0NwIhAIUPpKHxNX1MS4a3pzjXzio2GEoGP4SHQbH7GwYIOp3wKtABCCsQARoMNTQyNzU0NTg5MzI2Igxo%2FzZ6gDrD4DjNmC8qrQGyFL37ypsvzSjfsDz9uRwDwKRtypkEuByvV2JyvprMGV4Ngih%2FAhMNPqnC8p8eoqckLBSLFB18SyhkXjdOxEPKAO9iEc8MYoksIw7mTuctl10PDEeY%2FtgSceZoPCRWi8fRDOW0cnhFzSN%2BYbubxm1jnADOEgaPhUyGvC4xyGVi7a211iIrr%2FRXb7gXBNn%2BIpSUWYeVn3plHC1XvEKF8QH1vMEVIPrP8tgjBO3W%2FzDBofSABjrfAc1Sbt0FjOBktA2R1PpOBuUXVobZUzUPrBUh5I%2BNNPYiJz63GQo6%2F8yT1bVBdm51T%2BnjvAO5%2BrSj6xfDREqChaJ5cWAi7VjrH5o9Jj3xeWwnNV%2FdGjUl43N00%2BUb8kS4Q31PjgV84KEA4PDykuTMtJ%2F8Mjhky%2F%2F8OG%2FRYMXnkFMXYAdcRiy5L%2BkUOrNtmbWy6huHzuzML0SJnhi7nY4G8IGQDcqJYo2J7L74RTvoPUDXDaEuXrYD9K1C64iNpm4ZV%2BMxYfoYmTL%2B3FAQDOE9RGtqk6%2BHYIdbtYDEkkemuOU%3D&Expires=1612525884',
        'matrix': None,
    },
    'Dissecting the human liver cellular landscape by single cell RNA-seq reveals novel intrahepatic monocyte/ macrophage populations': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/476f541a-1f42-57a5-b8ea-a053534f895f.tsv?response-content-disposition=attachment%3Bfilename%3D%22SingleCellLiverLandscape%202021-02-01%2007.33.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHLLGW7BO4&Signature=oUqmDqQh5VboQRmTu8d7DZJ8mxs%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDIaCXVzLWVhc3QtMSJIMEYCIQCySvlCq1L5o7vittt6TXTh1BizZ%2FxsVHQtma9B2TB0NwIhAIUPpKHxNX1MS4a3pzjXzio2GEoGP4SHQbH7GwYIOp3wKtABCCsQARoMNTQyNzU0NTg5MzI2Igxo%2FzZ6gDrD4DjNmC8qrQGyFL37ypsvzSjfsDz9uRwDwKRtypkEuByvV2JyvprMGV4Ngih%2FAhMNPqnC8p8eoqckLBSLFB18SyhkXjdOxEPKAO9iEc8MYoksIw7mTuctl10PDEeY%2FtgSceZoPCRWi8fRDOW0cnhFzSN%2BYbubxm1jnADOEgaPhUyGvC4xyGVi7a211iIrr%2FRXb7gXBNn%2BIpSUWYeVn3plHC1XvEKF8QH1vMEVIPrP8tgjBO3W%2FzDBofSABjrfAc1Sbt0FjOBktA2R1PpOBuUXVobZUzUPrBUh5I%2BNNPYiJz63GQo6%2F8yT1bVBdm51T%2BnjvAO5%2BrSj6xfDREqChaJ5cWAi7VjrH5o9Jj3xeWwnNV%2FdGjUl43N00%2BUb8kS4Q31PjgV84KEA4PDykuTMtJ%2F8Mjhky%2F%2F8OG%2FRYMXnkFMXYAdcRiy5L%2BkUOrNtmbWy6huHzuzML0SJnhi7nY4G8IGQDcqJYo2J7L74RTvoPUDXDaEuXrYD9K1C64iNpm4ZV%2BMxYfoYmTL%2B3FAQDOE9RGtqk6%2BHYIdbtYDEkkemuOU%3D&Expires=1612525932',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/ada9a74e-7b34-4f9d-9a5d-89b02f1dbb2f/4d6f6c96-2a83-43d8-8fe1-0f53bffd4674.homo_sapiens.mtx.zip?Expires=1612525950&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=LegcEmd39WorF7Pw8%2FxmXljRlU%2FZir74FDZvgAtmUljKvi9cUCpFFU93wnHfSQXJc5TpThIOzmcxsovWPyUyHDfSjYDwk2UIb%2BCpAIWNvKDDv6BElCaLykfvwC%2FmfhBBzmj5A8Y44WbbITfr1rrFxU1cnXSkcXrZsMNnxR4PwMyEW%2BjWsPQqDk3YHpLictnZeQkfz58jRu1YWLeUD2jJoALwQQBsjFRAI%2Beuo6lsJ5%2FLcbzPw6aDTHVugRUxGcY2w0t2AvMoGS0z51aLOqAvUuGP55t%2FkxxESCHYo7brMbRJ6Wl4JRw6vQ9EhICl4qjwQf70vkaK62j7toqFht3irg%3D%3D&response-content-disposition=attachment%3B+filename%3D4d6f6c96-2a83-43d8-8fe1-0f53bffd4674.homo_sapiens.mtx.zip',
    },
    'Ischaemic sensitivity of human tissue by single cell RNA seq': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/7fe57bea-5c59-56bf-89bb-9d977f404d6c.tsv?response-content-disposition=attachment%3Bfilename%3D%22TissueStability%202021-02-03%2014.52.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHL5YDRSGU&Signature=uQVbGRUYdkARvaviIfyEP6ujxFQ%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDEaCXVzLWVhc3QtMSJIMEYCIQCXNdMsPs7CtZaT2c%2FKqrTkgxo6VMlPsQfNGOQzfhMyvAIhAMoDVjFqpPS%2Bw0UErOVIX8xg6VcV2chrsUohX9X6vX9BKtABCCoQARoMNTQyNzU0NTg5MzI2IgyTEiSMiyRXIqodbVEqrQHp%2Bc0rYVieQClKLiwiJ4QH9NnktZLJaManJ4RvZ3GPewQ3Hmr46CMOCvvr5DCEgl8lgQtll90jrKIV9JMhZmCZJSy5aWEui%2B4eZ%2B4vGFQP8hL836tB1DxjOJJCL1EgvpMTDXUVeKwuFwYVjf9dO9ei%2FcgAMmjFJGIcst0qyw3tuyFc9vYtkInEp3fnqLGo0cZaperWBrjcfvyiikqQNq747Prb5qx93BwzDoGJ6jCAjfSABjrfAcMpGfLC0nifaG7a2rDWR7b2wr%2F9qtcBGBcuzhgqrthz0oSRndk%2BX%2FBMJbr3ZPSXO9eplEKB2P0MBqDmDAkN3L%2F%2FuPJA5khqxeW4BHyOtuv7O5IA8b6qfMG5ABJQXOtAqAFzsRzQe2b14d4gesaJ4wEoBT3nAqm%2FFNdHO1cb7itsYJ%2FvSjfrU7q8dFRW9qSCQyPYTCqNcR8uWjOecvqUjPZvxYvYRmnwWhN5xzMcb5LwH3h3N%2FYm1bTjZTu45JVgoDS0ObTRsM1PJebjC%2F0OdZ4j9bbrozFU4y7KQoi2ra4%3D&Expires=1612525988',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/e7e0efe0-7cac-4af2-bcfb-81a0ef50ff79/c4077b3c-5c98-4d26-a614-246d12c2e5d7.homo_sapiens.mtx.zip?Expires=1612526012&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=b6uGrTTwAGi2qOz7bxlUuDjffgoE3NQsVSniR2QDJqVL55wfewQP5ltNmW7CM0ZAoLnS2BWjWxglehDJjIoZAXBdm87ZkBb0kwIIgTSxfBTLPv6EOX1bMn5GkO7pwez0X3Pr6%2FcGKHwjp%2BNcaFPYh6uV5bMYcZJBcPn0YF6dEi%2F4wPNpgzobI9ld3EbgA4%2FQcPYV5HUQ%2FB74MKkj1qnLjM6xRkcHhC4k%2FAJsMqKSiwz%2B%2FGpI4CJbvlcX9VEgZW2oZTLRsqQNR7cnbp4%2FNgDCQVqiz9NQ%2BcschHI%2BrZ3M6buTJOSGtZWl8awT8hIG735gtm3acF5MDq2JFWrXvO4XBg%3D%3D&response-content-disposition=attachment%3B+filename%3Dc4077b3c-5c98-4d26-a614-246d12c2e5d7.homo_sapiens.mtx.zip',
    },
    'Melanoma infiltration of stromal and immune cells': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/db367260-6eaf-5b1c-973d-fcd5566b786c.tsv?response-content-disposition=attachment%3Bfilename%3D%22Mouse%20Melanoma%202021-02-04%2011.18.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHJDFQLAY4&Signature=QeDq8%2BtJEJSXqhYchFY%2BjuIWSeM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDIaCXVzLWVhc3QtMSJHMEUCIHWxs6RBLEqnRHEA5VCay7yMYkuB5TszPoBPqT0e6AvpAiEA6H8xWOzgGRBrO9qZG0IcMdp0pjR9%2FJVyqA10rvqnGTcq0AEIKhABGgw1NDI3NTQ1ODkzMjYiDNlFHia3YWHKYm8ioyqtAZEA6BeBlENUg5rX3nrZxT7M9W%2FVIW1NRmLwm6tpq1OHru5boX23MyL%2FtLelz5qxc6%2B17d6IDdtFDxShVuMw6ATx0CFS3p8zGIGlQcED3IZV1Kfcu8tkVMBUTm%2BI56BhPace7lysmofB4ebedwhStJlWL7snZ55bIBl9tAR4ADLoWqO%2F1viMP%2FKXAHANjtIURgfXJuYJWHN4yFqLfMUjPHsFHJvdKuJh9nSPP7zuMMOb9IAGOuABS11yy43SD3t5LgUg20vzaMKeUI4pU4IE%2BzBkjSIkp0NvG%2BiSX6%2B7u5feOVNpi7LPZ81MybOsib7D9tQ69%2BglRN%2BdfWVWxmAXxooEL%2BHnFeZKQhphk8JzFRXHZDCGVi%2FjJza2j%2BNgqZiD5WCJH5jpk%2FbQPr4Mo49N3wbh1i1amJF%2FNxaSPjJ%2Bx2M0pCGFgogxVN6oct%2F8ufYym59ELJenHAq9kCQ7Q9xdR1R6dKloV%2BVlsvM8vG4QfrLMyYDSHKqw6OOQGzKbeqCwa9i7fDNTZwe18g2Bez7bUJEsVhjBSgw%3D&Expires=1612526055',
        'matrix': None,
    },
    'Precursors of human CD4+ cytotoxic T lymphocytes identified by single-cell transcriptome analysis': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/b0ae9dc9-aa70-51c8-8027-2c5aba429474.tsv?response-content-disposition=attachment%3Bfilename%3D%22CD4_%20cytotoxic%20T%20lymphocytes%202021-02-05%2010.54.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHLWQB5S4B&Signature=4gq8uhLiN%2Bcl7yX0e3E3TPqaiWk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJHMEUCIQCPAsi1tOhDiyfdlf1cDTrsAJVW1qF0%2FCGvNKBrR9x%2FLQIgKe4ySsRF7pKqnjpXwEhsdCc6I%2BJa%2Fx5t9wpeaTps%2Begq2QEILBABGgw1NDI3NTQ1ODkzMjYiDOJeA3C3HZ%2B3aQlVxyq2AVgwmVUG0S3v5N7PVV0K%2FSLzA3C%2FnP%2BB9JXRvpsUPIkkDVP427Wk9KWVH%2BL2WnEEiC5whiqcmHR%2Frv7KeA6UU8CD8jF%2FgAyIGknVWbMVcVqcrfqAZ7WTDDTFtqDmAUO1CLtLg8%2FRNwqiM7336Ajw8oTz5zEhsiXkrDkrD%2B0odNyo%2FvXNhuIJMrFGReTN%2BmnfONN8LOZmdWJy0kS7LIhblpY1ft0A3YzrqAusDao7MZsJTbIt3M2MMLXF9IAGOuABcVdLdd4eAnFA%2B6YtE0Y4iGkK91lxcEm3mayttSfFLgdeYjS8afCaumJisGTjt2fUWSx6xRK3%2Fx9k6ieg%2BOIcCxu1quWN3GgnHTTiIHHvWT7XyhoJbzyopQz1JIgwMnmH9ATQg34ncIOZYrzKKVeox08ko9En8PEPGiTM5bPYrdVRrcSkSY1R1T6cvh%2FOAFfeY99fvS1Y6fyt0mAlACHTvvjqOT0KchDIWZF7UlQlYueBd02GTcEX34Qni8dKSHpofGGZPmGQ6x%2FD7K5ZWWKPQhKyM8WMgYIB3ix%2B2%2BzvI%2Fs%3D&Expires=1612526079',
        'matrix': None,
    },
    'Profiling of CD34+ cells from human bone marrow to understand hematopoiesis': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/028a7ca0-5d65-5bcc-a105-cf9ea0284209.tsv?response-content-disposition=attachment%3Bfilename%3D%22Human%20Hematopoietic%20Profiling%202021-02-03%2001.55.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHHDDP65YO&Signature=Jk4lEtkVns%2BAzJFbVW6ckn%2FpDbg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJHMEUCIQDkll4gTPtl5jOoB0aU4oSBOml99xG3pqYm0wwRjLFZPAIgS7HFVvhh%2FnryFZUIHUyrRg%2BlEHHuQ3FhLKrgchzmm7wq0AEILBABGgw1NDI3NTQ1ODkzMjYiDMEBqMLC1KPS7JScCSqtAa6eJtq6BfNDKfDTVvPUwYV0CyoffLV%2BcVb%2FJkTpvMIPA6tuYkN%2BkXGD6dNLPOoJAj0KAhxr6dxKJX5bRFzVBVeQgnj4gekiVPcunoq7KlZq85b%2FKcjmVvUCOHvupoYh5kwjaFXf6x1Tt31vg64DWillXORxTfaPFc1QusyCV%2FUWEU7x%2F%2FDEiTnO0aG%2BIpB2tRzuNHdZ9SPHgGsytt3dwgNSKJQ4DUlJPOdjXxlsMIfH9IAGOuABtDKesBTYrSTuZJplqnNsBfp%2FdNAQO4m%2BbvqOTrqqky1v6QMWY0eW8E706442%2FQu8wzhnp25BG97U4m%2BtwGBxBTP9lV1gc5%2Fbj8Jy3EDEI4FvtEAJT0w5SkO5sIX8bvuauHV8wF0ySm52wG3pzWzoGQnpSajwqKS0bRWuSteTJzJsKJ8uLs8IxoZDuAKy%2BtYWIR%2BwQIs%2F25%2Bqc92v%2Flmcvht0pARPqGWOqj6UFPqHUrgojAWg8o%2Bf8y2IriAtcoz6V%2FsyWsvzFv9IE9elZn6v12gRqErOsHcFHDwPe4OfmkQ%3D&Expires=1612526109',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/6ee6dde6-27e7-4366-ae13-f54ecbaf5246/091cf39b-01bc-42e5-9437-f419a66c8a45.homo_sapiens.mtx.zip?Expires=1612526125&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=RtTbdyuUzTuKIR1VAYSSzXtfeVK0YuidLQhTVnhYipbq%2FoVrjGObYgEAqEM6W%2BAoLjZXPNJQYuXu24CO27ZM3VbIxB%2FH6DNKdOujH8eUgfAiOiYl270TV%2FFfspbE5Q%2BkWRmKQHLoVpPUgxCqCijr2YGzBgbpcHuuQUPoeg0bo2r2eE%2FWJtcliGQfL8D3XhZeviutnPOOih7ZUP5HgaS9Rl1mLvnF9Ba26p8QHVo%2ByulySw3SamDVTAHM8hBpqechmGmRJFgLUI4XlmINAbLHkL59jelt59luTDlrMTILdHFlTS8fnPn2MvujnuNeMOb0FbpDwpjgmHMlcvQ603IE6g%3D%3D&response-content-disposition=attachment%3B+filename%3D091cf39b-01bc-42e5-9437-f419a66c8a45.homo_sapiens.mtx.zip',
    },
    'Reconstructing the human first trimester fetal-maternal interface using single cell transcriptomics': {
        'metadata': None,
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/cafcd79d-b5ba-4b65-bf7b-6a798fa3f0ec/f83165c5-e2ea-4d15-a5cf-33f3550bffde.homo_sapiens.mtx.zip?Expires=1612526350&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=E3HtJA9Egdzq0oiLBhuSeASVsg%2BSgsEtVI73Kh43Zqq%2FTyqKcs50s453DYrIsmo38SGK%2FfeBFgvdYU2TeQlt%2BCHTs5SDpOzxBNc26EUepXMPtHXOt9QAgW0BwVgxPrRl36GuXzLQGU7IRYCT9HcBPEO52HoVlWA4I9gAKac91NAuULQP3ZlCRwY3an6hK8oZ6ho4U6HKTK%2BW8lypAYI9dGVEOF0XpVBAwMkg3sAJqxf%2BjMtJ0IZKbH0gkxNvYiSnyEVzti%2BAuS%2FOgaRjrsWJb%2BogTxvMcwB1QQ6ZvBqDYSzM3o%2F%2BZHoc%2Ba%2BUjn1QCVErnzkbavotXc0RUMCoqT328Q%3D%3D&response-content-disposition=attachment%3B+filename%3Df83165c5-e2ea-4d15-a5cf-33f3550bffde.homo_sapiens.mtx.zip',
    },
    'Single Cell Transcriptomics of a Human Kidney Allograft Biopsy Defines a Diverse Inflammatory Response': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/8c5f287c-b19d-5a43-8257-5dfc37c0c6e4.tsv?response-content-disposition=attachment%3Bfilename%3D%22Kidney%20biopsy%20scRNA-seq%202021-02-02%2008.26.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHLLGW7BO4&Signature=q%2FBiMFFZSnlDH7FYSfq%2BIUwxeqA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDIaCXVzLWVhc3QtMSJIMEYCIQCySvlCq1L5o7vittt6TXTh1BizZ%2FxsVHQtma9B2TB0NwIhAIUPpKHxNX1MS4a3pzjXzio2GEoGP4SHQbH7GwYIOp3wKtABCCsQARoMNTQyNzU0NTg5MzI2Igxo%2FzZ6gDrD4DjNmC8qrQGyFL37ypsvzSjfsDz9uRwDwKRtypkEuByvV2JyvprMGV4Ngih%2FAhMNPqnC8p8eoqckLBSLFB18SyhkXjdOxEPKAO9iEc8MYoksIw7mTuctl10PDEeY%2FtgSceZoPCRWi8fRDOW0cnhFzSN%2BYbubxm1jnADOEgaPhUyGvC4xyGVi7a211iIrr%2FRXb7gXBNn%2BIpSUWYeVn3plHC1XvEKF8QH1vMEVIPrP8tgjBO3W%2FzDBofSABjrfAc1Sbt0FjOBktA2R1PpOBuUXVobZUzUPrBUh5I%2BNNPYiJz63GQo6%2F8yT1bVBdm51T%2BnjvAO5%2BrSj6xfDREqChaJ5cWAi7VjrH5o9Jj3xeWwnNV%2FdGjUl43N00%2BUb8kS4Q31PjgV84KEA4PDykuTMtJ%2F8Mjhky%2F%2F8OG%2FRYMXnkFMXYAdcRiy5L%2BkUOrNtmbWy6huHzuzML0SJnhi7nY4G8IGQDcqJYo2J7L74RTvoPUDXDaEuXrYD9K1C64iNpm4ZV%2BMxYfoYmTL%2B3FAQDOE9RGtqk6%2BHYIdbtYDEkkemuOU%3D&Expires=1612526586',
        'matrix': '',
    },
    'Single cell profiling of human induced dendritic cells generated by direct reprogramming of embryonic fibroblasts': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/9f181de1-f63b-55f0-b5ee-7bc6d070ac9e.tsv?response-content-disposition=attachment%3Bfilename%3D%22Reprogrammed_Dendritic_Cells%202021-02-05%2011.03.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHMEQN6D5T&Signature=gym86ydvPbf6umgpnhD%2BLNodOa0%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJHMEUCIAgdmZvrCCGfoG%2Fzsi%2FHH0HaAFwzMze39TCJR34X3jzUAiEA59sjF6UJ93ScstC1apEfKtmEmAB0sXkIQZ46OhX%2BkG0q2QEILBABGgw1NDI3NTQ1ODkzMjYiDL%2BBCBXyzvAUuxBOnyq2AVXA420D%2BWw6bhC5cbhi6tJuj3mxpbLVH%2FswV4grEAnpIrAKu%2B4LZ6k12JmgWKvLiqwjJ48dKHNBTaXBAhTWNQF6P5oSiCQ03L%2BaaS8SZseUnBteadqv%2F2ikQBe5QdwTKNJmoLBt5ixX7V78K7vVXR8HagKYfDCMs3wojcKaIsl6c%2F7KYbaM7eBYi0HIzbQblXLEfZRBDWz3Oxt8aw1gSosvyppsq2h%2FR2dzeYQ9tv%2FUsmnEV5OGMJ%2FJ9IAGOuABcdQkNF%2FStv7ELgiFhxooUG6go%2BusMr0qTghOKdPqRcXQ4lwHEBiekMKfhsx5l9UIG9GEU80wxpd3vvBeSC%2BauaskXMdg8zjOEEQDevw1uOOc9YPeviw1ShLYqqEoS5rfcWYN2DYpRHMroWBiBPn9EVm1t3UZABcqLdUD9MihSPzHGP09e3OI02A3avX6WwAxNNkeLrmJwvJeNRZvHCPgSPEVpS6Kv3qxzAAqdHijQASSaeuQ6GAKOQJYj6952Q2QRQqgoW7BMxb7lMMeOffpLvUGjsPqvaiZUoYNN8tMHUw%3D&Expires=1612526605',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/2d5721d7-2ad8-4f0d-ac2e-869259eaeb13/116965f3-f094-4769-9d28-ae675c1b569c.homo_sapiens.mtx.zip?Expires=1612526618&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=cLVFoalGCIi%2BRD0%2FO7cSLvMdGuZ0NNlKy9roKQiOcsNWWNi5%2Bcqu33vdmGFTn%2Fsiaxtu3Fr76UFLy%2Bo%2B6qQAhYNRWYhwESgsg%2FYV%2BHgfyLUCPp4%2FRrBG7XD1Cn60lStU8p6Bf4kFc9xBUu967e6ReIo7n%2BZzsorlUFtc6Awbvzg8MCiZx3VKiJmDEPX9IYugz9D%2Fe5AyPH5NQyaZx3m9csXGVcRfLOW%2FMTu5KQET4Gzcu6dP4x7Ohvmrl%2FWr1KvXMcGaEK8AYGaA0RFM6ftrB4AhuNM%2FnijLkUcEGiPTO3%2FxQ2eH052%2F9AgDxHBRqA6rXRVMmijfJtjBOdrWjP0Nzw%3D%3D&response-content-disposition=attachment%3B+filename%3D116965f3-f094-4769-9d28-ae675c1b569c.homo_sapiens.mtx.zip',
    },
    'Single cell transcriptome analysis of human pancreas reveals transcriptional signatures of aging and somatic mutation patterns.': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/44caa66f-5af5-5a32-8661-e0ba5ec07746.tsv?response-content-disposition=attachment%3Bfilename%3D%22Single%20cell%20transcriptome%20analysis%20of%20human%20pancreas%202021-02-05%2011.06.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHMEQN6D5T&Signature=L1H7RofnfMeGB0rVSsCCHGSbAek%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJHMEUCIAgdmZvrCCGfoG%2Fzsi%2FHH0HaAFwzMze39TCJR34X3jzUAiEA59sjF6UJ93ScstC1apEfKtmEmAB0sXkIQZ46OhX%2BkG0q2QEILBABGgw1NDI3NTQ1ODkzMjYiDL%2BBCBXyzvAUuxBOnyq2AVXA420D%2BWw6bhC5cbhi6tJuj3mxpbLVH%2FswV4grEAnpIrAKu%2B4LZ6k12JmgWKvLiqwjJ48dKHNBTaXBAhTWNQF6P5oSiCQ03L%2BaaS8SZseUnBteadqv%2F2ikQBe5QdwTKNJmoLBt5ixX7V78K7vVXR8HagKYfDCMs3wojcKaIsl6c%2F7KYbaM7eBYi0HIzbQblXLEfZRBDWz3Oxt8aw1gSosvyppsq2h%2FR2dzeYQ9tv%2FUsmnEV5OGMJ%2FJ9IAGOuABcdQkNF%2FStv7ELgiFhxooUG6go%2BusMr0qTghOKdPqRcXQ4lwHEBiekMKfhsx5l9UIG9GEU80wxpd3vvBeSC%2BauaskXMdg8zjOEEQDevw1uOOc9YPeviw1ShLYqqEoS5rfcWYN2DYpRHMroWBiBPn9EVm1t3UZABcqLdUD9MihSPzHGP09e3OI02A3avX6WwAxNNkeLrmJwvJeNRZvHCPgSPEVpS6Kv3qxzAAqdHijQASSaeuQ6GAKOQJYj6952Q2QRQqgoW7BMxb7lMMeOffpLvUGjsPqvaiZUoYNN8tMHUw%3D&Expires=1612526760',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/6ec2cc1e-0176-403c-99d9-23d09829f401/cddab57b-6868-4be4-806f-395ed9dd635a.homo_sapiens.mtx.zip?Expires=1612526830&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=VczedtuCYvenLhn%2BeItUnezL%2BpJ75TNHveAqHsUlA5NA9c0Nn7IpXO4ulHKOR0M4%2Bjbk6NgcS6QGYw8nM8BJeA8pnl85jyiRc3mzCAppA8kD46zM%2F6OQupftK83fvxX60BAy5VY%2F1x2LZAu4s%2Fnpfl1Fzc55VrLVZD41RokXakijSCc6U3l1tl8rqTEZeES4YWqOHYaJTT6welhutdOSH8dh3YBdiR15yrI1oXRpC74NxTYOlJAfuMRfI8pb%2FGs1BLMZzOdpFUakjLINraFLOoSyv8rJM3iofqTkuM%2BKyuVsfuHvskU9kUn7JWMgdEVjxqTnPbiPixXwXDZItpLlXg%3D%3D&response-content-disposition=attachment%3B+filename%3Dcddab57b-6868-4be4-806f-395ed9dd635a.homo_sapiens.mtx.zip',
    },
    'Single-cell RNA-seq analysis  throughout a 125-day differentiation protocol that converted H1 human embryonic stem cells to a variety of ventrally-derived cell types.': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/a8e878d5-c551-5c78-b934-6c819560a43f.tsv?response-content-disposition=attachment%3Bfilename%3D%22Single%20cell%20RNAseq%20characterization%20of%20cell%20types%20produced%20over%20time%20in%20an%20in%20vitro%20model%20of%20human%20inhibitory%20interneuron%20differentiation.%202021-02-05%2011.09.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHMEQN6D5T&Signature=dDNZhslsrFlad1UPu87pLoMrR7Q%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJHMEUCIAgdmZvrCCGfoG%2Fzsi%2FHH0HaAFwzMze39TCJR34X3jzUAiEA59sjF6UJ93ScstC1apEfKtmEmAB0sXkIQZ46OhX%2BkG0q2QEILBABGgw1NDI3NTQ1ODkzMjYiDL%2BBCBXyzvAUuxBOnyq2AVXA420D%2BWw6bhC5cbhi6tJuj3mxpbLVH%2FswV4grEAnpIrAKu%2B4LZ6k12JmgWKvLiqwjJ48dKHNBTaXBAhTWNQF6P5oSiCQ03L%2BaaS8SZseUnBteadqv%2F2ikQBe5QdwTKNJmoLBt5ixX7V78K7vVXR8HagKYfDCMs3wojcKaIsl6c%2F7KYbaM7eBYi0HIzbQblXLEfZRBDWz3Oxt8aw1gSosvyppsq2h%2FR2dzeYQ9tv%2FUsmnEV5OGMJ%2FJ9IAGOuABcdQkNF%2FStv7ELgiFhxooUG6go%2BusMr0qTghOKdPqRcXQ4lwHEBiekMKfhsx5l9UIG9GEU80wxpd3vvBeSC%2BauaskXMdg8zjOEEQDevw1uOOc9YPeviw1ShLYqqEoS5rfcWYN2DYpRHMroWBiBPn9EVm1t3UZABcqLdUD9MihSPzHGP09e3OI02A3avX6WwAxNNkeLrmJwvJeNRZvHCPgSPEVpS6Kv3qxzAAqdHijQASSaeuQ6GAKOQJYj6952Q2QRQqgoW7BMxb7lMMeOffpLvUGjsPqvaiZUoYNN8tMHUw%3D&Expires=1612526968',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/e90fc340-f59e-435b-8b9f-e148cd4144b9/2043c65a-1cf8-4828-a656-9e247d4e64f1.homo_sapiens.mtx.zip?Expires=1612530744&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=eu1F2i2YFUIH1MSdxV6Hw8jB0gnaRILcxPIjn%2BRCK5ctdJWbW5D%2BbTEljZShngsNMmobbBtK7pxt8S6ahf5iofUjqqwSbAy4qtYZAEJVMwQ4CPQfIpQaIDPDyoqKUnmjNbkMHWvw6RncF1dRt2DmrCxuna%2FrvP8VWb7oisK7okKZUGUK3eYJBEzZ2pdJ7HPLAM4zpNrjJwIa14HTUQx2YMUiKZ65ErU6aIl8F8OCwUM7Nq5ZoovKEsKW5iugMueCaVIK66FJBOFm5R%2FoZqD5QDQra8iC4dky7A%2FP%2BEjCunGiL8IIPmEFJF8lb5hn0Uu5%2FOaVRo5i4aXROMY0EQD%2Bxg%3D%3D&response-content-disposition=attachment%3B+filename%3D2043c65a-1cf8-4828-a656-9e247d4e64f1.homo_sapiens.mtx.zip',
    },
    'Single-cell RNA-seq analysis of human pancreas from healthy individuals and type 2 diabetes patients': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/ebf158d2-635a-51fc-906c-5c4019fc981e.tsv?response-content-disposition=attachment%3Bfilename%3D%22Healthy%20and%20type%202%20diabetes%20pancreas%202021-02-05%2012.13.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHMTVTIFXN&Signature=ZJlAKlvAnCzfwmYijWE8yzetxR8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDUaCXVzLWVhc3QtMSJGMEQCIArVxH%2FCf55ZjfRfglDZyRNvtl%2FQTixjHCuEqgdq6MQ6AiBvm%2FO9MVkpeI%2BQAqih6mf9um0LcJF8w3%2B%2Bxu6NPwTc1CrZAQgtEAEaDDU0Mjc1NDU4OTMyNiIMpiiYGwZMePUCOKWCKrYBnX7vAvfYB3vyvUmkkty7zNyWg6P5odJpeKCMelIoJLpfU3j%2BD%2F9%2Fly8LDJdBe8TIlE7HAqfxTpVXtriR8gqKKAdwQoZXVc5baFT0IOh0fi7WBCqqEu7S2nRtbuACaCsCcVbH%2BXZaA5SfOeASKmxgzKdtiiaUBZ%2Bw8XXeM94GIWydXd07qC5cde2WjEgwGAuIDvLzMX1MiO2by4E5wHYu9C5eRWT0Ja9ETJjT%2Ft9jmyiDh2CV1KYwyOz0gAY64QG1K2tuGyiXIEdY4D0Ik8Jcln2MSKv8ht8Zk4QzyjqSUzfGkm03gcUJzvJOIpiissH4le%2Bx4n5anLcCl%2F8rxtehqojHYPdVqI8c%2B3sgR3aSbAZUBgAbnyzbExdLVC%2B6SsSZfrhltxR0Rpit0y93DltRllq%2FANl0ADUCH3LFb9AbBUXsVgfTmyK%2BT88yw65htZ7xHvk5qX4ooAvZy6Ef5ACGD4dxqMIK5F6XRv5%2FIfyGb%2BIkSB6KTgBRwbK8qUjzjk%2Fs3Vxkk7qMc8ZXqkxIbLIxFWENYljUcXgxf5AyxwJyuKg%3D&Expires=1612530782',
        'matrix': None,
    },
    'Spatio-temporal immune zonation of the human kidney': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/1e2fb4c6-f8a8-59a9-ba21-14d872e04730.tsv?response-content-disposition=attachment%3Bfilename%3D%22KidneySingleCellAtlas%202021-02-05%2012.13.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHMTVTIFXN&Signature=DhTJvD7hvc6YPJi1wYnEINOcjS4%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDUaCXVzLWVhc3QtMSJGMEQCIArVxH%2FCf55ZjfRfglDZyRNvtl%2FQTixjHCuEqgdq6MQ6AiBvm%2FO9MVkpeI%2BQAqih6mf9um0LcJF8w3%2B%2Bxu6NPwTc1CrZAQgtEAEaDDU0Mjc1NDU4OTMyNiIMpiiYGwZMePUCOKWCKrYBnX7vAvfYB3vyvUmkkty7zNyWg6P5odJpeKCMelIoJLpfU3j%2BD%2F9%2Fly8LDJdBe8TIlE7HAqfxTpVXtriR8gqKKAdwQoZXVc5baFT0IOh0fi7WBCqqEu7S2nRtbuACaCsCcVbH%2BXZaA5SfOeASKmxgzKdtiiaUBZ%2Bw8XXeM94GIWydXd07qC5cde2WjEgwGAuIDvLzMX1MiO2by4E5wHYu9C5eRWT0Ja9ETJjT%2Ft9jmyiDh2CV1KYwyOz0gAY64QG1K2tuGyiXIEdY4D0Ik8Jcln2MSKv8ht8Zk4QzyjqSUzfGkm03gcUJzvJOIpiissH4le%2Bx4n5anLcCl%2F8rxtehqojHYPdVqI8c%2B3sgR3aSbAZUBgAbnyzbExdLVC%2B6SsSZfrhltxR0Rpit0y93DltRllq%2FANl0ADUCH3LFb9AbBUXsVgfTmyK%2BT88yw65htZ7xHvk5qX4ooAvZy6Ef5ACGD4dxqMIK5F6XRv5%2FIfyGb%2BIkSB6KTgBRwbK8qUjzjk%2Fs3Vxkk7qMc8ZXqkxIbLIxFWENYljUcXgxf5AyxwJyuKg%3D&Expires=1612530808',
        'matrix': 'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/499c18d0-86e7-466f-8e36-eb2914e169c5/abe1a013-af7a-45ed-8c26-f3793c24a1f4.homo_sapiens.mtx.zip?Expires=1612530827&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=pobfEc54JIkSf8QLBQWYAX1r5OMDEaQe2dgJhRlhYpzEr34R3JVfcDm%2BwJ3GT5gu%2BBDD1ocBcHDGOYdE4%2FXArDwZBcJem2yW%2F5pIzgAAOejV%2BiBsBGy%2B8fFpm9pwaEjni0VOpcUf5MBVEMgyqQeCjsCyyAda3S2%2FQtXgQ3RiY3aIoZQdP2tiJyedrE6qACHw0HAcriBxBgxldqGtkLrLTvOktk2qlMf3y6dOwZ5zYuU0wKjGBnE%2BhPS66m4iOjHlc43nFz4zJR7t%2Fg8cCvY6047nBprrNhAqJbaCIN37s%2FW9%2BGTRF4ZcbpPy3h8CZXwctVCezDMzVcmtvq6d6X6Flw%3D%3D&response-content-disposition=attachment%3B+filename%3Dabe1a013-af7a-45ed-8c26-f3793c24a1f4.homo_sapiens.mtx.zip',
    },
    'Structural Remodeling of the Human Colonic Mesenchyme in Inflammatory Bowel Disease': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/f569fcb3-39a3-51c0-a2f2-ccf8cdce3051.tsv?response-content-disposition=attachment%3Bfilename%3D%22HumanColonicMesenchymeIBD%202021-02-05%2012.14.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHMTVTIFXN&Signature=QW324GGArOub31FVuG7ojNL78cA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDUaCXVzLWVhc3QtMSJGMEQCIArVxH%2FCf55ZjfRfglDZyRNvtl%2FQTixjHCuEqgdq6MQ6AiBvm%2FO9MVkpeI%2BQAqih6mf9um0LcJF8w3%2B%2Bxu6NPwTc1CrZAQgtEAEaDDU0Mjc1NDU4OTMyNiIMpiiYGwZMePUCOKWCKrYBnX7vAvfYB3vyvUmkkty7zNyWg6P5odJpeKCMelIoJLpfU3j%2BD%2F9%2Fly8LDJdBe8TIlE7HAqfxTpVXtriR8gqKKAdwQoZXVc5baFT0IOh0fi7WBCqqEu7S2nRtbuACaCsCcVbH%2BXZaA5SfOeASKmxgzKdtiiaUBZ%2Bw8XXeM94GIWydXd07qC5cde2WjEgwGAuIDvLzMX1MiO2by4E5wHYu9C5eRWT0Ja9ETJjT%2Ft9jmyiDh2CV1KYwyOz0gAY64QG1K2tuGyiXIEdY4D0Ik8Jcln2MSKv8ht8Zk4QzyjqSUzfGkm03gcUJzvJOIpiissH4le%2Bx4n5anLcCl%2F8rxtehqojHYPdVqI8c%2B3sgR3aSbAZUBgAbnyzbExdLVC%2B6SsSZfrhltxR0Rpit0y93DltRllq%2FANl0ADUCH3LFb9AbBUXsVgfTmyK%2BT88yw65htZ7xHvk5qX4ooAvZy6Ef5ACGD4dxqMIK5F6XRv5%2FIfyGb%2BIkSB6KTgBRwbK8qUjzjk%2Fs3Vxkk7qMc8ZXqkxIbLIxFWENYljUcXgxf5AyxwJyuKg%3D&Expires=1612530857',
        'matrix': [
            'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/e75077a2-f5f2-44b9-946d-98a545ad1372/f8aa201c-4ff1-45a4-890e-840d63459ca2.homo_sapiens.mtx.zip?Expires=1612531149&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=xz2cFxiqUnR7tQp9bvkX3Z%2B1vI1kdmMbTdzONEi3U4XavKvqPYkW5SQ%2FonSI11rK182C%2FWr%2Bv6BNZDg78pjWdn1etNTBe%2B57bMZviD4NhRFd9viNgD7DcY48yi4O3kx4XAMcpotdE35htPq0OwWml0uJt6tZo%2BTYqGJd679QPx21Ab5PdgAJ5QyPCpo1NA69dmswG%2FCsiBfVRvhJQPHmKa3xQbPFW5WjH%2FM1kD1%2BupITXTXm8lWX5c55ncYH5i6ezZFphr6ZKRUbUrus3bzvEgSKj1%2FhaXi9aIb5%2BvC0Gr1iJ7Bid4arkNtnPaOtNCcDYkawjgndE1y0sqFykdSung%3D%3D&response-content-disposition=attachment%3B+filename%3Df8aa201c-4ff1-45a4-890e-840d63459ca2.homo_sapiens.mtx.zip',
            'https://storage.googleapis.com/broad-datarepo-terra-prod-hca2-bucket/cdcf6882-7705-420e-bbfe-21f35342a475/d578eae9-8707-4fc0-a32a-7efc73bdb6b9/f8aa201c-4ff1-45a4-890e-840d63459ca2.mus_musculus.mtx.zip?Expires=1612531186&GoogleAccessId=azul-ucsc-0-prod%40platform-hca-prod.iam.gserviceaccount.com&Signature=BUE1WlK4Ev4mrjWOx0r3%2FucXmgq2J%2BkyJlzxx4P4iO5VY1sx5nX7mAlunJnNtWDlkXO%2B5vLXQsrEkL5bsPGuqHPkFSBNDljSVMcdpAoe5py%2FIsAvzO2BcBFMs%2BBNwBS%2BxiFWjnyEYQejUfZd7FKYJuP0oHU9IF%2B1Qpv3PbqNRpO4cT0KOU2PVFzS1WvWYZiRON8XmSXjLE%2BRU77Jb7dK355BdNGqK%2F5gMS4dlXXmKdvd9tumkZjwa5Kh8LtPy5tYtIdVht8SN1rUuKljSTO3WqjJd4olt0saE0NY9KZkXECgXXYEa%2BpEYxNGPwuiyYU1zQt8VvDkaUMU5VhT7NtFkw%3D%3D&response-content-disposition=attachment%3B+filename%3Df8aa201c-4ff1-45a4-890e-840d63459ca2.mus_musculus.mtx.zip'
        ],
    },
    'Systematic comparative analysis of single cell RNA-sequencing methods': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/bf5cf77a-41ee-57eb-9bd0-73da2a6f3af5.tsv?response-content-disposition=attachment%3Bfilename%3D%22scRNAseqSystemicComparison%202021-02-05%2005.44.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHGMXMLRXS&Signature=nCJULFLGUZA3AER%2BbkBdY%2BUigjk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDQaCXVzLWVhc3QtMSJIMEYCIQCfWCQmRN3FaM4G39raDjO8KGDq%2BMR9EN9J%2BVUIhodnvwIhALf9vlpCgriYd2M7JsROrNWP1Ti2xLg1P%2BbARY%2FDyZF%2FKtABCC0QARoMNTQyNzU0NTg5MzI2IgxlEk3NmtFw956IXPMqrQEHZU%2B4Hh0utPa%2FlJDO6AQarx5J2vz5ZYruBc1VEhHE1QEcbAFALmWySBRxul6M3R89dpk3nMhFrVOywHEzUFJ009NBCJO06BKd39W2A1Vh4j2sm6oz0xt6yK4HIHhPPEQAPAUdQSpFXY0wDfdihsju2dEP5PlpzRVEQOadumMrcNm%2FrRMSczrGiK9tdCykXJ4A2xndZdeXwcl94DWORv41ZLtxEUGjw7A7ZVTs9zCb1%2FSABjrfAUHU1V%2FxErFYO7m8zuwCbf8JMWIJ50QMoFukhrPKVzrk0F8QyAUuwGa2OODLoIgQMT8eXES9T66fpbj9kx8ImP5cQs56LNUnbJGaqsxa1WjgRNFDD1oIupxw3cVf%2FM6JgJmd7WK1%2B2Sgo3WX7e0wDIttjWVSilAAVs9j2FP9t2HPeBqrc2rUUt49AhT16MpVRkK3j2lxo8tQIbPLuIOBeLDZOnUXqb%2FeOzZqg9HR7powEFMFZNLBpbk1kUyTi2EJEMOSdBkQKIMX%2Bb%2FPD5R6%2BfPHkpXQ9o6Q8Q2tN%2FKgubE%3D&Expires=1612531216',
        'matrix': None,
    },
    'Tabula Muris: Transcriptomic characterization of 20 organs and tissues from Mus musculus at single cell resolution': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/9ee8ed78-cdc7-5add-a5e5-d9674ae319c8.tsv?response-content-disposition=attachment%3Bfilename%3D%22Tabula%20Muris%202021-01-29%2017.43.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHJZV73SGI&Signature=hBSnWeryB8%2Fhr4O%2Ffkb%2F%2F3gSvDI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDQaCXVzLWVhc3QtMSJHMEUCIQDAbbR5mV99KVc3jrv4w%2Fak56TaJd8rMa3liTAXT3k6igIgDXpWXX3pniIoDO9yWc%2B6ItiGqPW9ak9x9ty5YH9I8DAq0AEILRABGgw1NDI3NTQ1ODkzMjYiDPZ1frifj%2FSQii1h%2BSqtATYMfQY35bAiGOlCI6r1B43hGsF76yD6Kph6A7WKcqM7unk0BK%2F7qPibJM5zwIP9tHRYUmDvCZo1uxK0IMoAFTbgy6Iv%2BuPcOIQbYgUlqhaYUcFOJ4xSGwrgBVXhQt3gkubW1K8Is%2FrK5DnPE0rEQbdLy2Sfg9OpJTtuklaVRhZYzndH50j5MHgr6zXrT8SR0%2B3QiCytlFRp5woBoVECNiG%2FHo39e3P9msfeJ0HiMInZ9IAGOuABCK90XrREIFCrpkTEpRSvh4JnRTFo86fYOnn8SuD2zfTXePB2wUarEVTcFP9VOeWjbwEFeM7B90r%2F%2FakZ4ed8hjVQjy4hHRXLTbckfkA5MIg8qevJKt1ogQmQJNveio%2Bb%2FMJyxoEmcbkZHXLC8pegdhuaXMRuAiQEKnK2nSvWfnpz0Sj8H0bfwIfhjdWmhZCgBd7MtLr1toFXjCcLU2bIA7y8wZAJnnncLVL06Ddys5S1%2FnJ4XlsVHRpI9qCT5P5XT%2FPWtb7rwYt6oFQ0bkfOuCp%2F%2BEGHJXK2xmqz13Z89lU%3D&Expires=1612531254',
        'matrix': None,
    },
    'The Single Cell Transcriptomic Landscape of Early Human Diabetic Nephropathy': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/7ba77bc7-c9b5-5e03-8bb5-9580a21591a2.tsv?response-content-disposition=attachment%3Bfilename%3D%22Diabetic%20Nephropathy%20snRNA-seq%202021-02-02%2017.22.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHHDDP65YO&Signature=AUdbRYUCN8enPkicXs%2BnqxRB2QY%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJHMEUCIQDkll4gTPtl5jOoB0aU4oSBOml99xG3pqYm0wwRjLFZPAIgS7HFVvhh%2FnryFZUIHUyrRg%2BlEHHuQ3FhLKrgchzmm7wq0AEILBABGgw1NDI3NTQ1ODkzMjYiDMEBqMLC1KPS7JScCSqtAa6eJtq6BfNDKfDTVvPUwYV0CyoffLV%2BcVb%2FJkTpvMIPA6tuYkN%2BkXGD6dNLPOoJAj0KAhxr6dxKJX5bRFzVBVeQgnj4gekiVPcunoq7KlZq85b%2FKcjmVvUCOHvupoYh5kwjaFXf6x1Tt31vg64DWillXORxTfaPFc1QusyCV%2FUWEU7x%2F%2FDEiTnO0aG%2BIpB2tRzuNHdZ9SPHgGsytt3dwgNSKJQ4DUlJPOdjXxlsMIfH9IAGOuABtDKesBTYrSTuZJplqnNsBfp%2FdNAQO4m%2BbvqOTrqqky1v6QMWY0eW8E706442%2FQu8wzhnp25BG97U4m%2BtwGBxBTP9lV1gc5%2Fbj8Jy3EDEI4FvtEAJT0w5SkO5sIX8bvuauHV8wF0ySm52wG3pzWzoGQnpSajwqKS0bRWuSteTJzJsKJ8uLs8IxoZDuAKy%2BtYWIR%2BwQIs%2F25%2Bqc92v%2Flmcvht0pARPqGWOqj6UFPqHUrgojAWg8o%2Bf8y2IriAtcoz6V%2FsyWsvzFv9IE9elZn6v12gRqErOsHcFHDwPe4OfmkQ%3D&Expires=1612531281',
        'matrix': None,
    },
    'The emergent landscape of the mouse gut endoderm at single-cell resolution': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/e8b66c9e-c7b8-5e93-85d2-0344b114cc10.tsv?response-content-disposition=attachment%3Bfilename%3D%22Mouse%20Endoderm%20Project%202021-02-05%2012.21.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHHCCL7CWR&Signature=UJ5okukTNOqdIX2XC1JmP7Lc8Tk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDUaCXVzLWVhc3QtMSJHMEUCIQCdwMoY76UKdMs4fj5YQ5KofuSt9tsH2BIwZgQabeCJqwIgaWSHoSwgjaMf1R8ZqlV5gS16%2Bzyfiq8CYtIx147H7Ugq2QEILRABGgw1NDI3NTQ1ODkzMjYiDPnQLZX83MIiHmc0TCq2AcCbC%2BpGKeJ9hxsWjirKZF5cNyOQW52HrvwfA1gBEPTergLPStMgKG6BWGvJ8JLE1HhpaKyOQpNKsOeTMSzgivyjFRRY1%2FI%2BiqfXlLtMSCsG%2BDUo5s9AfuUIDiXvL0qj4etyx5OYnWGA6MKGDn2WFgk8s0MncnLPyWZxfZ%2FyuiuiY1TFnk6FHNQJBM%2FLDZE%2BWyW07tPi%2Fjc26ROiJu15RmoJmiyUGXyVZtOsbTnwB7I691pOClNSMNTw9IAGOuABC2x1YCpP7plqGrX3gxLgpoWFfw1M0hYuuuXnHkngY0pTR5jj1Wn9Sxb2SsaOafTr0wWnEreFwkjx5rpncfYZUvwV%2FKURvffcjBaqbCVEw%2B%2BWUvDs7mDr03IsncTGPo1M1OmhbstGEGZzWfDKQImA9n4vXSIX4aLq91%2FgpE2yZEpcqhhrvC4vg5UsqQ4wtTdeesssjmCnAdo3%2FDGrY8ukmvWyZtcAF1tkQpkAKCDslhYNzeHhiXcklwxl%2Fdsdqd7Ae62qiZ1SGD%2FQHhE0pxAYcuktuD820KwP%2Bg0aYe6zzNY%3D&Expires=1612531303',
        'matrix': None,
    },
    'Transcriptomic classification of human retinal cell types with single-nuclei RNA-seq.': {
        'metadata': 'https://edu-ucsc-gi-azul-dcp2-prod-storage-prod.s3.amazonaws.com/manifests/4a87d790-0958-516a-bdbd-be7a36610fd0.tsv?response-content-disposition=attachment%3Bfilename%3D%22snRNA-seq_for_human_retina%202021-02-05%2012.22.tsv%22&AWSAccessKeyId=ASIAX4XVRZKHHCCL7CWR&Signature=WDVivVMsObz6iJFHNCuPzLdKL4w%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDUaCXVzLWVhc3QtMSJHMEUCIQCdwMoY76UKdMs4fj5YQ5KofuSt9tsH2BIwZgQabeCJqwIgaWSHoSwgjaMf1R8ZqlV5gS16%2Bzyfiq8CYtIx147H7Ugq2QEILRABGgw1NDI3NTQ1ODkzMjYiDPnQLZX83MIiHmc0TCq2AcCbC%2BpGKeJ9hxsWjirKZF5cNyOQW52HrvwfA1gBEPTergLPStMgKG6BWGvJ8JLE1HhpaKyOQpNKsOeTMSzgivyjFRRY1%2FI%2BiqfXlLtMSCsG%2BDUo5s9AfuUIDiXvL0qj4etyx5OYnWGA6MKGDn2WFgk8s0MncnLPyWZxfZ%2FyuiuiY1TFnk6FHNQJBM%2FLDZE%2BWyW07tPi%2Fjc26ROiJu15RmoJmiyUGXyVZtOsbTnwB7I691pOClNSMNTw9IAGOuABC2x1YCpP7plqGrX3gxLgpoWFfw1M0hYuuuXnHkngY0pTR5jj1Wn9Sxb2SsaOafTr0wWnEreFwkjx5rpncfYZUvwV%2FKURvffcjBaqbCVEw%2B%2BWUvDs7mDr03IsncTGPo1M1OmhbstGEGZzWfDKQImA9n4vXSIX4aLq91%2FgpE2yZEpcqhhrvC4vg5UsqQ4wtTdeesssjmCnAdo3%2FDGrY8ukmvWyZtcAF1tkQpkAKCDslhYNzeHhiXcklwxl%2Fdsdqd7Ae62qiZ1SGD%2FQHhE0pxAYcuktuD820KwP%2Bg0aYe6zzNY%3D&Expires=1612531320',
        'matrix': None,
    },

}


class OntologyConversorHCA(OntologyConversorAbstract):

    ####################################################
    # region Define super class abstract methods

    def init_map(self):
        mapping_dict = {
            'Melanoma(Disease)': 'Melanoma',
            'Cataract(Disease)': 'Cataract',
            'UlcerativeColitis(Disease)': 'UlcerativeColitis',
            'Colitis(Disease)': 'UlcerativeColitis',
            'BenignProstaticHyperplasia(Disease)': 'BenignProstaticHyperplasia',
            'PericardialEffusion(Disease)': 'PericardialEffusion',
            'HiatusHernia(Disease)': 'HiatusHernia',
            'Hyperlipidemia(Disease)': 'Hyperlipidemia',
            'Non-AlcoholicFattyLiverDisease': 'NonAlcoholicFattyLiverDisease',
            'Hemolytic-UremicSyndrome': 'HemolyticUremicSyndrome',
            'Osteoarthritis,Hip': 'OsteoarthritisHip',
            'CAFs': 'Cancer-associatedFibroblasts(CAFs)',
            'IlluminaHiseq2500': 'IlluminaHiSeq2500',
            'Smart-Seq2': 'Smart-seq2',
            'Smart-Seq': 'Smart-seq',
            'Sci-RNA-Seq': 'Sci-RNA-seq',
            'MARS-Seq': 'MARS-seq',
            'CEL-Seq2': 'CEL-seq2',
            'CITE-Seq': 'CITE-seq',
            'DroNc-Seq': 'DroNc-seq',
            'Drop-Seq': 'Drop-seq',
            'Seq-Well': 'Seq-well',
            'CD8-Positive,Alpha-BetaTCell': 'CD8+AlphaBetaTcell',
            'CD11B+CD11C+DC': 'CD11b+CD11c+DC',
            'CD11C+DC': 'CD11c+DC',
            'CD11B+Macrophages/Monocytes': 'CD11b+Macrophages/Monocytes',
            'CD34-Positive,CD38-NegativeHematopoieticStemCell': 'CD34+CD38-HematopoieticStemCell',
            'EffectorMemoryCD8-Positive,Alpha-BetaTCell,TerminallyDifferentiated': 'EffectorMemoryCD8+AlphaBetaTCellTerminallyDifferentiated',
            '10XV2Sequencing': '10Xv2Sequencing',
            '10XV3Sequencing': '10xv3Sequencing',
            "10X3'V1Sequencing": "10X3v1Sequencing",
            "10X3'V2Sequencing": "10X3v2Sequencing",
            "10X3'V3Sequencing": "10x3v3Sequencing",
            "10X5'V2Sequencing": "10X5v2Sequencing",
            'CDNALibraryConstruction': 'cDNALibraryConstruction',
            'BladderOrgan': 'Bladder',
            'MuscleOrgan': 'Muscle',
            'SkinOfBody': 'Skin',
            'SkinEpidermis': 'Epidermis',
            'Cryopreservation,Other': 'CryopreservationOther',
            'CryopreservationInLiquidNitrogen(DeadTissue)': 'CryopreservationInLiquidNitrogenDeadTissue',
            'Optimus_V1.3.1': 'Optimus_v1.3.1',
            'Optimus_V1.3.2': 'Optimus_v1.3.2',
            'Optimus_V1.3.3': 'Optimus_v1.3.3',
            'Optimus_V1.3.5': 'Optimus_v1.3.5',
            'Smartseq2_V2.3.0': 'Smartseq2_v2.3.0',
            'Smartseq2_V2.4.0': 'Smartseq2_v2.4.0',
            'StemCell-Derived': 'StemCellDerived',
            'Metadata': 'ExperimentDesign',
            'Normal': 'Control',
            'ObstructiveSleepApneaSyndrome': 'ObstructiveSleepApnea',
            'CD4+TCell': 'Tcell',
            'TCell': 'Tcell',
            'BCell': 'Bcell',
            'PresumptiveGut': 'presumptiveGut'
        }

        return mapping_dict

    def format_concrete_specimen(self, raw_specimen, specimen_id):
        specimen = Specimen(specimen_id)

        specimen.part_of_collection = "HumanCellAtlas"
        specimen.part_of_repository = "HumanCellAtlas"

        # Cell Lines
        specimen = self.__format_HCD_cell_lines(specimen, raw_specimen)

        # Cell Suspensions
        specimen = self.__format_HCD_cell_suspensions(specimen, raw_specimen)

        # Donor Organism
        specimen = self.__format_HCD_donor_organism(specimen, raw_specimen)

        # Projects
        specimen = self.__format_HCD_projects(specimen, raw_specimen)

        # File Type Summaries
        specimen = self.__format_HCD_file_type_summaries(specimen, raw_specimen)

        # Organoids
        specimen = self.__format_HCD_organoids(specimen, raw_specimen)

        # Protocols
        specimen = self.__format_HCD_protocols(specimen, raw_specimen)

        # Samples
        specimen = self.__format_HCD_samples(specimen, raw_specimen)

        # Specimens
        specimen = self.__format_HCD_specimens_SR(specimen, raw_specimen)

        self.specimen = specimen

    def format_concrete_project(self, raw_project, project_id):

        project = Project(project_id)

        project.part_of_collection = "HumanCellAtlas"
        project.part_of_repository = "HumanCellAtlas"
        project.project_id = raw_project["entryId"]

        project.repository_link = "https://data.humancellatlas.org/explore/projects/" + project.project_id

        # Cell Lines
        project = self.__format_HCD_cell_lines(project, raw_project)

        # Protocols
        project = self.__format_HCD_protocols(project, raw_project)

        # Projects
        project = self.__format_HCD_projects_PR(project, raw_project)

        # Samples
        project = self.__format_HCD_samples(project, raw_project)

        # Specimens
        project = self.__format_HCD_specimens_PR(project, raw_project)

        # Donor Organism
        project = self.__format_HCD_donor_organism_PR(project, raw_project)

        # Organoids
        project = self.__format_HCD_organoids(project, raw_project)

        # Cell Suspensions
        project = self.__format_HCD_cell_suspensions(project, raw_project)

        # File Type Summaries
        project = self.__format_HCD_file_type_summaries_PR(project, raw_project)

        project.matrix_link = download_links[project.project_title]['matrix']

        self.project = project

    def parse_concrete(self, word):
        aux = list(word.title())

        for i in range(len(word)):
            if word[i].isupper():
                aux[i] = word[i]

        aux = ''.join(aux).replace(' ', '')

        return aux

    # endregion
    ####################################################

    ####################################################
    # region individual function auxiliar parts

    def __format_HCD_cell_lines(self, individual, individual_hca):
        if not individual_hca['cellLines']:
            return individual

        cell_line_type = individual_hca['cellLines'][0]['cellLineType']
        model_organ = individual_hca['cellLines'][0]['modelOrgan']

        individual.cell_line_type = self.parse_word(cell_line_type)
        individual.model_organ = self.parse_word(model_organ)

        return individual

    def __format_HCD_cell_suspensions(self, individual, individual_hca):
        if not individual_hca['cellSuspensions']:
            return individual

        selected_cell_type = []
        total_cells = 0

        for cellSuspension in individual_hca['cellSuspensions']:
            selected_cell_type += cellSuspension['selectedCellType']
            total_cells += cellSuspension['totalCells']

        if total_cells == 0:
            total_cells = -1

        individual.cell_type = self.parse_word(selected_cell_type)
        individual.total_cell_counts = total_cells

        return individual

    def __format_HCD_donor_organism(self, individual, individual_hca):
        if not individual_hca['donorOrganisms']:
            return individual

        biological_sex = individual_hca['donorOrganisms'][0]['biologicalSex']
        disease = individual_hca['donorOrganisms'][0]['disease']
        genus_species = individual_hca['donorOrganisms'][0]['genusSpecies']
        organism_age = individual_hca['donorOrganisms'][0]['organismAge'][0]
        organism_age_unit = individual_hca['donorOrganisms'][0]['organismAgeUnit']

        individual.biological_sex = biological_sex
        individual.disease = self.parse_word(disease)
        individual.specie = self.parse_word(genus_species)

        if organism_age is not None and '-' in organism_age:
            individual.min_age = int(organism_age.split('-')[0])
            individual.max_age = int(organism_age.split('-')[1])
        else:
            individual.min_age = int(float(organism_age)) if organism_age is not None else -1
            individual.max_age = int(float(organism_age)) if organism_age is not None else -1

        individual.age_unit = organism_age_unit

        return individual

    def __format_HCD_projects(self, individual, individual_hca):
        if not individual_hca['projects']:
            return individual

        laboratory = individual_hca['projects'][0]['laboratory']
        project_shortname = individual_hca['projects'][0]['projectShortname']
        project_title = individual_hca['projects'][0]['projectTitle']

        individual.laboratory = laboratory
        individual.project_short_name = project_shortname
        individual.project_title = project_title

        return individual

    def __format_HCD_organoids(self, individual, individual_hca):
        if not individual_hca['organoids']:
            return individual

        model_organ = individual_hca['organoids'][0]['modelOrgan']

        individual.model_organ = self.parse_word(model_organ)

        return individual

    def __format_HCD_protocols(self, individual, individual_hca):
        if not individual_hca['protocols']:
            return individual

        instrument_manufacturer_model = individual_hca['protocols'][0]['instrumentManufacturerModel']
        library_construction_approach = individual_hca['protocols'][0]['libraryConstructionApproach']
        paired_end = individual_hca['protocols'][0]['pairedEnd']
        workflow = individual_hca['protocols'][0]['workflow']

        individual.instrument = self.parse_word(instrument_manufacturer_model)
        individual.library = self.parse_word(library_construction_approach)
        individual.paired_end = paired_end
        individual.analysis_protocol = self.parse_word(workflow)

        return individual

    def __format_HCD_samples(self, individual, individual_hca):
        if not individual_hca['samples']:
            return individual

        sample_entity_type = individual_hca['samples'][0]['sampleEntityType']

        individual.sample_type = self.parse_word(sample_entity_type)

        try:
            preservation_method = individual_hca['samples'][0]['preservationMethod']

            individual.preservation = self.parse_word(preservation_method)

            return individual
        except:
            return individual

    def __format_HCD_file_type_summaries(self, individual, individual_hca):
        if not individual_hca['fileTypeSummaries']:
            return individual

        # It is possible that one individual has multiple files
        # count = []
        total_size = []

        for i in range(len(individual_hca['fileTypeSummaries'])):
            ind_type = individual_hca['fileTypeSummaries'][i]['fileType']

            # count.append(individual_hca['fileTypeSummaries'][i]['count'])
            total_size.append(individual_hca['fileTypeSummaries'][i]['totalSize'])

        individual.total_size_of_files = sum(total_size) / pow(2, 20)  # We save it in MB

        return individual

    # endregion
    ####################################################

    ####################################################
    # region specimen function auxiliar parts

    def __format_HCD_specimens_SR(self, specimen, specimen_hca):
        if not specimen_hca['specimens']:
            return specimen

        specimen = self.__format_HCD_specimens_PR(specimen, specimen_hca)

        sample_id = specimen_hca['specimens'][0]['id'][0]

        specimen.specimen_ID = sample_id

        return specimen

    # endregion
    ####################################################

    ####################################################
    # region project function auxiliar parts

    def __format_HCD_donor_organism_PR(self, project, project_hca):
        if not project_hca['donorOrganisms']:
            return project

        project = self.__format_HCD_donor_organism(project, project_hca)

        donor_count = project_hca['donorOrganisms'][0]['donorCount']

        project.donor_count = donor_count

        return project

    def __format_HCD_projects_PR(self, project, project_hca):
        if not project_hca['projects']:
            return project

        project_title = project_hca['projects'][0]['projectTitle']
        project_shortname = project_hca['projects'][0]['projectShortname']
        laboratory = project_hca['projects'][0]['laboratory']
        project_description = project_hca['projects'][0]['projectDescription']

        institutions = set()
        for contributor in project_hca['projects'][0]['contributors']:
            institutions.add(contributor["institution"])

        publication_titles = []
        publication_links = []
        for publication in project_hca['projects'][0]['publications']:
            publication_titles.append(publication['publicationTitle'])
            publication_links.append(publication['publicationUrl'])

        array_express = project_hca['projects'][0]['arrayExpressAccessions']
        geo_series = project_hca['projects'][0]['geoSeriesAccessions']
        insdc_project = project_hca['projects'][0]['insdcProjectAccessions']
        insdc_study = project_hca['projects'][0]['insdcStudyAccessions']
        supplementary_links = project_hca['projects'][0]['supplementaryLinks']

        project.project_title = project_title
        project.project_short_name = project_shortname
        project.laboratory = laboratory
        project.project_description = project_description
        project.institutions = list(institutions)
        project.publication_title = publication_titles
        project.publication_link = publication_links

        project.array_express_id = array_express
        project.geo_series_id = geo_series
        project.insdc_project_id = insdc_project
        project.insdc_study_id = insdc_study
        project.sumpplementary_link = supplementary_links

        return project

    def __format_HCD_file_type_summaries_PR(self, individual, individual_hca):
        if not individual_hca['fileTypeSummaries']:
            return individual

        # It is possible that one individual has multiple files
        file_type = ['metadata']
        count = []
        total_size = []

        for i in range(len(individual_hca['fileTypeSummaries'])):
            ind_type = individual_hca['fileTypeSummaries'][i]['fileType']

            if ind_type == 'matrix' and individual.project_title != "Systematic comparative " \
                                                                    "analysis of single cell " \
                                                                    "RNA-sequencing methods":
                file_type.append(ind_type)
            elif ind_type == 'results':
                file_type.append(ind_type)

            count.append(individual_hca['fileTypeSummaries'][i]['count'])
            total_size.append(individual_hca['fileTypeSummaries'][i]['totalSize'])

        individual.downloads_type = self.parse_word(file_type)
        individual.total_size_of_files = sum(total_size) / pow(2, 20)  # We save it in MB

        return individual

    def __format_HCD_specimens_PR(self, project, project_hca):
        if not project_hca['specimens']:
            return project

        organ = project_hca['specimens'][0]['organ']
        organ_part = project_hca['specimens'][0]['organPart']
        num_specimens = len(project_hca['specimens'][0]['id'])
        preservation_method = project_hca['specimens'][0]['preservationMethod']

        project.organism_part = self.parse_word(organ)
        project.biopsy_site = self.parse_word(organ_part)
        project.specimen_count = num_specimens
        project.preservation = self.parse_word(preservation_method)

        return project

    # endregion
    ####################################################
