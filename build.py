CSS = """
body {
    font-family: Georgia, "Times New Roman", serif;
    margin: 0;
    padding: 0;
    background: #f5f0ea;
    color: #201a1d;
    line-height: 1.6;
}

header, footer {
    background: linear-gradient(135deg, #141214 0%, #1f1a1d 55%, #2a2026 100%);
    color: #fdf8f4;
    padding: 28px 0;
}

nav a {
    color: #f7efe9;
    margin-right: 22px;
    text-decoration: none;
    font-weight: 700;
    font-family: Arial, sans-serif;
    letter-spacing: 0.2px;
}

nav a:hover {
    color: #d7a98c;
}

.container {
    max-width: 1120px;
    margin: 0 auto;
    padding: 34px 24px;
}

h1 {
    font-size: 3rem;
    margin: 0 0 14px 0;
    font-weight: 700;
    letter-spacing: 0.4px;
}

h2 {
    font-size: 2.2rem;
    margin-bottom: 18px;
    color: #201a1d;
}

h3 {
    font-size: 1.5rem;
    margin-bottom: 12px;
    color: #2b1f24;
}

p {
    font-size: 1.08rem;
    color: #4e4346;
}

.hero {
    padding: 70px 0 44px 0;
}

.hero h2 {
    font-size: 3rem;
    line-height: 1.15;
    max-width: 760px;
    margin-bottom: 18px;
    color: #22181d;
}

.hero p {
    max-width: 700px;
    font-size: 1.14rem;
    color: #5a4a50;
}

.button {
    display: inline-block;
    background: linear-gradient(135deg, #8c4f3d 0%, #6d2f4d 100%);
    color: white;
    padding: 13px 22px;
    text-decoration: none;
    border-radius: 999px;
    margin-top: 12px;
    font-family: Arial, sans-serif;
    font-weight: 700;
    box-shadow: 0 6px 16px rgba(95, 46, 58, 0.18);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.button:hover {
    transform: translateY(-1px);
    box-shadow: 0 10px 22px rgba(95, 46, 58, 0.24);
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 28px;
}

.card {
    background: #fffaf7;
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 6px 18px rgba(60, 30, 40, 0.08);
    border: 1px solid #eadbd2;
}

.book-cover {
    width: 100%;
    max-height: 380px;
    object-fit: cover;
    border-radius: 14px;
    margin-bottom: 16px;
    box-shadow: 0 4px 14px rgba(40, 20, 30, 0.12);
}

.author-photo {
    max-width: 280px;
    border-radius: 18px;
    margin-bottom: 22px;
    box-shadow: 0 8px 24px rgba(40, 20, 30, 0.16);
}

.section-title {
    margin-bottom: 20px;
    position: relative;
}

.section-title::after {
    content: "";
    display: block;
    width: 72px;
    height: 3px;
    background: linear-gradient(135deg, #8c4f3d 0%, #6d2f4d 100%);
    margin-top: 8px;
    border-radius: 999px;
}

.small-note {
    color: #6a5960;
    font-style: italic;
    font-size: 1.02rem;
}

footer p {
    color: #f5e8df;
    font-family: Arial, sans-serif;
    font-size: 1rem;
}

section {
    margin-bottom: 42px;
}
"""