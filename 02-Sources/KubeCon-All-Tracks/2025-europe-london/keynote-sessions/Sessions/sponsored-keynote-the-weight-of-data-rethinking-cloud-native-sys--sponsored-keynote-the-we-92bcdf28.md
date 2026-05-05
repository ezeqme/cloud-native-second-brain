---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Keynote Sessions"
themes: ["AI ML", "Storage Data"]
speakers: ["Vincent Caldeira", "CTO", "APAC", "Red Hat", "Holly Cummins", "Senior Principal Software Engineer", "Red Hat"]
sched_url: https://kccnceu2025.sched.com/event/1vUbe/sponsored-keynote-the-weight-of-data-rethinking-cloud-native-systems-for-the-age-of-ai-vincent-caldeira-cto-apac-red-hat-holly-cummins-senior-principal-software-engineer-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+The+Weight+of+Data%3A+Rethinking+Cloud-Native+Systems+for+the+Age+of+AI+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Sponsored Keynote: The Weight of Data: Rethinking Cloud-Native Systems for the Age of AI - Vincent Caldeira, CTO, APAC, Red Hat & Holly Cummins, Senior Principal Software Engineer, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: United Kingdom / London
- Speakers: Vincent Caldeira, CTO, APAC, Red Hat, Holly Cummins, Senior Principal Software Engineer, Red Hat
- Schedule: https://kccnceu2025.sched.com/event/1vUbe/sponsored-keynote-the-weight-of-data-rethinking-cloud-native-systems-for-the-age-of-ai-vincent-caldeira-cto-apac-red-hat-holly-cummins-senior-principal-software-engineer-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+The+Weight+of+Data%3A+Rethinking+Cloud-Native+Systems+for+the+Age+of+AI+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: The Weight of Data: Rethinking Cloud-Native Systems for the Age of AI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1vUbe/sponsored-keynote-the-weight-of-data-rethinking-cloud-native-systems-for-the-age-of-ai-vincent-caldeira-cto-apac-red-hat-holly-cummins-senior-principal-software-engineer-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+The+Weight+of+Data%3A+Rethinking+Cloud-Native+Systems+for+the+Age+of+AI+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=W_EF1HnP4tU
- YouTube title: Sponsored Keynote: The Weight of Data: Rethinking Cloud-Native Systems f... V. Caldeira & H. Cummins
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sponsored-keynote-the-weight-of-data-rethinking-cloud-native-systems-f/W_EF1HnP4tU.txt
- Transcript chars: 4860
- Keywords: native, management, systems, distributed, already, provide, models, bigger, provides, projects, agents, evolve, strong, storage, workload, scheduling, better, weight

### Resumo baseado na transcript

Next generation models ingested more and more and more and more of humanity's knowledge and got bigger and bigger. Instead of just having small snippets of text, we had enormous volumes of context state. We can also tap on the growing and thriving ecosystem for data on kubernetes. I would mention projects such as VEST which provides you know cloud native distributed MySQL at scale or projects like Rook which provide us for an orchestration for storage systems such as SE. We also have been seeing a growing interest in event-driven architecture and projects such as K native or streamy which enable capka and kubernetes have helped us to build dynamically linked application and microservices but AI workload operate at a totally different scale if you So the current construct that we have they need to evolve and they need to evolve because we are already dealing with huge issue at large scale.

### Excerpt da transcript

Hello Cucon. Two and a half years ago, our industry changed fundamentally. Chat GPT brought AI into every organization. Next generation models ingested more and more and more and more of humanity's knowledge and got bigger and bigger. And the way we interacted with these models got bigger as well. We moved from just chat to multimodal AI. We also got bigger in how we interacted with them. Instead of just having small snippets of text, we had enormous volumes of context state. But state has weight. All of this data in one big monolith wasn't sustainable and it wasn't scalable. So we had to break up the monolith again. We need to move to smaller models. Smaller models means orchestration and we also want agents that are interacting with the various parts of the system which is distributed computing. So if you squint this should look really quite familiar. This should look a lot like the same kinds of patterns that we've already solved with Kubernetes, which is awesome, but there's always a butt. These systems have an awful lot of state.

The model, the paradigm that we've been working with for cloud native is that stateless is good. AI is the opposite. AI is all about state. So the question is how do we evolve? How do we shift that paradigm to make Kubernetes AI native? So let's not forget that Kubernetes already provides very strong primitives for us to manage state. We have persistent volumes uh which provides durable storage. We've got stateful sets that provides us with a stable identity and access to storage for pots and we also have demons set that provide us with a consistent way of deploying pod across node and to some extent that allows us to have kind of node level state management. We can also tap on the growing and thriving ecosystem for data on kubernetes. I would mention projects such as VEST which provides you know cloud native distributed MySQL at scale or projects like Rook which provide us for an orchestration for storage systems such as SE. We also have been seeing a growing interest in event-driven architecture and projects such as K native or streamy which enable capka and kubernetes have helped us to build dynamically linked application and microservices but AI workload operate at a totally different scale if you look at state management AI agent just don't store state they share they modify and they react to data in a very dynamic and high volume and high throughput manner.

So the current construct that we have they need to evolve and
