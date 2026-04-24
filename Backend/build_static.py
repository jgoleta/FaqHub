import os
import django
from django.template import engines
from django.test.client import RequestFactory

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from availability.views import login_page, dashboard

# Create a fake request object
factory = RequestFactory()
request = factory.get('/')

# Render login page
login_html = login_page(request).content.decode('utf-8')
with open('staticfiles/index.html', 'w', encoding='utf-8') as f:
    f.write(login_html)
print("✓ Generated index.html (login page)")

# Render dashboard page
dashboard_html = dashboard(request).content.decode('utf-8')
with open('staticfiles/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dashboard_html)
print("✓ Generated dashboard.html")

# Copy any static files (CSS/JS) - if you have a static folder
import shutil
if os.path.exists('static'):
    shutil.copytree('static', 'staticfiles/static', dirs_exist_ok=True)
    print("✓ Copied static files")