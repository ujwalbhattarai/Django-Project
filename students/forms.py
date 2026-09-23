from django import forms

from .models import Student


class StudentForm(forms.ModelForm):

    name = forms.CharField(
        label="Student Name",
        help_text="Enter the student's full name.",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter student name",
                "class": "student-input"
            }
        )
    )

    age = forms.IntegerField(
        label="Student Age",
        help_text="Age must be between 5 and 100.",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter student age",
                "class": "student-input"
            }
        )
    )

    class Meta:
        model = Student
        fields = ["name", "age"]

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 5:
            raise forms.ValidationError(
                "Student age must be at least 5."
            )

        if age > 100:
            raise forms.ValidationError(
                "Student age cannot be greater than 100."
            )

        return age