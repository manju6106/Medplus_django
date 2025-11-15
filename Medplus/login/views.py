from django.shortcuts import render,redirect
from login.models import Register
from login.models import Login
# from .models import medicine
from django.http import HttpResponse
from .models import Medicine, Bill
from django.db.models import Sum
from datetime import date
from django.http import HttpResponseRedirect
from django.urls import reverse


def home1(req):
     return render(req,'home.html')
def register(request):
    if request.method=='POST':
        cid=request.POST.get('cid')
        cn=request.POST.get('cname')
        g=request.POST.get('gender')
        dob=request.POST.get('DOB')
        pn=request.POST.get('phno')
        email=request.POST.get('email')
        state=request.POST.get('state')
        city=request.POST.get('city')
        password = request.POST.get('password')
        Register.objects.create(cid=cid,cname=cn,gender=g,DOB=dob,phno=pn,email=email,state=state,city=city,password=password)
    return render(request, 'register.html')


# def login(request):
#     if request.method == 'POST':
#         uname = request.POST.get('uname')
#         p = request.POST.get('p')
#         if uname == 'Manjula' and p == 'manju@123':
#             return render(request, 'operator.html')
#         elif Register.objects.filter(email=uname, password=p).exists():
#             return render(request, 'operator.html')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
#     return render(request, 'login.html')
#
# from django.shortcuts import render, redirect
# from .models import Register, Operator
#
# def login(request):
#     if request.method == 'POST':
#         uname = request.POST.get('uname')
#         pwd = request.POST.get('p')
#
#         # Operator login
#         if Operator.objects.filter(uname=uname, pwd=pwd).exists():
#             operator = Operator.objects.get(uname=uname, pwd=pwd)
#             request.session['user_type'] = 'operator'
#             request.session['operator_id'] = operator.opid
#             return redirect('operator')  # operator full access page
#
#         # Customer login
#         elif Register.objects.filter(email=uname, password=pwd).exists():
#             customer = Register.objects.get(email=uname, password=pwd)
#             request.session['user_type'] = 'customer'
#             request.session['customer_id'] = customer.cid
#             return redirect('search')  # customers can only search/enter quantity
#
#         else:
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
#
#     return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('p')

        # Operator login
        operator = Operator.objects.filter(uname=uname, pwd=pwd).first()
        if operator:
            request.session['user_type'] = 'operator'
            request.session['operator_id'] = operator.opid
            return redirect('operator')

        # Customer login
        customer = Register.objects.filter(email=uname, password=pwd).first()
        if customer:
            request.session['user_type'] = 'customer'
            request.session['customer_id'] = customer.cid
            return redirect('search')

        # Invalid login
        return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')



def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def admin_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        p = request.POST.get('p')
        if uname == 'Manjula' and p == 'manju@1234':
            return redirect('admin_page')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid username or password'})
    return render(request, 'admin_login.html')


def admin_page(request):
    return render(request, 'admin.html')




def operator(request):
    return render(request,'operator.html')
##====================================================================================

# cart = []
#
# def add(request):
#     if request.method == "POST":
#         Medicine.objects.create(
#             mid=request.POST['mid'],
#             name=request.POST['name'],
#             cost=request.POST['cost'],
#             expiry=request.POST['expiry'],
#             usage=request.POST['usage'],
#             dosage=request.POST['dosage'],
#             image=request.FILES['image']
#         )
#         return HttpResponseRedirect(reverse("add"))
#     return render(request, 'add.html')
#
#
# def remove(request):
#     if request.method == "POST":
#         mid = request.POST['mid']
#         Medicine.objects.filter(mid=mid).delete()
#         return HttpResponse("Medicine Removed")
#     return render(request, 'remove.html')
#
#
# def search(request):
#     med = None
#     error_msg = ""
#
#     if request.method == "POST":
#         name = request.POST['name']
#         med = Medicine.objects.filter(name=name).first()
#
#         if not med:
#             error_msg = f"Medicine '{name}' not found. Please add it."
#
#     return render(request, 'search.html', {'med': med, 'error_msg': error_msg})


