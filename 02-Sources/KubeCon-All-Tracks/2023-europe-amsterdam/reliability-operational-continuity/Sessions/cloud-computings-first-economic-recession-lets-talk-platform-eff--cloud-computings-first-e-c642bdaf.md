---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["Platform Engineering", "SRE Reliability"]
speakers: ["Aparna Subramanian", "Shopify", "Todd Ekenstam", "Intuit", "Phillip Wittrock", "Apple", "Nagarajan Chinnakaveti Thulasiraman", "Zalando SE"]
sched_url: https://kccnceu2023.sched.com/event/1HycO/cloud-computings-first-economic-recession-lets-talk-platform-efficiency-aparna-subramanian-shopify-todd-ekenstam-intuit-phillip-wittrock-apple-nagarajan-chinnakaveti-thulasiraman-zalando-se
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Computing%E2%80%99s+First+Economic+Recession%3F+Let%E2%80%99s+Talk+Platform+Efficiency+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Cloud Computing’s First Economic Recession? Let’s Talk Platform Efficiency - Aparna Subramanian, Shopify; Todd Ekenstam, Intuit; Phillip Wittrock, Apple; Nagarajan Chinnakaveti Thulasiraman, Zalando SE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Aparna Subramanian, Shopify, Todd Ekenstam, Intuit, Phillip Wittrock, Apple, Nagarajan Chinnakaveti Thulasiraman, Zalando SE
- Schedule: https://kccnceu2023.sched.com/event/1HycO/cloud-computings-first-economic-recession-lets-talk-platform-efficiency-aparna-subramanian-shopify-todd-ekenstam-intuit-phillip-wittrock-apple-nagarajan-chinnakaveti-thulasiraman-zalando-se
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Computing%E2%80%99s+First+Economic+Recession%3F+Let%E2%80%99s+Talk+Platform+Efficiency+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Cloud Computing’s First Economic Recession? Let’s Talk Platform Efficiency.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HycO/cloud-computings-first-economic-recession-lets-talk-platform-efficiency-aparna-subramanian-shopify-todd-ekenstam-intuit-phillip-wittrock-apple-nagarajan-chinnakaveti-thulasiraman-zalando-se
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Computing%E2%80%99s+First+Economic+Recession%3F+Let%E2%80%99s+Talk+Platform+Efficiency+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kBx0qahxbGo
- YouTube title: Cloud Computing’s First Economic Recession? Let’s... - Subramanian, Ekenstam, Wittrock, Thulasiraman
- Match score: 0.78
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/cloud-computings-first-economic-recession-lets-talk-platform-efficienc/kBx0qahxbGo.txt
- Transcript chars: 31657
- Keywords: cost, application, platform, efficiency, scaling, actually, important, cluster, applications, resources, running, business, measure, workload, infrastructure, shopify, making, mentioned

### Resumo baseado na transcript

good morning everybody Welcome to our panel discussion on cloud computing's first economic recession let's talk platform efficiency and let me ask by uh start by asking a question how many of you have a mild efficiency Panic at your companies at your organizations all right so you're at the right place uh we are a group of end users and we also have a efficiency Panic at work and we've been spending some time doing optimizations and figuring out what's the best way to make the platform efficient and

### Excerpt da transcript

good morning everybody Welcome to our panel discussion on cloud computing's first economic recession let's talk platform efficiency and let me ask by uh start by asking a question how many of you have a mild efficiency Panic at your companies at your organizations all right so you're at the right place uh we are a group of end users and we also have a efficiency Panic at work and we've been spending some time doing optimizations and figuring out what's the best way to make the platform efficient and um back in the day it used to be capital expenditure like you'd have a data center the spend was predictable and these days with the move to Cloud it's a pay as you go model and it's really becoming a Opex operational expense and impacting uh companies greatly so I think that's the reason why we have this and the increased focus on optimizing and squeezing more and doing more uh with less is the is the Mantra these days so uh in this talk we are going to be talking about three aspects so culture operations and design so these are the three broad categories that we are going to be talking about today and with that we'll introduce ourselves and I'll hand it over to Todd to facilitate the panel yeah thanks a partner yeah go ahead Phil hello my name is Phil whitrock and I work at Apple on kubernetes uh I'm nagu I'm working in zalando in the cloud infrastructure Department I'm managing two teams Cloud I'm sorry container platform and Cloud cost efficiency teams my name is aparna subramanian I am director of production engineering at Shopify and I've been involved in platform efficiency efforts for the past year and a half at Shopify hi Antarctica Stam I'm principal engineer at Intuit working in our course systems team that also includes our kubernetes platform well let's get started talking about culture obviously the goal is ultimately to increase efficiency and reduce costs but where do you really start what do you how can you get started how can you gain organizational commitment to improve efficiency and reduce the costs uh Phil yeah I can take this one so one thing I think is helpful to start with is start out measuring where your big wins are where do you want to focus uh what's going to move the needle a lot but it's going to take a long time to do what's maybe not going to move it as much but it's very easy to get done and then from there figuring out who the right folks to engage with are what are the right teams so you can start moving forward yeah and I c
