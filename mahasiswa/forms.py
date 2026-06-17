from django import forms



from .models import Buku







class BukuForm(forms.ModelForm):



    class Meta:



        model = Buku



        fields = ['judul', 'penulis', 'penerbit', 'tahun_terbit']



        



        # Opsional: Memberikan style bawaan agar inputan rapi



        widgets = {



            'judul': forms.TextInput(attrs={'style': 'width: 100%; padding: 5px;'}),



            'penulis': forms.TextInput(attrs={'style': 'width: 100%; padding: 5px;'}),



            'penerbit': forms.TextInput(attrs={'style': 'width: 100%; padding: 5px;'}),



            'tahun_terbit': forms.NumberInput(attrs={'style': 'width: 100%; padding: 5px;'}),



        }