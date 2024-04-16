CREATE TABLE IF NOT EXISTS item_folders (
  item_id INTEGER REFERENCES projects(id),
  folder_id INTEGER REFERENCES folders(id),
  PRIMARY KEY (item_id, folder_id)
);