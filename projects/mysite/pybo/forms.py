from pybo.models import Question, Answer
from django import forms



class QuestionForm(forms.ModelForm):
    class Meta:
        model= Question #사용할 모델
        fields= ['subject', 'content']
        #QuestionForm에서 사용할 Question 모델의 속성,
#         widgets={
#             'subject': forms.TextInput(attrs={'class':'form-control'}),
#             'content': forms.Textarea(attrs={'class':'form-control','rows':10}),
#         }
        labels={
            'subject': '제목',
            'content': '내용',
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model= Answer #사용할 모델
        fields= ['content']
        labels={
            'content': '답변내용',
        }