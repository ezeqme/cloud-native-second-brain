---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Adrien Gillard", "Decathlon"]
sched_url: https://kccnceu2024.sched.com/event/1YeQh/assessing-service-meshs-net-worth-a-pragmatic-onboarding-adrien-gillard-decathlon
youtube_search_url: https://www.youtube.com/results?search_query=Assessing+Service+Mesh%27s+Net+Worth%3A+A+Pragmatic+Onboarding+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Assessing Service Mesh's Net Worth: A Pragmatic Onboarding - Adrien Gillard, Decathlon

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: France / Paris
- Speakers: Adrien Gillard, Decathlon
- Schedule: https://kccnceu2024.sched.com/event/1YeQh/assessing-service-meshs-net-worth-a-pragmatic-onboarding-adrien-gillard-decathlon
- Busca YouTube: https://www.youtube.com/results?search_query=Assessing+Service+Mesh%27s+Net+Worth%3A+A+Pragmatic+Onboarding+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Assessing Service Mesh's Net Worth: A Pragmatic Onboarding.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQh/assessing-service-meshs-net-worth-a-pragmatic-onboarding-adrien-gillard-decathlon
- YouTube search: https://www.youtube.com/results?search_query=Assessing+Service+Mesh%27s+Net+Worth%3A+A+Pragmatic+Onboarding+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5quqbj8npRo
- YouTube title: Assessing Service Mesh's Net Worth: A Pragmatic Onboarding - Adrien Gillard, Decathlon
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/assessing-service-meshs-net-worth-a-pragmatic-onboarding/5quqbj8npRo.txt
- Transcript chars: 26355
- Keywords: mesh, basically, gateway, solution, traffic, management, proxies, clusters, implement, inside, issues, cluster, another, network, actually, communities, course, observability

### Resumo baseado na transcript

all right hi everyone uh really happy to be here in front of you today uh I'm Adrian I'm a senior Ops engineer and the kathan in the clude platform engineering business unit so at the name suggest we provide the CL platform product to our internal users so the idea is to uh standardize and is the adoption of uh uh Cloud Solutions for all our it users I'm more specifically in the uh clud Native partners team uh which handles everything related to kubernetes container orchestration and several

### Excerpt da transcript

all right hi everyone uh really happy to be here in front of you today uh I'm Adrian I'm a senior Ops engineer and the kathan in the clude platform engineering business unit so at the name suggest we provide the CL platform product to our internal users so the idea is to uh standardize and is the adoption of uh uh Cloud Solutions for all our it users I'm more specifically in the uh clud Native partners team uh which handles everything related to kubernetes container orchestration and several components to inter integrate them into this platform and uh today I will talk to you about service mesh and uh first I wanted to talk to you about the study we did about service Mish last year but uh then I changed my mind and I'm going to uh talk to you about how we can uh improve service mesh with AI at the edge uh basically the idea is to uh uh see you can uh connect your uh let's say your uh connected bike into your service mesh and talk to it when you go to work uh in order to uh configure uh your various service mes ah it don't seem so excited uh well I I actually talked to you about the study we did about service smesh um so basically uh this is the conclusion uh service SM is not the solution thank you uh feedbacks appreciated uh we are iring by the way uh thank you I saw some up in the eyes of my colleague in the front they were thinking yeah we can go to lunch early but uh I owe to you to uh deep di more on that so uh why is service SM not the best solution we'll uh see a bit about that later first a few words about the cath so the kathin is the world's largest uh sport good retailer in the world uh we had uh 15 ions in Revenue in 2022 and we have around uh 5,000 teammates as we call them working in the it overall in digital few words about our container Journey so we started with containers quite early we did our first test with communities in 2017 we put our first communities in production uh in 2019 in 2021 we went uh full P Cloud so we basically shut down our latest data centers in 20 21 that was the end of a long journey that started like in 2016 and now we're in 2024 and in the 2023 we did this study about Sor smash so we look uh at why we did this study uh we look at what were uh our user needs and who were this users we'll focus a bit more on service mesh to see how it works uh what it does and then we'll uh Focus again on the study itself and these conclusions so first of all the context uh before diving into the uh container context uh I want to sa
