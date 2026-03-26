from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Lead, HeroBanner, Product, Project
from django.shortcuts import render, redirect


def normalize_phone(raw: str) -> str:
    phone = raw.strip()
    for ch in (" ", "(", ")", "-", "\t"):
        phone = phone.replace(ch, "")
    if phone.startswith("8") and len(phone) == 11:
        phone = "+7" + phone[1:]
    elif phone.startswith("7") and len(phone) == 11:
        phone = "+7" + phone[1:]
    return phone


def send_lead_email(lead: Lead):
    subject = "Новая заявка с сайта WarmWindows"
    message = (
        f"Имя: {lead.name}\n"
        f"Телефон: {lead.phone}\n"
        f"Источник: {lead.source}\n"
        f"Комментарий: {lead.comment}\n"
        f"Создано: {lead.created_at}"
    )
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_EMAIL],
        fail_silently=True,
    )


def index(request):
    success_hero = False
    success_contacts = False

    if request.method == "POST":
        honeypot = request.POST.get("email_confirm", "")
        if honeypot:
            return render(request, "landing/index.html", {})

        if "name" in request.POST and "phone" in request.POST:
            name = request.POST.get("name", "").strip()
            phone_raw = request.POST.get("phone", "")
            obj_type = request.POST.get("type", "").strip()
            phone = normalize_phone(phone_raw)
            if name and phone:
                lead = Lead.objects.create(
                    name=name,
                    phone=phone,
                    source="hero",
                    comment=f"Тип объекта: {obj_type}",
                )
                send_lead_email(lead)
                return redirect('thanks')

        elif "contact_name" in request.POST and "contact_phone" in request.POST:
            name = request.POST.get("contact_name", "").strip()
            phone_raw = request.POST.get("contact_phone", "")
            message = request.POST.get("contact_message", "").strip()
            phone = normalize_phone(phone_raw)
            if name and phone:
                lead = Lead.objects.create(
                    name=name,
                    phone=phone,
                    source="contacts",
                    comment=message,
                )
                send_lead_email(lead)
                return redirect('thanks')

    hero = HeroBanner.objects.filter(is_active=True).first()
    context = {
        "success_hero": success_hero,
        "success_contacts": success_contacts,
        "hero": hero,
    }
    return render(request, "landing/index.html", context)


def products(request):
    products = Product.objects.all()
    return render(request, "landing/products.html", {"products": products})


def technology(request):
    return render(request, "landing/technology.html")


def projects(request):
    projects = Project.objects.all()
    return render(request, "landing/projects.html", {"projects": projects})


def reviews(request):
    return render(request, "landing/reviews.html")


def faq(request):
    return render(request, "landing/faq.html")


def contacts(request):
    success_contacts = False

    if request.method == "POST":
        honeypot = request.POST.get("email_confirm", "")
        if honeypot:
            return render(request, "landing/contacts.html", {})

        name = request.POST.get("contact_name", "").strip()
        phone_raw = request.POST.get("contact_phone", "")
        message = request.POST.get("contact_message", "").strip()
        phone = normalize_phone(phone_raw)

        if name and phone:
            lead = Lead.objects.create(
                name=name,
                phone=phone,
                source="contacts",
                comment=message,
            )
            send_lead_email(lead)
            return redirect('thanks')

    return render(request, "landing/contacts.html", {"success_contacts": success_contacts})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def privacy(request):
    return render(request, "landing/privacy.html")

def thanks(request):
    return render(request, "landing/thanks.html")