def search(request):
    # Only logged-in users can access
    if request.session.get('user_type') not in ['operator', 'customer']:
        return redirect('login')

    med = None
    error_msg = ""
    can_bill = request.session.get('user_type') == 'operator'  # Only operators can bill

    if request.method == "POST":
        name = request.POST['name']
        med = Medicine.objects.filter(name=name).first()

        if not med:
            error_msg = f"Medicine '{name}' not found. Please add it."

    return render(request, 'search.html', {
        'med': med,
        'error_msg': error_msg,
        'can_bill': can_bill
    })

#
# def billing(request):
#     total = None
#     if request.method == "POST":
#         mid = request.POST['mid']
#         qty = int(request.POST['qty'])
#
#         med = Medicine.objects.get(mid=mid)
#         total = med.cost * qty
#         Bill.objects.create(amount=total)
#     return render(request, 'billing.html', {'total': total})
#
# def amount(request):
#     bills = Bill.objects.all().order_by('-date')  # latest first
#     total = Bill.objects.aggregate(Sum('amount'))['amount__sum'] or 0
#
#     return render(request, 'amount.html', {
#         'bills': bills,
#         'total': total
#     })

#
# def medicines_list(request):
#     meds = Medicine.objects.all()
#     return render(request, 'medlist.html', {"meds": meds})

#---------------------------------------------------------------------------------------------------------
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Medicine, Bill, Operator
from django.db.models import Sum

# -------------------- Operator-only views --------------------

def add(request):
    if request.session.get('user_type') != 'operator':
        return redirect('login')

    if request.method == "POST":
        Medicine.objects.create(
            mid=request.POST['mid'],
            name=request.POST['name'],
            cost=request.POST['cost'],
            expiry=request.POST['expiry'],
            usage=request.POST['usage'],
            dosage=request.POST['dosage'],
            image=request.FILES['image']
        )
        return HttpResponseRedirect(reverse("add"))

    return render(request, 'add.html')


def remove(request):
    if request.session.get('user_type') != 'operator':
        return redirect('login')

    if request.method == "POST":
        mid = request.POST['mid']
        Medicine.objects.filter(mid=mid).delete()
        return HttpResponse("Medicine Removed")

    return render(request, 'remove.html')


def billing(request):
    if request.session.get('user_type') != 'operator':
        return redirect('login')

    total = None
    if request.method == "POST":
        mid = request.POST['mid']
        qty = int(request.POST['qty'])

        med = Medicine.objects.get(mid=mid)
        total = med.cost * qty

        operator_id = request.session.get('operator_id')
        operator = Operator.objects.get(opid=operator_id)

        Bill.objects.create(operator=operator, mname=med.name, amount=total)

    return render(request, 'billing.html', {'total': total})


def amount(request):
    if request.session.get('user_type') != 'operator':
        return redirect('login')

    bills = Bill.objects.all().order_by('-date')  # latest first
    total = Bill.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'amount.html', {
        'bills': bills,
        'total': total
    })


def medicines_list(request):
    if request.session.get('user_type') != 'operator':
        return redirect('login')

    meds = Medicine.objects.all()
    return render(request, 'medlist.html', {"meds": meds})
#--------------------------------------------------------------------------------------------------------------

def logout(request):
    if request.method == "POST":
        if request.POST.get("action") == "Logout":
            request.session.flush()
            return redirect('welcome')
        elif request.POST.get("action") == "Cancel":
            return redirect('operator')
    return render(request, 'logout.html')


def welcome(request):
    return render(request, 'welcome.html')


def totalsales(request):
    return render(request, 'totalsales.html')

# def datewise(request):
#     return render(request, 'datewise.html')
from django.db.models import Sum
from datetime import datetime

