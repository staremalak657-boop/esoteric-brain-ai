# مشغل ومحاكي لغة Brainfuck محلي وبدون إنترنت
def run_brainfuck(bf_code):
    memory = [0] * 30000  # خلايا الذاكرة
    ptr = 0  # مؤشر الذاكرة
    output = ""
    
    code_ptr = 0
    while code_ptr < len(bf_code):
        cmd = bf_code[code_ptr]
        
        if cmd == '+':
            memory[ptr] = (memory[ptr] + 1) % 256
        elif cmd == '-':
            memory[ptr] = (memory[ptr] - 1) % 256
        elif cmd == '.':
            output += chr(memory[ptr])
        
        # تخطي الأوامر الأخرى لتشغيل النصوص البسيطة حالياً
        code_ptr += 1
        
    return output

# قراءة الملف المشفر الذي صنعناه قبل قليل
try:
    with open("ai_brainfuck.bf", "r") as f:
        secret_code = f.read()
    
    print("--- [جاري فك تشفير وتشغيل العقل التعجيزي...] ---")
    result = run_brainfuck(secret_code)
    print("\nالنتيجة التي خرجت من كود الطلاسم هي:")
    print(result)

except FileNotFoundError:
    print("خطأ: لم يتم العثور على ملف ai_brainfuck.bf!")