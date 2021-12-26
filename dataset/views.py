from django.shortcuts import render,redirect

# Create your views here.
def download(request):
    if request.method == 'POST':
        drop = request.POST['drone01_dropdown']
        filename = request.POST['filename']
        if drop == "data":
            path = request.build_absolute_uri("/dataset/download/api/" + drop + "/" + filename)
        else:
            path = request.build_absolute_uri("/dataset/download/api/" + drop)

        return render(request, 'download.html', {"path": path})
    else:
        print("test")
        return render(request, 'download.html')

def drone01_zip(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/data-01/train/Drone-01.rar"
    return redirect(url)

def drone01_sample(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/data-01/train/Drone-01_sample.rar"
    return redirect(url)

def drone01_image(request,name):
    print(name)
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/data-01/train/" + name + ".JPG"
    return redirect(url)

def drone01_image(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/data-01/train/"
    return redirect(url)

def drone01_label(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/data-01/train_label/train.json"
    return redirect(url)