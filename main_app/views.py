from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'page_name': 'Home'})

def about(request):
    return render(request, 'about.html')

class Crystal:
    def __init__(self, name, description, properties, chakras, zodiac, color):
        self.name = name
        self.description = description
        self.properties = properties
        self.chakras = chakras
        self.zodiac = zodiac
        self.color = color

crystals = [
    Crystal('Amazonite', 'Aligning your values', 'Balance, Calm, and Clarity', 'Heart and Throat', 'Virgo', 'Pearly Brihgt turquoise-green with white fine veins'),
    Crystal('Black Obsidian', 'Empowers inner strength to see destructive behavioural patterns', 'Grounding, Intuition, Protection', 'Root', 'Scorpio and Saggitarius', 'Black Glass Like'),
    Crystal('Blue Lace Agate', 'Increases confidence to clearly communicate', 'Balance, Calm, Communication', 'Throat', 'Gemini and Pisces', 'Light Blue with white and lighter tones'),
]        

def crystals_index(request):
    return render(request, 'crystals/index.html', { 'crystals': crystals })
