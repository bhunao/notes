from typing import List, Tuple
from enum import Enum


class Tags(Enum):
    h1 = "# "
    h2 = "## "
    h3 = "### "
    h4 = "#### "
    h5 = "##### "
    h6 = "###### "
    li = "- "
    hr = "---"


PARSED_LINES = List[Tuple[Tags, str]]


def parse(text: str) -> PARSED_LINES:
    lines = text.split("\n")
    parsed_lines: PARSED_LINES = []
    for line in lines:
        for tag in Tags:
            if line.strip().startswith(tag.value):
                parsed_lines.append((tag, line))
                break
        else:
            parsed_lines.append((None, line))
    return parsed_lines


def html_tag(content: str, tag=None, _class="", _id=""):
    if not tag:
        return content

    result = f"<{tag.name} "

    if _class:
        result += f"class=\"{_class}\" "
    if _id:
        result += f"id=\"{_id}\" "

    result += ">"

    result += content[len(tag.name):]
    result += f"</{tag.name}>"
    return result


def text_index(text: str):
    lines = parse(text)
    result = []
    for i, line in enumerate(lines):
        tag, content = line
        match tag:
            case Tags.h1 | Tags.h2 | Tags.h3 | Tags.h4 | Tags.h5 | Tags.h5 | Tags.h6:
                result.append(
                    f'<a class="list-group-item list-group-item-action" href="#{content[len(tag.value):]}">{content}</a>')
            case _:
                pass
    return "\n".join(result)


def parsed_html_line(lines):
    result = []
    for i, line in enumerate(lines):
        content_tag, content = line
        match content_tag:
            case None:
                result.append(content)
            case Tags.li:
                if i >= 1 and lines[i-1][0] != Tags.li:
                    result.append(
                        "<ul class=\"list-group list-group-flush\">")

                result.append(
                    html_tag(content, content_tag, "list-group-item"))

                if len(lines)-1 > i and lines[i+1][0] != Tags.li:
                    result.append("</ul>")
            case Tags.h1 | Tags.h2 | Tags.h3 | Tags.h4 | Tags.h5 | Tags.h5 | Tags.h6:
                result.append(html_tag(
                    content,
                    content_tag,
                    _class="text-center text-light bg-dark mb-3 border",
                    _id=content[len(content_tag.value):]
                ))
            case _:
                result.append(html_tag(content, content_tag))
    return result


def html(text: str) -> str:
    lines = parse(text)
    result = parsed_html_line(lines)
    return "\n".join(result)
