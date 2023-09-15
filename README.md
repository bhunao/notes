# notes

SSR project written in Nim 👑 with HappyX ❤

## 


## database 

### notes
|   field_name      |   type        |
|---                | ---           |
| id                |   primary     |
| path              |   varchar     |
| name              |   varchar     |
| last_edit         |   DATETIME    |
| date_created      |   DATETIME    |
| content           |   TEXT        |
| parent            |   foreign(int)|
| type              |   varchar     |

### tags
|   field_name      |   type        |
|   ---             |   ---         |
| id                |   primary     |
| note_id           |   foreign(int)|
| tag               |   varchar     |

### parent
|   field_name      |   type            |
|   ---             |   ---             |
| parent            |   foreign(note.id)|
| child             |   foreign(note.id)|
