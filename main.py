import sqlite3
import arabic_reshaper
from bidi.algorithm import get_display
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

def fix_arabic(text):
    if not text:
        return ""
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

class MedicalRxApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # عنوان التطبيق
        title = MDLabel(text=fix_arabic("عيادة د. عبدالله محمود تهامي"), halign="center", font_style="H5")
        
        # بيانات المريض
        self.patient_name = MDTextField(hint_text=fix_arabic("اسم المريض"), text_size="16sp")
        self.patient_age = MDTextField(hint_text=fix_arabic("السن"), input_filter="int")
        
        # أزرار التحكم
        btn_add = MDRaisedButton(text=fix_arabic("إضافة دواء"), pos_hint={"center_x": 0.5})
        btn_print = MDRaisedButton(text=fix_arabic("طباعة الروشتة PDF"), md_bg_color=(0, 0.5, 0, 1), pos_hint={"center_x": 0.5})
        
        layout.add_widget(title)
        layout.add_widget(self.patient_name)
        layout.add_widget(self.patient_age)
        layout.add_widget(btn_add)
        layout.add_widget(btn_print)
        
        return layout

if __name__ == "__main__":
    MedicalRxApp().run()
