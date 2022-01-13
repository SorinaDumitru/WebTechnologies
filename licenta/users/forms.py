from django import forms
from .models import NewUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Layout, ButtonHolder, Submit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'test@example.com'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'John'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Winson'})
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '0712345678'}))
    cnp = forms.CharField(
        label='CNP',
        widget=forms.TextInput(attrs={'placeholder': '123456789101'})
    )
    birthday = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Street New Avenue 63'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label='Password (again)',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password validation'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div (
                Div (
                    Div (
                        Div (
                            HTML("""
                            <div class="u-container-style u-group u-opacity u-opacity-30 u-radius-30 u-shape-round u-white u-group-3">
                                <div class="u-container-layout form-content-title" >
                                    <h2 class="u-subtitle u-text u-text-default u-text-3">Join us</h2>
                                </div>
                            </div>"""),
                            Div (
                                Div (
                                    Field('email', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-name u-form-group'
                                ),
                                Div (
                                    Field('first_name', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-group u-form-partition-factor-2 u-form-phone u-form-group-3'
                                ),
                                Div (
                                    Field('last_name', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-group u-form-partition-factor-2 u-form-phone u-form-group-3'
                                ),
                                Div (
                                    Field('phone_number', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-group u-form-partition-factor-2 u-form-phone u-form-group-3'
                                ),
                                Div (
                                    Field('cnp', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-group u-form-partition-factor-2 u-form-phone u-form-group-3'
                                ),
                                Div (
                                    Field('birthday', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-group u-form-partition-factor-2 u-form-phone u-form-group-3'
                                ),
                                Div (
                                    Field('address', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-group u-form-partition-factor-2 u-form-phone u-form-group-3'
                                ),
                                Div (
                                    Field('password1', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-group u-form-partition-factor-2 u-form-phone u-form-group-3'
                                ),
                                Div (
                                    Field('password2', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-group u-form-partition-factor-2 u-form-phone u-form-group-3'
                                ),
                                Div (
                                    ButtonHolder(
                                        Submit('submit', 'Create account', css_class='u-active-palette-2-dark-1 u-border-none u-btn u-btn-round u-btn-submit u-button-style u-custom-font u-heading-font u-hover-palette-2-dark-1 u-palette-2-base u-radius-50 u-text-hover-white u-btn-1')
                                    ),
                                    css_class='u-align-center u-form-group u-form-submit'
                                ),
                                HTML("""
                                <div class="u-container-layout u-container-layout-6">
                                    <p class="u-align-center u-custom-font u-heading-font u-text u-text-4">
                                        <a class="u-btn u-button-link u-button-style u-custom-font u-heading-font u-none u-text-black u-text-hover-palette-2-base u-btn-3"
                                            href="{% url 'dashboard-homepage' %}">You already have an account?<br>Click here to login!
                                        </a>
                                    </p>
                                </div>"""),
                                css_class='u-clearfix u-form-spacing-13 u-form-vertical u-inner-form form-content'
                            ),
                            css_class='u-form u-form-1'
                        ),
                        css_class='u-container-layout u-valign-top form-content-bottom'
                    ),
                    css_class='u-container-style u-group u-shape-rectangle u-group-2',
                ),
                css_class='u-container-layout u-container-layout-3'
            ),
        )

    class Meta:
        model = NewUser
        fields = ['email', 'first_name', 'last_name', 'cnp', 'address', 'birthday', 'phone_number', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'test@example.com'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = '/'
        self.form_method = 'post'
        self.helper.layout = Layout(
            Div (
                Div (
                    Div (
                        Div (
                            HTML("""
                            <div class="u-container-style u-group u-opacity u-opacity-30 u-radius-30 u-shape-round u-white u-group-3">
                                <div class="u-container-layout form-content-title" >
                                    <h2 class="u-subtitle u-text u-text-default u-text-3">Login</h2>
                                </div>
                            </div>"""),
                            Div (
                                Div (
                                    Field('email', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-name u-form-group'
                                ),
                                Div (
                                    Field('password', css_class="u-border-no-bottom u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-radius-50"),
                                    css_class='form-content-pos u-form-name u-form-group'
                                ),
                                Div (
                                    ButtonHolder(
                                        Submit('submit', 'Login', css_class='u-active-palette-2-dark-1 u-border-none u-btn u-btn-round u-btn-submit u-button-style u-custom-font u-heading-font u-hover-palette-2-dark-1 u-palette-2-base u-radius-50 u-text-hover-white u-btn-1')
                                    ),
                                    css_class='u-align-center u-form-group u-form-submit'
                                ),
                                HTML("""
                                <div class="u-container-layout u-container-layout-6">
                                    <p class="u-align-center u-custom-font u-heading-font u-text u-text-4">
                                        <a class="u-btn u-button-link u-button-style u-custom-font u-heading-font u-none u-text-black u-text-hover-palette-2-base u-btn-3"
                                            href="{% url 'dashboard-register' %}">You don't have an account?&nbsp;<br>Click here to sign up!
                                        </a>
                                    </p>
                                </div>"""),
                                css_class='u-clearfix u-form-spacing-13 u-form-vertical u-inner-form form-content'
                            ),
                            css_class='u-form u-form-2'
                        ),
                        css_class='u-container-layout u-valign-top form-content-bottom'
                    ),
                    css_class='u-container-style u-group u-shape-rectangle u-group-2',
                ),
                css_class='u-container-layout u-container-layout-3'
            ),
        )

    class Meta:
        model = NewUser
        fields = ['email', 'password']
