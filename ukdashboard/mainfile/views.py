from django.shortcuts import render
from .models import UkCompany, Segment
import csv
from django.contrib import messages


def decode_utf8(line_iterator):
    for line in line_iterator:
        yield line.decode('utf-8')


def update_existing_data(csvfile): 
    file_data = list(csv.reader(decode_utf8(csvfile)))
    for csv_row_data in file_data[1:]:
        temporary_list = []
        for element in csv_row_data:
            temporary_list.append(element) 
        # print(temporary_list)
        filter_data =  UkCompany.objects.filter(name=temporary_list[0])
        filter_one_data= filter_data.first()  
        if filter_one_data:        
            # filter_one_data.segment = Segment(id=segment_one_data.id),
            filter_one_data.segment = temporary_list[1]
            filter_one_data.product_type = temporary_list[2],
            filter_one_data.Funding_Status = temporary_list[3],
            filter_one_data.Estimated_Number_of_Employees = temporary_list[4],
            filter_one_data.Total_Funding = temporary_list[5],
            filter_one_data.Estimated_Revenue = temporary_list[6],
            filter_one_data.Last_Funding_Date = temporary_list[7],
            filter_one_data.Last_Funding_Type = temporary_list[8]
            filter_one_data.save()
    return True


def add_and_update(csvfile):
    file_data = list(csv.reader(decode_utf8(csvfile)))
    for csv_row_data in file_data[1:]:
        temporary_list = []
        for element in csv_row_data:
            temporary_list.append(element) 
        # print(temporary_list)
        filter_data =  UkCompany.objects.filter(name=temporary_list[0])
        filter_one_data= filter_data.first()  
        # print(temporary_list[5])  
        if filter_one_data:        
            filter_one_data.segment = temporary_list[1],
            filter_one_data.product_type = temporary_list[2],
            filter_one_data.Funding_Status = temporary_list[3],
            filter_one_data.Estimated_Number_of_Employees = temporary_list[4],
            filter_one_data.Total_Funding = temporary_list[5],
            filter_one_data.Estimated_Revenue = temporary_list[6],
            filter_one_data.Last_Funding_Date = temporary_list[7],
            filter_one_data.Last_Funding_Type = temporary_list[8],
            filter_one_data.save()
        else:
            segment_data = Segment.objects.filter(name=temporary_list[1])
            segment_one_data = segment_data.first()
            UkCompany.objects.create(
                    name = temporary_list[0],
                    segment = Segment(id=segment_one_data.id),
                    product_type = temporary_list[2],
                    funding_status = temporary_list[3],
                    estimated_number_of_employees = temporary_list[4],
                    total_funding = temporary_list[5],
                    estimated_revenue = temporary_list[6],
                    last_funding_date = temporary_list[7],
                    last_funding_type = temporary_list[8]
                )
    return True


#segment data
def add_segment_data(csvfile):
    file_data = list(csv.reader(decode_utf8(csvfile)))
    for csv_row_data in file_data[1:]:
        temporary_list = []
        for element in csv_row_data:
            temporary_list.append(element) 
        # print(temporary_list[1])    
        Segment.objects.create(
            name = temporary_list[1]
        )
    return True


def home(request):
    if request.method == "POST":
        select_value = request.POST.get('name_of_select')
        csvfile =request.FILES['csv_file']
        # print(csvfile)
        file_data = list(csv.reader(decode_utf8(csvfile)))
        if len(file_data[0]) <=8 or len(file_data[0])>9:
            messages.error(request, "File not correct !!!")
            return render(request, 'home.html')

        if select_value == 'add_new_data':
            for csv_row_data in file_data[1:]:
                temporary_list = []
                for element in csv_row_data:
                    temporary_list.append(element) 
                # print(temporary_list)
                segment_data = Segment.objects.filter(name=temporary_list[1])
                segment_one_data = segment_data.first()
                # print(segment_one_data.id)    
                # break            
                UkCompany.objects.create(
                    name = temporary_list[0],
                    segment = Segment(id=segment_one_data.id),
                    product_type = temporary_list[2],
                    funding_status = temporary_list[3],
                    estimated_number_of_employees = temporary_list[4],
                    total_funding = temporary_list[5],
                    estimated_revenue = temporary_list[6],
                    last_funding_date = temporary_list[7],
                    last_funding_type = temporary_list[8]
                )
            messages.success(request, 'Data has been added !!!')
            return render(request, 'home.html') 
        elif select_value == "update_existing_data": 
            update_existing_data(csvfile)
            return render(request, 'home.html')   
        elif select_value == "add_and_update":
            add_and_update(csvfile)
            return render(request, 'home.html')
        elif select_value =='segment':
            add_segment_data(csvfile)
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')





