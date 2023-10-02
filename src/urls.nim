import prologue

import ./views


let urlPatterns* = @[
  pattern("/", getIndex),
  pattern("/note/{id}", getNote, HttpGet),
  pattern("/note/{id}", putNote, HttpPut),
  pattern("/search/", postSearch, HttpPost),
  pattern("/edit/{id}", getEdit, HttpGet),
]


