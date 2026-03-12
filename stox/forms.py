from django import forms

class PriceCheckForm(forms.Form):
    url = forms.URLField()
    size = forms.CharField()

    def stockxurl(self):
        if "stockx" not in (self.url):
            raise forms.ValidationError("The url must be from the StockX site.")
        
        return self.url
    
    def size_validation(self):
        if self.size > 52.5 or self.size < 35.5:
            raise forms.ValidationError("There no such size in the StockX site. Try one smaller or bigger.")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)