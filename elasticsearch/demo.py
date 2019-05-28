from elasticsearch import Elasticsearch

# es库的封装
class ElasticObj:
    # 初始化
    def __init__(self,index_name,ip="127.0.0.1"):
        self.index_name = index_name
        # self.index_type = index_type
        self.es = Elasticsearch([ip])

    #按照传入的条件搜索
    def getData(self,query):
        searched_data = self.es.search(index=self.index_name,body=query)
        return searched_data

# main函数
if __name__ == '__main__':
    query_list = {
        "query": {
            "bool": {
                "should": [],
                "filter": [{"range": {"xxx": {"from": xxx, "to": xxx}}}]
            }
        },
    }
    searchData = esobj.getData(query_list)