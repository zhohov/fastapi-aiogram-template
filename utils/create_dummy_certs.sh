#!/bin/bash

DOMAIN="domain.com"
DUMMY_CERT_DIR="/etc/letsencrypt/temp/$DOMAIN"
mkdir -p $DUMMY_CERT_DIR

if [ ! -f "$DUMMY_CERT_DIR/privkey.pem" ] || [ ! -f "$DUMMY_CERT_DIR/fullchain.pem" ]; then
  echo "Creating dummy certificates..."
  openssl req -x509 -nodes -newkey rsa:2048 -days 1 -keyout "$DUMMY_CERT_DIR/privkey.pem" -out "$DUMMY_CERT_DIR/fullchain.pem" -subj "/CN=dummy.$DOMAIN"
else
  echo "Dummy certificates already exist."
fi

nginx -g "daemon off;"
