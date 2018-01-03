from django.shortcuts import render, redirect
from .models import Folder,File

from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request, curFolder=None):
    if curFolder:
        print(curFolder)
        files = File.objects.filter(parent_folder__foldername=curFolder)
        folders = Folder.objects.filter(parent_folder__foldername=curFolder)
        print(files)
        print(folders)
        pass
    else:
        print("index folder")
        files = File.objects.filter(parent_folder=None)
        folders = Folder.objects.filter(parent_folder=None)

    if request.method == "POST":
        if request.POST['action'] == "uploadFolder":
            AddFolder(request, curFolder)
        elif request.POST['action'] == "uploadFile":
            AddFile(request, curFolder)

    return render(request, 'drive/index.html',{'files': files,'folders': folders, 'ctr1':0, 'ctr':0})

def AddFolder(request, curFolder=None):
    flname = request.POST['foldername']
    fldesc = request.POST['folderdesc']

    if curFolder:
        print("added in folder "+curFolder)
        parent_folder = Folder.objects.get(foldername=curFolder)
        newfolder = Folder.objects.create(foldername=flname, folderdesc=fldesc, parent_folder=parent_folder)
        newfolder.save()
    else:
        newfolder = Folder.objects.create(foldername=flname,folderdesc=fldesc)
        newfolder.save()

    return redirect('index')

def AddFile(request, curFolder=None):

    myfile = request.FILES['file']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)

    if curFolder:
        print("added file "+ filename + "in folder "+curFolder +", "+uploaded_file_url)
        parent_folder = Folder.objects.get(foldername=curFolder)
        newfile = File.objects.create(filename=filename, filedir=uploaded_file_url, parent_folder=parent_folder)
        newfile.save()

    else:
        newfile = File.objects.create(filename=filename, filedir=uploaded_file_url)
        newfile.save()

    return redirect('index')

