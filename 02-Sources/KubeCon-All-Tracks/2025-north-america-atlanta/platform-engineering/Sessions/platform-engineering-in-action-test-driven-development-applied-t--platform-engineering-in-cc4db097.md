---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "Storage Data"]
speakers: ["Charles-Edouard Brétéché", "Nirmata", "Sara Qasmi", "NTT Data"]
sched_url: https://kccncna2025.sched.com/event/27FVY/platform-engineering-in-action-test-driven-development-applied-to-developer-platforms-charles-edouard-breteche-nirmata-sara-qasmi-ntt-data
youtube_search_url: https://www.youtube.com/results?search_query=Platform+Engineering+in+Action%3A+Test-Driven+Development+Applied+To+Developer+Platforms+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Platform Engineering in Action: Test-Driven Development Applied To Developer Platforms - Charles-Edouard Brétéché, Nirmata & Sara Qasmi, NTT Data

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Storage Data]]
- País/cidade: United States / Atlanta
- Speakers: Charles-Edouard Brétéché, Nirmata, Sara Qasmi, NTT Data
- Schedule: https://kccncna2025.sched.com/event/27FVY/platform-engineering-in-action-test-driven-development-applied-to-developer-platforms-charles-edouard-breteche-nirmata-sara-qasmi-ntt-data
- Busca YouTube: https://www.youtube.com/results?search_query=Platform+Engineering+in+Action%3A+Test-Driven+Development+Applied+To+Developer+Platforms+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Platform Engineering in Action: Test-Driven Development Applied To Developer Platforms.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVY/platform-engineering-in-action-test-driven-development-applied-to-developer-platforms-charles-edouard-breteche-nirmata-sara-qasmi-ntt-data
- YouTube search: https://www.youtube.com/results?search_query=Platform+Engineering+in+Action%3A+Test-Driven+Development+Applied+To+Developer+Platforms+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=p2QPtjHp77I
- YouTube title: Platform Engineering in Action: Test-Driven Development App... Charles-Edouard Brétéché & Sara Qasmi
- Match score: 0.844
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/platform-engineering-in-action-test-driven-development-applied-to-deve/p2QPtjHp77I.txt
- Transcript chars: 20720
- Keywords: platform, cluster, database, application, drupal, argo, secret, instance, exactly, composition, repository, running, create, development, crossplane, implementation, trying, mariab

### Resumo baseado na transcript

Um when building a platform we a developer platform we usually think about things like availability, scalability, user experience and things like this but we rarely think about testability. So today we'll talk about platforms of course, but most importantly we'll see how to apply testdriven development to platform engineering if we can. We have Kubernetes cluster uh gargo cd for githopsdriven continuous deployment and uh crossplane. So let's try for example to scale it up and try to have a second replica of this bolt. example the a simple secret name change um doesn't break right away it breaks when the application scales So you don't see it, you see it maybe 2 hours later. It's not specific to any Kubernetes distribution, but Chainsaw will not create clusters for you.

### Excerpt da transcript

Hello everyone. Um thank for coming today. In this session we are going to talk about a rather special topic. Um when building a platform we a developer platform we usually think about things like availability, scalability, user experience and things like this but we rarely think about testability. So today we'll talk about platforms of course, but most importantly we'll see how to apply testdriven development to platform engineering if we can. And here's what to expect during this session. Um we will first um we will first build the platform without any test. um we run it and surprisingly something is probably going to go wrong. Uh Siguan will introduce testdriven development. We'll start from scratch again and rebuild the same platform. This time writing test before writing the different components of the platform and um we will ensure that the platform contracts remain valid uh within every single change. And third, we'll see how this test can be automated uh executed automatically uh both locally by a platform engineer during development and um by developer teams or in a continuous integration pipeline on a on a on a continuous integration platform.

Uh for this example, it will be GitHub. So yes um before diving into the main content let's let's start with introductions. So I'll give the floor first to Sarah. >> Hi um introduce yourself. >> Yeah. Hi everyone. I'm Sarah Casmi. I'm a platform engineer working at entity data. >> So welcome. Um I'm Charlotte the Sarah co speaker. Uh I work at Neata. I'm a senior software engineer and I mostly work on Kiverano and open source projects um in the Kibano organization. So now the introductions are done. Um Sarah, our favorite platform engineer today, um can you present the need and the platform we'll be building? >> Yeah, sure. So our our goal is simple. We want to uh run Drupal application in our platform. We have two teams involved here. A platform team guaranteeing the uh the fun fundamentals Kubernetes cluster database services for example taking care of the networking CI/CD etc. And we have a developer development team that needs a functioning environment to run it the the Drupal application. So in on the surface things seems very pretty obvious and every team has its own uh scope and things are clear but like what could go wrong in this scenario.

>> Let's see. >> Let's see. So our stack is very simple. We have Kubernetes cluster uh gargo cd for githopsdriven continuous deployment and uh crossplane. This
