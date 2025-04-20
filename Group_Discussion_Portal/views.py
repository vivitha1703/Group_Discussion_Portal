import json
from django.shortcuts import render,redirect
from django.http import HttpRequest
from Group_Discussion_Portal.models import Student,Evaluation,SelfIntro,Faculty
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    
from urllib.parse import parse_qs
from django.http import JsonResponse
from datetime import datetime
from .forms import EvaluationForm

def landing_view(request):
    return render(request, 'landing_page.html')

def login_view(request):
    role = request.GET.get('role')
    if request.method == "POST":
        role = request.POST.get("role")
        print(f"Role: {role}")
        if role == "faculty":
            print("Redirecting to faculty_dashboard")  
            return redirect("admin_dashboard")  
        elif role == "student":
            print("Redirecting to user_dashboard") 
            return redirect("user_dashboard")  
        else:
            print("Invalid role, redirecting to login")
            return redirect("login") 
    return render(request, "login.html", {"role": role})

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def user_dashboard(request):
    evaluations = Evaluation.objects.all() 
    print("Hello")
    print(evaluations)
    return render(request, 'user_dashboard.html', {'evaluations': evaluations})
    return render(request, 'user_dashboard.html')

def admin_events(request):
    return render(request,'admin_events.html')

def admin_evaluation(request):
    if request.method == "POST":
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    else:
        form = EvaluationForm()
    
    return render(request, 'admin_evaluation.html', {'form': form}) 

def admin_group(request):
    return render(request,'admin_group.html')

def admin_mock(request):
    return render(request,'admin_mock.html')

def admin_self(request):
    return render(request, 'admin_self.html')

def save_self_intro(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received Data:", data)
            event = SelfIntro.objects.create(
                batch=data['batch'],
                students_per_slot=data['students_per_slot'],
                slot_timing=data['slot_timing'],
                faculties = data.get("faculties", []),
                event_date=data['event_date']
            )
            self_intro = SelfIntro.objects.create(
                batch=batch,
                students_per_slot=students_per_slot,
                slot_timing=slot_timing,
                dates=",".join(dates)
            )
            for faculty in faculties:
                faculty_name = faculty["name"]
                faculty_venues = faculty["venues"]  
                print(f"Faculty: {faculty.faculty_name}, Venue: {faculty.venue}")
                for venue in faculty_venues:
                    Faculty.objects.create(self_intro=self_intro, faculty_name=faculty_name, venue=venue)

            return JsonResponse({"status": "success", "message": "Data saved successfully"})
        except Exception as e:
            print("Error:", e)
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

def user_events(request):
    return render(request, 'user_events.html')

def user_booking(request):
    return render(request, 'user_booking.html')

def get_students_count(request):
    batch = request.GET.get('batch', '').strip()  
    if batch:
        try:
            student_count = Student.objects.filter(batch__iexact=batch).count() 
            return JsonResponse({'total_students': student_count})
        except Exception as e:
            print(f"Error: {e}")  
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Batch not provided'}, status=400)

@csrf_exempt
def event_selfintro(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            print("Received payload:", payload)

            batch = payload.get("batch")
            students_per_slot = payload.get("students_per_slot")
            slot_timing = payload.get("slot_timing")
            faculties = payload.get("faculties")
            dates = payload.get("dates")

            if not all([batch, students_per_slot, slot_timing, faculties, dates]):
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            faculty_names = ", ".join([faculty['name'] for faculty in faculties])
            faculty_venues = ", ".join([faculty['venue'] for faculty in faculties])
            event_dates = ", ".join(dates)

            EventSelfIntro.objects.create(
                batch=batch,
                students_per_slot=students_per_slot,
                slot_timing=slot_timing,
                faculty_name=faculty_names,
                faculty_venue=faculty_venues,
                event_date=event_dates,  
            )

            return JsonResponse({'status': 'success'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def slot_page(request):
    events = EventSelfIntro.objects.all()  
    print(events)
    return render(request, 'user_bookig.html', {'events': events})

    