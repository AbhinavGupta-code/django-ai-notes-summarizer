from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm
from .models import Note
from .utils import ai_summarizer, extract_keywords, generate_title

def summarize_text(text: str, max_sentences: int = 3, max_words: int = 80) -> str:
    """
    Simple rule-based summarizer:
    - Split by '.', '!', '?'
    - Take first few sentences
    - If still too long, trim by words
    """
    if not text:
        return ""

    # Split into sentences roughly
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s.strip() for s in sentences if s.strip()]

    # Take first N sentences
    selected = sentences[:max_sentences]
    summary = " ".join(selected)

    # Limit by words
    words = summary.split()
    if len(words) > max_words:
        summary = " ".join(words[:max_words]) + "..."

    return summary


def index(request):
    summary = None
    keywords = None
    mode = "medium"

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)

            # If no title entered → Auto-generate title
            if not note.title.strip():
                note.title = generate_title(note.original_text)

            # Get selected summary mode
            mode = request.POST.get("mode", "medium")

            # Generate summary
            summary = ai_summarizer(note.original_text, mode)

            # Extract keywords
            keywords = extract_keywords(note.original_text)

            note.summary_text = summary
            note.save()

            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm()

    recent_notes = Note.objects.all().order_by("-created_at")[:5]

    return render(request, "summarizer/index.html", {
        "form": form,
        "recent_notes": recent_notes,
        "summary": summary,
        "keywords": keywords,
        "mode": mode,
    })



def note_detail(request, pk):
    """
    Show full original text + summary for one note
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'summarizer/detail.html', {'note': note})
