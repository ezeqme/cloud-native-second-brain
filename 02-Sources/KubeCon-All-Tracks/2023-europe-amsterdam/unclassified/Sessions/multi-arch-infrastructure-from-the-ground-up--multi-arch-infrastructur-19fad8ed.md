---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["Cloud Native"]
speakers: ["Cheryl Hung", "Arm"]
sched_url: https://kccnceu2023.sched.com/event/1HyaY/multi-arch-infrastructure-from-the-ground-up-cheryl-hung-arm
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Arch+Infrastructure+from+the+Ground+up+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Multi-Arch Infrastructure from the Ground up - Cheryl Hung, Arm

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[Cloud Native]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Cheryl Hung, Arm
- Schedule: https://kccnceu2023.sched.com/event/1HyaY/multi-arch-infrastructure-from-the-ground-up-cheryl-hung-arm
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Arch+Infrastructure+from+the+Ground+up+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Multi-Arch Infrastructure from the Ground up.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyaY/multi-arch-infrastructure-from-the-ground-up-cheryl-hung-arm
- YouTube search: https://www.youtube.com/results?search_query=Multi-Arch+Infrastructure+from+the+Ground+up+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VeN9x9eza7I
- YouTube title: Multi-Arch Infrastructure from the Ground up - Cheryl Hung, Arm
- Match score: 0.926
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/multi-arch-infrastructure-from-the-ground-up/VeN9x9eza7I.txt
- Transcript chars: 18536
- Keywords: actually, running, infrastructure, software, couple, multi-arch, started, everything, support, workloads, environment, probably, performance, upgrade, second, basically, machines, native

### Resumo baseado na transcript

welcome everyone welcome hope you're having a really good first day of kubecon this talk is going to be about multi-arch infrastructure from the ground up a little bit about me my name is Cheryl I have been part of the cloud native Community for a little while um now I work at arm where I'm the senior director of the infrastructure ecosystem but generally I say my background is software Cloud native and open source so I've built software and built software teams at Google and apple I started me to for us to look at our whole infrastructure and see what see what we can do about it so more explicitly the goals of multi-art infrastructure is for workloads to run on the best hardware for their price performance needs without the developers having to consider what is the underlying architecture so that's the whole goal of why we wanted to do multi-arch the problem is multi-arch is not just one thing it touches absolutely everything so this is a sort of sample e-commerce kind of website so ones that they were learning in supported um and then the very last piece in that was and for their load tests they chose logins because the logins were particularly CPU intensive um they tested 50 000 logins and found that um handled between 26

### Excerpt da transcript

welcome everyone welcome hope you're having a really good first day of kubecon this talk is going to be about multi-arch infrastructure from the ground up a little bit about me my name is Cheryl I have been part of the cloud native Community for a little while um now I work at arm where I'm the senior director of the infrastructure ecosystem but generally I say my background is software Cloud native and open source so I've built software and built software teams at Google and apple I started working in the open source community Through meetups I run Cloud native London which has about 7 000 members and I worked for cncf as well building up the end user Community around Cloud native and kubernetes when I say the um info ecosystem this is what I I mostly do so I have a team of five we split across Cloud 5G Telco networking and generally we try and make it as easy and painless as possible to adopt arm so we do three things we do developer Outreach we try and make people aware of what arm is doing um we try and encourage as much software and Hardware support so make it really easy to get hold of arm hardware and then all the software that you want on top of it should support Army as well and then making sure that um is in all of the standards bodies and arms customers are also represented so chcf and if networking OPI and a bunch of other open source foundations but overall my my goal my mission is just make it as easy and painless as possible to adopt um so when I talk about naughty Arch um mostly I talk about x86 and arm but you know risk five and you know there are other options as well but just because of my background I'm going to talk mostly about mostly about x86 and um oh yeah one thing to point out here I don't do anything to do with mobile phones so I know arm is in every mobile device ever I don't do anything to do with mobile phones and I don't have anything to do with cars either so objectives of today's 30 35 minutes I want to answer following questions so why is multi-arch infrastructure tricky why do you even want to do it secondly if you are running kubernetes what are some things that you should look out for when you get started and then I'm going to look at a couple of case studies right first up why is multi-arch tricky a quick Poll for the audience before a start so um there's your infrastructure support multi-arch today I'm going to give you five options so just raise your hand so I want to see what everybody's at right now so first one i
