---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "SDLC"
themes: ["Observability"]
speakers: ["Nicolas Woerner", "Clario", "Andreas Grabner", "Dynatrace"]
sched_url: https://kccncna2024.sched.com/event/1i7nM/how-we-made-opentelemetry-be-our-fitness-tracker-for-your-cicd-pipelines-nicolas-woerner-clario-andreas-grabner-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Made+OpenTelemetry+Be+Our+Fitness+Tracker+for+Your+CI%2FCD+Pipelines%21+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How We Made OpenTelemetry Be Our Fitness Tracker for Your CI/CD Pipelines! - Nicolas Woerner, Clario & Andreas Grabner, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[SDLC]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Nicolas Woerner, Clario, Andreas Grabner, Dynatrace
- Schedule: https://kccncna2024.sched.com/event/1i7nM/how-we-made-opentelemetry-be-our-fitness-tracker-for-your-cicd-pipelines-nicolas-woerner-clario-andreas-grabner-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Made+OpenTelemetry+Be+Our+Fitness+Tracker+for+Your+CI%2FCD+Pipelines%21+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How We Made OpenTelemetry Be Our Fitness Tracker for Your CI/CD Pipelines!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nM/how-we-made-opentelemetry-be-our-fitness-tracker-for-your-cicd-pipelines-nicolas-woerner-clario-andreas-grabner-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=How+We+Made+OpenTelemetry+Be+Our+Fitness+Tracker+for+Your+CI%2FCD+Pipelines%21+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IRNyf_MLHDw
- YouTube title: How We Made OpenTelemetry Be Our Fitness Tracker for Your CI/CD Pipelines! - N. Woerner, A. Grabner
- Match score: 0.96
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-we-made-opentelemetry-be-our-fitness-tracker-for-your-ci-cd-pipeli/IRNyf_MLHDw.txt
- Transcript chars: 29580
- Keywords: pipeline, trace, pipelines, collector, already, gitlab, receiver, actually, traces, deployment, questions, application, production, pretty, change, deploy, dashboard, argo

### Resumo baseado na transcript

hello everybody sleeping or are you awake morning awesome uh thanks for being here um my name is Andy I am a cncf Ambassador I also work at Dino Trace but I'm really happy to actually have with me today Nicolas who is a firsttime speaker which I think uh a round of applause [Applause] please it is it is not easy to stay on stage and look at this but Nicholas maybe a quick introduction who you are and especially what does clario do yeah hello everyone also from

### Excerpt da transcript

hello everybody sleeping or are you awake morning awesome uh thanks for being here um my name is Andy I am a cncf Ambassador I also work at Dino Trace but I'm really happy to actually have with me today Nicolas who is a firsttime speaker which I think uh a round of applause [Applause] please it is it is not easy to stay on stage and look at this but Nicholas maybe a quick introduction who you are and especially what does clario do yeah hello everyone also from my side so I'm pretty happy to be here today like Andy said it's the very first time for me standing here on stage at the cubec con and yeah um I'm working for clario I guess most of you already know the company where Andy is working for Dino Trace but um clario is is doing a bit different so we're working um on software and hardware for clinical trials that means um yeah if you think about a truck which is supposed to be released on the public market so that patients get access to that we first need an FDA approval and in order to get that FDA approval that's where claria comes into play with developing modern software or medical devices um yeah in order to do those clinical trials um we are one of the market leaders in that area and we have around 3 to 4,000 employees so yeah that's about claria yeah you you make sure that the world is a healthier place where the people are healthier uh talking about health who of you has any type of Fitness track yeah how many who has more than 10,000 steps already today show of hands because these are the ones that went running in the morning I guess or you got lost in the uh Convention Center uh the reason why mentioning it uh we will have a couple of references to health tracking which makes sense with clario being in that in that business uh one of the things that I'm passionate about is in my role as a cncf Ambassador we try to bring new people in the community forward on stage to show what they're doing and what they've done um and so one of the things that I want to highlight here is want to start with why are we actually on stage the reason why we are on stage it was in Paris early this year I did a presentation at argoon where I talked about how we can get observability into Argo deployments if they start failing or if they get slow I was promoting a cncf project called Captain as you can see on my head maybe KTN that provides automated uh traces for every deployment that you do on kubernetes and Argo is a very common tool in that space so we bundled it u
