from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Client, Professional, ClientAddress, ProfessionalAddress, Service, Qualification, Appointment, AppointmentLink, Availability
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

# Adress
class AddressInline(admin.StackedInline):
    fields = (
        'street',
        'city',
        'postal_code',
        'country',
        'latitude',
        'longitude'
        )
    can_delete = True
    extra = 1

class ClientAddressInline(AddressInline):
    model = ClientAddress

class ProfessionalAddressInline(AddressInline):
    model = ProfessionalAddress

# User
class CustomUserAdmin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'role',
        'is_staff',
        'is_active'
        )
    list_filter = (
        'role',
        'is_staff',
        'is_active'
        )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'phone_number'
            )}),
        ('Permissions', {'fields': (
            'role',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
            )}),
        ('Important dates', {'fields': (
            'last_login',
            'created_at',
            'updated_at'
            )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'role',
                'is_staff',
                'is_active'
                )},
        ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'role')
    ordering = ('email',)
    readonly_fields = ('created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('password1'):
            obj.set_password(form.cleaned_data['password1'])
        super().save_model(request, obj, form, change)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password1']:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Les deux mots de passe ne correspondent pas."
                )
        if password2:
            try:
                validate_password(password2)
            except ValidationError as e:
                raise forms.ValidationError(e)

        return password2

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'role')

class UserInLine(admin.StackedInline):
    model = User
    fields = (
        'email',
        'password',
        'is_active',
        'is_staff'
    )
    extra = 1

    def save(self, commit=True):
        client = super().save(commit=False)
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if commit:
            user, created = User.objects.get_or_create(email=email)
            if created:
                user.set_password(password)
                user.save()

            client.user = user
            client.save()

        return client

# Client
class ClientAdminForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=True
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        required=True
    )

    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].choices = [('CLIENT', 'Client')]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Les deux mots de passe ne correspondent pas."
                )
        if password2:
            try:
                validate_password(password2)
            except ValidationError as e:
                raise forms.ValidationError(e)

        return password2

    def save(self, commit=True):
        client = super().save(commit=False)
        if self.cleaned_data['password1']:
            client.set_password(self.cleaned_data["password1"])
        if commit:
            client.save()
        return client

class ClientAdmin(admin.ModelAdmin):
    form = ClientAdminForm
    inlines = [ClientAddressInline]

    list_display = (
        'email',
        'first_name',
        'last_name',
        'phone_number',
        'role',
        'is_helper',
        'is_active'
        )
    list_filter = ('is_helper', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    fieldsets = (
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'phone_number',
            )}),
        ('Account info', {'fields': (
            'email',
            'role',
            'password1',
            'password2'
        )}),
        ('Client info', {'fields': ('is_helper',)}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'phone_number',
                'is_helper',
                'is_active',
                'role'
                )}
        ),
    )

    def save_model(self, request, obj, form, change):
        if not change:  # Si c'est un nouvel objet
            obj.set_password(form.cleaned_data['password1'])  # Utilise l'objet Professional directement
        else:  # Si on modifie un objet existant
            if form.cleaned_data.get('password1'):  # Si un nouveau mot de passe est défini
                obj.set_password(form.cleaned_data['password1'])

        # Mets à jour d'autres champs
        obj.email = form.cleaned_data['email']
        obj.first_name = form.cleaned_data['first_name']
        obj.last_name = form.cleaned_data['last_name']
        obj.is_active = form.cleaned_data['is_active']

        obj.save()  # Sauvegarde l'objet Professional directement
        super().save_model(request, obj, form, change)

# Professional
class ProfessionalAdminForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=True
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        required=True
    )

    class Meta:
        model = Professional
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].choices = [('PROFESSIONAL', 'Professional')]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Les deux mots de passe ne correspondent pas."
                )
        if password2:
            try:
                validate_password(password2)
            except ValidationError as e:
                raise forms.ValidationError(e)

        return password2

    def save(self, commit=True):
        professional = super().save(commit=False)
        if self.cleaned_data['password1']:
            professional.set_password(self.cleaned_data["password1"])
        if commit:
            professional.save()
        return professional

class ProfessionalAdmin(admin.ModelAdmin):
    form = ProfessionalAdminForm

    inlines = [ProfessionalAddressInline]
    list_display = (
        'email',
        'first_name',
        'last_name',
        'phone_number',
        'profession',
        'role',
        'is_mobile',
        'intervention_radius',
        'is_active'
        )
    list_filter = ('profession', 'is_mobile', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'profession')
    fieldsets = (
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'phone_number'
            )}),
        ('Account info', {'fields': (
            'email',
            'role',
            'password1',
            'password2'
        )}),
        ('Professional info', {'fields': (
            'profession',
            'is_mobile',
            'intervention_radius'
            )}),
        ('Permissions', {'fields': (
            'is_active',
            )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'phone_number',
                'profession',
                'is_mobile',
                'intervention_radius',
                'is_active',
                'role'
                )}
        ),
    )

    def save_model(self, request, obj, form, change):
        if not change:  # Si c'est un nouvel objet
            obj.set_password(form.cleaned_data['password1'])  # Utilise l'objet Professional directement
        else:  # Si on modifie un objet existant
            if form.cleaned_data.get('password1'):  # Si un nouveau mot de passe est défini
                obj.set_password(form.cleaned_data['password1'])

        # Mets à jour d'autres champs
        obj.email = form.cleaned_data['email']
        obj.first_name = form.cleaned_data['first_name']
        obj.last_name = form.cleaned_data['last_name']
        obj.is_active = form.cleaned_data['is_active']

        obj.save()  # Sauvegarde l'objet Professional directement
        super().save_model(request, obj, form, change)


class QualificationInline(admin.TabularInline):
    model = Qualification
    extra = 1

class ServiceInline(admin.TabularInline):
    model = Service.professionals.through
    extra = 1

class AppointmentLinkInline(admin.TabularInline):
    model = AppointmentLink
    extra = 1

class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 1

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = (
        'degree',
        'institution',
        'year_of_obtention',
        'is_verified',
        'professional'
        )
    list_filter = (
        'is_verified',
        'year_of_obtention'
        )
    search_fields = (
        'degree',
        'institution',
        'professional__first_name',
        'professional__last_name'
        )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'service_name',
        'service_description',
        'service_category',
        'custom_service_category'
        )
    list_filter = (
        'service_category',
        )
    search_fields = (
        'service_name',
        'service_description'
        )
    filter_horizontal = [
        'professionals'
    ]

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'appntmnt_datetime_start',
        'appntmnt_status'
        )
    list_filter = (
        'appntmnt_status',
        'appntmnt_datetime_start'
        )
    search_fields = (
        'appntmnt_link__client__first_name',
        'appntmnt_link__client__last_name',
        'appntmnt_link__professional__first_name',
        'appntmnt_link__professional__last_name'
        )


admin.site.register(Client, ClientAdmin)
admin.site.register(Professional, ProfessionalAdmin)
admin.site.register(User, CustomUserAdmin)
