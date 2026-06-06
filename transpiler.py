# كود المصنع (Transpiler) لتحويل النصوص إلى لغة Brainfuck
def text_to_brainfuck(text):
    bf_code = ""
    current_val = 0
    
    for char in text:
        target_val = ord(char) # تحويل الحرف إلى قيمته الرقمية (ASCII)
        diff = target_val - current_val
        
        if diff > 0:
            bf_code += "+" * diff
        elif diff < 0:
            bf_code += "-" * abs(diff)
            
        bf_code += "." # أمر الطباعة في Brainfuck
        current_val = target_val
        
    return bf_code

# النص الذي نريد من الـ AI التعجيزي أن يطبعه كبداية
ai_message = "AI Offline: Hello!"

print("--- جاري توليد كود Brainfuck للمشروع... ---")
brainfuck_result = text_to_brainfuck(ai_message)

# حفظ كود البراين فاك الناتج في ملف نصي مستقل
with open("ai_brainfuck.bf", "w") as f:
    f.write(brainfuck_result)

print("\nتم بنجاح! تم إنشاء ملف يحتوي على الطلاسم البرمجية باسم: ai_brainfuck.bf")