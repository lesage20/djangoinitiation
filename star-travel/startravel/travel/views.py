from django.shortcuts import render
# Create your views here.


def index(request):
    datas = {

    }
    return render(request, "index.html", datas)


def dashboard(request):
    datas = {

    }
    return render(request, "dashboard.html", datas)


def aboutus(request):
    datas = {

    }
    return render(request, "about-us.html", datas)


def flighthomepage(request):
    datas = {

    }
    return render(request, "flight-homepage.html", datas)


def hotelhomepage(request):
    datas = {

    }
    return render(request, "hotel-homepage.html", datas)


def tourhomepage(request):
    datas = {

    }

    return render(request, "tour-homepage.html", datas)


def cruisehomepage(request):
    datas = {

    }

    return render(request, "cruise-homepage.html", datas)


def carhomepage(request):
    datas = {

    }

    return render(request, "car-homepage.html", datas)


def landingpage(request):
    datas = {

    }

    return render(request, "landing-page.html", datas)


def flight_listing_right_sidebar(request):
    datas = {

    }
    return render(request, 'flight-listing-right-sidebar.html', datas)


def flight_listing_left_sidebar(request):
    datas = {

    }
    return render(request, "flight-listing-left-sidebar.html", datas)


def flight_grid_right_sidebar(request):
    datas = {

    }
    return render(request, "flight-grid-right-sidebar.html", datas)


def flight_grid_left_sidebar(request):
    datas = {

    }
    return render(request, "flight-grid-left-sidebar.html", datas)


def flight_detail_right_sidebar(request):
    datas = {

    }
    return render(request, "flight-detail-right-sidebar.html", datas)


def flight_detail_left_sidebar(request):
    datas = {

    }
    return render(request, "flight-detail-left-sidebar.html", datas)
