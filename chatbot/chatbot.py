import ollama
import gradio as gr

# 사용할 모델 이름 설정
MODEL_NAME = "qwen3:1.7b"

# Ollama API를 사용하여 응답을 생성하고 대화 컨텍스트를 유지하는 함수
def respond_to_user(message, history):
    # Gradio의 history는 이미 Ollama의 messages 형식과 유사하게 변경되었을 수 있으나,
    # 이전 버전 호환 및 명확성을 위해 history를 messages 리스트로 변환합니다.
    messages = []
    
    # history는 list[list[str, str]] 또는 list[dict] 형태일 수 있습니다.
    # 안전하게 메시지 형식으로 변환합니다.
    for item in history:
        # history의 항목이 튜플/리스트 [user_msg, bot_msg] 형태인 경우
        if isinstance(item, list) and len(item) == 2:
            user_msg, bot_msg = item
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": bot_msg})
        # history의 항목이 dict 형태로, 이미 'role'과 'content'를 가지고 있는 경우 (최신 Gradio)
        elif isinstance(item, dict):
            messages.append(item)
            
    # 현재 사용자의 메시지 추가
    # Gradio 4.0 이후의 ChatInterface는 `message`를 문자열로 전달합니다.
    messages.append({"role": "user", "content": message})
    
    try:
        # Ollama 클라이언트 생성
        client = ollama.Client()
        
        # Ollama chat API 호출
        response = client.chat(
            model=MODEL_NAME,
            messages=messages
        )
        
        # 모델의 응답 텍스트 추출
        bot_message = response['message']['content']
        return bot_message
        
    except Exception as e:
        return f"🚨 Ollama 서버 연결 오류 또는 모델 로드 오류: {e}\n\nOllama 서버가 실행 중인지, 그리고 `{MODEL_NAME}` 모델이 다운로드되었는지 확인해 주세요."


# Gradio ChatInterface를 사용하여 웹 인터페이스 생성
chat_interface = gr.ChatInterface(
    fn=respond_to_user,
    title=f"🧠 Ollama ({MODEL_NAME}) + Gradio LLM 챗봇",
    description="Qwen3:1.7b 모델을 사용한 멀티턴 대화 챗봇입니다.",
    # UserWarning을 제거하기 위해 type='messages'를 명시합니다.
    chatbot=gr.Chatbot(type='messages', height=500), 
    textbox=gr.Textbox(placeholder="여기에 메시지를 입력하세요...", container=False, scale=7),
    # 오류를 일으킨 'retry_btn' 인자를 제거했습니다.
    # 'stop_btn', 'clear_btn' 등도 최신 버전에서는 다르게 처리되거나
    # 기본값으로 작동하므로, 오류 발생 시 제거하는 것이 안전합니다.
    examples=[
        "안녕하세요? 저는 당신의 AI 챗봇입니다.",
        "서울의 날씨는 어떤가요?",
        "파이썬에서 리스트의 특징을 설명해 줘."
    ]
)

# Gradio 앱 실행
if __name__ == "__main__":
    print(f"🎉 Gradio 챗봇을 시작합니다. 잠시 후 웹 브라우저에서 열립니다.")
    chat_interface.launch(inbrowser=True, show_api=False)