# notes

> poetry run uvicorn main:app --reload --host 0.0.0.0

## banco
### notes
notes metadata

#### fields
- id
- name
- path
- parent
- type
- created_at
- last_edit

## regras
### crud
- create note
- select note
    - select one
    - select all
- update note
- delete note

### file contents
- list all files
- get file content
- update_note_file
- create_note_file
- insert_metadata_on_db

## back-end
### endpoints
- all: `get`: `/`
- get: `get`: `/{id}`
- upd: `patch`: `/{id}/edit`
- new: `put`: `/{id}/new`
- del: `del`: `/{id}/del`

## frot-end
### pages
- template

### components
- all_notes
- note
- edit
- new
- del
- search
