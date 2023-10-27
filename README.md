# notes
Site para criação, edição e busca de textos em markdown. Feito inicialmente para rodar localmente lendo e salvando os textos em arquivos `.md` no computador.

Website for creating, editing and search for texts in markdown. Initialy made to run locally reanding and writing the texts in `.md` files on the computer.

## páginas html / html pages
- index
- search
- new
- note
    - delete
- edit

## API endpoints
`localhost:8000/docs/`

| method    | endpoint    | name    |
|---------------- | --------------- | --------------- |
| **GET**       |     / |               |    Index   |
| **GET**       |     /{id}             | Get  |
| **POST**      |    /{id}             | Update  |
| **DELETE**    |  /{id}             | Delete  |
| **GET**       |     /{id}/edit        | Edit  |
| **GET**  |     /new/             | Create  |
| **POST**  |    /new/             | Insert New  |
| **POST**  |    /search/          | Search  |
| **POST**  |    /insert/metadata/ | Post Insert Metadata -- debug  |

## TODOS
- create tests
- add logging
- add docker to project
    - try postgreeSQL
- create button for `new` page
- create pagination in index and search
- add link to other pages (links for non-existing file should create a new one?)
- make textarea in `edit` page fill height
- fix created and last_edit dates
- document domain layer
