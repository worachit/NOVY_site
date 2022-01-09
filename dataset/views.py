from django.shortcuts import render,redirect

# Create your views here.
def download(request):
    path1 = request.build_absolute_uri("/dataset/download/api/datasets")
    if request.method == 'POST':
        try:
            drop_name = request.POST['name_dropdown']
            drop_type = request.POST['select_type']
        except:
            drop_name = "drone-01"  
            drop_type = "data/all"
        filename = request.POST['filename']
        
        if drop_type == "data":
            path2 = request.build_absolute_uri("/dataset/download/api/" + drop_name + "/" + drop_type + "/" + filename)
        else:
            path2 = request.build_absolute_uri("/dataset/download/api/" + drop_name + "/" + drop_type)

        return render(request, 'download.html', {"path1" : path1, "path2" : path2})
    else:
        return render(request, 'download.html', {"path1" : path1})

def datasets(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/datasets.json"
    return redirect(url)

def drone01_zip(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/data-01/train/Drone-01.rar"
    return redirect(url)

def drone01_sample(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/data-01/train/Drone-01_sample.rar"
    return redirect(url)

def drone01_image(request,name):
    print(name)
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/data-01/train/" + name
    return redirect(url)

def drone01_name(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/data-01/train/Drone-01_filenames.json"
    return redirect(url)

def drone01_label(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/data-01/train_label/train.json"
    return redirect(url)