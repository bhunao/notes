import crud

import std/os
import std/strutils
import std/strformat
import std/sequtils
import db_connector/db_sqlite

let notesFolder* = getEnv("NOTES_DIR")
echo notesFolder

proc insertNotesFromPath(dir: string) =
  var paths = toSeq(walkDirRec(dir))
  for filePath in paths:
    var (pathFile, name) = filePath.splitPath()
    name = filePath.extractFilename
    pathFile = pathFile[dir.len-1 .. ^1]
    echo fmt"name: {name} | pathFile: {pathFile}"
    insertRow(name, pathFile)
  

proc openNote*(pathFile: string): string =
  let beforePath = "/home/bhunao/notes/z_bkp/"
  echo "oppening file: ", beforePath / pathFile
  return readFile(beforePath / pathFile)

proc saveNote*(row: Row, content, rootDir = notesFolder) =
    updateRow(row[0], row[1], row[2])
    writeFile(notesFolder / row[1] / row[2], content)

# insertNotesFromPath(notesFolder)
