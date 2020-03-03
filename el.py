import geopy.distance
from elasticsearch import Elasticsearch 

es=Elasticsearch([{'host':'localhost','port':9200}])
e1={
    "wp":1,
    "lat":1.22345566,
    "lon":1.56899944,

}
e1={
    "wp":1,
    "lat":1.22345566,
    "lon":1.56899944,
}
e2={
    "wp":2,
    "lat":1.22643566,
    "lon":1.89994774,
}
e3={
    "wp":3,
    "lat":1.5645566,
    "lon":1.2389994,
}
e4={
    "wp":4,
    "lat":1.55234556,
    "lon":1.86889944,
}
e5={
    "wp":5,
    "lat":52.2296756,
    "lon":21.0122287,
}
e6={
    "wp":6,
    "lat":52.406374,
    "lon":16.9251681,
}
#es=es.index(index='agu',doc_type='waypoints',body=e3)
#res=es.index(index='agu',doc_type='waypoints',body=e5)
#res=es.index(index='agu',doc_type='waypoints',body=e6)
res = es.search(index = 'agu',body={"_source":["lat","lon"],"query":{"match":{"wp":5}}} ,size=100)
res1 = es.search(index = 'agu',body={"_source":["lat","lon"],"query":{"match":{"wp":6}}} ,size=100)
print("Location 1")
for hit in res['hits']['hits']:
    print("lat1: %(lat)s" % hit["_source"])
    print("lon1: %(lon)s" % hit["_source"])
    lat1 ="%(lat)s" % hit["_source"]
    lon1 ="%(lon)s" % hit["_source"]
print("Location 2")    
for hit in res1['hits']['hits']:
    print("lat2: %(lat)s" % hit["_source"])
    print("lon2: %(lon)s" % hit["_source"])    
    lat2 ="%(lat)s" % hit["_source"]
    lon2 ="%(lon)s" % hit["_source"]
coords_1 = (lat1, lon1) 
coords_2 = (lat2, lon2)    
print("Distance in kms:")
print (geopy.distance.distance(coords_1, coords_2).km)
print("Distance in miles:")
print (geopy.distance.distance(coords_1, coords_2).miles)    
