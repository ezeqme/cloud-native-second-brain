---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Cloud Native Novice"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Abdel Sghiouar", "Mofi Rahman", "Google Cloud"]
sched_url: https://kccnceu2025.sched.com/event/1txFw/yes-you-can-run-llms-on-kubernetes-abdel-sghiouar-mofi-rahman-google-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Yes+You+Can+Run+LLMs+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Yes You Can Run LLMs on Kubernetes - Abdel Sghiouar & Mofi Rahman, Google Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Abdel Sghiouar, Mofi Rahman, Google Cloud
- Schedule: https://kccnceu2025.sched.com/event/1txFw/yes-you-can-run-llms-on-kubernetes-abdel-sghiouar-mofi-rahman-google-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Yes+You+Can+Run+LLMs+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Yes You Can Run LLMs on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFw/yes-you-can-run-llms-on-kubernetes-abdel-sghiouar-mofi-rahman-google-cloud
- YouTube search: https://www.youtube.com/results?search_query=Yes+You+Can+Run+LLMs+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8fB3k95dCRE
- YouTube title: Yes you can run LLMs on Kubernetes | Cloud Native Denmark 2025 Aarhus
- Match score: 0.773
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/yes-you-can-run-llms-on-kubernetes/8fB3k95dCRE.txt
- Transcript chars: 33136
- Keywords: language, models, serving, inference, running, called, essentially, request, traffic, bigger, container, actually, gateway, little, single, particular, gpu, multiple

### Resumo baseado na transcript

We're going to talk about running large language models on Kubernetes because we live in 2025 and generative AI is everywhere. If you have been doing Kubernetes for as long as I've been doing it for almost 7 or 8 years, running large language models is your job guarantees. The challenge is that these models are getting bigger and bigger and bigger and bigger. Ray Ray is an open source Python framework for doing large end-to-end large language um end-to-end machine learning including training, fine-tuning, reinforcement learning, etc. Kubernetes gives you a little bit of that mixed between the fully managed solution because you have the self-healing, the automation, and all the stuff that Kubernetes brings, and then the the flexibility of doing things or tuning things your way. I don't I don't think I need to to to to to spend too much time on this, but why do we want to run large language models on Kubernetes?

### Excerpt da transcript

Hi everyone. We're going to talk about running large language models on Kubernetes because we live in 2025 and generative AI is everywhere. If you have been doing Kubernetes for as long as I've been doing it for almost 7 or 8 years, running large language models is your job guarantees. Because running stuff on top of Kubernetes is the equivalent of writing COBOL code 25 years ago. This thing is going to be around for a while, so don't worry about it. All right. So, we created this talk a while ago with a colleague of mine and we called it this provocative title. Yes, you can run LLMs on Kubernetes. And the idea was would would be that if somebody reads it the title, they would be like, "Who said you can't?" And the idea is not you can't. The idea is how can you do it? And I'm not going to focus too much on actually running large language models on Kubernetes itself, but focus more on the challenges of running running large language models. My name is Abdel. I'm a cloud developer advocate, as Casper said, at Google.

So, by show of hands, how many of you knows Kubernetes? All right, good. You are at the right conference. Awesome. How many of you have run large language models on Kubernetes? Oh, okay. If there was more hands, I would have said, "Thank you," and walk off stage. But apparently there is none, so. >> [snorts] >> Generative AI is evolving. It's evolving very fast. And it's evolving also in a pace and in a manner where people care more about local open large language models, not only cloud-hosted ones. You can't use cloud-hosted LLMs all the time. Gemini, ChatGPT, Claude, all these things are not always useful for you. Either because they cannot do the things you need them to do, or for regulation reasons you cannot use them, or for latency reasons you cannot use them. And so therefore, open LLMs are the alternative. They are open because they are either open source or open weights. Open source means you have the code that used to be that used to train the model, or open weights means the weights themselves are available.

And there is like a whole, you know, ecosystem of large language models. Everything from Google to Llama to Gemma to Mistral to whatever to DeepSeek to all of these things. The challenge is that these models are getting bigger and bigger and bigger and bigger. They're not only bigger in size, but they're also bigger in terms of the the complexity of the model itself and what it can do. So, before I move on, I want to spend a lit
