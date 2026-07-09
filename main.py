import os
import sys
import time
import urllib.request
import urllib.parse

# تجهيز وتأمين محرك الواجهات بالهاتف
try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.textinput import TextInput
    from kivy.uix.button import Button
    from kivy.core.window import Window
except ImportError:
    import os
    os.system('pip install kivy')
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.textinput import TextInput
    from kivy.uix.button import Button

# عقل المنظومة والذاكرة المحلية
def ask_global_ai(question_text):
    q = question_text.strip()
    if not q:
        return "Please type a question first!"
        
    # الذاكرة الفورية المستقرة محلياً
    if "من هو الله" in q or "من الله" in q:
        return "الله هو الإله الواحد الأحد، الخالق البارئ المصور، ليس كمثله شيء وهو السميع البصير."
    elif "بشر" in q or "ادم" in q or "آدم" in q:
        return "أبو البشر هو سيدنا آدم عليه السلام، خلقه الله سبحانه وتعالى بيده وعلمه الأسماء كلها."
    elif "زاو" in q or "قائم" in q or "angle" in q:
        return "قياس الزاوية القائمة هو 90 درجة دائماً وثابت هندسياً في الرياضيات."
    elif "سكان" in q or "عراق" in q:
        return "عدد سكان جمهورية العراق يبلغ حوالي 46 مليون نسمة حسب أحدث التقديرات الرسمية."
    elif "رئيس" in q or "وزراء" in q or "سودان" in q:
        return "رئيس مجلس الوزراء الحالي لجمهورية العراق هو السيد محمد شياع السوداني."

    # خط الاتصال العالمي عبر الإنترنت
    prompt_config = f"أجب باختصار شديد جداً ومباشر باللغة العربية الفصحى: {q}"
    url = f"https://text.pollinations.ai/{urllib.parse.quote(prompt_config)}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=7) as response:
            reply = response.read().decode('utf-8').strip()
            if reply:
                return reply.replace("```", "").strip()
    except:
        pass
    return "تم استلام سؤالك! يرجى التحقق من اتصال الإنترنت لجلب الإجابة العالمية."

# بناء نافذة التطبيق المستقل
class HeroAssistantApp(App):
    def build(self):
        self.title = "HERO ASSISTANT"
        layout = BoxLayout(orientation='vertical', padding=25, spacing=20)
        
        # 1. الشعار الرئيسي للبرنامج
        self.title_label = Label(
            text="📱 HERO ASSISTANT SYSTEM", 
            font_size='24sp', 
            bold=True,
            size_hint_y=None, 
            height=60
        )
        layout.add_widget(self.title_label)
        
        # 2. صندوق الكتابة الذكي
        self.input_box = TextInput(
            hint_text="Type your question here...",
            font_size='18sp',
            multiline=False,
            size_hint_y=None,
            height=60,
            halign='center'
        )
        layout.add_widget(self.input_box)
        
        # 3. زر الإرسال الأحمر الأنيق (رفيقي)
        self.submit_btn = Button(
            text="ASK RAFIQI NOW ✨",
            font_size='20sp',
            bold=True,
            background_color=(0.8, 0.1, 0.1, 1),
            size_hint_y=None,
            height=65
        )
        self.submit_btn.bind(on_press=self.generate_answer)
        layout.add_widget(self.submit_btn)
        
        # 4. شاشة عرض الإجابات الحية
        self.output_label = Label(
            text="System is ready. Waiting for your question...",
            font_size='18sp',
            text_size=(Window.width - 50, None),
            halign='center',
            valign='middle'
        )
        layout.add_widget(self.output_label)
        
        return layout

    def generate_answer(self, instance):
        self.output_label.text = "⏳ Processing your question..."
        user_q = self.input_box.text
        
        # معالجة السؤال وعرض النتيجة فوراً
        reply = ask_global_ai(user_q)
        self.output_label.text = reply
        self.input_box.text = ""

if __name__ == "__main__":
    HeroAssistantApp().run()
