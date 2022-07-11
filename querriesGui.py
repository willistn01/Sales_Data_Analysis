from pyspark.sql import SparkSession
import pandas as pd
from spark_functions import SparkQuerrying


spark = SparkSession.builder.getOrCreate()
data = pd.read_csv("csvGenerator/data.csv")
spark_df = spark.createDataFrame(data)

def topSellingProductCountry(countryName):
    data = spark_df.select(['productName', 'orderID']).where(spark_df.country == countryName).groupBy('productName').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def topSellingProductCity(cityName):
    data = spark_df.select(['productName', 'orderID']).where(spark_df.city == cityName).groupBy('productName').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def totalSalesPerCity():
    data = spark_df.select(['city', 'orderID']).groupBy('city').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def totalSalesPerCountry():
    data = spark_df.select(['country', 'orderID']).groupBy('country').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def totalTopSelling():
    data = spark_df.select(['productCategory', 'orderID']).groupBy('productCategory').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def topSellingCategoryCountry(countryName):
    data = spark_df.select(['productCategory', 'orderID']).where(spark_df.country == countryName).groupBy('productCategory').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def topSellingCategoryCity(cityName):
    data = spark_df.select(['productCategory', 'orderID']).where(spark_df.city == cityName).groupBy('productCategory').agg({'orderID': 'count'}).sort('count(orderID)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList
    
def productPopYear(prodName):
    data = spark_df.select(['productName', 'datetime', 'quantity']).where(spark_df.productName == prodName).groupBy(spark_df.datetime.substr(1,2)).agg({'quantity': 'sum'}).sort('substring(datetime, 1, 2)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def productPopYearCountry(prodName, countryName):
    data = spark_df.select(['productName', 'datetime', 'country', 'quantity']).where((spark_df.productName == prodName) & (spark_df.country == countryName)).groupBy(spark_df.datetime.substr(1,2)).agg({'quantity': 'sum'}).sort('substring(datetime, 1, 2)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def productPopYearCity(prodName, cityName):
    data = spark_df.select(['productName', 'datetime', 'city', 'quantity']).where((spark_df.productName == prodName) & (spark_df.city == cityName) & (spark_df.quantity < 20000)).groupBy(spark_df.datetime.substr(1,2)).agg({'quantity': 'sum'}).sort('substring(datetime, 1, 2)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def totalSalesTime():
    data = spark_df.select(['orderID', 'datetime']).groupBy(spark_df.datetime.substr(12,2)).agg({'orderID': 'count'}).sort('substring(datetime, 12, 2)').collect()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def productSalesTime(product):
    data = spark_df.select(['productName', 'orderID', 'datetime']).where(spark_df.productName == product).groupBy(spark_df.datetime.substr(12,2)).agg({'orderID': 'count'}).sort('substring(datetime, 12, 2)').collect()
    spark_df.select(['productName', 'datetime']).where(spark_df.productName == product).groupBy(spark_df.datetime.substr(12,2)).agg({'productName': 'count'}).sort('substring(datetime, 12, 2)').show()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def productSalesTimeCountry(product, country):
    data = spark_df.select(['productName', 'datetime']).where((spark_df.productName == product) & (spark_df.country == country)).groupBy(spark_df.datetime.substr(12,2)).agg({'productName': 'count'}).sort('substring(datetime, 12, 2)').collect()
    spark_df.select(['productName', 'datetime']).where((spark_df.productName == product) & (spark_df.country == country)).groupBy(spark_df.datetime.substr(12,2)).agg({'productName': 'count'}).sort('substring(datetime, 12, 2)').show()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList

def productSalesTimeCity(product, city):
    data = spark_df.select(['productName', 'orderID', 'datetime']).where((spark_df.productName == product) & (spark_df.city == city)).groupBy(spark_df.datetime.substr(12,2)).agg({'orderID': 'count'}).sort('substring(datetime, 12, 2)').collect()
    spark_df.select(['productName', 'datetime']).where((spark_df.productName == product) & (spark_df.city == city)).groupBy(spark_df.datetime.substr(12,2)).agg({'productName': 'count'}).sort('substring(datetime, 12, 2)').show()
    idList = [i[0] for i in data]
    dataList = [i[1] for i in data]

    return idList, dataList


