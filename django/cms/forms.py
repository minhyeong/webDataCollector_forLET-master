from django import forms
from .models import QuestionList


class BasicQuestion(forms.ModelForm):
    class Meta:
        model = QuestionList
        widgets = {
            'birth': forms.TextInput(attrs={'placeholder': '1960-01-01'}),
        }
        fields = ('gendar','birth', 'blood',
                  # 'life_style',
                  'sleep_time_top','sleep_time_bottom',
                  'sport', 'music',
                  'taste',
                  # 'tv_program', 'travel', 'event', 'weak','help','family', 'friend'
        )

class LifeQualityQuestion(forms.ModelForm):
    class Meta:
        model = QuestionList
        fields = ('eat', 'move',
                  'think','breath',
                  'fun','no_pain',)


class LifeProlongingQuestion(forms.ModelForm):
    class Meta:
        model = QuestionList
        fields = ('yk', 'tje',
                  'ke', 'syo',
                  'zk', 'ks',
                  'zt', 'sm',
                  'ot')


class TIPI_JQuestion(forms.ModelForm):
    class Meta:
        model = QuestionList
        fields = ('tipi_j_01','tipi_j_02',
                  'tipi_j_03','tipi_j_04',
                  'tipi_j_05','tipi_j_06',
                  'tipi_j_07','tipi_j_08',
                  'tipi_j_09','tipi_j_10',)


class DASQuestion(forms.ModelForm):
    class Meta:
        model = QuestionList
        fields = ('das_01', 'das_02',
                  'das_03', 'das_04',
                  'das_05', 'das_06',
                  'das_07', 'das_08',
                  'das_09', 'das_10',
                  'das_11', 'das_12',
                  'das_13', 'das_14',
                  'das_15', 'das_16',
                  'das_17', 'das_18',
                  'das_19', 'das_20',
                  'das_21', 'das_22',
                  'das_23', 'das_24',
                  'das_25', 'das_26',
                  'das_27',)

