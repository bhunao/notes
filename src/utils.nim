import std/os
import std/strutils
import std/strformat
import std/sequtils
import crud

let notesFolder* = getEnv("NOTES_DIR")
echo notesFolder

proc insertNotesFromPath(dir: string) =
  var paths = toSeq(walkDirRec(dir))
  for filePath in paths:
    var (path, name) = filePath.splitPath()
    name = filePath.extractFilename
    path = path[dir.len-1 .. ^1]
    echo fmt"name: {name} | path: {path}"
    insertRow(name, path)
  

proc openNote*(path: string): string =
  let beforePath = "/home/bhunao/notes/z_bkp/"
  echo "oppening file: ", beforePath / path
  return readFile(beforePath / path)

# insertNotesFromPath(notesFolder)
