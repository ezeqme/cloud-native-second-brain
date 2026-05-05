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
themes: ["AI ML", "Security", "Runtime Containers", "Kubernetes Core"]
speakers: ["Suraj Deshmukh", "Microsoft", "Pradipta Banerjee", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1YeOx/fortifying-ai-security-in-kubernetes-with-confidential-containers-coco-suraj-deshmukh-microsoft-pradipta-banerjee-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Fortifying+AI+Security+in+Kubernetes+with+Confidential+Containers+%28CoCo%29+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Fortifying AI Security in Kubernetes with Confidential Containers (CoCo) - Suraj Deshmukh, Microsoft & Pradipta Banerjee, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Suraj Deshmukh, Microsoft, Pradipta Banerjee, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1YeOx/fortifying-ai-security-in-kubernetes-with-confidential-containers-coco-suraj-deshmukh-microsoft-pradipta-banerjee-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Fortifying+AI+Security+in+Kubernetes+with+Confidential+Containers+%28CoCo%29+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Fortifying AI Security in Kubernetes with Confidential Containers (CoCo).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOx/fortifying-ai-security-in-kubernetes-with-confidential-containers-coco-suraj-deshmukh-microsoft-pradipta-banerjee-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Fortifying+AI+Security+in+Kubernetes+with+Confidential+Containers+%28CoCo%29+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ko0o5_hpmxI
- YouTube title: Fortifying AI Security in Kubernetes with Confidential Containers (CoCo)
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/fortifying-ai-security-in-kubernetes-with-confidential-containers-coco/Ko0o5_hpmxI.txt
- Transcript chars: 26617
- Keywords: confidential, memory, containers, trusted, inside, encrypted, access, encryption, computing, hardware, container, secret, runtime, protect, course, running, cluster, infrastructure

### Resumo baseado na transcript

why do we need to protect the model and the data of course we know that so what happens if the model gets stolen model can get stolen right so you're you lose the intellectual property that comes with the model uh think of another story where the input that you interact with the model right let's say you are we are talking about a health chatbot where you are kind of sending inputs which are confidential in nature your health related queries that you are sending to the board

### Excerpt da transcript

why do we need to protect the model and the data of course we know that so what happens if the model gets stolen model can get stolen right so you're you lose the intellectual property that comes with the model uh think of another story where the input that you interact with the model right let's say you are we are talking about a health chatbot where you are kind of sending inputs which are confidential in nature your health related queries that you are sending to the board to the chat B and then it Returns what if that data gets lost which means there is a reputational damage to your because if that data gets lost and also loss of users trust how the users will trust you if you cannot Safeguard the data right and not not the least that of course your competitive Advantage is also lost so model protection and of course the data protection is very important now the question is how do you protect the model and data of course what we do today right currently we have various ways so so if we consider security as a layered uh onion then what happens you have API so we we are considering apis and the models and key thing is the model so you can encrypt the model at rest and of course when when the data that of comes uh to the model it's all encrypted in translit so you use encryption to protect the data that you already use you also have uh role based access controls right to kind of protect it then you also have uh API Security in place so these are the usual stuff you will have Network policies Fireballs right segmentations and all and of course auditing and login now in this whole thing do you see anything missing so this I I believe if if you are familiar in the sense of uh in the infrastructure side and protecting these are common right these are table STS today without this anyway we won't run a real application in production but do you see anything missing from this okay no sir this was just leading question now what I will do is I will show you a small demo right which is uh so this is basically a demo which we are running on a single note kubernetes cluster for ease of use so for a moment uh let me just uh okay so for a moment you wear the hat of an infrastructure admin who has access to the kubernetes worker noes so I I would want you to imagine that you can access the kubernetes water node and this is a very simple demo which what it does it just uh creates a simple pod which downloads a secret and keeps it in the memory that's all it's a very simple
