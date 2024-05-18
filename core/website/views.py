from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from website.forms import ContactForm, NewsletterForm
from django.http.response import HttpResponseRedirect

class IndexView(TemplateView):
    template_name = "website/index.html"


class AboutView(TemplateView):
    template_name = "website/about.html"


# class ContactView(View):
#     def get(self, request):
#         form = ContactForm()
#         return render(request, "website/contact.html", {"form": form})

#     def post(self, request):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(
#                 request, messages.SUCCESS, "Your ticket has been successfully sent"
#             )
#         else:
#             messages.add_message(request, messages.ERROR, "Your ticket was not sent")
#         return render(request, "website/contact.html", {"form": form})

class ContactView(FormView):
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = '/contact/'  

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request, messages.SUCCESS, "Your ticket has been successfully sent"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Your ticket was not sent")
        return super().form_invalid(form)

class NewsletterView(View):
    def post(self, request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
