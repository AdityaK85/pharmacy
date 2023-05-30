from django.shortcuts import render

# Create your views here.

def Dashboard(request):
    return render(request, 'index.html')

def Invoice(request):
    return render(request, 'invoice.html')

def Stock(request):
    return render(request, 'stock.html')

def Medicien(request):
    return render(request, 'medicien.html')

def Purchase(request):
    return render(request, 'purchase.html')

def ManageStock(request):
    return render(request, 'manage_stock.html')

def StockReports(request):
    return render(request, 'stock_reports.html')