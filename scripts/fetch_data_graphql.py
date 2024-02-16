from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


_transport = RequestsHTTPTransport(
    url='http://209.38.172.107/graphql/',
    use_json=True,
    headers={'Accept': 'application/json'}
)

client = Client(
    transport = _transport,
    fetch_schema_from_transport=True,
)

query = gql('''
query MyQuery {
  playerPerGame(name: "James Harden") {
    playerName
    season
    team
    position
    points
    playerId
  }
}
''')



response = client.execute(query)


print(response)