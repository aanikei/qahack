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

