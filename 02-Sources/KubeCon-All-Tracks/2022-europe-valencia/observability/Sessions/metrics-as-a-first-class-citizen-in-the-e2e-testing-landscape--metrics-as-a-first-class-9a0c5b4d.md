---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Observability"
themes: ["Observability"]
speakers: ["Matej Gera", "Jéssica Lins", "Red Hat"]
sched_url: https://kccnceu2022.sched.com/event/ytuD/metrics-as-a-first-class-citizen-in-the-e2e-testing-landscape-matej-gera-jessica-lins-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Metrics+as+a+First-Class+Citizen+in+the+E2E+Testing+Landscape+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Metrics as a First-Class Citizen in the E2E Testing Landscape - Matej Gera & Jéssica Lins, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Spain / Valencia
- Speakers: Matej Gera, Jéssica Lins, Red Hat
- Schedule: https://kccnceu2022.sched.com/event/ytuD/metrics-as-a-first-class-citizen-in-the-e2e-testing-landscape-matej-gera-jessica-lins-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Metrics+as+a+First-Class+Citizen+in+the+E2E+Testing+Landscape+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Metrics as a First-Class Citizen in the E2E Testing Landscape.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytuD/metrics-as-a-first-class-citizen-in-the-e2e-testing-landscape-matej-gera-jessica-lins-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Metrics+as+a+First-Class+Citizen+in+the+E2E+Testing+Landscape+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jFm3WBtFhv4
- YouTube title: Metrics as a First-Class Citizen in the E2E Testing Landscape - Matej Gera & Jéssica Lins, Red Hat
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/metrics-as-a-first-class-citizen-in-the-e2e-testing-landscape/jFm3WBtFhv4.txt
- Transcript chars: 26927
- Keywords: metrics, application, framework, testing, requests, prometheus, applications, jessica, metric, end-to-end, interactive, actually, scenarios, together, already, observability, systems, understand

### Resumo baseado na transcript

all right hi everyone uh so we are very happy to be here hope you had a good time at kubicon um today we are here to talk to you about metrics and entry and testing how those things can be combined together but first let's present ourselves so my name is jessica i'm a software engineer at red hat i'm also a contributor and approver for portuguese content at the cncf glossary i'm one of the maintainers of the observatorium project this is our observability backhand i will see

### Excerpt da transcript

all right hi everyone uh so we are very happy to be here hope you had a good time at kubicon um today we are here to talk to you about metrics and entry and testing how those things can be combined together but first let's present ourselves so my name is jessica i'm a software engineer at red hat i'm also a contributor and approver for portuguese content at the cncf glossary i'm one of the maintainers of the observatorium project this is our observability backhand i will see more about it today and i'm currently working with go i'm also interested in distributed systems and also observability so hey everyone i'm mate i'm also working with jessica at the monitoring team at red hat i'm a contributor and a triage member at the at the thanos project as you can also get from my cool tunnel socks that i got yesterday from the cncf store and i'm also maintained observatorium uh together with jessica so yeah the usual interested in distributed systems observability and all of those things cool so let's go through our agenda today so the idea today is that we want to understand what are metrics why are they important why do we need them then we will jump into understanding metrics and then trend testing as a concept so like how this differ from the conventional engine testing what are the advantages which patterns can we use and we also go through different types of tests then we will show how this can be used in real world applications and at the end we'll have a demo so we can understand how all of this can be used in practice but first i want to ask everyone who in this room has your application instrumented with metrics cool nice nice i see some hands i first want to share my personal story how i got introduced to metrics on the first place was not very funny but yeah i pushed a new service to production the code worked the prs were review everything was okay in my head at least i had the code there the tests were passing and then the service went live people started to use it i saw some logs okay i got some requests but i had no idea how everything was going right i had no idea how my application was performing it was a new service so like how am i supposed to do that everything is fine right like how many requests do i get like i had no dashboards like how many requests per second how many errors um and what about resources right like i don't know if i have enough cpu or memory or actually if i had more if i provision more so that's when i noticed that metric
