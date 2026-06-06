# ذكاء اصطناعي مصغر ومحلي (يعمل بدون إنترنت) لترجمة المشاعر
import os

def offline_ai_classifier():
    print("--- [مرحباً بك في الذكاء الاصطناعي المحلي] ---")
    user_input = input("AI: كيف كان يومك اليوم؟ أخبرني بالتفصيل: \nأنت: ").lower()

    # قاعدة المعرفة المحلية (Keywords)
    positive_words = ["سعيد", "رائع", "جميل", "ممتاز", "نجاح", "خير", "good", "happy", "awesome", "great"]
    negative_words = ["حزين", "سيء", "متعب", "فشل", "صعب", "ضيق", "bad", "sad", "tired", "difficult"]

    # عدادات لتحليل النص
    positive_score = 0
    negative_score = 0

    # تحليل الكلمات محلياً
    for word in positive_words:
        if word in user_input:
            positive_score += 1

    for word in negative_words:
        if word in user_input:
            negative_score += 1

    # اتخاذ القرار (العقل الذكي)
    print("\n--- [تحليل الـ AI] ---")
    if positive_score > negative_score:
        print("AI: أنا سعيد جداً لسماع ذلك! يبدو أن طاقتك إيجابية اليوم. استمر في التألق! ✨")
    elif negative_score > positive_score:
        print("AI: يؤسفني أن يومك كان صعباً. تذكر أن الأيام السيئة تمر دائماً، خذ قسطاً من الراحة. ☕")
    else:
        print("AI: يبدو أن يومك كان عادياً أو هادئاً. أتمنى لك بقية يوم ممتعة! 🌿")

# تشغيل البرنامج
if __name__ == "__main__":
    offline_ai_classifier()