import sys
import re

# Look at the images showing what these regexes do for more details.
# It's not as complex as it looks.
def detect(html):
    # (?is): i means regex should be case-insensitive
    # and s means '.' could stand for a newline character as well
    # '?' after * means be non-greedy (i.e. don't go as far as you can go)
    # (?: ... ) means that the group is non-capturing (i.e. not back-referenced)
    # this regex just finds all the valid anchor tags
    regex_links = r"(?is)(<a(?:\s|(?:\s.*?\s))href=\s*(?:([\"']).*?\2.*?>|[^\"'][^\s]*(?:\s.*?>|>)).*?</a>)"
    a_tags = [i[0] for i in re.findall(regex_links, html)]

    # this regex gets the href from the anchor tag
    regex_href = r"(?is)(?<=href=)\s*(?:([\"']).*?(?=\1)|[^\"'][^\s]*(?=\s|>))"
    # I'm not dealing with the following case for getting the anchor tag's text:
    # <a href="#"><strong>asdf</strong> hack</a> (the text is: "asdf hack")
    # but I'm dealing with <a href="#"><em>asdf hack</em></a>
    regex_text = r"(?<=>)[^>]*?(?=</)"
    for tag in a_tags:
        href = (re.search(regex_href, tag).group(0)).strip()
        if href[0] == '"':
            href = href[1:]
        
        text = (re.search(regex_text, tag).group(0)).strip()
        print(href + "," + text)


def main():
    num_lines = int(sys.stdin.readline())
    if num_lines >= 100:
        return 1

    char_count = 0
    html_fragment = ""
    for i in range(num_lines):
        line = sys.stdin.readline()
        # reached end of file before reading N lines
        if line == '':
            break

        char_count += len(line)
        if char_count > 10000:
            return 1
        
        html_fragment += line

    detect(html_fragment)

if __name__ == '__main__':
    main()
