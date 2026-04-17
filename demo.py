import google.generativeai as genai

genai.configure(api_key="AIzaSyDQrVEevER13v-BKPSt4LQAhnKC7HXbXvU")

for m in genai.list_models():
    print(m.name)
