user_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "example": "Max",
      "maxLength": 100,
      "minLength": 1,
      "pattern": "^\\S.+$"
    },
    "email": {
      "type": "string",
      "example": "max@gmail.com",
      "maxLength": 100,
      "minLength": 5,
      "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
    },
    "nickname": {
      "type": "string",
      "example": "max",
      "maxLength": 100,
      "minLength": 2,
      "pattern": "^[a-zA-Z0-9_.+-]+$"
    },
    "uuid": {
      "type": "string",
      "format": "uuid",
      "example": "00000000-0000-4562-b3fc-2c963f66afa6",
      "maxLength": 36,
      "minLength": 36,
      "pattern": "[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}"
    },
    "password": {
      "type": "string",
      "example": "password",
      "maxLength": 100,
      "minLength": 6,
      "pattern": "^\\S.+$",
      "writeOnly": True
    },
    "avatar_url": {
      "type": "string",
      "default": "",
    }
  },
  "required": ["email", "name", "nickname", "avatar_url", "uuid"]
}

category_uuid_games_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "games": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "category_uuids": {
            "type": "array",
            "items": {
              "type": "string",
              "format": "uuid",
              "minLength": 36,
              "maxLength": 36,
              "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$",
              "example": "00000000-0000-4562-b3fc-2c963f66afa6"
            }
          },
          "price": {
            "type": "integer",
            "minimum": 0,
            "example": 5999
          },
          "title": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "example": "The Witcher 3: Wild Hunt"
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "minLength": 36,
            "maxLength": 36,
            "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$",
            "example": "00000000-0000-4562-b3fc-2c963f66afa6"
          }
        },
        "required": ["uuid", "title", "price", "category_uuids"]
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "example": 10
        }
      },
      "required": ["total"]
    }
  },
  "required": ["games", "meta"]
}


game_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Game",
  "type": "object",
  "properties": {
    "category_uuids": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uuid",
        "minLength": 36,
        "maxLength": 36,
        "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$",
        "example": "00000000-0000-4562-b3fc-2c963f66afa6"
      }
    },
    "price": {
      "type": "integer",
      "minimum": 0,
      "example": 5999
    },
    "title": {
      "type": "string",
      "minLength": 1,
      "maxLength": 100,
      "example": "The Witcher 3: Wild Hunt"
    },
    "uuid": {
        "type": "string",
        "format": "uuid",
        "minLength": 36,
        "maxLength": 36,
        "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$",
        "example": "00000000-0000-4562-b3fc-2c963f66afa6"
    }
  },
  "required": ["uuid", "title", "price", "category_uuids"]
}

uuid_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "UUID",
  "type": "string",
  "format": "uuid",
  "minLength": 36,
  "maxLength": 36,
  "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$",
  "example": "00000000-0000-4562-b3fc-2c963f66afa6"
}

whishlist_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Wishlist",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "category_uuids": {
            "type": "array",
            "items": {
              "type": "string",
              "format": "uuid",
              "minLength": 36,
              "maxLength": 36,
              "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$",
              "example": "00000000-0000-4562-b3fc-2c963f66afa6"
            }
          },
          "price": {
            "type": "integer",
            "minimum": 0,
            "example": 5999
          },
          "title": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100,
            "example": "The Witcher 3: Wild Hunt"
          },
          "uuid": {
              "type": "string",
              "format": "uuid",
              "minLength": 36,
              "maxLength": 36,
              "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$",
              "example": "00000000-0000-4562-b3fc-2c963f66afa6"
          }
        },
        "required": ["uuid", "title", "price", "category_uuids"]
      },
      "maxItems": 10
    },
    "user_uuid": {
      "type": "string",
      "format": "uuid",
      "minLength": 36,
      "maxLength": 36,
      "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$",
      "example": "00000000-0000-4562-b3fc-2c963f66afa6"
    }
  },
  "required": ["user_uuid", "items"]
}

user_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "User",
  "type": "object",
  "properties": {
    "avatar_url": {
      "default": "",
      "type": "string"
    },
    "uuid": {
      "type": "string",
      "format": "uuid",
      "minLength": 36,
      "maxLength": 36,
      "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$",
      "example": "00000000-0000-4562-b3fc-2c963f66afa6"
    },
    "name": {
      "type": "string",
      "example": "Max",
      "maxLength": 100,
      "minLength": 1,
      "pattern": "^\\S.+$"
    },
    "email": {
      "type": "string",
      "example": "max@gmail.com",
      "maxLength": 100,
      "minLength": 5,
      "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
    },
    "nickname": {
      "type": "string",
      "example": "max",
      "maxLength": 100,
      "minLength": 2,
      "pattern": "^[a-zA-Z0-9_.+-]+$"
    }
  },
  "required": [
    "uuid",
    "avatar_url",
    "email",
    "name",
    "nickname"
  ]
}
