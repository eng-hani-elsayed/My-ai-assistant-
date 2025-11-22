import gradio as gr

def chat(message, history):
    return "أهلاً بك! أنا مساعدك الذكي. كيف يمكنني مساعدتك؟ 🌟"

demo = gr.ChatInterface(
    chat,
    title="🤖 مساعدي الذكي",
    description="تحدث معي وسأرد عليك! يمكنك الكتابة بالعربية أو الإنجليزية."
)

if __name__ == "__main__":
    demo.launch()
