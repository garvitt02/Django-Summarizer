from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .nlp_model import read_document, summarize_text
from .models import Document

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('document'):
        document = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(document.name, document)
        file_path = fs.path(filename)

        content = read_document(file_path)

        summary = summarize_text(content)

    
        doc = Document(name=document.name, upload=document, summary=summary)
        doc.save()

        return render(request, 'summary/upload.html', {'summary': summary})

 
    return render(request, 'summary/upload.html', {'summary': None})
