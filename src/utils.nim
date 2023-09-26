import std/os
import std/strutils
import std/sequtils
import crud

let dirPath = "/home/bhunao/notes/z/"

proc insertNotesFromPath(dir: string) =
  var paths = toSeq(walkDirRec(dir))
  for path in paths:
    var (path, name) = path.splitPath()
    name = path.extractFilename
    path = path[dir.len-1 .. ^1]
    insertRow(name, path)
  

proc openNote*(path: string): string =
  let beforePath = "/home/bhunao/notes/z/"
  echo beforePath / path
  return readFile(beforePath / path)
