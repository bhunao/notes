import asyncdispatch, jester, os, strutils

router myrouter:
  get "/":
    resp "It's alive!"

proc main() =
  let port = 8000.Port
  let settings = newSettings(port=port)
  var jester = initJester(myrouter, settings=settings)
  jester.serve()

when isMainModule:
  main()