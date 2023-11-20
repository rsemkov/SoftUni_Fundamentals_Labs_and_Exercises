def title(text):
    print(f"<h1>\n\t{text}\n</h1>")


def content(text):
    print(f"<article>\n\t{text}\n</article>")


def comment(text):
    print(f"<div>\n\t{text}\n</div>")


title(input())
content(input())
while True:
    command = input()
    if command == "end of comments":
        break
    comment(command)
