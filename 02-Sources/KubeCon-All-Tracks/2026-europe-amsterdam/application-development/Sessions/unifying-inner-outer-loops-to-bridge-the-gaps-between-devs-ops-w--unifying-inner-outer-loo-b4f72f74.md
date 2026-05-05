---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Application Development"
themes: ["Application Development"]
speakers: ["Laurent Broudoux", "Microcks", "Mathieu Benoit", "Docker"]
sched_url: https://kccnceu2026.sched.com/event/2CVxb/unifying-inner-outer-loops-to-bridge-the-gaps-between-devs-ops-with-microcks-+-score-laurent-broudoux-microcks-mathieu-benoit-docker
youtube_search_url: https://www.youtube.com/results?search_query=Unifying+Inner+%26+Outer+Loops+To+Bridge+the+Gaps+Between+Devs+%26+Ops+With+Microcks+%2B+Score+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Unifying Inner & Outer Loops To Bridge the Gaps Between Devs & Ops With Microcks + Score - Laurent Broudoux, Microcks & Mathieu Benoit, Docker

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Application Development]]
- Temas: [[Application Development]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Laurent Broudoux, Microcks, Mathieu Benoit, Docker
- Schedule: https://kccnceu2026.sched.com/event/2CVxb/unifying-inner-outer-loops-to-bridge-the-gaps-between-devs-ops-with-microcks-+-score-laurent-broudoux-microcks-mathieu-benoit-docker
- Busca YouTube: https://www.youtube.com/results?search_query=Unifying+Inner+%26+Outer+Loops+To+Bridge+the+Gaps+Between+Devs+%26+Ops+With+Microcks+%2B+Score+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Unifying Inner & Outer Loops To Bridge the Gaps Between Devs & Ops With Microcks + Score.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVxb/unifying-inner-outer-loops-to-bridge-the-gaps-between-devs-ops-with-microcks-+-score-laurent-broudoux-microcks-mathieu-benoit-docker
- YouTube search: https://www.youtube.com/results?search_query=Unifying+Inner+%26+Outer+Loops+To+Bridge+the+Gaps+Between+Devs+%26+Ops+With+Microcks+%2B+Score+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Y_jfBWbBTZQ
- YouTube title: Unifying Inner & Outer Loops To Bridge the Gaps Between Devs... Laurent Broudoux & Mathieu Benoit
- Match score: 0.813
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/unifying-inner-outer-loops-to-bridge-the-gaps-between-devs-ops-with-mi/Y_jfBWbBTZQ.txt
- Transcript chars: 23717
- Keywords: developer, platform, application, environment, resources, actually, access, dependencies, implementation, workload, production, remember, compose, staging, opportunity, compost, locally, deployed

### Resumo baseado na transcript

So uh in this session this morning we are going to explore solutions on how to avoid this situation. How to make the transition from your developer laptop to the production environment and other environment the easier possible the the most smooth possible. and still as a platform engineer there is also a big risk about having a configuration drift risk between your local development and the Kubernetes cluster in staging in QA grain production whatever. Micro is a CNCF sandbox project and you'll learn more about Microx in a few minutes. maybe a Kubernetes platform more for integrating uh and staging environment or even production. But you could have also the Kubernetes one from the same exact score file.

### Excerpt da transcript

Yeah. >> Okay. >> All right. >> Shall we start? All right. Good morning, everyone. I hope everybody has find its way. >> How is this room? Is everyone doing? >> Yeah. Excited. Nice. >> Okay. So, thank you for joining this session. So, uh have you ever heard it works on my machine mantra? Yeah, I'm pretty sure everybody has. Yeah. So uh in this session this morning we are going to explore solutions on how to avoid this situation. How to make the transition from your developer laptop to the production environment and other environment the easier possible the the most smooth possible. And we want to uh yes to to avoid also putting too much cognitive load to the developers to the platform engineers and also to avoid consuming too much resources when developing locally when deploying environment and so on and so forth. So we have a lot of challenge to address. So without further ado let's jump to uh our demo application. This is the finest trade trader hicks sample application and this is basically an application that was made to illustrate the microservices architecture in a banking situation.

So you can place orders, you can uh review positions, you can manage accounts, add users to accounts and so on so forth. So it looks pretty simple. However, if you look at the architecture, yes, it's still a lot of components in different technologies uh using different development stacks. So, quite a lot of resource and I have made the the diagram the most simple as possible. There are way more components that are deployed. So, here on the demonstration, it runs on Kubernetes. It uses a fair amount of resources and a fair amount of Kubernetes object. Okay. uh and because it's containers it can also run on your local machine okay using docker compose but here still you have as a developer to pull a lot of images wait for a lot of time each and every time someone updates an image uh it takes a lot of place on your hard drive okay uh and it consumes a lot of resources so it's possible but the hard reality is that developing the Trader Hicks application could be kind of hard because as a developer you may have no access to the dependencies.

Maybe they are not yet ready. A new feature is being developed at the moment by another developer. So it's kind of hard and you have to to wait or you can access all the dependencies but it comes with a price CPUs memories cognitive load because you have to remember anything to remember how to deploy stuff how to run stuff locally and
