from django import forms
from .models import Video

class UploadFileForm(forms.Form):
  file = forms.FileField()
  title = forms.CharField(max_length=80)
  description =  forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), max_length=1000)

  class Meta:
    model = Video
    fields = ("file", "title", "description")

  def save(self, commit=True):
    video = Video(
      file = self.cleaned_data['file'],
      title = self.cleaned_data['title'],
      description = self.cleaned_data['description']
    )
    if commit:
      video.save()
    return video
