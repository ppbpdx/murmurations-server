# Simple GraphQL Profile Server
This example is a simple Flask Python implementation of a server that updates from the Murmurations directory and
serves up the results using a GraphQL API. 

#### What it does
The server consists of a simple api and cache of profile data (murmurations). The cache is loaded by making a request to
murmurations index server, taking the profiles that are available and caching them in a local database. The cached 
profiles are then exposed through a GraphQl query API. 

The GraphQL API gives developers a lot of flexibility over
what data they want, how to shape the data when it is returned and many other cool things.

More information about the query and mutation mechanisms take a look at https://graphql.org/learn/

The data is cached in a SqlLite database for simplicity, however, this can be swapped out for another RDBMS in the 
configuration. See Flask documentation for details.

Note this implementation is intended as an example. To run it in a production configuration it will be necessary to 
change the configurations to turn off debugging etc.


## Project Setup
To run the server locally the easiest thing to do is to run it in Docker.

**Ensure that `docker v2.x` and above is installed**

Then run the following commands to build the image and run the container:

```
$ cd /examples/python
$ docker build -t flask-murmuration .
$ docker run -d  -p 5000:5000 flask-murmuration
```

When the container is running you can navigate to http://localhost:5000/graphql and interact with the query browser.
To load the data from the murmurations idex server you will need to run the update cache mutation. The query looks like 
this:

```
mutation{
  updateCache {
    ok
    message
  }
}
```

When that query has successfully executed the local cache will be populated. You can start to build queries using the 
query objects. See GraphQL documentation for details. 

A basic query looks like this (use the control + spacebar to get
additional field suggestions):

```
query{
  murmuration {
    id
    name
    url
    tagline
    updated
    mission
    location
  }
}
```

#### Todo
There are a lot of ways this could be enhanced...
* Update cache automation based on time config
* Data mapping rules and configuration
* CRUD functions for profiles
* Other good ideas...