def datewise(request):
    bills = None
    total = 0

    if request.method == "POST":
        entered_date = request.POST['cid']   # example: 2025-01-10

        try:
            # convert string → date
            date_object = datetime.strptime(entered_date, "%Y-%m-%d").date()

            # filter bills
            bills = Bill.objects.filter(date=date_object)

            total = bills.aggregate(Sum('amount'))['amount__sum'] or 0

        except ValueError:
            bills = []
            total = 0

    return render(request, 'datewise.html', {
        'bills': bills,
        'total': total
    })


# def operatorwise(request):
#     return render(request, 'operatorwise.html')
from django.shortcuts import render
from .models import Bill, Operator

def operatorwise(request):
    bills = None
    msg = None

    if request.method == "POST":
        opid = request.POST.get("opid")
        bdate = request.POST.get("bdate")

        try:
            operator = Operator.objects.get(opid=opid)
        except Operator.DoesNotExist:
            msg = f"No operator found with ID {opid}"
            return render(request, 'operatorwise.html', {'msg': msg})

        bills = Bill.objects.filter(operator=operator, date=bdate)

        if not bills.exists():
            msg = f"No billing records for Operator ID {opid} on {bdate}"

    return render(request, 'operatorwise.html', {'bills': bills, 'msg': msg})

#
# def betweendates(request):
#     return render(request, 'betweendates.html')

def betweendates(request):
    if request.method == "POST":
        sdate = request.POST.get("sdate")
        edate = request.POST.get("edate")

        # filter between dates
        bills = Bill.objects.filter(date__range=[sdate, edate]).order_by('date')

        return render(request, 'betweendates.html', {
            'bills': bills,
            'sdate': sdate,
            'edate': edate
        })

    return render(request, 'betweendates.html')


#======================================================================================================================

# def addoperator(request):
#     if request.method == 'POST':
#         a = request.POST.get('cid')
#         b = request.POST.get('cname')
#         c = request.POST.get('password')
#         d = request.POST.get('gender')
#         e = request.POST.get('phno')
#         operator.objects.create(opid=a, uname=b, pwd=c, g=d, phno=e)
#     return render(request, 'addoperator.html')
from .models import Operator

# def addoperator(request):
#     if request.method == 'POST':
#         a = request.POST.get('cid')
#         b = request.POST.get('cname')
#         c = request.POST.get('password')
#         d = request.POST.get('gender')
#         e = request.POST.get('phno')
#
#         Operator.objects.create(opid=a, uname=b, pwd=c, g=d, phno=e)
#
#     return render(request, 'addoperator.html')
#
#
# def deleteoperator(request):
#     return render(request, 'deleteoperator.html')

#=================================================================================================

def addoperator(request):
    if request.session.get('user_type') != 'operator':
        return redirect('login')

    if request.method == 'POST':
        a = request.POST.get('cid')
        b = request.POST.get('cname')
        c = request.POST.get('password')
        d = request.POST.get('gender')
        e = request.POST.get('phno')

        Operator.objects.create(opid=a, uname=b, pwd=c, g=d, phno=e)

    return render(request, 'addoperator.html')


from django.contrib import messages
from .models import Operator

def deleteoperator(request):
    if request.session.get('user_type') != 'operator':
        return redirect('login')

    if request.method == "POST":
        cid = request.POST.get("cid")

        try:
            op = Operator.objects.get(opid=cid)   # ← matches your DB column
            op.delete()
            messages.success(request, f"Operator with ID {cid} deleted successfully!")
        except Operator.DoesNotExist:
            messages.error(request, f"No operator found with ID {cid}.")

        return redirect("deleteoperator")

    return render(request, 'deleteoperator.html')


#============================================================================================================

def log(request):
    if request.method == "POST":
        if request.POST.get("action") == "Logout":
            request.session.flush()
            return redirect('welcome1')
        elif request.POST.get("action") == "Cancel":
            return redirect('addoperator')
    return render(request, 'log.html')


def welcome1(request):
    return render(request, 'welcome1.html')



