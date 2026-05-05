---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["AI ML", "Observability", "GitOps Delivery", "SRE Reliability"]
speakers: ["Avik Basu", "Saravanan Balasubramanian", "Intuit"]
sched_url: https://kccncna2024.sched.com/event/1i7kp/towards-zero-change-incidents-intuits-strategy-for-implementing-ai-driven-progressive-delivery-avik-basu-saravanan-balasubramanian-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Towards+Zero+Change+Incidents%3A+Intuit%27s+Strategy+for+Implementing+AI-Driven+Progressive+Delivery+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Towards Zero Change Incidents: Intuit's Strategy for Implementing AI-Driven Progressive Delivery - Avik Basu & Saravanan Balasubramanian, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Avik Basu, Saravanan Balasubramanian, Intuit
- Schedule: https://kccncna2024.sched.com/event/1i7kp/towards-zero-change-incidents-intuits-strategy-for-implementing-ai-driven-progressive-delivery-avik-basu-saravanan-balasubramanian-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Towards+Zero+Change+Incidents%3A+Intuit%27s+Strategy+for+Implementing+AI-Driven+Progressive+Delivery+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Towards Zero Change Incidents: Intuit's Strategy for Implementing AI-Driven Progressive Delivery.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kp/towards-zero-change-incidents-intuits-strategy-for-implementing-ai-driven-progressive-delivery-avik-basu-saravanan-balasubramanian-intuit
- YouTube search: https://www.youtube.com/results?search_query=Towards+Zero+Change+Incidents%3A+Intuit%27s+Strategy+for+Implementing+AI-Driven+Progressive+Delivery+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5k8Djsjt8eA
- YouTube title: Towards Zero Change Incidents: Intuit's Strategy for Implementing AI... A. Basu, S. Balasubramanian
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/towards-zero-change-incidents-intuits-strategy-for-implementing-ai-dri/5k8Djsjt8eA.txt
- Transcript chars: 35431
- Keywords: metrics, anomaly, stable, canary, pipeline, actually, latency, progressive, metric, scores, delivery, version, window, source, understand, anomal, anomalies, question

### Resumo baseado na transcript

all right so hello everyone uh thank you for being here I'm super stoked and excited to be here uh my name is aik I am a data scientist at int this is my colleague Bala um you know who is a senior staff software engineer um and today I'm going to talk about the AI driven Progressive delivery and um really show how we uh we were able to achieve this purely using open source tools so our goal from this talk is to give you a solid intuition

### Excerpt da transcript

all right so hello everyone uh thank you for being here I'm super stoked and excited to be here uh my name is aik I am a data scientist at int this is my colleague Bala um you know who is a senior staff software engineer um and today I'm going to talk about the AI driven Progressive delivery and um really show how we uh we were able to achieve this purely using open source tools so our goal from this talk is to give you a solid intuition behind the whole process uh you know so that you guys can implement this yourself all right so with that so the agenda is that we're going to start with what is Progressive delivery talk about that uh and then go straight away into AI based Progressive delivery uh and then finally we will actually go a bit deeper into the multivariate anomal detection and like and also how to we Implement that okay and then finally a demo all right and by the way I am having a bad throat so I sound funny so please excuse me um okay so like at into it our mission is to power Prosperity uh like you know around the world and if you haven't heard of into it uh we are actually a global fintech company that is building an AI native development platform um we serve about 100 million you know customers across our various Brands um namely Turbo Tax Credit kma QuickBooks and MailChimp uh we are really excited to be here and uh you know as we are big users of open- source tools and we love giving back to the open source community so a little bit more about our platform so our AI native uh development platform is massive in scale okay and it like supports over four uh a million models running in production every day and our dep velocity has increased 8X uh you know over the past 4 years and the platform you Powers more than or you know about around you know 60 billion machine learning predictions uh you know per day and one of the most exciting Parts about working at into it is how much open source software we use to build our Dev platform uh we received the end user award in 2019 and you know 2022 um and we love to create an open source many projects here into it especially our gon approach Etc which I think many of you know about so with that let's move on to the core part of our talk so what really is Progressive delivery like I'm pretty sure many of if you know this but we'll just you know brush up on that so uh you know Progressive delivery is basically a gradual release of a new version all right so uh and the reason we do it is because it reduc
