create table if not exists `notes` (
  `id` integer not null primary key autoincrement,
  `name` VARCHAR(255) null,
  `path` varchar(255) null,
  `content` varchar(255) not null,
  `created_at` datetime not null,
  `last_update` datetime null default CURRENT_TIMESTAMP,
  `parent` varchar(255) null,
  `type` varchar(255) null
);

create table if not exists `tags` (
  `id` integer not null primary key autoincrement,
  `note_id` integer not null,
  `tag` VARCHAR(255) null,
  foreign key (note_id) references parent(`notes`)
);

create table if not exists `parent` (
  `parent_id` integer not null,
  `child_id` integer not null,
  foreign key (parent_id) references parent(`notes`)
  foreign key (child_id) references parent(`notes`)
);
