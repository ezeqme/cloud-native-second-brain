---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Application + Development"
themes: ["Application + Development"]
speakers: ["Nick Santos", "Tilt"]
sched_url: https://kccncna2021.sched.com/event/lV1E/the-control-loop-as-an-application-development-framework-nick-santos-tilt
youtube_search_url: https://www.youtube.com/results?search_query=The+Control+Loop+As+An+Application+Development+Framework+CNCF+KubeCon+2021
slides: []
status: parsed
---

# The Control Loop As An Application Development Framework - Nick Santos, Tilt

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Application + Development]]
- Temas: [[Application + Development]]
- País/cidade: United States / Los Angeles
- Speakers: Nick Santos, Tilt
- Schedule: https://kccncna2021.sched.com/event/lV1E/the-control-loop-as-an-application-development-framework-nick-santos-tilt
- Busca YouTube: https://www.youtube.com/results?search_query=The+Control+Loop+As+An+Application+Development+Framework+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre The Control Loop As An Application Development Framework.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1E/the-control-loop-as-an-application-development-framework-nick-santos-tilt
- YouTube search: https://www.youtube.com/results?search_query=The+Control+Loop+As+An+Application+Development+Framework+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uKF8v9X6hSE
- YouTube title: The Control Loop As An Application Development Framework - Nick Santos, Tilt
- Match score: 0.948
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/the-control-loop-as-an-application-development-framework/uKF8v9X6hSE.txt
- Transcript chars: 24707
- Keywords: control, problems, changes, around, server, objects, actually, library, runtime, called, manage, simple, decisions, whether, client, status, cuddle, watching

### Resumo baseado na transcript

hi it's it's good to see all your faces uh so i apologize for the title this talk because i realized afterwards that unless you've seen the talk you don't actually know what the title means uh hopefully we will fix that by the end of the talk let me tell you about the motivation for this talk and why i'm giving it um so my name is nick i work on a product called tilt and we interoperate a lot with kubernetes and as we interoperated a lot with

### Excerpt da transcript

hi it's it's good to see all your faces uh so i apologize for the title this talk because i realized afterwards that unless you've seen the talk you don't actually know what the title means uh hopefully we will fix that by the end of the talk let me tell you about the motivation for this talk and why i'm giving it um so my name is nick i work on a product called tilt and we interoperate a lot with kubernetes and as we interoperated a lot with kubernetes we started to realize how much the design decisions that kubernetes makes were influencing the design decisions we were making in our own app and it when we kind of we kind of thought about why this was happening and we said well you know if we squint really hard kubernetes is just a framework for solving control loop problems and if you squint really hard till also needs to solve a lot of control loop problems and we really admired the way that kubernetes broke those problems down into pieces and solved them and so we said okay kubernetes actually has a pretty good opinion on how to solve these kinds of problems why are we building all this libraries for ourselves to build this app to build control loops why don't we just pull in more of kubernetes as a library take a lot of the controller runtime the api server and just really just pull it into our own app and use it instead of building it ourselves uh i can't see your faces but you probably look horrified uh maybe by the end of the talk i will convince you to at least be less horrified by this idea and i will tell you what happened and i will tell you if you should also use kubernetes as a library yourself uh so let me just start by talking about what i mean by the control loop problem uh control loops are a lot of places in the kubernetes documentation this is a very old engineering concept the idea of a control loop is that in an environment where things can change at runtime where you need to react to changes where you need to steer to avoid obstacles you really need an engineering system that can self-regulate that can continuously respond to changes and keep the system in a consistent state there are many mechanical control loops in the world but we're going to focus really on software control loops these systems look very different than kind of traditional web apps where traditional web app looks very much like you send a request you get back a response that tells you if your or request succeeded software control loops are constantly adjusting thei
