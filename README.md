# Shopify installer
This simple webserver written in flask is used to install a Shopify app on a
Shopify store, by providing a complete hand-shake between the merchant and our
services, allowing us to fetch an access token from the merchant.

## Environment variable that needs to be set
- DB\_NAME (no default): The name of the database to connect to.
- DB\_USER (no default): The user to connect to the database with.
- DB\_PASSWORD (no default): The password to connect to the database with.
- DB\_HOST (no default): The host of the database.
- DB\_PORT (no default): The port of the database.
- SHOPIFY\_API\_KEY (no default): The API key to connect to the Shopify API
  with.
- SHOPIFY\_API\_SECRET (no default): The API secret to connect to the Shopify
  API with.
- REDIS\_HOST (no default): The host of the Redis server.
- REDIS\_PORT (no default): The port of the Redis server.

## How to run ?

### In development mode

#### For Foundxtion and nixOS users

In a terminal, do the following commands:
```zsh
cd tools/;
nix-shell --run zsh;
cd ..;
poetry install;
# export all environment variables...
poetry run python3 -m installer.setup
```

### In production mode
You can use the available docker-compose file to run the server in production mode.
