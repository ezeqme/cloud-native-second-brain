---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["AI ML", "GitOps Delivery"]
speakers: ["Ezequiel Lanza", "Arun Gupta", "Intel"]
sched_url: https://kccnceu2024.sched.com/event/1YeNH/cloud-native-llm-deployments-made-easy-using-langchain-ezequiel-lanza-arun-gupta-intel
youtube_search_url: https://www.youtube.com/results?search_query=Cloud-Native+LLM+Deployments+Made+Easy+Using+LangChain+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cloud-Native LLM Deployments Made Easy Using LangChain - Ezequiel Lanza & Arun Gupta, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[GitOps Delivery]]
- País/cidade: France / Paris
- Speakers: Ezequiel Lanza, Arun Gupta, Intel
- Schedule: https://kccnceu2024.sched.com/event/1YeNH/cloud-native-llm-deployments-made-easy-using-langchain-ezequiel-lanza-arun-gupta-intel
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud-Native+LLM+Deployments+Made+Easy+Using+LangChain+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cloud-Native LLM Deployments Made Easy Using LangChain.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNH/cloud-native-llm-deployments-made-easy-using-langchain-ezequiel-lanza-arun-gupta-intel
- YouTube search: https://www.youtube.com/results?search_query=Cloud-Native+LLM+Deployments+Made+Easy+Using+LangChain+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DVf5O2Xm_RY
- YouTube title: Cloud-Native LLM Deployments Made Easy Using LangChain - Ezequiel Lanza & Arun Gupta, Intel
- Match score: 0.851
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cloud-native-llm-deployments-made-easy-using-langchain/DVf5O2Xm_RY.txt
- Transcript chars: 31812
- Keywords: basically, models, external, course, llm, question, business, running, container, multiple, probably, native, github, server, answer, pipeline, define, everything

### Resumo baseado na transcript

good afternoon um my name is Aron uh I am at Intel I'm part of the open ecosystem team hello my name is iik Lanza and I'm I an AI open source evangelist yeah so today we're going to talk about um how do you deploy llms using Cloud native with Lang chain and what is the use case for that specifically we all want we have always wanted assistant you know I want assistant that can cook food for me I can get that with AI but at least intel.com internally and that's where my pay is available um all my um my workday is available and those could go through a LM proxy and then that llm proxy is where you could do model provisioning model governance you know how much cost allocation really unite all the elements over there and if you are deploying all of that together in like a kubernetes architecture know the llm proxy where we'll probably have a llm proxy adapter running as a pod that could be like a horizontal scale that could scale really good and at the back end typically when you are running the llm backend worker those are generally vertically scaled as opposed to horizontally scaled because they need more M memory and CPU and GPU and all so that's sort of the

### Excerpt da transcript

good afternoon um my name is Aron uh I am at Intel I'm part of the open ecosystem team hello my name is iik Lanza and I'm I an AI open source evangelist yeah so today we're going to talk about um how do you deploy llms using Cloud native with Lang chain and what is the use case for that specifically we all want we have always wanted assistant you know I want assistant that can cook food for me I can get that with AI but at least in my job how can I get an assistant that could make me more productive whether is writing my emails whether it's summarizing my meeting minutes simple assistance you know I mean bouncing ideas back and forth conversational chat BS all sorts of assistance could be very very helpful actually um and if you put that in a business context you know in a company there are different business units so to say there is a finance there is it you know there is is legal there is engineering and their needs are very different their jurisdiction is very different uh how much amount of data can they keep within the business unit can they stand outside the business unit should it stay inside the company can it go outside the company so each business unit in that sense if they want to explore how do you leverage an llm their needs are very different and very unique in that sense so that's sort of where we are going to to talk about there are many ways by which customers are deploying llms uh in Cloud native so what we're going to talk about is one specific Way by which you know you could deploy um llms in Cloud native exactly yes and this our is one way to do it so basically we Define in five main steps the first one is the model the definition you need to Define your model the second one is the API the third is the packaging because you need to put everything in one package you need to containerize that and you need to use kubernetes of course so let's go for we will go deep in all of them so let's go right let's go for the model definition which is probably the most challenging part right because we need to know what is our problem so we need to pick which model we would like to use and what is the use case do we do we want to build a conversational chatbot a text imization you know that llms we can use it for multiple things so classification question answering and so on so the first thing to find is a problem the second one is the the is the model we have tons of models as you may hear Lama Falcon open AI everything you have tons of models and w
