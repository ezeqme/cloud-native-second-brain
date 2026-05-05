---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Sayan Mondal", "Harness", "Raj Vadheraju", "FIS"]
sched_url: https://kccnceu2024.sched.com/event/1YeNB/cultural-shifts-fostering-a-chaos-first-mindset-in-platform-engineering-sayan-mondal-harness-raj-vadheraju-fis
youtube_search_url: https://www.youtube.com/results?search_query=Cultural+Shifts%3A+Fostering+a+Chaos+First+Mindset+in+Platform+Engineering+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cultural Shifts: Fostering a Chaos First Mindset in Platform Engineering - Sayan Mondal, Harness & Raj Vadheraju, FIS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: France / Paris
- Speakers: Sayan Mondal, Harness, Raj Vadheraju, FIS
- Schedule: https://kccnceu2024.sched.com/event/1YeNB/cultural-shifts-fostering-a-chaos-first-mindset-in-platform-engineering-sayan-mondal-harness-raj-vadheraju-fis
- Busca YouTube: https://www.youtube.com/results?search_query=Cultural+Shifts%3A+Fostering+a+Chaos+First+Mindset+in+Platform+Engineering+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cultural Shifts: Fostering a Chaos First Mindset in Platform Engineering.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNB/cultural-shifts-fostering-a-chaos-first-mindset-in-platform-engineering-sayan-mondal-harness-raj-vadheraju-fis
- YouTube search: https://www.youtube.com/results?search_query=Cultural+Shifts%3A+Fostering+a+Chaos+First+Mindset+in+Platform+Engineering+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WUXFKxgZRsk
- YouTube title: Cultural Shifts: Fostering a Chaos First Mindset in Platform Engineering
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cultural-shifts-fostering-a-chaos-first-mindset-in-platform-engineerin/WUXFKxgZRsk.txt
- Transcript chars: 38086
- Keywords: platform, engineering, application, actually, litmus, experiment, production, course, backstage, definitely, experiments, specific, applications, pipeline, components, everything, create, running

### Resumo baseado na transcript

so today um this talk is specifically about cultural shifts and how you can leverage chaos in platform engineering which is something we wanted to tap in uh me and Raj unfortunately Raj could not be here because of some issues but um rest assure uh he has provided a demo recording of a few like a 5 minute recording so he'll be talking and going in depth about the architecture how he's using it and stuff like that so we'll see all the good stuff but let's jump right

### Excerpt da transcript

so today um this talk is specifically about cultural shifts and how you can leverage chaos in platform engineering which is something we wanted to tap in uh me and Raj unfortunately Raj could not be here because of some issues but um rest assure uh he has provided a demo recording of a few like a 5 minute recording so he'll be talking and going in depth about the architecture how he's using it and stuff like that so we'll see all the good stuff but let's jump right into it so a little bit about me I'm a senior software engineer at harness and also a maintainer at the project called litmas which is the cncf incubating project and Raj is a senior Enterprise architect at FIS and he has more than 20 plus years of experience so definitely somebody uh you would want to listen to now moving on uh the agenda of this stock so we be uh of course you guys are platform Engineers so I'm not here talking about the basics of platform engineering uh but we'll be covering the core components of IDP uh talking a bit about the cognitive problem which is why we are introducing chaos engineering the what and why the chaos first principles and then we'll see how we can introduce the chaos in a Hands-On demo and talk about the vision and the tools that are in the market that you can use of course the tools are just U you know U an abstract view of things you can integrate your own tools it's not vendor specific or tool specific but yeah and then we are going to execute chaos observe the impact on a gra dashboard hopefully if the Democrats are happy now let's talk about the problems uh the cloud native era has on all of us right so we are basically running our uh we have we have shifted from a legacy a very simple architecture to something as complicated as Cloud native so our devop score scany self-service they are policy driven we have zero trust environment so so much problem so much extra overhead has come into our manufacuring of a single software which used to be so simple and has so many components so this leads to something we call the devops problem which is you shipping your uh containers you shipping your applications 10 times faster and for that to manage everything we introduce something like platform engineering to have everything in a single uh layer right so the core components of an IDP these are all these are some of the high level uh components that I've mentioned which is the application configuration management the infrastructure orchestration uh the environm
