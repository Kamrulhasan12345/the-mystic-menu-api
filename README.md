# The Mystic Menu API

The Mystic Menu API empowers culinary creativity. It provides the tools for developers to build innovative recipe creation and management applications.

## Key Features

*   **Recipe Creation:** Enable users to easily create and store their own recipes.
*   **Customization:** Support personalized recipe variations.
*   **Organization:** Facilitate recipe organization through categories, tags, collections, and meal planning features.
*   **Sharing:** Allow users to share their culinary creations.
*   **Integration:** Seamlessly integrate recipe management into existing food-related apps or platforms.

## License

MIT License

## Authentication

*   **Tag:** `auth`
*   **Description:** Operations with authentication. Provides `access_token` and user information.

    *   `POST /auth/signup`: Signup
    *   `POST /auth/signin`: Signin
    *   `GET /auth/me`: Me

## Recipes

*   **Tag:** `recipes`
*   **Description:** Operations with recipes. Requires authentication via the Authorize button above, accepting `access_token` from `/auth` URLs.

    *   `GET /recipes/`: Get Recipes
    *   `POST /recipes/`: Add Recipe
    *   `GET /recipes/{id}`: Get Recipe
    *   `DELETE /recipes/{id}`: Delete Recipe
    *   `POST /recipes/random`: Create Random

## Default

*   `GET /`: Root

### Protip: You can try out the API for yourself at [https://the-mystic-menu-api.vercel.app/docs](https://the-mystic-menu-api.vercel.app/docs)