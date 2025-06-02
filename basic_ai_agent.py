
#Basic AI Agent with Web UI

import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

#Load AI Model
llm=OllamaLLM(model="mistral")

#define and Initialize memory variable in the session (st.session_state is like a dict-like object storing variables)
if "chat_history" not in st.session_state:
	st.session_state.chat_history=ChatMessageHistory()

#Define AI Chat prompt
prompt = PromptTemplate(
	input_variables=["chat_history", "question"], 
	template="Previous conversation: {chat_history}\nUser: {question}\nAI:")


#function to run AI chat with memory


def run_chain(question):
	chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])

	#run the AI response generation
	response=llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

	#store the new user input  and AI response in memory
	st.session_state.chat_history.add_user_message(question)
	st.session_state.chat_history.add_ai_message(response)

	return response


#StreamLit UI

st.title("💬 Israa's Smart Chatbot")
st.caption("Powered by Mistral + LangChain + Streamlit")
st.write("🚀 Ask me anything and I’ll remember the conversation.")


user_input=st.text_input("🎤 Your question: ")

if user_input: #the whole script is re-run when the user press enter to check the if again
	response=run_chain(user_input)
	st.write(f"👧 **You**: ", user_input)
	st.write(f"🤖 **AI Input**: ", response)


st.divider()


#Show full chat history (no need for a loop since streamlit rerun the whole script in each interaction)
st.subheader("📜 Chat History")
for msg in st.session_state.chat_history.messages:
    if msg.type == "human":
        st.markdown(f"👧 **You:** {msg.content}")
    elif msg.type == "ai":
        st.markdown(f"🤖 **AI:** {msg.content}")

if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = ChatMessageHistory()
    st.rerun()












#------Basic AI Agent with Memory------
# #to store and manage memory to remember responses
# from langchain_community.chat_message_histories import ChatMessageHistory
# #to keep prompts consistent and usable
# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import OllamaLLM



# llm=OllamaLLM(model="mistral")


# #initialize memory
# chat_history = ChatMessageHistory() #store user-AI message conversation

# #Define AI Chat prompt (how it is going to be displayed when run) the {chat_history} variable will contain formatted text specified in chat_history_text
# prompt = PromptTemplate(input_variables=["chat_history", "question"], template="Previous conversation: {chat_history}\nUser: {question}\nAI:")



# #function to run Ai chat with memory
# def run_chain(question):
# 	#retrieve chat history manually format it in a string, it will loop in chat_history.messages and store each message object in msg, each one seperated by a new line
# 	chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])
	
# 	#run the AI response generation
# 	response=llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

# 	#store the new user input  and AI response in memory
# 	chat_history.add_user_message(question)
# 	chat_history.add_ai_message(response)

# 	return response


# #Interactive CLI chatbot (command line interface; through the terminal)
# print("\n 🧠 AI Chatbot with memory")
# print("type 'exit' to stop")



# while True:
# 	user_input=input("\n 🔹You: ")
# 	if user_input.lower() =="exit":
# 		print(" 👋 Goodbye!")
# 		break
# 	ai_response = run_chain(user_input)

# 	print("\n 🤖 AI Response: ", ai_response)







#-----Basic AI Agent-----""

# from langchain_ollama import OllamaLLM

# #Load AI model from Ollama
# llm = OllamaLLM(model="mistral")

# print("Hello! Welcome to your first AI Model, you can ask me anything!")

# while True:
# 	question= input("Type your question or type 'exit' to end\n")
# 	if question.lower() =='exit':
# 		print("Goodbye")
# 		break
# 	response=llm.invoke(question)
# 	print("\nAI response: "+response)


# #invoke used to pass the question to the llm model

