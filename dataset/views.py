from django.shortcuts import render,redirect

# Create your views here.
def download(request):
    path1 = request.build_absolute_uri("/dataset/download/api/datasets")

    dataset_list = [
            {"name" : "drone-01",
            "header_image" : "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/drone-01/train/DJI_0513.JPG",
            "train_images" : "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/drone-01/train/drone-01_dataset.rar",
            "annotations": "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/drone-01/train_label/drone-01_train.json"},
            
            {"name" : "Marvic-15m",
            "header_image" : "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/Marvic-15m/train/DJI_0413.JPG",
            "train_images" : "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/Marvic-15m/train/Marvic-15m_dataset.rar",
            "annotations": "#"},
            ]


    if request.method == 'POST':
        try:
            drop_name = request.POST['name_dropdown']
            drop_type = request.POST['select_type']
        except:
            drop_name = "drone-01"  
            drop_type = "data/all"
        filename = request.POST['filename']
        
        if drop_type == "data" or drop_type == "datac":
            path2 = request.build_absolute_uri("/dataset/download/api/" + drop_name + "/" + drop_type + "/" + filename)
        else:
            path2 = request.build_absolute_uri("/dataset/download/api/" + drop_name + "/" + drop_type)

        return render(request, 'download.html', {"dataset_list" : dataset_list, "path1" : path1, "path2" : path2})
    else:
        return render(request, 'download.html', {"dataset_list" : dataset_list, "path1" : path1})

def datasets(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/datasets.json"
    return redirect(url)

#########################################
def drone01_zip(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/drone-01/train/drone-01_dataset.rar"
    return redirect(url)

# def drone01_sample(request):
#     url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/drone-01/train/Drone-01_sample.rar"
#     return redirect(url)

def drone01_image(request,name):
    print(name)
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/drone-01/train/" + name
    return redirect(url)

def drone01_image_compress(request,name):
    print(name)
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/drone-01/train_compress/" + name
    return redirect(url)

def drone01_info(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/drone-01/train/drone-01_info.json"
    return redirect(url)

def drone01_label(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/drone-01/train_label/drone-01_train.json"
    return redirect(url)

#########################################
def Marvic_zip(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/Marvic-15m/train/Marvic-15m_dataset.rar"
    return redirect(url)

def Marvic_image(request,name):
    print(name)
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/Marvic-15m/train/" + name
    return redirect(url)

def Marvic_image_compress(request,name):
    print(name)
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/Marvic-15m/train_compress/" + name
    return redirect(url)

def Marvic_info(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/Marvic-15m/train/Marvic-15m_info.json"
    return redirect(url)

def Marvic_label(request):
    url = "https://novy-static.sgp1.digitaloceanspaces.com/dataset/dataset/Marvic-15m/train_label/Marvic-15m_train.json"
    return redirect(url)