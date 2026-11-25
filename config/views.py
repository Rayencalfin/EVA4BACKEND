from django.conf import settings
from django.http import FileResponse
from django.views.decorators.http import require_safe


@require_safe
def home(request):
    return FileResponse(
        (settings.BASE_DIR / "index.html").open("rb"),
        content_type="text/html; charset=utf-8",
    )