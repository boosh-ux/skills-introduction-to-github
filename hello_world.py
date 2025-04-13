
def generate_html():
    """
    Generate an HTML page with 'hello world' centered on the page.
    """
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            font-size: 2rem;
        }
    </style>
</head>
<body>
    <div>hello world</div>
</body>
</html>
"""
    
    with open('index.html', 'w') as f:
        f.write(html_content)
    
    print("HTML file 'index.html' has been generated successfully!")
    print("Open the file in a web browser to see the centered 'hello world' text.")

if __name__ == "__main__":
    generate_html()
