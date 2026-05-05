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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Hema Veeradhi", "Aakanksha Duggal", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1YeMP/self-hosted-llms-on-kubernetes-a-practical-guide-hema-veeradhi-aakanksha-duggal-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Self-Hosted+LLMs+on+Kubernetes%3A+A+Practical+Guide+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Self-Hosted LLMs on Kubernetes: A Practical Guide - Hema Veeradhi & Aakanksha Duggal, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Hema Veeradhi, Aakanksha Duggal, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1YeMP/self-hosted-llms-on-kubernetes-a-practical-guide-hema-veeradhi-aakanksha-duggal-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Self-Hosted+LLMs+on+Kubernetes%3A+A+Practical+Guide+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Self-Hosted LLMs on Kubernetes: A Practical Guide.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMP/self-hosted-llms-on-kubernetes-a-practical-guide-hema-veeradhi-aakanksha-duggal-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Self-Hosted+LLMs+on+Kubernetes%3A+A+Practical+Guide+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JD8ZD3pNij0
- YouTube title: Self-Hosted LLMs on Kubernetes: A Practical Guide - Hema Veeradhi & Aakanksha Duggal, Red Hat
- Match score: 0.791
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/self-hosted-llms-on-kubernetes-a-practical-guide/JD8ZD3pNij0.txt
- Transcript chars: 28582
- Keywords: language, models, llm, particular, whisper, container, source, application, started, requires, format, self-hosting, parameters, performance, running, resources, python, repository

### Resumo baseado na transcript

welcome everyone and thank you uh for coming to my talk I'm super excited that all of you all are here and I cannot wait to take you on a journey with large language models um you've all you've all noticed that in recent times there's been an undeniable Buzz surrounding large language models or as you call them llms perhaps you've encountered discussions articles or even first and experience the remarkable capabilities these models have to offer yet despite all this excitement many of us may find ourselves hesitant

### Excerpt da transcript

welcome everyone and thank you uh for coming to my talk I'm super excited that all of you all are here and I cannot wait to take you on a journey with large language models um you've all you've all noticed that in recent times there's been an undeniable Buzz surrounding large language models or as you call them llms perhaps you've encountered discussions articles or even first and experience the remarkable capabilities these models have to offer yet despite all this excitement many of us may find ourselves hesitant to dive in the world of llms held back by the perceived complexity of deploying and utilizing these powerful tools so let's get into the REM of large language models and hosting your own models using kubernetes to harness the full potential of llms within your own projects and workflows so before we get into the world of llms I'll take a quick moment to introduce myself and my co-speaker my name is akanga Dugal I am a senior data scientist in the office of the CTO at Red Hat I work in the emerging Technologies data science team my co-speaker HMA veradi is also a senior data scientist in my team but unfortunately couldn't make it here today so in this talk we are going to talk about what is llms where does llm come from we'll also go over what are some open source llms what are the commercial llms that you can get started with what are some close source llms that you should be careful when you're using them then we'll go over what are the various steps when you're trying to build a large language model application then we'll quickly go over the concept of self-hosting your large language model models and Then followed by a demo we also help you set up your own llm using kubernetes before diving into llms let's take a step back let's address a language model first a language model is a type of machine learning model that is trained to conduct a probability distribution over words simply put it tries to predict the next most appropriate word to fill in a blank space in a sentence or a phrase based on the context of the previously given text just like when you're trying to write an email or a text message the language model tries to predict the next set of words so the job of a language model is to approximate a function that would fit your input data so if the input data is onedimensional like on the left um you can have a linear Trend that linear function that basically fits the input data but if your input data is natural language or an image we
