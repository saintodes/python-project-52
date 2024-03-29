#!/usr/bin/env bash

#Build this .sh to deploy app and db at localhost

# Attempt to get DATABASE_URL from .env file
DATABASE_URL=$(grep -E "^DATABASE_URL=" ./.env | cut -d '=' -f2-)

if [[ -z "$DATABASE_URL" ]]; then
    echo "Error: .env file is missing or DATABASE_URL environment variable is not set."
    exit 1
fi

echo "Using DATABASE_URL: $DATABASE_URL"

# Parse db url
regex="postgres://([^:]+):([^@]+)@([^:]+):([^/]+)/(.+)"
if [[ $DATABASE_URL =~ $regex ]]; then
    DB_USER="${BASH_REMATCH[1]}"
    DB_USER_PASSWORD="${BASH_REMATCH[2]}"
    DB_HOST="${BASH_REMATCH[3]}"
    DB_PORT="${BASH_REMATCH[4]}"
    DB_NAME="${BASH_REMATCH[5]}"

    echo "Parsed DATABASE_URL:"
    echo "User: $DB_USER"
    echo "Host: $DB_HOST"
    echo "Port: $DB_PORT"
    echo "Database Name: $DB_NAME"
else
    echo "Error: Invalid or missing DATABASE_URL format."
    exit 1
fi

#Start postgresql service
if sudo service postgresql start; then
    echo "PostgreSQL service started succesfully"
else
    echo "Error: Failed to start PostgreSQL service"
fi

#Check if db role exists
ROLE_EXISTS=$(sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='$DB_USER'")
if [ "$ROLE_EXISTS" = "1" ]; then
    echo "Database role '$DB_USER' already exists. Skipping creation."
else
    # Create db role
    COMMAND_CREATE_ROLE="CREATE ROLE $DB_USER WITH CREATEDB LOGIN PASSWORD '$DB_USER_PASSWORD';"
    if sudo -u postgres psql -c "$COMMAND_CREATE_ROLE"; then
        echo "Database role '$DB_USER' created successfully."
    else
        echo "Error: Failed to create database role '$DB_USER'."
        exit 1
    fi
fi
s
# Create db
if sudo -u postgres createdb --owner=$DB_USER $DB_NAME; then
    echo "Database '$DB_NAME' created successfully."
else
    echo "Error: Failed to create database '$DB_NAME'."
fi

# Install app and setup the database
if make install && psql -a -d $DATABASE_URL -f database.sql; then
    echo "Database setup completed successfully."
else
    echo "Error: Failed to setup the database."
    exit 1
fi