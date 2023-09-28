import std/osproc
import std/os
import std/strformat
import std/strutils


let notesFolder* = getEnv("NOTES_DIR")

echo notesFolder
let (output, exitCode) =  execCmdEx("git commit", workingDir=notesFolder)

for res in output.split("\n"):
  echo res

