import tailwindcss

# Hero section uchun ma'lumotlar
hero_data = {
    "title": "SaaS Landing Page",
    "description": "SaaS uchun ideal landing sahifa",
    "button_text": "Batafsil",
    "button_link": "#"
}

# Hero section uchun HTML
hero_html = f"""
<div class="max-w-7xl mx-auto px-4 py-12">
    <div class="text-center">
        <h1 class="text-4xl font-bold tracking-tight text-gray-900">{hero_data['title']}</h1>
        <p class="mt-4 text-lg text-gray-500">{hero_data['description']}</p>
        <button class="mt-8 inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
            {hero_data['button_text']}
        </button>
    </div>
</div>
"""

# Hero section uchun CSS
hero_css = """
.hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #f7f7f7);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 300px;
    transition: background-position 0.5s ease-in-out;
}

.hero:hover {
    background-position: 0% 0%;
}
"""

# Hero section uchun JavaScript
hero_js = """
const hero = document.querySelector('.hero');
hero.addEventListener('mouseover', () => {
    hero.classList.add('hover');
});
hero.addEventListener('mouseout', () => {
    hero.classList.remove('hover');
});
"""

# Tayyor hero section uchun HTML
print(hero_html)

# Tayyor hero section uchun CSS
print(hero_css)

# Tayyor hero section uchun JavaScript
print(hero_js)
