"""
ETL-Query script
"""

# from mylib.extract import extract
# from mylib.transform_load import load
# from mylib.query import query_create, query_read, query_update, query_delete

# # Extract
# extract()

# # transform & load
# load()

# # Query
# query_create()
# query_read()
# query_update()
# query_delete()


# def main_results():
#     results = {
#         "extract_to": extract(),
#         "transform_db": load(),
#         "create": query_create(),
#         "read": query_read(),
#         "update": query_update(),
#         "delete": query_delete(),
#     }
#     return results


from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import queryCreate, queryRead, queryUpdate, queryDelete

# Extract
extract()

# Transform and Load
load()

# Query
queryCreate()
queryRead()
queryUpdate()
queryDelete()


def main_result():
    results = {
        "extract_to": extract(),
        "transform_db": load(),
        "create": queryCreate(),
        "read": queryRead(),
        "update": queryUpdate(),
        "delete": queryDelete(),
    }

    return results


if __name__ == "__main__":
    main_result()
