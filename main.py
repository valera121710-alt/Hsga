#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import json
from datetime import datetime

class DeepSeekMini:
    def __init__(self):
        self.name = "DeepSeek Mini"
        self.version = "1.0"
        self.knowledge_base = self.load_knowledge_base()
        self.conversation_history = []
        
    def load_knowledge_base(self):
        """База знаний с ответами"""
        return {
            "greetings": {
                "patterns": ["привет", "здравствуй", "добрый", "hello", "hi", "хай", "здаров", "ку", "салам"],
                "responses": [
                    "Привет! 😊 Рад тебя видеть!",
                    "Здравствуй! Чем могу помочь?",
                    "Привет-привет! Готов к общению!",
                    "Привет! Как твои дела?",
                    "Хай! Как настроение? ✨"
                ]
            },
            "about": {
                "patterns": ["кто ты", "что ты", "расскажи о себе", "твои возможности", "ты бот", "ты ии"],
                "responses": [
                    "Я DeepSeek Mini - упрощенная версия ИИ-помощника! Могу помогать с программированием, отвечать на вопросы и поддерживать беседу.",
                    "Я ИИ-ассистент, созданный на основе знаний о DeepSeek. Специализируюсь на программировании и общих вопросах!",
                    "Я цифровой помощник, готовый помочь с техническими вопросами, кодом или просто пообщаться! 😊",
                    "Я твой ИИ-друг! Могу пошутить, помочь с кодом или просто поболтать."
                ]
            },
            "programming": {
                "patterns": ["python", "javascript", "java", "код", "программирование", "функция", "переменн", "html", "css", "git", "github"],
                "responses": [
                    "Отличный вопрос по программированию! Давай разберемся...",
                    "В программировании важно понимать основы. Что именно тебя интересует?",
                    "Могу помочь с кодом! Какой язык тебя интересует?",
                    "Программирование - это круто! Расскажи подробнее о твоей задаче.",
                    "О, технические вопросы! Это моя любимая тема! 🚀"
                ]
            },
            "jokes": {
                "patterns": ["шутка", "пошути", "смешн", "прикол", "юмор", "анекдот"],
                "responses": [
                    "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25! 😄",
                    "Какой у программиста тост? Без ошибок! 🥂",
                    "Почему Python не смог выиграть в скачках? Потому что он был привязан к своим змеям! 🐍",
                    "Что сказал null другому null? Ничего, они оба упали с NPE! 💥",
                    "Почему программист всегда мокрый? Потому что он постоянно в Python! 🐍",
                    "Как программисты называют лифт? Метод для вертикального перемещения! 🏢"
                ]
            },
            "help": {
                "patterns": ["помощь", "помоги", "команды", "что ты умеешь", "функции"],
                "responses": [
                    "Я умею:\n• Общаться на разные темы\n• Шутить и поднимать настроение 😄\n• Помогать с программированием\n• Отвечать на вопросы\nПросто напиши что-нибудь!",
                    "Мои возможности:\n- Поддержка беседы\n- Юмористические ответы\n- Помощь в технических вопросах\n- Ответы на общие вопросы\nЧто тебя интересует?",
                    "Я здесь чтобы:\n🎯 Помочь с кодом\n😊 Пообщаться\n🎭 Пошутить\n💡 Ответить на вопросы\nПросто напиши мне!"
                ]
            },
            "time": {
                "patterns": ["время", "который час", "дата", "сколько времени"],
                "responses": [
                    f"Сейчас: {datetime.now().strftime('%H:%M:%S %d.%m.%Y')} ⏰",
                    f"Время: {datetime.now().strftime('%H:%M')}, Дата: {datetime.now().strftime('%d.%m.%Y')} 📅",
                    f"На моих цифровых часах: {datetime.now().strftime('%H:%M:%S')} 🕒"
                ]
            },
            "goodbye": {
                "patterns": ["пока", "до свидан", "прощай", "увидимся", "bye", "goodbye", "выход", "quit", "exit"],
                "responses": [
                    "Пока! Было приятно пообщаться! 👋",
                    "До свидания! Возвращайся с новыми вопросами!",
                    "Пока-пока! Удачи в твоих проектах!",
                    "До скорой встречи! Не стесняйся обращаться! 😊",
                    "Пока! Если что, я всегда тут! ✨"
                ]
            }
        }
    
    def find_category(self, message):
        """Находит подходящую категорию для сообщения"""
        message_lower = message.lower()
        
        for category, data in self.knowledge_base.items():
            for pattern in data["patterns"]:
                if pattern in message_lower:
                    return category
        return None
    
    def get_response(self, message):
        """Генерирует ответ на сообщение"""
        category = self.find_category(message)
        
        if category:
            responses = self.knowledge_base[category]["responses"]
            
            # Для времени обновляем ответ
            if category == "time":
                self.knowledge_base["time"]["responses"] = [
                    f"Сейчас: {datetime.now().strftime('%H:%M:%S %d.%m.%Y')} ⏰",
                    f"Время: {datetime.now().strftime('%H:%M')}, Дата: {datetime.now().strftime('%d.%m.%Y')} 📅",
                    f"На моих цифровых часах: {datetime.now().strftime('%H:%M:%S')} 🕒"
                ]
                responses = self.knowledge_base[category]["responses"]
            
            return random.choice(responses)
        else:
            # Ответ по умолчанию
            default_responses = [
                "Интересно! Расскажи подробнее? 🤔",
                "Хм, хороший вопрос! Давай поговорим о чем-то другом? 😊",
                "Не совсем понял, но я всегда рад поболтать! 💬",
                "Может, поговорим о программировании или я расскажу шутку? 😄",
                "Интересная мысль! Что еще тебя волнует? ✨"
            ]
            return random.choice(default_responses)
    
    def chat(self):
        """Основной цикл чата"""
        print(f"🤖 {self.name} v{self.version}")
        print("=" * 40)
        print("Привет! Я твой ИИ-помощник.")
        print("Напиши 'помощь' чтобы узнать что я умею")
        print("Напиши 'пока' чтобы выйти")
        print("=" * 40)
        
        while True:
            try:
                user_input = input("\n👤 Ты: ").strip()
                
                if not user_input:
                    continue
                
                # Сохраняем в историю
                self.conversation_history.append(f"Ты: {user_input}")
                
                # Проверяем на выход
                if any(word in user_input.lower() for word in ["пока", "выход", "quit", "exit"]):
                    response = self.get_response(user_input)
                    print(f"🤖 Я: {response}")
                    break
                
                # Имитируем набор сообщения
                print("🤖 Я: ", end="", flush=True)
                thinking_time = random.uniform(0.5, 2.0)
                time.sleep(thinking_time)
                
                # Получаем и выводим ответ
                response = self.get_response(user_input)
                print(response)
                
                # Сохраняем ответ в историю
                self.conversation_history.append(f"Бот: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n🤖 Я: Пока! Возвращайся! 👋")
                break
            except Exception as e:
                print(f"\n🤖 Я: Ой, что-то пошло не так! 😅")
                print(f"Ошибка: {e}")

def main():
    """Запуск бота"""
    bot = DeepSeekMini()
    bot.chat()

if __name__ == "__main__":
    main()
